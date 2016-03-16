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

"""New acquisition commands (scan and count)."""

from nicos.commands import helparglist, usercommand
from nicos.commands.output import printinfo, printwarning
from time import sleep, time as currenttime

from nicos import session
from nicos.core.device import Measurable, SubscanMeasurable
from nicos.core.constants import SIMULATION
from nicos.core.errors import UsageError, NicosError
from nicos.core.utils import waitForStatus
from nicos.core.data import dataman, INTERRUPTED, FINAL
from nicos.pycompat import number_types, string_types


def _wait_for_continuation(delay, only_pause=False):
    """Wait until any countloop requests are processed and the watchdog
    "pausecount" is empty.

    Return True if measurement can continue, or False if detectors should be
    stopped.
    """
    req, current_msg = session.countloop_request  # pylint: disable=E0633
    session.countloop_request = None
    if only_pause and req != 'pause':
        # for 'finish' requests, we don't want to finish *before* starting the
        # measurement, because then we don't have any results to return
        session.log.info('request for early finish ignored, not counting')
        return True
    exp = session.experiment
    if req == 'finish':
        session.log.warning('counting stopped: ' + current_msg)
        return False
    # allow the daemon to pause here, if we were paused by it
    session.breakpoint(3)
    # but after continue still check for other conditions
    while exp.pausecount:
        if exp.pausecount != current_msg:
            current_msg = exp.pausecount
            session.log.warning('counting paused: ' + current_msg)
        sleep(delay)
    session.log.info('counting resumed')
    return True


def acquire(point, preset):
    """Low-level acquisition function.

    The loop delay is configurable in the instrument object, and defaults to
    0.025 seconds.

    The result is stored in the given argument, which must be an empty list.
    This is so that a result can be returned even when a stop exception is
    propagated upwards.
    """
    # put detectors in a set and discard them when completed
    detset = set(point.detectors)
    delay = (session.instrument and session.instrument.countloopdelay or 0.025
             if session.mode != SIMULATION else 0.0)

    session.beginActionScope('Counting')
    if session.countloop_request:
        _wait_for_continuation(delay, only_pause=True)
    dataman.updateMetainfo()
    point.started = currenttime()
    try:
        for det in point.detectors:
            det.start(**preset)
    except:
        session.endActionScope()
        raise
    sleep(delay)
    try:
        while True:
            looptime = currenttime()
            for det in list(detset):
                if session.mode != SIMULATION:
                    quality = det.duringMeasureHook(looptime - point.started)
                if det.isCompleted():
                    det.finish()
                    quality = FINAL
                if quality:
                    try:
                        res = det.read(), det.readArrays()
                    except Exception:
                        det.log.exception('error reading measurement data')
                        res = None
                    dataman.putResults(quality, {det.name: res})
                if quality == FINAL:
                    detset.discard(det)
            if not detset:
                # all detectors finished measuring
                break
            if session.countloop_request:
                for det in detset:
                    if not det.pause():
                        session.log.warning(
                            'detector %r could not be paused' % det.name)
                if not _wait_for_continuation(delay):
                    for det in detset:
                        # next iteration of loop will see det is finished
                        det.finish()
                else:
                    for det in detset:
                        det.resume()
            sleep(delay)
    except BaseException as e:
        point.finished = currenttime()
        if e.__class__.__name__ != 'ControlStop':
            session.log.warning('Exception during count, trying to save data',
                                exc=True)
        for det in detset:
            try:
                # XXX: in theory, stop() can return True or False to indicate
                # whether saving makes sense.
                #
                # However, it might be better to leave that to the data sink
                # handling the INTERRUPTED quality.
                det.stop()
                res = det.read(), det.readArrays()
            except Exception:
                det.log.exception('error reading measurement data')
                res = None
            dataman.putResults(INTERRUPTED, {det.name: res})
        raise
    finally:
        point.finished = currenttime()
        session.endActionScope()


class CountResult(list):
    __display__ = None


@usercommand
@helparglist('[detectors], [presets]')
def newcount(*detlist, **preset):
    """Perform a single counting.

    With preset arguments, this preset is used instead of the default preset.

    With detector devices as arguments, these detectors are used instead of the
    default detectors set with `SetDetectors()`.

    Examples:

    >>> count()             # count once with the default preset and detectors
    >>> count(t=10)         # count once with time preset of 10 seconds
    >>> count(psd, t=10)    # count 10 seconds with the psd detector

    Within a manual scan, this command is also used to perform the count as one
    point of the manual scan.
    """
    # sanitize detector list; support count(1) and count('info')
    detectors = []
    for det in detlist:
        if isinstance(det, number_types):
            preset['t'] = det
            continue
        elif isinstance(det, string_types):
            preset['info'] = det  # XXX
            continue
        if not isinstance(det, Measurable):
            raise UsageError('device %s is not a measurable device' % det)
        detectors.append(det)
    # check if manual scan is active (XXX)
    # scan = getattr(session, '_manualscan', None)
    # if scan is not None:
    #     if detectors:
    #         raise UsageError('cannot specify different detector list '
    #                          'in manual scan')
    #     return scan.step(**preset)
    # counting without detectors is not useful, but does not error out
    if not detectors:
        detectors = session.experiment.detectors
        if not detectors:
            printwarning('counting without detector, use SetDetectors() '
                         'to select which detector(s) you want to use')
    # check preset names for validity
    names = set(preset)
    for det in detectors:
        names.difference_update(det.presetInfo())
    if names:
        printwarning('these preset keys were not recognized by any of '
                     'the detectors: %s -- detectors are %s' %
                     (', '.join(names), ', '.join(map(str, detectors))))
    # check detector types
    has_sub = sum(isinstance(det, SubscanMeasurable) for det in detectors)
    if has_sub > 0:
        # XXX support both types
        if not len(detectors) == has_sub == 1:
            # XXX message
            raise NicosError('cannot acquire on normal and subscan detectors')

    # preparation before count command (XXX)
    for det in detectors:
        det.prepare()
    for det in detectors:
        waitForStatus(det)
    # start counting
    point = dataman.beginPoint(detectors=detectors,
                               environment=session.experiment.sampleenv)
    acquire(point, preset)
    msg = []
    retval = []
    for det in detectors:
        res = point.results[det.name][0]
        for i, v in enumerate(det.valueInfo()):
            msg.append('%s = %s' % (v.name, res[i]))
            retval.append(res[i])
    printinfo('count: ' + ', '.join(msg))
    return CountResult(retval)
