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
#   Enrico Faulhaber <enrico.faulhaber@frm2.tum.de>
#
# *****************************************************************************

"""Devices for the Beckhoff Busklemmensystem."""

from Modbus import Modbus

import time
import struct
import threading
from nicos.core import Param, Override, listof, none_or, oneof, \
                        oneofdict, floatrange, intrange, status, \
                        InvalidValueError, UsageError, CommunicationError, \
                        TimeoutError, PositionError
from nicos.core.device import usermethod, requires
from nicos.devices.abstract import CanReference, Motor
from nicos.devices.taco.core import TacoDevice
from nicos.devices.taco.io import DigitalOutput, NamedDigitalOutput,\
                                   DigitalInput, NamedDigitalInput
from nicos.devices.generic import Switcher
from nicos.core import SIMULATION


class Sans1ColliSwitcher(Switcher):
    """Switcher, specially adopted to Sans1 needs"""
    parameter_overrides = {
        'precision' : Override(default=0.1, mandatory=False),
        'fallback'  : Override(default='Unknown', mandatory=False),
    }

    def _mapReadValue(self, pos):
        """Override default inverse mapping to allow a deviation <= precision"""
        prec = self.precision
        def myiter(mapping):
            # use position names beginning with P as last option
            for name, value in mapping.iteritems():
                if name[0] != 'P':
                    yield name, value
            for name, value in mapping.iteritems():
                if name[0] == 'P':
                    yield name, value
        for name, value in myiter(self.mapping):
            if prec:
                if abs(pos - value) <= prec:
                    return name
            elif pos == value:
                return name
        if self.fallback is not None:
            return self.fallback
        if self.relax_mapping:
            return self._adevs['moveable'].format(pos,True)
        raise PositionError(self, 'unknown position of %s' %
                            self._adevs['moveable'])


