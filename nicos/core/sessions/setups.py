#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the FRM-II
# Copyright (c) 2009-2015 by the NICOS contributors (see AUTHORS)
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
#
# *****************************************************************************

"""
Setup file handling.
"""

import os
from os import path

from nicos.pycompat import exec_, iteritems, listitems


SETUP_GROUPS = set([
    'basic', 'optional', 'lowlevel', 'simulated', 'special'
])


def readSetups(paths, logger):
    infodict = {}
    for rootpath in paths:
        for root, _, files in os.walk(rootpath, topdown=False):
            for filename in files:
                if not filename.endswith('.py'):
                    continue
                modname = filename[:-3]
                try:
                    with open(path.join(root, filename), 'r') as modfile:
                        code = modfile.read()
                except IOError as err:
                    logger.exception('Could not read setup '
                                     'module %r: %s' % (modname, err))
                    infodict[modname] = None
                    continue
                # device() is a helper function to make configuration prettier
                ns = {
                    'device': lambda cls, **params: (cls, params),
                    'setupname': modname,
                }
                try:
                    exec_(code, ns)
                except Exception as err:
                    logger.exception('An error occurred while processing '
                                     'setup %s: %s' % (modname, err))
                    continue
                info = {
                    'description': ns.get('description', modname),
                    'group': ns.get('group', 'optional'),
                    'sysconfig': ns.get('sysconfig', {}),
                    'includes': ns.get('includes', []),
                    'excludes': ns.get('excludes', []),
                    'modules': ns.get('modules', []),
                    'devices': ns.get('devices', {}),
                    'startupcode': ns.get('startupcode', ''),
                    'extended': ns.get('extended', {}),
                    'filename': path.join(root, filename),
                }
                if info['group'] not in SETUP_GROUPS:
                    logger.warning('Setup %s has an invalid group (valid groups '
                                   'are: %s)' % (modname, ', '.join(SETUP_GROUPS)))
                    info['group'] = 'optional'
                if modname in infodict:
                    # setup already exists; override/extend with new values
                    oldinfo = infodict[modname] or {}
                    oldinfo['description'] = ns.get('description',
                                                    oldinfo['description'])
                    oldinfo['group'] = ns.get('group', oldinfo['group'])
                    oldinfo['sysconfig'].update(info['sysconfig'])
                    oldinfo['includes'].extend(info['includes'])
                    oldinfo['excludes'].extend(info['excludes'])
                    oldinfo['modules'].extend(info['modules'])
                    oldinfo['devices'].update(info['devices'])
                    # remove devices overridden by "None" entries completely
                    for devname, value in listitems(oldinfo['devices']):
                        if value is None:
                            del oldinfo['devices'][devname]
                    oldinfo['startupcode'] += '\n' + info['startupcode']
                    oldinfo['extended'].update(info['extended'])
                    oldinfo['filename'] = path.join(root, filename)
                    logger.debug('%r setup partially merged with version '
                                 'from parent directory' % modname)
                else:
                    infodict[modname] = info
    # check if all includes exist
    for name, info in iteritems(infodict):
        if info is None:
            continue  # erroneous setup
        for include in info['includes']:
            if not infodict.get(include):
                logger.error('Setup %s includes setup %s which does not '
                             'exist or has errors' % (name, include))
                infodict[name] = None

    return infodict
