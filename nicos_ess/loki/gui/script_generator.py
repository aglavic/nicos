#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the MLZ
# Copyright (c) 2009-2021 by the NICOS contributors (see AUTHORS)
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
#
#   Ebad Kamil <Ebad.Kamil@ess.eu>
#   Matt Clarke <matt.clarke@ess.eu>
#
# *****************************************************************************

"""LoKI Script Generator."""

from enum import Enum


class TransOrder(Enum):
    TRANSFIRST = 0
    SANSFIRST = 1
    TRANSTHENSANS = 2
    SANSTHENTRANS = 3
    SIMULTANEOUS = 4


def _get_position(value):
    return f"set_position({value})"


def _get_sample(name, thickness):
    return f"set_sample('{name}', {thickness})"


def _do_trans(row_values, trans_duration_type):
    template = (
        f"# Sample = {row_values['sample']}\n"
        f"{_get_sample(row_values['sample'], row_values['thickness'])}\n"
        f"{_get_position(row_values['position'])}\n"
        f"do_trans({row_values['trans_duration']}, "
        f"'{trans_duration_type}')\n")
    return template


def _do_sans(row_values, sans_duration_type):
    template = (
        f"# Sample = {row_values['sample']}\n"
        f"{_get_sample(row_values['sample'], row_values['thickness'])}\n"
        f"{_get_position(row_values['position'])}\n"
        f"do_sans({row_values['sans_duration']}, "
        f"'{sans_duration_type}')\n")
    return template


def _do_simultaneous(row_values, sans_duration_type):
    template = (
        f"# Sample = {row_values['sample']}\n"
        f"{_get_sample(row_values['sample'], row_values['thickness'])}\n"
        f"{_get_position(row_values['position'])}\n"
        f"do_sans_simultaneous({row_values['sans_duration']}, "
        f"'{sans_duration_type}')\n")
    return template


class TransFirst:
    def generate_script(self, labeled_data, trans_duration_type,
                        sans_duration_type):
        template = ""
        for row_values in labeled_data:
            template += _do_trans(row_values, trans_duration_type)
            template += "\n"

        for row_values in labeled_data:
            template += _do_sans(row_values, sans_duration_type)
            template += "\n"
        return template


class SansFirst:
    def generate_script(self, labeled_data, trans_duration_type,
                        sans_duration_type):
        template = ""
        for row_values in labeled_data:
            template += _do_sans(row_values, sans_duration_type)
            template += "\n"

        for row_values in labeled_data:
            template += _do_trans(row_values, trans_duration_type)
            template += "\n"
        return template


class TransThenSans:
    def generate_script(self, labeled_data, trans_duration_type,
                        sans_duration_type):
        template = ""
        for row_values in labeled_data:
            template += _do_trans(row_values, trans_duration_type)
            template += _do_sans(row_values, sans_duration_type)
            template += "\n"
        return template


class SansThenTrans:
    def generate_script(self, labeled_data, trans_duration_type,
                        sans_duration_type):
        template = ""
        for row_values in labeled_data:
            template += _do_sans(row_values, sans_duration_type)
            template += _do_trans(row_values, trans_duration_type)
            template += "\n"
        return template


class Simultaneous:
    def generate_script(self, labeled_data, trans_duration_type,
                        sans_duration_type):
        template = ""
        for row_values in labeled_data:
            template += _do_simultaneous(row_values, sans_duration_type)
            template += "\n"
        return template


class ScriptGenerator:
    @classmethod
    def from_trans_order(cls, trans_order):
        classes_by_trans_order = {
            TransOrder.TRANSFIRST: TransFirst,
            TransOrder.SANSFIRST: SansFirst,
            TransOrder.TRANSTHENSANS: TransThenSans,
            TransOrder.SANSTHENTRANS: SansThenTrans,
            TransOrder.SIMULTANEOUS: Simultaneous
        }
        if trans_order in classes_by_trans_order:
            return classes_by_trans_order[trans_order]()
        else:
            raise NotImplementedError(
                f"Unspecified trans order {trans_order.name}")