class Sans1ColliMotor(TacoDevice, Motor, CanReference):
    """
    Device object for a digital output device via a Beckhoff modbus interface.
    Minimum Parameter Implementation.
    Relevant Parameters need to be configured in the setupfile or in the
    Beckhoff PLC.
    """

    taco_class = Modbus

    relax_mapping = True

    parameters = {
        # provided by parent class: speed, unit, fmtstr, warnlimits, abslimits,
        #                           userlimits, precision and others
        'address': Param('Starting offset of Motor control Block in words',
                         type=int, mandatory=True, settable=False, userparam=False),
        'slope': Param('Slope of the Motor in _FULL_ steps per _physical unit_',
                       type=float, default=1., unit='steps/main',
                       userparam=False, settable=True),
        'microsteps': Param('Microstepping for the motor',
                            type=oneof(1, 2, 4, 8, 16, 32, 64), default=1,
                            userparam=False, settable=False),
        'autozero': Param('Maximum distance from referencepoint for forced '
                          'referencing before moving, or None',
                          type=none_or(float), default=10, unit='main',
                          settable=False),
        'autopower': Param('Automatically disable Drivers if motor is not moving',
                           type=oneofdict({0: 'off', 1: 'on'}), default='on',
                           settable=False),
        'refpos': Param('Position of reference switch', unit='main',
                        type=float, mandatory=True, settable=False,
                        prefercache=False),
    }

    def doInit(self, mode):
        # make sure we are in the right address range
        if not (0x4000 <= self.address <= 0x47ff) or \
            (self.address - 0x4020) % 10:
            # each motor-control-block is 20 bytes = 10 words, starting from
            # byte 64
            raise InvalidValueError(self,
                'Invalid address 0x%04x, please check settings!' %
                self.address)
        # switch off watchdog, important before doing any write access
        if mode != SIMULATION:
            self._taco_guard(self._dev.writeSingleRegister, (0, 0x1120, 0))
            if self.autopower == 'on':
                threading.Thread(target=self._autopoweroff).start()

    # access-helpers for accessing the fields inside the MotorControlBlock
    def _readControlBit(self, bit):
        self.log.debug('_readControlBit %d'%bit)
        value = self._taco_guard(self._dev.readInputRegisters,
                                 (0, self.address, 1))[0]
        return (value & (1 << int(bit))) >> int(bit)

    def _writeControlBit(self, bit, value):
        self.log.debug('_writeControlBit %r, %r'%(bit,value))
        tmpval = self._taco_guard(self._dev.readInputRegisters,
                                  (0, self.address, 1))[0]
        tmpval &= ~(1 << int(bit))
        tmpval |= (int(value) << int(bit))
        self._taco_guard(self._dev.writeSingleRegister,
                         (0, self.address, tmpval))
        # wait 1 sps-cycle to make sure the PLC knows about this bit
        time.sleep(0.020)

    def _writeDestination(self, value):
        self.log.debug('_writeDestination %r'%value)
        value = struct.unpack('<2H',struct.pack('=i',value))
        self._taco_guard(self._dev.writeMultipleRegisters,
                         (0, self.address+2) + value)

    def _readStatusWord(self):
        value = self._taco_guard(self._dev.readInputRegisters,
                                (0, self.address+4, 1))[0]
        self.log.debug('_readStatusWord %04x'%value)
        return value

    def _readErrorWord(self):
        value = self._taco_guard(self._dev.readInputRegisters,
                                (0, self.address+5, 1))[0]
        self.log.debug('_readErrorWord %04x'%value)
        return value

    def _readPosition(self):
        # or readHoldingRegisters
        value = self._taco_guard(self._dev.readInputRegisters,
                                 (0, self.address+6, 2))
        value = struct.unpack('=i',struct.pack('<2H',*value))[0]
        self.log.debug('_readPosition: -> %d steps'%value)
        return value

    #
    # math: transformation of position and speed:
    #       µsteps(/s) <-> phys. unit(/s)
    #
    def _steps2phys(self, steps):
        value = steps / float(self.microsteps * self.slope)
        self.log.debug('_steps2phys: %r steps -> %s' %
                       (steps, self.format(value, unit=True)))
        return value

    def _phys2steps(self, value):
        steps = int(value * float(self.microsteps * self.slope) )
        self.log.debug('_phys2steps: %s -> %r steps' %
                       (self.format(value, unit=True), steps))
        return steps

    def _speed2phys(self, speed):
        # see manual
        return speed  / float(self.microsteps * self.slope * 1.6384e-2)

    def _phys2speed(self, value):
        # see manual
        return int(value * self.slope * self.microsteps * 1.6384e-2 )

    #
    # nicos methods
    #
    def doRead(self, maxage=0):
        return self._steps2phys(self._readPosition())

    def doStart(self, value):
        self.log.debug('doStart %r' % value)
        self._writeControlBit(0, 1)     # docu: bit0 = 1: enable
        if self.autozero is not None:
            currentpos = self.read(0)
            mindist = min(abs(currentpos - self.refpos), abs(value - self.refpos))
            if mindist < self.autozero:
                self._reference()
                # returns after referencing has been done.
        # now just go where commanded....
        self._writeControlBit(0, 1)     # docu: bit0 = 1: enable
        self.log.debug('Starting positioning')
        self._writeDestination(self._phys2steps(value))
        self._writeControlBit(2, 1)     # docu: bit2 = go to absolute position, autoresets
        if self.autopower == 'on':
            threading.Thread(target=self._autopoweroff).start()

    def _autopoweroff(self):
        time.sleep(1)
        self.log.debug('AutoPowerOff checking status')
        while self.doStatus()[0]==status.BUSY:
            time.sleep(1)
        self.log.debug('AutoPowerOff')
        self._writeControlBit(0, 0)     # docu: bit0 = 0: disable

    def doStop(self):
        self._writeControlBit(6, 1)     # docu: bit6 = stop, autoresets

    def doReset(self):
        self._writeControlBit(7, 1)     # docu: bit7 = ERROR-ACK, autoresets

    def doStatus(self, maxage=0):
        ''' used Status bits:
        0-2 : Load-angle (0 good, 7 bad)
        3   : limit switch -
        4   : limit switch +
        5   : moving in pos. direction
        6   : target reached
        7   : motor moving
        8   : driver on and ready
        9   : Overtemperature
        10  : Target NOT reached, but a limit switch triggered
        11  : Target NOT reached due PowerOff or Stop
        12  : Can not move towards requested position, command ignored
        14  : N_ACK (last set/get command was unsuccessful), auto clears after 1s
        15  : ACK (last get/set command was successful, value in RETURN is valid),
              auto clears after 1s
        '''
        statval = self._readStatusWord()
        errval = self._readErrorWord()
        code, msg = status.ERROR, ['Unknown Status value 0x%04x!' % statval]

        # status Stuff
        if statval & (1<<7):
            code, msg = status.BUSY, ['busy']
        elif statval & (1<<6):
            code, msg = status.OK, ['Target reached']
        elif ~statval & (1<<8):
            code, msg = status.OK, ['Disabled']
        elif statval & (1<<9):
            code, msg = status.ERROR, ['Overtemperature!']
        elif statval & (7<<10):   # check any of bit 10, 11, 12 at the same time!
            code, msg = status.ERROR, ['Can not reach Target!']
        if errval:
            code, msg = status.ERROR, ['Error']
            if errval & (1<<0): msg.append('Control voltage too low')
            if errval & (1<<1): msg.append('Motor driving voltage too low')
            if errval & (1<<2): msg.append('Overcurrent or short in winding A')
            if errval & (1<<3): msg.append('Overcurrent or short in winding B')
            if errval & (1<<4): msg.append('Open load or broken wire in winding A')
            if errval & (1<<5): msg.append('Open load or broken wire in winding B')
            if errval & (1<<7): msg.append('Overtemperature (T>125 degC)')
            if errval & 0b1111111101000000:
                msg.append('Unknown Error 0x%04x'%errval)

        # informational stuff
        if statval & (1<<4):
            msg.append('limit switch +')
        if statval & (1<<3):
            msg.append('limit switch -')
        if statval & (1<<8):
            msg.append('driver on and ready')
        if statval & (1<<7):
            msg.append('load=%d' % (statval & 0x0007))

        msg = ', '.join(msg)
        self.log.debug('doStatus returns %r'%((code,msg),))
        return code, msg

    def doWait(self):
        self.log.debug('doWait')
        for _ in range(300):
            time.sleep(1)
            if self.doStatus()[0] == status.BUSY:
                continue
            return
        raise TimeoutError(self, 'Device timed out wait during wait!')

    @requires(level='admin')
    def doReference(self):
        self._writeControlBit(0, 1)     # docu: bit0 = 1: enable
        self._reference()  # this is blocking until finished
        if self.autopower:
            self._writeControlBit(0, 0)     # docu: bit0 = 0: disable

    def _reference(self):
        self.log.debug('_reference begin')
        if self.doStatus(0)[0] != status.OK:
            raise UsageError(self, 'Referencing only possible if Idle! '
                             'Hint: use stop or reset')
        # first move to negative limit switch to mimic anatel
        for i, p in enumerate([self.refpos + 5.,
                               self.refpos - abs(self.usermax) - abs(self.usermin)]):
            self.log.debug('doReference: %d) go to %.2f'% (2*i+1, p))
            self._writeDestination(self._phys2steps(p))
            self._writeControlBit(2, 1)
            self.log.debug('doReference: %d) wait'%(2*i+2))
            self.wait()
        # now we should be deep in limit-switch -
        self.log.debug('doReference: 5) start the referencing')
        # do the referencing & update position to refpos
        self._writeControlBit(4, 1)
        self.log.debug('doReference: 6) wait')
        self.wait()
        #~ currentpos = self.read(0)
        #~ self.log.debug('doReference: 7) set current pos %.2f to refpos %.2f'%(
            #~ self.mapping.get(currentpos, currentpos), self.refpos))
        #~ self.writeParameter(1, self._phys2steps(self.refpos), False)
        self.log.debug('doReference: Done...')

    #~ # Parameter 1 : CurrentPosition
    #~ def doSetPosition(self, value):
        #~ self.writeParameter(1, self._phys2steps(self.mapping.get(value,value)))

    #~ def doReadSpeed(self):
        #~ return self._speed2phys(self.readParameter(3))

    #~ def doReadAccel(self):
        #~ return self._speed2phys(self.readParameter(6))

    #~ def doReadMicrosteps(self):
        #~ return 2**self.readParameter(8)



