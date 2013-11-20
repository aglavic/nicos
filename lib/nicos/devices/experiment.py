#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the FRM-II
# Copyright (c) 2009-2013 by the NICOS contributors (see AUTHORS)
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
# Module authors:
#   Georg Brandl <georg.brandl@frm2.tum.de>
#   Enrico Faulhaber <enrico.faulhaber@frm2.tum.de>
#
# *****************************************************************************

"""NICOS Experiment devices."""

import os
import re
import time

from os import path
from uuid import uuid1
from StringIO import StringIO

# both will fail on M$win
try:
    from pwd import getpwnam
except ImportError:
    getpwnam = lambda x: (x, '', None, 0, '', 'c:\\', 'cmd')
try:
    from grp import getgrnam
except ImportError:
    getgrnam = lambda x: (x, '', None, [])

from nicos import session
from nicos.core import listof, anytype, oneof, \
     none_or, dictof, mailaddress, usermethod, Device, Measurable, Readable, Param, \
     Dataset, NicosError, ConfigurationError, UsageError, ProgrammingError
from nicos.core.params import subdir
from nicos.core.scan import DevStatistics
from nicos.utils import ensureDirectory, expandTemplate, disableDirectory, \
     enableDirectory, readonlydict, lazy_property, printTable, \
     DEFAULT_FILE_MODE, readFileCounter, updateFileCounter
from nicos.core.utils import DeviceValueDict
from nicos.utils.ftp import ftpUpload
from nicos.utils.emails import sendMail
from nicos.utils.loggers import ELogHandler
from nicos.utils.compression import zipFiles
from nicos.commands.basic import run
from nicos.devices.abstract import ImageStorage
from nicos.core import SIMULATION, MASTER

class Sample(Device):
    """A special device to represent a sample.

    An instance of this class is used as the *sample* attached device of the
    `Experiment` object.  It can be subclassed to add special sample properties,
    such as lattice and orientation calculations, or more parameters describing
    the sample.
    """

    parameters = {
        'samplename':  Param('Sample name', type=str, settable=True,
                             category='sample'),
    }

    def reset(self):
        """Reset experiment-specific information."""
        self.samplename = ''

    def doWriteSamplename(self, name):
        if name:
            session.elog_event('sample', name)


