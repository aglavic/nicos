#  -*- coding: utf-8 -*-
# *****************************************************************************
# Module:
#   $Id$
#
# Description:
#   NICOS Experiment devices
#
# Author:
#   Georg Brandl <georg.brandl@frm2.tum.de>
#
#   The basic NICOS methods for the NICOS daemon (http://nicos.sf.net)
#
#   Copyright (C) 2009 Jens Krüger <jens.krueger@frm2.tum.de>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# *****************************************************************************

"""
NICOS Experiment devices.
"""

__author__  = "$Author$"
__date__    = "$Date$"
__version__ = "$Revision$"


from nicm.utils import listof
from nicm.device import Device


class Experiment(Device):
    """A special singleton device to represent the experiment."""

    parameters = {
        'title': (str, '', False, 'Experiment title.'),
        'proposalnumber': (int, 0, False, 'Proposal number.'),
        'users': (listof(str), [], False, 'User names.'),
    }

    def doSetTitle(self, value):
        self._params['title'] = value

    def doSetProposalnumber(self, value):
        self._params['proposalnumber'] = value

    def doSetUsers(self, value):
        self._params['users'] = value

    def new(self, proposalnumber, title=None):
        if not isinstance(proposalnumber, int):
            proposalnumber = int(proposalnumber)
        self.proposalnumber = proposalnumber
        if title is not None:
            self.title = title
        self.users = []

    def addUser(self, name, email, affiliation=None):
        user = '%s <%s>' % (name, email)
        if affiliation is not None:
            user += ' -- ' + affiliation
        self._params['users'].append(user)