class Sans1ColliMotorAllParams(Sans1ColliMotor):
    """
    Device object for a digital output device via a Beckhoff modbus interface.
    Maximum Parameter Implementation.
    All Relevant Parameters are accessible and can be configured.
    """
    taco_class = Modbus

    _paridx = dict(refpos=2, vmax=3, v_max=3, vmin=4, v_min=4, vref=5, v_ref=5,
                acc=6, a_acc=6, ae=7, a_e=7, microsteps=8, backlash=9,
                fullsteps_u=10, fullsteps=10, imax=11, i_max=11, iv=12, i_v=12, iv0=12,
                i_v0=12, imin=12, i_min=12, encodersteps_u=20, features=30,
                t=40, temp=40, temperature=40, type=250, hw=251, fw=252, reset=255,
                )

    parameters = {
        # provided by parent class: speed, unit, fmtstr, warnlimits, userlimits,
        # abslimits, precision and others
        'power': Param('Power on/off for the motordriver and enable/disable for the logic',
                        type=oneof('off','on'), default='off', settable=True),
        'backlash': Param('Backlash correction in physical units',
                        type=float, default=0.0, mandatory=False, settable=True, prefercache=False),
        'maxcurrent': Param('Max Motor current in A',
                        type=floatrange(0.05, 5), settable=True, prefercache=False),
        'idlecurrent': Param('Idle Motor current in A',
                        type=floatrange(0.05, 5), settable=True, prefercache=False),
        'temperature': Param('Temperature of the motor driver',
                        type=float, settable=False, volatile=True),
        'minspeed': Param('The minimum motor speed', unit='main/s', settable=True, prefercache=False),
        'refspeed': Param('The referencing speed', unit='main/s', settable=True, prefercache=False),
        'accel': Param('Acceleration/Decceleration', unit='main/s**2', settable=True, prefercache=False),
        'stopaccel': Param('Emergency Decceleration', unit='main/s**2', settable=True, prefercache=False),

        # needed ? Ask the Sans1 people...
        'hw_vmax' : Param('Maximum Velocity in HW-units',
                        type=intrange(1,2047), settable=True, prefercache=False),
        'hw_vmin' : Param('Minimum Velocity in HW-units',
                        type=intrange(1,2047), settable=True, prefercache=False),
        'hw_vref' : Param('Referencing Velocity in HW-units',
                        type=intrange(1,2047), settable=True, prefercache=False),
        'hw_accel' : Param('Acceleration in HW-units',
                        type=intrange(16,2047), settable=True, prefercache=False),
        'hw_accel_e' : Param('Acceleration when hitting a limit switch in HW-units',
                        type=intrange(16,2047), settable=True, prefercache=False),
        'hw_backlash' : Param('Backlash in HW-units',
                        type=intrange(-32768,32767), settable=True, prefercache=False),
        'hw_fullsteps' : Param('Motor steps per turn in HW-units',
                        type=intrange(1,65535), settable=True, prefercache=False),
        'hw_enc_steps' : Param('Encoder steps per turn in HW-units',
                        type=intrange(1,65535), settable=True, prefercache=False),
        'hw_features' : Param('Value of features register (16 Bit, see docu)',
                        type=intrange(0,65535), volatile=True, settable=True, prefercache=False),
        'hw_type' : Param('Value of features register (16 Bit, see docu)',
                        type=int, settable=True, prefercache=False),
        'hw_revision' : Param('Value of HW-revision register (16 Bit, see docu)',
                        type=int, settable=True, prefercache=False),
        'hw_firmware' : Param('Value of HW-Firmware register (16 Bit, see docu)',
                        type=int, settable=True, prefercache=False),
        'hw_disencfltr' : Param('Input filter for Encoder signals',
                        type=oneofdict({1:'disabled',0:'enabled'}), default='enabled',
                        volatile=True, settable=True, prefercache=False),
        'hw_feedback' : Param('Feedback signal for positioning',
                        type=oneofdict({0:'encoder',1:'motor'}), default='motor',
                        settable=True, prefercache=False),
        'hw_invposfb' : Param('Turning direction of encoder',
                        type=oneofdict({1:'opposite',0:'concordant'}), default='concordant',
                        settable=True, prefercache=False),
        'hw_ramptype' : Param('Shape of accel/deccel ramp',
                        type=oneofdict({1:'exponential',0:'linear'}), default='linear',
                        settable=True, prefercache=False),
        'hw_revin1' : Param('type of input 1',
                        type=oneofdict({1:'nc',0:'no'}), default='no', settable=True,
                        prefercache=False),
        'hw_revin2' : Param('type of input 2',
                        type=oneofdict({1:'nc',0:'no'}), default='no', settable=True,
                        prefercache=False),
        'hw_disin1rev' : Param('use Input 1 as reference input',
                        type=oneofdict({1:'off',0:'on'}), default='on', settable=True,
                        prefercache=False),
        'hw_disin2rev' : Param('use Input 2 as reference input',
                        type=oneofdict({1:'off',0:'on'}), default='on', settable=True,
                        prefercache=False),
        'hw_invrev' : Param('direction of reference drive',
                        type=oneofdict({1:'pos',0:'neg'}), default='neg', settable=True,
                        prefercache=False),
    }

    parameter_overrides = {
        'microsteps' : Override(mandatory=False, settable=True, prefercache=False),
        'refpos' : Override(settable=True),
    }
    # access-helpers for the fields inside to MotorControlBlock
    def _readUpperControlWord(self):
        self.log.error('_readUpperControlWord')
        return self._taco_guard(self._dev.readInputRegisters,
                                (0, self.address+1, 1))[0]
    def _writeUpperControlWord(self, value):
        self.log.debug('_writeUpperControlWord 0x%04x'%value)
        value = int(value) & 0xffff
        self._taco_guard(self._dev.writeSingleRegister,
                         (0, self.address + 1, value))
    def _readDestination(self):
        value = self._taco_guard(self._dev.readInputRegisters,    # or readHoldingRegisters
                                 (0, self.address+2, 2))
        value = struct.unpack('=i',struct.pack('<2H',*value))[0]
        self.log.debug('_readDestination: -> %d steps'%value)
        return value
    def _readReturn(self):
        value = self._taco_guard(self._dev.readInputRegisters,    # or readHoldingRegisters
                                 (0, self.address+8, 2))
        value = struct.unpack('=i',struct.pack('<2H',*value))[0]
        self.log.debug('_readReturn: -> %d (0x%08x)'%(value,value))
        return value

    # more advanced stuff: setting/getting parameters
    # only to be used manually at the moment
    @usermethod
    @requires(level='user')
    def readParameter(self, index):
        self.log.debug('readParameter %d'%index)
        try:
            index = int(self._paridx.get(index,index))
        except ValueError:
            UsageError(self, 'Unknown parameter %r, try one of %s' %
                       (index,', '.join(self._paridx.keys()+self._paridx.values)))
        if self._readStatusWord() & (1<<7):
            raise UsageError(self, 'Can not access Parameters while Motor is '
                                    'moving, please stop it first!')
        if self.power == 'on':
            self.power = 'off'

        # wait for inactive ACK/NACK
        self.log.debug('Wait for idle ACK/NACK bits')
        for _ in range(1000):
            if self._readStatusWord() & (3<<14) == 0:
                break
            time.sleep(0.001)
        else:
            raise CommunicationError(self, 'HW still busy, can not read Parameter, '
                                            'please retry later....')

        self._writeUpperControlWord((index << 8) | 4)

        self.log.debug('Wait for ACK/NACK bits')
        for _ in range(1000):
            if self._readStatusWord() & (3<<14) != 0:
                break
            time.sleep(0.001)
        else:
            raise CommunicationError(self, 'ReadPar command not recognized by HW, please retry later....')

        if self._readStatusWord() & (1<<14):
            raise CommunicationError(self, 'Reading of Parameter %r failed, got a NACK'%index)
        return self._readReturn()

    @usermethod
    @requires(level='admin')
    def writeParameter(self, index, value, store2eeprom=False):
        self.log.debug('writeParameter %d:0x%04x'%(index,value))
        if store2eeprom:
            self.log.warning('writeParameter stores to eeprom !')
        try:
            index = int(self._paridx.get(index,index))
        except ValueError:
            UsageError(self, 'Unknown parameter %r'%index)
        if self._readStatusWord() & (1<<7):
            raise UsageError(self, 'Can not access Parameters while Motor is '
                                    'moving, please stop it first!')
        if self.power == 'on':
            self.power = 'off'

        # wait for inactive ACK/NACK
        self.log.debug('Wait for idle ACK/NACK bits')
        for _ in range(1000):
            if self._readStatusWord() & (3<<14) == 0:
                break
            time.sleep(0.001)
        else:
            raise CommunicationError(self, 'HW still busy, can not write Parameter, please retry later....')

        self._writeDestination( value )
        if store2eeprom:
            self._writeUpperControlWord( (index<< 8) | 3) # store to eeprom
        else:
            self._writeUpperControlWord( (index<< 8) | 1) # store to volatile memory

        self.log.debug('Wait for ACK/NACK bits')
        for _ in range(1000):
            if self._readStatusWord() & (3<<14) != 0:
                break
            time.sleep(0.001)
        else:
            raise CommunicationError(self, 'WritePar command not recognized by HW, please retry later....')

        if self._readStatusWord() & (1<<14):
            raise CommunicationError(self, 'Writing of Parameter %r failed, got a NACK'%index)
        return self._readReturn()

    #
    # Parameter access methods
    #
    def doWritePower(self, value):
        if self._readStatusWord() & (1<<7):
            raise UsageError(self, 'Never switch off Power while Motor is moving !')
        value = ['off','on'].index(value)
        self._writeControlBit(0, value)    # docu: bit0 = enable/disable
    def doReadPower(self):
        return ['off','on'][self._readControlBit(0)]    # docu: bit0 = enable/disable

    # Parameter 1 : CurrentPosition
    def doSetPosition(self, value):
        self.writeParameter(1, self._phys2steps(value))

    # Parameter 2 : Refpos
    def doReadRefpos(self):
        return self._steps2phys(self.readParameter(2))
    def doWriteRefpos(self, value):
        self.writeParameter(2, self._phys2steps(value), store2eeprom=True)

    # Parameter 3 : hw_vmax -> speed
    def doReadHw_Vmax(self):
        return self.readParameter(3)
    def doReadSpeed(self):
        return self._speed2phys(self.hw_vmax) # units per second
    def doWriteHw_Vmax(self, value):
        self.writeParameter(3, value)
    def doWriteSpeed(self, speed):
        self.hw_vmax = self._phys2speed(speed)

    # Parameter 4 : hw_vmin -> minspeed
    def doReadHw_Vmin(self):
        return self.readParameter(4)
    def doReadMinspeed(self):
        return self._speed2phys(self.hw_vmin) # units per second
    def doWriteHw_Vmin(self, value):
        self.writeParameter(4, value)
    def doWriteMinspeed(self, speed):
        self.hw_vmin = self._phys2speed(speed)

    # Parameter 5 : hw_vref -> refspeed
    def doReadHw_Vref(self):
        return self.readParameter(5)   # µSteps per second
    def doReadRefspeed(self):
        return self._speed2phys(self.hw_vref) # units per second
    def doWriteHw_Vref(self, value):
        self.writeParameter(5, value)
    def doWriteRefspeed(self, speed):
        self.hw_vref = self._phys2speed(speed)

    # Parameter 6 : hw_accel -> accel
    def doReadHw_Accel(self):
        return self.readParameter(6)   # µSteps per second
    def doReadAccel(self):
        return self._speed2phys(self.hw_accel) # units per second
    def doWriteHw_Accel(self, value):
        self.writeParameter(6, value)
    def doWriteAccel(self, accel):
        self.hw_accel = self._phys2speed(accel)

    # Parameter 7 : hw_accel_e -> stopaccel
    def doReadHw_Accel_E(self):
        return self.readParameter(7)   # µSteps per second
    def doReadStopaccel(self):
        return self._speed2phys(self.hw_accel_e) # units per second
    def doWriteHw_Accel_E(self, value):
        self.writeParameter(7, value)
    def doWriteStopaccel(self, accel):
        self.hw_accel_e = self._phys2speed(accel)

    # Parameter 8 : microsteps
    def doWriteMicrosteps(self, value):
        for i in range(7):
            if value == 2**i:
                self.writeParameter(8, i)
                break
        else:
            raise InvalidValueError(self,
                'This should never happen! value should be one of: '
                '1, 2, 4, 8, 16, 32, 64 !')

    def doReadMicrosteps(self):
        return 2**self.readParameter(8)

    # Parameter 9 : hw_backlash -> backlash
    def doReadHw_Backlash(self):
        return self.readParameter(9)   # µSteps per second
    def doReadBacklash(self):
        return self._steps2phys(self.hw_backlash)
    def doWriteHw_Backlash(self, value):
        self.writeParameter(9, value)
    def doWriteBacklash(self, value):
        self.hw_backlash = self._phys2steps(value)

    # Parameter 10 : Fullsteps per turn
    def doReadHw_Fullsteps(self):
        return self.readParameter(10)
    def doWriteHw_Fullsteps(self, value):
        self.writeParameter(10, value)

    # Parameter 11 : MaxCurrent
    def doReadMaxcurrent(self):
        return self.readParameter(11) * 0.05
    def doWriteMaxcurrent(self, value):
        self.writeParameter(11, int(0.5 + value / 0.05))

    # Parameter 12 : IdleCurrent
    def doReadIdlecurrent(self):
        return self.readParameter(12) * 0.05
    def doWriteIdlecurrent(self, value):
        self.writeParameter(12, int(0.5 + value / 0.05))

    # Parameter 20 : Encodersteps per turn
    def doReadHw_Enc_Steps(self):
        return self.readParameter(20)
    def doWriteHw_Enc_Steps(self, value):
        self.writeParameter(20, value)

    # Parameter 30 : Features
    def doReadHw_Features(self):
        value = self.readParameter(30)
        self.log.debug('Feature0: Inputfilter for encodersignals: %d'
            % (value & 1))
        self.log.debug('Feature1: Positionsrueckfuehrung (0=Encoder, 1=Zaehler): %d'
            % ((value>>1) & 1))
        self.log.debug('Feature2: Zaehlrichtung encoder (0=mitlaufend, 1=gegenlaufend): %d'
            % ((value>>2) & 1))
        self.log.debug('Feature3: Bremsrampe (0=linear, 1=exponentiell): %d'
            % ((value>>3) & 1))
        self.log.debug('Feature4: Eingang1 (0=Schliesser, 1=oeffner): %d'
            % ((value>>4) & 1))
        self.log.debug('Feature5: Eingang2 (0=Schliesser, 1=oeffner): %d'
            % ((value>>5) & 1))
        self.log.debug('Feature6: Eingang1 (0=referenz, 1=normal): %d'
            % ((value>>6) & 1))
        self.log.debug('Feature7: Eingang2 (0=referenz, 1=normal): %d'
            % ((value>>7) & 1))
        self.log.debug('Feature8: Richtung der Referenzfahrt (0=negativ, 1=positiv): %d'
            % ((value>>8) & 1))
        return value
    def doWriteHw_Features(self, value):
        self.writeParameter(30, value)

    # bitwise access
    def doReadHw_Disencfltr(self):
        return (self.hw_features >> 0) & 1
    def doWriteHw_Disencfltr(self, value):
        if value in [0, 1]:
            self.hw_features = (self.hw_features & ~(1<<0)) | (value<<0)
        else:
            raise InvalidValueError(self, 'hw_disencfltr can only be 0 or 1')

    def doReadHw_Feedback(self):
        return (self.hw_features >> 1) & 1
    def doWriteHw_Feedback(self, value):
        if value in [0, 1]:
            self.hw_features = (self.hw_features & ~(1<<1)) | (value<<1)
        else:
            raise InvalidValueError(self, 'hw_feedback can only be 0 or 1')

    def doReadHw_Invposfb(self):
        return (self.hw_features >> 2) & 1
    def doWriteHw_Invposfb(self, value):
        if value in [0, 1]:
            self.hw_features = (self.hw_features & ~(1<<2)) | (value<<2)
        else:
            raise InvalidValueError(self, 'hw_invposfb can only be 0 or 1')

    def doReadHw_Ramptype(self):
        return (self.hw_features >> 3) & 1
    def doWriteHw_Ramptype(self, value):
        if value in [0, 1]:
            self.hw_features = (self.hw_features & ~(1<<3)) | (value<<3)
        else:
            raise InvalidValueError(self, 'hw_ramptype can only be 0 or 1')

    def doReadHw_Revin1(self):
        return (self.hw_features >> 4) & 1
    def doWriteHw_Revin1(self, value):
        if value in [0, 1]:
            self.hw_features = (self.hw_features & ~(1<<4)) | (value<<4)
        else:
            raise InvalidValueError(self, 'hw_revin1 can only be 0 or 1')

    def doReadHw_Revin2(self):
        return (self.hw_features >> 5) & 1
    def doWriteHw_Revin2(self, value):
        if value in [0, 1]:
            self.hw_features = (self.hw_features & ~(1<<5)) | (value<<5)
        else:
            raise InvalidValueError(self, 'hw_revin2 can only be 0 or 1')

    def doReadHw_Disin1Rev(self):
        return (self.hw_features >> 6) & 1
    def doWriteHw_Disin1Rev(self, value):
        if value in [0, 1]:
            self.hw_features = (self.hw_features & ~(1<<6)) | (value<<6)
        else:
            raise InvalidValueError(self, 'hw_disin1rev can only be 0 or 1')

    def doReadHw_Disin2Rev(self):
        return (self.hw_features >> 7) & 1
    def doWriteHw_Disin2Rev(self, value):
        if value in [0, 1]:
            self.hw_features = (self.hw_features & ~(1<<7)) | (value<<7)
        else:
            raise InvalidValueError(self, 'hw_disin2rev can only be 0 or 1')

    def doReadHw_Invrev(self):
        return (self.hw_features >> 8) & 1
    def doWriteHw_Invrev(self, value):
        if value in [0, 1]:
            self.hw_features = (self.hw_features & ~(1<<8)) | (value<<8)
        else:
            raise InvalidValueError(self, 'hw_invrev can only be 0 or 1')

    # Parameter 40 : Temperature
    def doReadTemperature(self):
        return self.readParameter(40)

    # Parameter 250 : Klemmentyp
    def doReadHw_Type(self):
        return self.readParameter(250)

    # Parameter 251 : Hardwarestand
    def doReadHw_Revision(self):
        return self.readParameter(251)

    # Parameter 252 : Firmwarestand
    def doReadHw_Firmware(self):
        return self.readParameter(252)

    # Parameter 255 : Factory Reset
    @usermethod
    def FactoryReset(self, password):
        '''resets the motorcontroller to factory default values
        for the right password see docu'''
        # 0x544B4531
        self.writeParameter(255, password)


