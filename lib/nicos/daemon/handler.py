#  -*- coding: utf-8 -*-
# *****************************************************************************
# Module:
#   $Id$
#
# Author:
#   Georg Brandl <georg.brandl@frm2.tum.de>
#
# NICOS-NG, the Networked Instrument Control System of the FRM-II
# Copyright (c) 2009-2011 by the NICOS-NG contributors (see AUTHORS)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# *****************************************************************************

"""
The connection handler for the execution daemon, handling the protocol commands.
"""

__author__  = "$Author$"
__date__    = "$Date$"
__version__ = "$Revision$"

import os
import errno
import socket
import struct
from Queue import Queue
from SocketServer import BaseRequestHandler

from nicos import session, nicos_version
from nicos.daemon.utils import LoggerWrapper, serialize, unserialize
from nicos.daemon.pyctl import STATUS_IDLE, STATUS_IDLEEXC, STATUS_RUNNING, \
     STATUS_STOPPING, STATUS_INBREAK
from nicos.daemon.script import EmergencyStopRequest, ScriptRequest, \
     ScriptError, RequestError


READ_BUFSIZE = 4096

# one-byte responses without length
ACK = '\x06'   # executed ok, no further information follows

# responses with length, encoded as a 32-bit integer
STX = '\x03'   # executed ok, reply follows
NAK = '\x15'   # error occurred, message follows
LENGTH = struct.Struct('>I')   # used to encode length

# argument separator in client commands
RS = '\x1e'

_queue_freelist = [Queue() for i in range(5)]


class CloseConnection(Exception):
    """Raised to unconditionally close the connection."""

licos_commands = {}

def command(needcontrol=False, needscript=None, name=None):
    """
    Decorates a nicosd protocol command.  The `needcontrol` and `needscript`
    parameters can be set to avoid boilerplate in the handler functions.
    """
    def deco(func):
        nargs = func.func_code.co_argcount - 1
        def wrapper(self, args):
            if len(args) != nargs:
                self.write(NAK, 'invalid number of arguments')
            if needcontrol:
                if not self.check_control():
                    return
            if needscript is True:
                if self.controller.status in (STATUS_IDLE, STATUS_IDLEEXC):
                    self.write(NAK, 'no script is running')
                    return
            elif needscript is False:
                if self.controller.status not in (STATUS_IDLE, STATUS_IDLEEXC):
                    self.write(NAK, 'a script is running')
                    return
            try:
                return func(self, *args)
            except CloseConnection:
                raise
            except Exception:
                self.log.exception('exception executing command %s' %
                                   (name or func.__name__))
                self.write(NAK, 'exception occurred executing command')
        wrapper.__name__ = func.__name__
        licos_commands[name or func.__name__] = wrapper
        return wrapper
    return deco

stop_queue = object()