class Experiment(Device):
    """A special singleton device to represent the experiment.

    This class is normally subclassed for specific instruments to e.g. select
    the data paths according to instrument standards.

    Several parameters configure special behavior:

    * `datapath` (usually set proposal-specific by the `new` method) is a list
      of paths where raw data files are stored.  If there is more than one entry
      in the list, the data files are created in the first path and hardlinked
      in the others.
    * `detlist` and `envlist` are lists of names of the currently selected
      standard detector and sample environment devices, respectively.  The
      Experiment object has `detectors` and `sampleenv` properties that return
      lists of the actual devices.
    * `scripts` is managed by the session and should contain a stack of code of
      user scripts currently executed.

    The experiment singleton is available at runtime as
    `nicos.session.experiment`.
    """

    parameters = {
        'title':        Param('Experiment title', type=str, settable=True,
                              category='experiment'),
        'proposal':     Param('Current proposal number or proposal string',
                              type=str, settable=True, category='experiment'),
        'proptype':     Param('Current proposal type', settable=True,
                              type=oneof('service', 'user', 'other')),
        'propprefix':   Param('Prefix of the proposal if is a number', type=str,
                              settable=True, default='p'),
        'users':        Param('User names and emails for the proposal',
                              type=str, settable=True, category='experiment'),
        'localcontact': Param('Local contact for current experiment',
                              type=str, settable=True, category='experiment'),
        'remark':       Param('Current remark about experiment configuration',
                              type=str, settable=True, category='experiment'),
        # XXX: unfortunately tests need this to be non-absolute atm.
        'dataroot':     Param('Root data path under which all proposal specific'
                              ' paths are created', type=str,
                              default='/data', mandatory=True),
        'detlist':      Param('List of default detector device names',
                              type=listof(str), settable=True, userparam=False),
        'envlist':      Param('List of default environment device names to read'
                              ' at every scan point', type=listof(str),
                              settable=True, userparam=False),
        'elog':         Param('True if the electronig logbook should be '
                              'enabled', type=bool, default=True),
        'scripts':      Param('Currently executed scripts',
                              type=listof(str), settable=True, userparam=False),
        'templates':    Param('Name of the directory with script templates '
                              '(relative to dataroot)', type=str),
        'managerights': Param('A dict of en/disableDir/FileMode to manage '
                              'access rights of data dirs on proposal change.',
                              mandatory=False, settable=False, default={},
                              type=dictof(oneof('owner', 'group',
                                  'enableDirMode', 'enableFileMode',
                                  'disableDirMode', 'disableFileMode'), anytype),
                              userparam=False),
        'zipdata':      Param('Whether to zip up experiment data after '
                              'experiment finishes', type=bool, default=True),
        'sendmail':     Param('Whether to send proposal data via email after '
                              'experiment finishes', type=bool, default=False),
        'mailserver':   Param('Mail server name', type=str, settable=True,
                              userparam=False),
        'mailsender':   Param('Mail sender address', type=none_or(mailaddress),
                              settable=True),
        'mailtemplate': Param('Mail template file name (in templates)',
                              type=str, default='mailtext.txt'),
        'reporttemplate': Param('File name of experimental report template '
                                '(in templates)',
                              type=str, default='experimental_report.rtf'),
        'serviceexp':   Param('Name of proposal to switch to after user '
                              'experiment', type=str),
        'servicescript': Param('Script to run for service time', type=str,
                               default='', settable=True),
        'pausecount':   Param('Reason for pausing the count loop', type=str,
                              settable=True, userparam=False),
        'propinfo':     Param('dict of info for the current proposal', type=dict,
                              default={}, settable=False, userparam=False),
        # dir param
        'sampledir':    Param('Sample specific subdir', type=subdir, default='',
                              userparam=False, mandatory=False, settable=True),
        # counter
        'scancounter':  Param('Name of the global scan counter in dataroot',
                              default='scancounter', userparam=False,
                              type=subdir, mandatory=False, settable=False),
        'lastscan':     Param('Last used value of the scancounter', type=int,
                              settable=False, volatile=True, mandatory=False),
        'lastscanfile': Param('Last/Currently written scanfile in this experiment',
                              type=str, settable=False, mandatory=False),
        'imagecounter': Param('Name of the global image counter in dataroot',
                              default='imagecounter', userparam=False,
                              type=subdir, mandatory=False, settable=False),
        'lastimage':    Param('Last used value of the imagecounter', type=int,
                              settable=False, volatile=True, mandatory=False),
        'lastimagefile': Param('Last/Currently written imagefile in this experiment',
                              type=str, settable=False, mandatory=False),
    }

    attached_devices = {
        'sample': (Sample, 'The device object representing the sample'),
    }

    #
    # hooks: may be overriden in derived classes to enhance functionality
    #
    def proposalpath_of(self, proposal):
        """proposalpath of a given proposal"""
        return path.join(self.dataroot, time.strftime("%Y"), proposal)

    @property
    def samplepath(self):
        """path to current active sample, if used, defaults to proposalpath"""
        if self.sampledir:
            return path.join(self.proposalpath, self.sampledir)
        return self.proposalpath

    @property
    def scriptpath(self):
        """path to the scripts of the curent experiment/sample"""
        return path.join(self.samplepath, 'scripts')

    @property
    def elogpath(self):
        """path to the eLogbook of the curent experiment/sample"""
        return path.join(self.samplepath, 'logbook')

    @property
    def datapath(self):
        """path to the data storage of the curent experiment/sample

        here scanfiles and images of image-type detectors will be stored
        """
        return path.join(self.samplepath, 'data')

    @property
    def linkpaths(self):
        """iterable of all paths where 'counted' objects will be linked to.

        At the moment these are scanfiles and images"""
        return tuple()

    @property
    def extrapaths(self):
        """if derived classes need more autocreated dirs, they should be put here!"""
        return tuple()

    @property
    def allpaths(self):
        """return a list of all autocreated paths

        needed to keep track of directory structure upon proposal change
        """
        return [self.proposalpath, self.datapath,
                     self.scriptpath, self.elogpath] + list(self.linkpaths)\
                     + list(self.extrapaths)

    @property
    def templatepath(self):
        """Path where all template files are stored"""
        return path.abspath(path.join(self.dataroot, self.templates))

    @property
    def proposalsymlink(self):
        """dataroot based location of 'current' experiment symlink to maintain,
        or empty string
        """
        return path.join(self.dataroot, 'current')

    @property
    def samplesymlink(self):
        """dataroot based location of 'current' sample symlink to maintain,
        or empty string
        """
        return ''

    @lazy_property
    def skiptemplates(self):
        """list of template filenames which are to be ignored upon creating
        a new experiment
        """
        return []

    def getProposalType(self, proposal):
        """determine proposaltype of a given proposalstring"""
        if proposal in ('template', 'current'):
            raise UsageError(self, 'The proposal names "template" and "current"'
                             ' are reserved and cannot be used')
        # check for defines service 'proposal'
        if self.serviceexp and proposal == self.serviceexp:
            return 'service'
        # all proposals starting with the define prefix are user-type,
        # all others are service
        if self.propprefix:
            if proposal.startswith(self.propprefix):
                return 'user'
            return 'service'
        # if we have no prefix, all number-like proposals >0 are usertype,
        # else service
        try:
            if int(proposal) == 0:
                return 'service'
            return 'user'
        except ValueError:
            return 'service'

    def _beforeNewHook(self):
        """Hook to do something before NewExperiment gets to work"""
        pass

    def _newPropertiesHook(self, proposal, kwds):
        """Hook for querying a database for proposal related stuff

        should return an updated kwds dictionary"""
        return kwds

    def _afterNewHook(self):
        """Hook to do something after NewExperiment did its work"""
        pass

    def _beforeFinishHook(self):
        """Hook to do something before FinishExperiment gets to work"""
        pass

    def _afterFinishHook(self):
        """Hook to do something after FinishExperiment did its work"""
        pass
    #
    # end hooks
    #

    @property
    def proposalpath(self):
        """current proposalpath (defaults to <dataroot>/<year>/<proposal>)

        DON'T OVERRIDE!
        """
        return self.proposalpath_of(self.proposal)

    #
    # counter stuff
    #
    @property
    def scanCounterPath(self):
        return path.join(self.dataroot, self.scancounter)

    def advanceScanCounter(self):
        """increments the value of the scancounter and returns it"""
        updateFileCounter(self.scanCounterPath, self.lastscan + 1)
        return self.lastscan

    def doReadLastscan(self):
        return readFileCounter(self.scanCounterPath)

    def createScanFile(self, nametemplate, *subdirs, **kwargs):
        """creates an scanfile acccording to the given nametemplate in the given
        subdir structure

        returns a tuple containing the basic filename, the path to the file,
        relative to proposalpath, i.e. the 'file path within the current
        experiment' and the filehandle to the already opened (for writing)
        file which has the right FS attributes.
        """
        fullfilename, fp = self.createDataFile(nametemplate, self.lastscan,
                                               *subdirs, **kwargs)
        # setting lastscanfile here might have unwanted side effects if
        # multiple datasinks are used.
        self._setROParam('lastscanfile', path.relpath(fullfilename,
                                                      self.proposalpath))
        return path.basename(fullfilename), fullfilename, fp

    @property
    def imageCounterPath(self):
        return path.join(self.dataroot, self.imagecounter)

    def advanceImageCounter(self, detlist=tuple(), dataset=None):
        """increments the value of the imagecounter if needed and returns it"""
        for det in detlist:
            # only increment for ImageStorage-type detector, also prepare them....
            # -> if two such detectors are used, each one gets a different number
            # -> no file collisions!
            if isinstance(det, ImageStorage):
                updateFileCounter(self.imageCounterPath, self.lastimage + 1)
                det.prepareImageFile(dataset)
        return self.lastimage

    def doReadLastimage(self):
        return readFileCounter(self.imageCounterPath)

    def createImageFile(self, nametemplate, *subdirs, **kwargs):
        """creates an imagefile acccording to the given nametemplate in the
        given subdir structure

        returns a tuple containing the basic filename, the path to the file,
        relative to proposalpath, i.e. the 'file path within the current
        experiment' and the filehandle to the already opened (for writing)
        file which has the right FS attributes.

        the nametemplate may contain references like %(counter)s,
        %(scanpoint)s or %(proposal)s which replaced with appropriate values.
        """
        fullfilename, fp = self.createDataFile(nametemplate, self.lastimage,
                                               *subdirs, **kwargs)
        # setting lastimagefile here might have unwanted side effects if
        # multiple 2D-datasinks are used.
        self._setROParam('lastimagefile', path.relpath(fullfilename,
                                                       self.proposalpath))
        return path.basename(fullfilename), fullfilename, fp

    #
    # datafile stuff
    #
    def getDataDir(self, *subdirs):
        """returns the current path for the data directory in subdir
        structure subdirs

        returned directory is created if it did not exist
        """
        dirname = path.abspath(path.join(self.datapath, *subdirs))
        if self._mode != SIMULATION:
            ensureDirectory(dirname, **self.managerights)
        return dirname

    def getDataFilename(self, filename, *subdirs):
        """returns the current path for given filename in subdir structure
        subdirs

        if filename is an absolute path, ignore the subdirs and start at
        dataroot returned filename is usable 'as-is', i.e. the required
        directory structure is already created.
        """
        if path.isabs(filename):
            fullname = path.join(self.dataroot, filename[1:])
            dirname = path.dirname(fullname)
            if self._mode != SIMULATION:
                ensureDirectory(dirname, **self.managerights)
        else:
            fullname = path.join(self.getDataDir(*subdirs), filename)
        return fullname

    def createDataFile(self, nametemplate, counter, *subdirs, **kwargs):
        """creates and returns a file named according to the given nametemplate
        in the given subdir of the datapath

        if the optional keyworded argument nofile is True, the file is not
        created. This is needed for some data-saving libraries creating the
        file by themselfs. In this case, the filemode is (obviously) not
        managed by us.

        if the nametemlate contains '|' (pipe symbols), it is split there and
        all resulting template names are created as hardlinks.

        In 'simulation' mode this returns a file-like object to avoid accessing
        or changing the filesystem.
        """
        if '%(' in nametemplate:
            kwds = dict(self.propinfo)
            kwds.update(kwargs)
            kwds.update(counter=counter, proposal=self.proposal)
            try:
                filename = nametemplate % DeviceValueDict(kwds)
            except KeyError:
                self.log.error('Can\'t create datafile, illegal key in '
                               'nametemplate!')
                raise
        else:
            filename = nametemplate % counter
        otherfiles = []
        if '|' in filename:
            otherfiles = filename.split('|')
            filename = otherfiles.pop(0)
        fullfilename = self.getDataFilename(filename, *subdirs)
        if path.isfile(fullfilename):
            raise ProgrammingError('Data file named %r already exists! '
                                   'Check filenametemplates !' %
                                   fullfilename)
        if self._mode == SIMULATION or kwargs.get('nofile'):
            self.log.debug('Not creating any file, returning a StringIO buffer instead.')
            fp = StringIO()
        else:
            self.log.debug('Creating file %r' % fullfilename)
            fp = open(fullfilename, 'wb')
            if self.managerights:
                os.chmod(fullfilename,
                         self.managerights.get('enableFileMode',
                                                DEFAULT_FILE_MODE))
            linkfunc = os.link if hasattr(os,  'link') else \
                       os.symlink if hasattr(os, 'symlink') else None
            if linkfunc:
                for otherfile in otherfiles:
                    self.log.debug('Linking %r to %r' % (self.getDataFilename(
                                                otherfile, *subdirs), fullfilename))
                    try:
                        linkfunc(fullfilename, self.getDataFilename(otherfile, *subdirs))
                    except OSError:
                        self.log.warning('linking %r to %r failed, ignoring' %
                                         (self.getDataFilename(otherfile, *subdirs),
                                          fullfilename))
            else:
                self.log.warning('can\'t link datafiles, no os support!')
        return (fullfilename, fp)


    def linkDataFiles(self, filename, *subdirs):
        """links all datapaths to the same file...

        may be overriden in custom experiments if they don't like the names...
        """
        if not self.linkpaths:
            return
        if not hasattr(os, 'link'):
            self.log.warning(self, 'your OS can not make links, no links '
                             'created!')
            return
        fullname = path.join(self.getDataDir(*subdirs), filename)
        if not os.exist(fullname):
            self.log.error(self, 'linkDataFiles: data file %r does not exist!' %
                           fullname)
            return
        for linktarget in self.linkpaths:
            link = path.join(linktarget, '_'.join(subdirs + tuple(filename)))
            if self._mode != SIMULATION:
                ensureDirectory(path.dirname(link), **self.managerights)
                os.link(fullname, link)

    #
    # nicos interface
    #
    def doInit(self, mode):
        self._last_datasets = []
        instname = session.instrument and session.instrument.instrument or ''
        if self.elog and mode != SIMULATION:
            ensureDirectory(path.join(self.proposalpath, 'logbook'))
            session.elog_event('directory', (self.proposalpath,
                                             instname, self.proposal))
            self._eloghandler = ELogHandler()
            # only enable in master mode, see below
            self._eloghandler.disabled = session.mode != MASTER
            session.addLogHandler(self._eloghandler)
        if self.templates == '':
            self._setROParam('templates',
                path.abspath(path.join(session.config.control_path, 'template')))

    def doUpdateManagerights(self, mrinfo):
        """check and transform the managerights dict into values used later"""
        if mrinfo in (None, False): # ease upgrade 2.4->2.5
            self._setROParam('managerights', readonlydict())
        elif mrinfo:
            changed = dict()
            # check values and transform them to save time later
            for k, f in [('owner', getpwnam), ('group', getgrnam)]:
                v = mrinfo.get(k)
                if isinstance(v, str):
                    try:
                        r = f(v)
                    except Exception, e:
                        raise ConfigurationError(self,
                            'managerights: illegal value for key %r: %r (%s)' %\
                                              (k, v, e), exc=1)
                    if r[2] is not None:
                        changed[k] = r[2]
            for k in ['enableDirMode', 'enableFileMode',
                       'disableDirMode', 'disableFileMode']:
                v = mrinfo.get(k, None)
                if isinstance(v, str):
                    try:
                        r = int(v,8)  # filemodes are given in octal!
                    except Exception, e:
                        raise ConfigurationError(self,
                            'managerights: illegal value for key %r: %r (%s)' %\
                                              (k, v, e), exc=1)
                    if r is not None:
                        changed[k] = r
            if changed:
                d = dict(mrinfo)
                d.update(changed)
                # assignment would trigger doUpdateManagerights again, looping!
                self._setROParam('managerights', readonlydict(d))

    #
    # Experiment handling: New&Finish
    #
    @usermethod
    def new(self, proposal, title=None, localcontact=None, user=None, **kwds):
        """Called by `.NewExperiment`."""
        if self._mode == SIMULATION:
            raise UsageError('Simulating switching experiments is not supported!')
        # determine real proposal number: some instruments assign a prefix to
        # numeric proposals
        if isinstance(proposal, (int, long)):
            proposal = '%s%d' % (self.propprefix, proposal)
        self.log.debug('new proposal real name is %s' % proposal)

        # check proposal type (can raise)
        proptype = self.getProposalType(proposal)
        self.log.debug('new proposal type is %s' % proptype)

        # check if we should finish the experiment first
        if self.serviceexp and proptype == self.proptype == 'user':
            self.log.error('cannot switch directly to new user experiment, '
                           'please use "FinishExperiment" first')
            return

        self._beforeNewHook()

        # allow instruments to override (e.g. from proposal DB)
        if title:
            kwds['title'] = title
        if user:
            kwds['user'] = user
        if localcontact:
            kwds['localcontact'] = localcontact
        kwds['proposal'] = proposal

        # need to enable before checking templated files...
        enableDirectory(self.proposalpath_of(proposal), **self.managerights)

        if proptype != 'service':
            if self.templates:
                try:
                    self.checkTemplates(proposal, kwds) # may raise
                except Exception:
                    # restore previous state completely, thus disabling
                    if self.managerights:
                        disableDirectory(self.proposalpath_of(proposal),
                                         **self.managerights)
                    raise

        #all prepared, do the switch
        # remove access rights to old proposal if wanted
        if self.managerights and self.proptype == 'user':
            try:
                disableDirectory(self.proposalpath, **self.managerights)
            except Exception:
                self.log.warning('could not remove permissions for old '
                                 'experiment directory', exc=1)
            else:
                self.log.debug('disabled directory %s' % self.proposalpath)

        # reset all experiment dependent parameters and values to defaults
        self.remark = ''
        self.sample.reset()
        self.envlist = []
        for notifier in session.notifiers:
            notifier.reset()
        self._last_datasets = []
        self._setROParam('lastscanfile','') # none written yet
        self._setROParam('lastimagefile','')

        # set new experiment properties given by caller
        self.proptype = proptype
        kwds = self._newPropertiesHook(proposal, kwds)
        self._setROParam('propinfo', kwds)
        self.title = kwds.get('title', '')
        self.users = kwds.get('user', '')
        self.localcontact = kwds.get('localcontact', '')

        # newSample also calls datapathChanged, which (re-)creates all needed
        # dirs and adjusts possible symlinks
        self.proposal = proposal
        self.newSample(kwds.get('sample', ''), {})

        # debug output
        self.log.info('experiment directory is now %s' % self.proposalpath)
        self.log.info('script directory is now %s' % self.scriptpath)
        self.log.info('data directory is now %s' % self.datapath)

        # notify logbook
        session.elog_event('newexperiment', (proposal, title))
        session.elog_event('setup', list(session.explicit_setups))

        # expand templates
        if proptype != 'service':
            if self.templates:
                kwds['proposal'] = self.proposal
                self.handleTemplates(proposal, kwds)
            self.log.info('New experiment %s started' % proposal)
        else:
            if self.servicescript:
                run(self.servicescript)
            else:
                self.log.debug('not running service script, none configured')
            self.log.info('Maintenance time started')

        # send 'experiment' change event before the last hook
        session.experimentCallback(self.proposal) # maybe better after the last hook?

        self._afterNewHook()

    @usermethod
    def finish(self, *args, **kwds):
        """Called by `.FinishExperiment`."""
        self._beforeFinishHook()

        # update metadata
        propinfo = dict(self.propinfo)
        propinfo.setdefault('from_time', time.time())
        propinfo['to_time'] = time.time()
        self._setROParam('propinfo', propinfo)

        # zip up the experiment data if wanted
        if self.proptype == 'user':
            self._generateExpReport(**kwds)
            zipname = None
            if self.zipdata or self.sendmail:
                zipname = self._zip()
            if self.sendmail and zipname:
                receivers = None
                if args:
                    receivers = args[0]
                else:
                    receivers = self.propinfo.get('user_email', receivers)
                receivers = kwds.get('receivers', kwds.get('email', receivers))
                try:
                    if receivers:
                        self._mail(receivers, zipname)
                except Exception:
                    self.log.warning('could not send the data via email',
                                     exc=1)

        self._afterFinishHook()

        # switch to service experiment (will hide old data if configured)
        if self.serviceexp:
            self.new(self.serviceexp)
        else:
            self.log.debug('no service experiment configured, cannot switch')

    #
    # template stuff
    #
    def getTemplate(self, tmplname):
        """returns the content of the requested template"""
        try:
            with open(path.join(self.templatepath, tmplname), 'rb') as f:
                return f.read()
        except OSError, e:
            self.log.error(self, 'Can\'t read template %r (%s), please check settings' %
                            (tmplname, e))
            raise

    def iterTemplates(self, only_dot_template=True):
        """iterator of all templates (and their content)..."""
        if not path.isdir(self.templatepath):
            return
        filelist = os.listdir(self.templatepath)
        for fn in filelist:
            if self.mailtemplate and fn.startswith(self.mailtemplate):
                continue
            if self.reporttemplate and fn.startswith(self.reporttemplate):
                continue
            if fn in self.skiptemplates:
                continue
            if only_dot_template and not fn.endswith('.template'):
                continue
            yield (fn, self.getTemplate(fn))

    def checkTemplates(self, proposal, kwargs):
        """try to fill in all templates to see if some keywords are missing"""
        if self._mode == SIMULATION:
            return # dont touch fs if in simulation!
        allmissing = []
        alldefaulted = []
        for fn, content in self.iterTemplates(only_dot_template=True):
            newfn = fn[:-9] # strip ".template" from the name
            newfn, _, _ = expandTemplate(newfn, kwargs)

            finalname = path.join(self.proposalpath_of(proposal), self.sampledir,
                                  'scripts', newfn)

            if path.isfile(finalname):
                self.log.debug('skipping already translated file %r' % newfn)
                continue

            self.log.debug('checking template %r' % fn)
            _, defaulted, missing = expandTemplate(content, kwargs)
            if missing:
                allmissing.extend(missing)
            if defaulted:
                alldefaulted.extend(defaulted)

        if not allmissing and not alldefaulted:
            return

        # format nicely
        headers = ['missing keyword', 'defaultvalue', 'description']
        errkwds = [item['key'] for item in allmissing]

        items = [[item['key'], item['default'] or '', item['description'] or '']
                    for item in allmissing + alldefaulted]
        def myprintfunc(what):
            if what.strip().split(' ')[0] in errkwds:
                self.log.error(what)
            else:
                self.log.warning(what)

        printTable(headers, items, myprintfunc)
        if allmissing:
            raise NicosError('some keywords are missing, please provide them as '
                              'keyword arguments to `NewExperiment`')

    def handleTemplates(self, proposal, kwargs):
        if self._mode == SIMULATION:
            return # dont touch fs if in simulation!
        for fn, content in self.iterTemplates(only_dot_template=False):
            istemplate = fn.endswith('.template')
            newfn = fn
            if istemplate:
                newfn = fn[:-9] # remove '.template' at end
                newfn, _, _ = expandTemplate(newfn, kwargs)
                self.log.debug('%s -> %s' % (fn, newfn))
            else:
                self.log.debug('%s is no template, just copy it.' % fn)

            finalname = path.join(self.scriptpath, newfn)
            if path.isfile(finalname):
                self.log.info('not overwriting existing file %s' % newfn)
                continue

            if istemplate:
                self.log.debug('templating file content of %r' % fn)
                try:
                    content, _, _ = expandTemplate(content, kwargs)
                except Exception:
                    self.log.warning('could not translate template file %s' % fn,
                                     exc=1)
            # save result
            with open(finalname, 'wb') as fp:
                fp.write(content)
            os.chmod(finalname, self.managerights.get('enableFileMode',
                                                      DEFAULT_FILE_MODE))

    #
    # various helpers
    #
    def _zip(self):
        """Zip all files in the current experiment folder into a .zip file."""
        if self._mode == SIMULATION:
            return # dont touch fs if in simulation!
        self.log.info('zipping experiment data, please wait...')
        zipname = zipFiles(path.join(self.proposalpath, '..',
                                     self.proposal + '.zip'),
                           self.proposalpath)
        self.log.info('done: stored as ' + zipname)
        return zipname

    def _mail(self, receivers, zipname, maxAttachmentSize=10000000):
        """Send a mail with the experiment data"""

        if self._mode == SIMULATION:
            return # dont touch fs if in simulation!
        # check parameters
        if not self.mailserver:
            raise NicosError('%s.mailserver parameter is not set' % self)
        if not self.mailsender:
            raise NicosError('%s.mailsender parameter is not set' % self)
        if '@' not in receivers:
            raise NicosError('need full email address(es) (\'@\' missing!)')

        # read and translate mailbody template
        self.log.debug('looking for template in %r' % self.templatepath)
        try:
            mailbody = self.getTemplate(self.mailtemplate)
        except IOError:
            self.log.warning('reading mail template %s failed' %
                             self.mailtemplate, exc=1)
            mailbody = 'See data in attachment.'

        stats = self._statistics()
        stats.update(self.propinfo)
        mailbody, _, _ = expandTemplate(mailbody, stats)

        instname = session.instrument and session.instrument.instrument or '?'
        topic = 'Your recent experiment %s on %s from %s to %s' % \
              (self.proposal, instname, stats.get('from_date'), stats.get('to_date'))

        if os.stat(zipname).st_size < 10000000:
            # small enough -> send directly
            sendMail(self.mailserver, receivers, self.mailsender, topic, mailbody,
                     [zipname], 1 if self.loglevel == 'debug' else 0)
        else:
            # not small enough -> upload and send link
            self.log.info('Zipfile is too big to send via email and will be '
                          'uploaded to a temporary storge for download.')
            mailbody += """
            =====

            Due to size limitations, the attachment was put to a temporary storage,
            where it will be kept for SEVEN DAYS and then it will be deleted.

            Please download the data from:
            %s
            within the next seven days.

            We apologize for the inconvinience.
            """ % ftpUpload(zipname)
            sendMail(self.mailserver, receivers, self.mailsender, topic, mailbody,
                     [], 1 if self.loglevel == 'debug' else 0)

        # "hide" compressed file by moving it into the proposal directory
        self.log.info('moving compressed file to ' + self.proposalpath)
        try:
            os.rename(zipname,
                      path.join(self.proposalpath, path.basename(zipname)))
        except Exception:
            self.log.warning('moving compressed file into proposal dir failed',
                             exc=1)
            # at least withdraw the access rights
            os.chmod(zipname, self.managerights.get('disableFileMode', 0400))

    def _setMode(self, mode):
        if self.elog:
            self._eloghandler.disabled = mode != MASTER
        Device._setMode(self, mode)

    @usermethod
    def addUser(self, name, email=None, affiliation=None):
        """Called by `.AddUser`."""
        if email:
            user = '%s <%s>' % (name, email)
        else:
            user = name
        if affiliation is not None:
            user += ' (' + affiliation + ')'
        if not self.users:
            self.users = user
        else:
            self.users = self.users + ', ' + user
        self.log.info('User "%s" added' % user)

    @usermethod
    def newSample(self, name, parameters):
        """Called by `.NewSample`."""
        self.sample.samplename = name
        for param, value in parameters.iteritems():
            setattr(self.sample, param, value)
        self.datapathChanged()  # may have changed...

    def _statistics(self):
        """Return some statistics about the current experiment in a dict.
        May need improvements."""

        # get start of proposal from cache history
        hist, d = [], 7
        while not hist and d < 60:
            hist = self.history('proposal', -d*24)
            d += 7
        if hist:
            from_time = hist[-1][0]
        to_time = time.time()
        from_date = time.strftime('%a, %d. %b %Y', time.localtime(from_time))
        to_date = time.strftime('%a, %d. %b %Y', time.localtime(to_time))

        # check number of (scan) data files
        # maybe this should be live collected in propinfo and not
        # after the experiment by scanning the filesystem.
        numscans = 0
        firstscan = 99999999
        lastscan = 0
        scanfilepattern = re.compile(r'%s_(\d{8})\.dat$' % self.proposal)
        for fn in os.listdir(self.datapath):
            m = scanfilepattern.match(fn)
            if m:
                firstscan = min(firstscan, int(m.group(1)))
                lastscan = max(lastscan, int(m.group(1)))
                numscans += 1

        d = {
            'proposal':  self.proposal,
            'from_date': from_date,
            'to_date':   to_date,
            'firstfile': '%08d' % firstscan,
            'lastfile':  '%08d' % lastscan,
            'numscans':  str(numscans),
            'title':     self.title,
            'users':     self.users,
            'samplename':     self.sample.samplename,
            'localcontact': self.localcontact,
            'instrument' : session.instrument.instrument,
        }
        d.update(self.propinfo)
        return d

    def _generateExpReport(self, **kwds):
        if self._mode == SIMULATION:
            return # dont touch fs if in simulation!
        # read and translate ExpReport template
        self.log.debug('looking for template in %r' % self.templatepath)
        try:
            data = self.getTemplate(self.reporttemplate)
        except IOError:
            self.log.warning('reading Experimental Report template %s failed, '
                             'please fetch a copy from the UserOffice' %
                             self.reporttemplate)
            return # nothing to do about it.

        # prepare template....
        # can not do this directly in rtf as {} have special meaning....
        # KEEP IN SYNC WHEN CHANGING THE TEMPLATE!
        # reminder: format is {{key:default#description}},
        # always specify default here !
        #
        # first clean up template
        data = data.replace('\\par Please replace the place holder in the upper'
            ' part (brackets <>) by the appropriate values.', '')
        data = data.replace('\\par Description', '\\par\n\\par '
            'Please check all pre-filled values carefully! They were partially '
            'read from the proposal and might need correction.\n'
            '\\par\n'
            '\\par Description')
        # replace placeholders with templating markup
        data = data.replace('<your title as mentioned in the submission form>',
                            '"{{title:The title of your proposed experiment}}"')
        data = data.replace('<proposal No.>', 'Proposal {{proposal:0815}}')
        data = data.replace('<your name> ', '{{users:A. Guy, A. N. Otherone}}')
        data = data.replace('<coauthor, same affilation> ', 'and coworkers')
        data = data.replace('<other coauthor> ', 'S. T. Ranger')
        data = data.replace('<your affiliation>, }',
                            '{{affiliation:affiliation of main proposer and '
                            'coworkers}}, }\n\\par ')
        data = data.replace('<other affiliation>', 'affiliation of coproposers '
                            'other than 1')
        data = data.replace('<Instrument used>',
                            '{{instrument:<The Instrument used>}}')
        data = data.replace('<date of experiment>', '{{from_date:01.01.1970}} '
                            '- {{to_date:12.03.2038}}')
        data = data.replace('<local contact>', '{{localcontact:L. Contact '
                            '<l.contact@frm2.tum.de>}}')

        # collect info
        stats = self._statistics()
        stats.update(self.propinfo)
        stats.update(kwds)

        # template data
        newcontent, _, _ = expandTemplate(data, stats)
        newfn, _, _ = expandTemplate(self.reporttemplate, stats)

        with open(path.join(self.proposalpath, newfn), 'wb') as fp:
            fp.write(newcontent)
        self.log.info('An experimental report template was created at %r for '
                      'your convenience.' % path.join(self.proposalpath, newfn))


    def doWriteRemark(self, remark):
        if remark:
            session.elog_event('remark', remark)

    def datapathChanged(self):
        if self._mode == SIMULATION:
            return # dont touch fs if in simulation!

        for _dir in self.allpaths:
            ensureDirectory(_dir, **self.managerights)

        # manage symlinks, if requested
        if self.proposalsymlink and path.islink(self.proposalsymlink):
            self.log.debug('removing symlink %s' % self.proposalsymlink)
            os.unlink(self.proposalsymlink)
        if self.proposalsymlink and hasattr(os, 'symlink'):
            self.log.debug('setting symlink %s to %s' %
                           (self.proposalsymlink, self.proposalpath))
            os.symlink(self.proposalpath, self.proposalsymlink)

        if self.samplesymlink and path.islink(self.samplesymlink):
            self.log.debug('removing symlink %s' % self.samplesymlink)
            os.unlink(self.samplesymlink)
        if self.samplesymlink and hasattr(os, 'symlink'):
            self.log.debug('setting symlink %s to %s' %
                           (self.samplesymlink, self.sampledir))
            os.symlink(self.sampledir, self.samplesymlink)

        # inform elog about changed paths.
        if self.elog:
            instname = session.instrument and session.instrument.instrument or ''
            session.elog_event('directory', (self.proposalpath, instname, self.proposal))

    #
    # dataset stuff
    #
    def createDataset(self, scantype=None):
        dataset = Dataset()
        dataset.uid = str(uuid1())
        dataset.sinks = [sink for sink in session.datasinks
                         if sink.isActive(scantype)]
        dataset.started = time.localtime()
        dataset.updateHeaderInfo()
        return dataset

    @property
    def sample(self):
        return self._adevs['sample']

    #
    # Detectorlist
    #
    @property
    def detectors(self):
        if self._detlist is not None:
            return self._detlist[:]
        detlist = []
        all_created = True
        for detname in self.detlist:
            try:
                det = session.getDevice(detname, source=self)
            except Exception:
                self.log.warning('could not create %r detector device' %
                                 detname, exc=1)
                all_created = False
            else:
                if not isinstance(det, Measurable):
                    self.log.warning('cannot use device %r as a '
                                     'detector: it is not a Measurable' % det)
                    all_created = False
                else:
                    detlist.append(det)
        if all_created:
            self._detlist = detlist
        return detlist[:]

    def setDetectors(self, detectors):
        dlist = []
        for det in detectors:
            if isinstance(det, Device):
                det = det.name
            if det not in dlist:
                dlist.append(det)
        self.detlist = dlist
        dummy = self.detectors  # try to create them right now
        session.elog_event('detectors', dlist)

    def doUpdateDetlist(self, detectors):
        self._detlist = None  # clear list of actual devices

    #
    # Environment devicelist
    #
    @property
    def sampleenv(self):
        if self._envlist is not None:
            return self._envlist[:]
        devlist = []
        all_created = True
        for devname in self.envlist:
            try:
                if ':' in devname:
                    devname, stat = devname.split(':')
                    dev = session.getDevice(devname, source=self)
                    dev = DevStatistics.subclasses[stat](dev)
                else:
                    dev = session.getDevice(devname, source=self)
            except Exception:
                self.log.warning('could not create %r environment device' %
                                 devname, exc=1)
                all_created = False
            else:
                if not isinstance(dev, (Readable, DevStatistics)):
                    self.log.warning('cannot use device %r as '
                                     'environment: it is not a Readable' % dev)
                    all_created = False
                else:
                    devlist.append(dev)
        if all_created:
            self._envlist = devlist
        return devlist[:]

    def setEnvironment(self, devices):
        dlist = []
        for dev in devices:
            if isinstance(dev, Device):
                dev = dev.name
            elif isinstance(dev, DevStatistics):
                dev = str(dev)
            if dev not in dlist:
                dlist.append(dev)
        self.envlist = dlist
        dummy = self.sampleenv  # try to create them right now
        session.elog_event('environment', dlist)

    def doUpdateEnvlist(self, devices):
        self._envlist = None  # clear list of actual devices