class BeckhoffDigitalInput(DigitalInput):
    """
    Device object for a digital input device via a Beckhoff modbus interface.
    """
    taco_class = Modbus
    valuetype = listof(int)

    parameters = {
        'startoffset': Param('Starting offset of digital output values',
                             type=int, mandatory=True),
        'bitwidth':    Param('Number of bits to read', type=int,
                             mandatory=True),
    }

    def doInit(self, mode):
        # switch off watchdog, important before doing any write access
        if mode != SIMULATION:
            self._taco_guard(self._dev.writeSingleRegister, (0, 0x1120, 0))

    def doRead(self, maxage=0):
        return tuple(self._taco_guard(self._dev.readDiscreteInputs, (0,
                                      self.startoffset, self.bitwidth)))

    def doReadFmtstr(self):
        return '[' + ', '.join(['%d'] * self.bitwidth) + ']'


class BeckhoffNamedDigitalInput(NamedDigitalInput):
    taco_class = Modbus

    parameters = {
        'startoffset': Param('Starting offset of digital output values',
                             type=int, mandatory=True),
    }

    def doInit(self, mode):
        # switch off watchdog, important before doing any write access
        if mode != SIMULATION:
            self._taco_guard(self._dev.writeSingleRegister, (0, 0x1120, 0))
        NamedDigitalOutput.doInit(self, mode)

    def doRead(self, maxage=0):
        value = self._taco_guard(self._dev.readDiscreteInputs,
                                 (0, self.startoffset, 1))[0]
        return self._reverse.get(value, value)