class ConnectionHandler(BaseRequestHandler):
    """
    This class is the SocketServer "request handler" implementation for the
    licos server.  One instance of this class is created for every control
    connection (not event connections) from a client.  When the event connection
    is opened, the `event_sender` method of the existing instance is spawned as
    a new thread.

    The `handle` method reads commands from the client, dispatches them to
    methods of the same name, and writes the responses back.

    Command methods must be decorated with the `@command` decorator; it
    registers the command for dispatching and avoids boilerplate: if the
    `needcontrol` argument is True, the command will need to be called in the
    controlling session.  If the `needscript` argument is True or False, the
    command can only be called if a script is running or not running,
    respectively.

    Note that the SocketServer interface is such that the request handling is
    done while the constructor runs, i.e. the `__init__` method calls `handle`.
    """

    def __init__(self, request, client_address, server):
        # HACK: the Queue constructor does an import of threading, therefore
        # constructing one here will lock the import system, which leads to
        # clients freezing on login while the startup modules are imported
        try:
            self.event_queue = _queue_freelist.pop()
        except IndexError:
            self.event_queue = Queue()
        # bind often used daemon attributes to self
        self.daemon = server.daemon
        self.controller = server.daemon._controller
        # register self as a new handler
        server.register_handler(self, client_address[0])
        self.sock = request
        self.log = LoggerWrapper(self.daemon.log,
                                 '[handler #%d] ' % self.ident)
        # read buffer
        self._buffer = ''
        try:
            # this calls self.handle()
            BaseRequestHandler.__init__(self, request, client_address, server)
        except CloseConnection:
            pass
        except Exception:
            self.log.exception('unhandled exception')
        self.event_queue.put(stop_queue)
        server.unregister_handler(self.ident)

    def write(self, prefix, msg=None):
        """Write a message to the client."""
        try:
            if msg is None:
                self.sock.sendall(prefix)
            else:
                self.sock.sendall(prefix + LENGTH.pack(len(msg)) + msg)
        except socket.error, err:
            self.log.error('write: connection broken (%s)' % err)
            raise CloseConnection

    def read(self):
        """Read a command and arguments from the client."""
        try:
            # receive first byte (must be STX) + length
            start = self.sock.recv(5)
            if len(start) != 5:
                self.log.error('read: connection broken')
                raise CloseConnection
            if start[0] != STX:
                self.log.error('read: invalid command')
                raise CloseConnection
            # it has a length...
            length, = LENGTH.unpack(start[1:])
            buf = ''
            while len(buf) < length:
                read = self.sock.recv(READ_BUFSIZE)
                if not read:
                    self.log.error('read: connection broken')
                    raise CloseConnection
                buf += read
            return buf.split(RS)
        except socket.error, err:
            self.log.error('read: connection broken (%s)' % err)
            raise CloseConnection

    def check_host(self):
        """Match the connecting host against the daemon's trusted hosts list."""
        for allowed in self.daemon.trustedhosts:
            for possible in self.clientnames:
                if allowed == possible:
                    return
        self.write(NAK, 'permission denied')
        self.log.error('login attempt from untrusted host: %s' %
                       self.clientnames)
        raise CloseConnection

    def check_control(self):
        """Check if the current thread is the session's controlling thread."""
        he = self.controller.controlling_user
        me = self.user[0]
        if self.user[2]:
            # admin may do anything
            return True
        if he is None:
            self.controller.controlling_user = me
            return True
        elif he != me:
            self.write(NAK, 'you do not have control of the session')
            return False
        return True

    def handle(self):
        """Handle a single connection."""
        host, aliases, addrlist = socket.gethostbyaddr(self.client_address[0])
        self.clientnames = [host] + aliases + addrlist
        self.log.debug('connection from %s' % self.clientnames)

        # check trusted hosts list, if nonempty
        if self.daemon.trustedhosts:
            self.check_host()

        credentials = self.read()
        if len(credentials) != 3:
            self.log.error('invalid login: credentials=%s' % credentials)
            self.write(NAK, 'invalid credentials')
            raise CloseConnection
        login, passw, display = credentials

        self.log.info('auth request: login=%s display=%s' % (login, display))

        # check login data (if config.passwd is an empty list, no login
        # control is done and everybody may log in)
        if self.daemon.passwd:
            for entry in self.daemon.passwd:
                if entry[0] == login:
                    self.user = entry
                    break
            else:
                self.log.warning('invalid login name: %s' % login)
                self.write(NAK, 'login not accepted')
                raise CloseConnection
            if passw != self.user[1]:
                self.log.warning('invalid password from user %s' % login)
                self.write(NAK, 'login not accepted')
                raise CloseConnection
        else:
            self.user = [login, passw, True]
        self.log.info('login succeeded')

        # XXX only works for the client that logged in last
        self.display = credentials[2]
        os.environ['DISPLAY'] = self.display

        # acknowledge the login
        self.write(ACK)

        # start main command loop
        while 1:
            request = self.read()
            command, cmdargs = request[0], request[1:]
            if command not in licos_commands:
                self.log.warning('got unknown command: %s' % command)
                self.write(NAK, 'unknown command')
                continue
            licos_commands[command](self, cmdargs)

    # -- Event thread entry point ----------------------------------------------

    def event_sender(self, sock):
        """Take events from the handler instance's event queue and send them
        to the client using the event connection.
        """
        self.log.info('event sender started')
        queue_get = self.event_queue.get
        send = sock.sendall
        while 1:
            item = queue_get()
            if item is stop_queue:
                break
            event, data = item
            try:
                # first, send length header and event name
                send(LENGTH.pack(len(event) + len(data) + 1) + event + RS)
                # then, send data separately (doesn't create temporary strings)
                send(data)
            except Exception, err:
                if isinstance(err, socket.error) and err.args[0] == errno.EPIPE:
                    # close sender on broken pipe
                    self.log.warning('broken pipe in event sender')
                    break
                self.log.exception('exception in event sender; '
                                   'event: %s, data: %r' % (event, data))
        self.log.debug('closing event connection')
        sock.close()

    # -- Script control commands ------------------------------------------------

    @command(needcontrol=False, needscript=False)
    def start(self, name, code):
        """Start a named script within the script thread."""
        if not name:
            name = None
        try:
            self.controller.new_request(ScriptRequest(code, name))
        except RequestError, err:
            self.write(NAK, str(err))
            return
        # take control of the session
        self.controller.controlling_user = self.user[0]
        self.write(ACK)

    @command(needcontrol=False)
    def queue(self, name, code):
        """Start a named script, or queue it if the script thread is busy."""
        if not name:
            name = None
        try:
            self.controller.new_request(ScriptRequest(code, name))
        except RequestError, err:
            self.write(NAK, str(err))
            return
        self.write(ACK)

    @command()
    def unqueue(self, reqno):
        """Mark the given request number (or all, if '*') so that it is not
        executed.
        """
        # XXX: notify other clients
        if reqno == '*':
            self.controller.blocked_reqs.update(
                range(self.controller.reqno_work + 1,
                  self.controller.reqno_latest + 1))
        else:
            reqno = int(reqno)
            if reqno <= self.controller.reqno_work:
                self.write(NAK, 'script already executing')
                return
            self.controller.blocked_reqs.add(reqno)
        self.write(ACK)

    @command(needcontrol=True, needscript=True)
    def update(self, newcode):
        """Update the currently running script."""
        try:
            self.controller.current_script.update(newcode, self.controller)
        except ScriptError, err:
            self.write(NAK, str(err))
            return
        self.write(ACK)

    @command(needcontrol=True, needscript=True, name='break')
    def break_(self):
        """Interrupt the current script."""
        if self.controller.status == STATUS_STOPPING:
            self.write(NAK, 'script is already stopping')
        elif self.controller.status == STATUS_INBREAK:
            self.write(NAK, 'script is already interrupted')
        else:
            self.controller.set_break(None)
            self.log.info('script interrupt request')
            #time.sleep(0.01)
            self.write(ACK)

    @command(needcontrol=True, needscript=True, name='continue')
    def continue_(self):
        """Continue the interrupted script."""
        if self.controller.status == STATUS_STOPPING:
            self.write(NAK, 'could not continue script')
        elif self.controller.status == STATUS_RUNNING:
            self.write(NAK, 'script is not interrupted')
        else:
            self.log.info('script continue request')
            self.controller.set_continue(False)
            self.write(ACK)

    @command(needcontrol=True, needscript=True)
    def stop(self):
        """Abort the interrupted script."""
        if self.controller.status == STATUS_STOPPING:
            self.write(ACK)
        elif self.controller.status == STATUS_RUNNING:
            self.log.info('script stop request while running')
            self.controller.set_break('stop')
            self.write(ACK)
        else:
            self.log.info('script stop request while in break')
            self.controller.set_continue('stop')
            self.write(ACK)

    @command(needcontrol=True)
    def emergency(self):
        """Stop the script unconditionally and run emergency stop functions."""
        if self.controller.status in (STATUS_IDLE, STATUS_IDLEEXC):
            # only execute emergency stop functions
            self.log.warning('emergency stop without script running')
            self.controller.new_request(EmergencyStopRequest())
            self.write(ACK)
            return
        elif self.controller.status == STATUS_STOPPING:
            self.write(ACK)
            return
        self.log.warning('emergency stop request in %s' %
                         self.controller.current_location(True))
        if self.controller.status == STATUS_RUNNING:
            self.controller.set_stop('emergency stop')
        else:
            # in break
            self.controller.set_continue('emergency stop')
        self.write(ACK)

    # -- Asynchronous script interaction ---------------------------------------

    @command(needcontrol=True, needscript=True, name='exec')
    def exec_(self, cmd):
        """Execute a Python statement in the context of the running script."""
        if self.controller.status == STATUS_STOPPING:
            self.write(NAK, 'script is stopping')
            return
        try:
            self.log.info('executing command in script context\n%s' % cmd)
            self.controller.exec_script(cmd)
        except Exception, err:
            self.log.exception('exception in exec command')
            self.write(NAK, 'exception raised while executing cmd: %s' % err)
        else:
            self.write(ACK)

    @command()
    def eval(self, expr):
        """Evaluate and return an expression."""
        try:
            self.log.info('evaluating expresson in script context\n%s' % expr)
            retval = self.controller.eval_expression(expr)
        except Exception, err:
            self.log.exception('exception in eval command')
            self.write(NAK, 'exception raised while evaluating: %s' % err)
        else:
            self.write(STX, serialize(retval))

    @command(needcontrol=True)
    def simulate(self, name, code):
        """Simulate a named script by forking into simulation mode."""
        try:
            self.log.info('running simulation\n%s' % code)
            self.controller.simulate_script(code, name or None)
        except Exception, err:
            self.log.exception('exception in simulate command')
            self.write(NAK, 'exception raised running simulation: %s' % err)
        else:
            self.write(ACK)

    # -- Runtime information commands ------------------------------------------

    @command()
    def getversion(self):
        """Return the daemon's version."""
        self.write(STX, serialize('NICOS-NG daemon version %s' % nicos_version))

    @command()
    def getstatus(self):
        """Return all important status info."""
        current_script = self.controller.current_script
        self.write(STX, serialize(
                ((self.controller.status, self.controller.lineno),
                 current_script and current_script.text or '',
                 self.daemon._messages,
                 self.controller.eval_watch_expressions(),
                 session.explicit_setups,
                 )))

    @command()
    def gethistory(self, key, fromtime, totime):
        """Return history of a cache key, if available."""
        if not session.cache:
            self.write(STX, serialize([]))
        history = session.cache.history('', key, float(fromtime), float(totime))
        self.write(STX, serialize(history))

    # -- Watch expression commands ---------------------------------------------

    @command(needcontrol=True)
    def watch(self, vallist):
        """Add watch expressions."""
        vallist = unserialize(vallist)
        if not isinstance(vallist, list):
            self.write(NAK, 'wrong argument type for add_values: %s' %
                       vallist.__class__.__name__)
            return
        for val in vallist:
            if not isinstance(val, str):
                self.write(NAK, 'wrong type for add_values item: %s' %
                           val.__class__.__name__)
                return
            if ':' not in val:
                val += ':default'
            self.controller.add_watch_expression(val)
        self.write(ACK)

    @command(needcontrol=True)
    def unwatch(self, vallist):
        """Delete watch expressions."""
        vallist = unserialize(vallist)
        if not isinstance(vallist, list):
            self.write(NAK, 'wrong argument type for del_values: %s' %
                       vallist.__class__.__name__)
            return
        for val in vallist:
            if not isinstance(val, str):
                self.write(NAK, 'wrong type for del_values item: %s' %
                           val.__class__.__name__)
                return
            if ':' not in val:
                val += ':default'
            if val.startswith('*:'):
                group = val[val.find(':'):]
                self.controller.remove_all_watch_expressions(group)
            else:
                self.controller.remove_watch_expression(val)
        self.write(ACK)

    # -- Data interface commands -----------------------------------------------

    @command()
    def getdataset(self, index):
        """Get the current dataset."""
        if index == '*':
            try:
                self.write(STX, serialize(session.experiment._last_datasets))
            except AttributeError:  # session.experiment may be None
                self.write(STX, serialize(None))
        else:
            index = int(index)
            try:
                dataset = session.experiment._last_datasets[index]
                self.write(STX, serialize(dataset))
            except (IndexError, AttributeError):
                self.write(STX, serialize(None))

    # -- Miscellaneous commands ------------------------------------------------

    @command(needcontrol=True)
    def unlock(self):
        """Give up control of the session."""
        self.controller.controlling_user = None
        self.write(ACK)

    @command(needcontrol=True, needscript=False)
    def reloadsetup(self):
        """Reload the current setup (and possible NICOS modules), starting a new
        script thread.
        """
        try:
            # stop the script thread
            self.controller.stop_script_thread()
        except RuntimeError:
            # no script thread running
            pass
        # clear sys.modules
        self.daemon._module_manager.purge()
        # start a new script thread, this will reimport all modules
        self.controller.start_script_thread()
        self.write(ACK)

    @command()
    def quit(self):
        """Close the session."""
        me = self.user[0]
        if self.controller.controlling_user == me:
            self.controller.controlling_user = None
        self.log.info('disconnect')
        self.write(ACK)
        raise CloseConnection