class BeckhoffDigitalOutput(DigitalOutput):
    """
    Device object for a digital output device via a Beckhoff modbus interface.
    """
    taco_class = Modbus
    valuetype = listof(int)

    parameters = {
        'startoffset': Param('Starting offset of digital output values',
                             type=int, mandatory=True),
        'bitwidth':    Param('Number of bits to switch', type=int,
                             mandatory=True),
    }

    def doInit(self, mode):
        # switch off watchdog, important before doing any write access
        if mode != SIMULATION:
            self._taco_guard(self._dev.writeSingleRegister, (0, 0x1120, 0))

    def doRead(self, maxage=0):
        return tuple(self._taco_guard(self._dev.readCoils, (0,
                                      self.startoffset, self.bitwidth)))

    def doStart(self, value):
        self._taco_guard(self._dev.writeMultipleCoils, (0,
                         self.startoffset) + tuple(value))

    def doIsAllowed(self, target):
        try:
            if len(target) != self.bitwidth:
                return False, ('value needs to be a sequence of length %d, '
                               'not %r' % (self.bitwidth, target))
        except TypeError:
            return False, 'invalid value for device: %r' % target
        return True, ''

    def doReadFmtstr(self):
        return '[' + ', '.join(['%d'] * self.bitwidth) + ']'


class BeckhoffNamedDigitalOutput(NamedDigitalOutput):
    taco_class = Modbus

    parameters = {
        'startoffset': Param('Starting offset of digital output values',
                             type=int, mandatory=True),
    }

    def doInit(self, mode):
        # switch off watchdog, important before doing any write access
        if mode != SIMULATION:
            self._taco_guard(self._dev.writeSingleRegister, (0, 0x1120, 0))
        NamedDigitalOutput.doInit(self, mode)

    def doStart(self, target):
        value = self.mapping.get(target, target)
        self._taco_guard(self._dev.writeMultipleCoils,
                         (0, self.startoffset) + (value,))

    def doRead(self, maxage=0):
        value = self._taco_guard(self._dev.readCoils,
                                 (0, self.startoffset, 1))[0]
        return self._reverse.get(value, value)
