#pylint: skip-file
# Python stubs generated by omniidl from absdev.idl

import _omnipy
import omniORB
from omniORB import CORBA, PortableServer

_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "_GlobalIDL"
#
__name__ = "_GlobalIDL"
_0__GlobalIDL = omniORB.openModule("_GlobalIDL", r"absdev.idl")
_0__GlobalIDL__POA = omniORB.openModule("_GlobalIDL__POA", r"absdev.idl")

_0__GlobalIDL.MAX_ITEMS = 4096

# typedef ... module_info_seq_t
class module_info_seq_t:
    _NP_RepositoryId = "IDL:module_info_seq_t:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.module_info_seq_t = module_info_seq_t
_0__GlobalIDL._d_module_info_seq_t  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_any, 0)
_0__GlobalIDL._ad_module_info_seq_t = (omniORB.tcInternal.tv_alias, module_info_seq_t._NP_RepositoryId, "module_info_seq_t", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_any, 0))
_0__GlobalIDL._tc_module_info_seq_t = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_module_info_seq_t)
omniORB.registerType(module_info_seq_t._NP_RepositoryId, _0__GlobalIDL._ad_module_info_seq_t, _0__GlobalIDL._tc_module_info_seq_t)
del module_info_seq_t

# typedef ... char_data_seq_t
class char_data_seq_t:
    _NP_RepositoryId = "IDL:char_data_seq_t:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.char_data_seq_t = char_data_seq_t
_0__GlobalIDL._d_char_data_seq_t  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_char, 0)
_0__GlobalIDL._ad_char_data_seq_t = (omniORB.tcInternal.tv_alias, char_data_seq_t._NP_RepositoryId, "char_data_seq_t", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_char, 0))
_0__GlobalIDL._tc_char_data_seq_t = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_char_data_seq_t)
omniORB.registerType(char_data_seq_t._NP_RepositoryId, _0__GlobalIDL._ad_char_data_seq_t, _0__GlobalIDL._tc_char_data_seq_t)
del char_data_seq_t

# typedef ... short_data_seq_t
class short_data_seq_t:
    _NP_RepositoryId = "IDL:short_data_seq_t:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.short_data_seq_t = short_data_seq_t
_0__GlobalIDL._d_short_data_seq_t  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_short, 0)
_0__GlobalIDL._ad_short_data_seq_t = (omniORB.tcInternal.tv_alias, short_data_seq_t._NP_RepositoryId, "short_data_seq_t", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_short, 0))
_0__GlobalIDL._tc_short_data_seq_t = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_short_data_seq_t)
omniORB.registerType(short_data_seq_t._NP_RepositoryId, _0__GlobalIDL._ad_short_data_seq_t, _0__GlobalIDL._tc_short_data_seq_t)
del short_data_seq_t

# typedef ... int_data_seq_t
class int_data_seq_t:
    _NP_RepositoryId = "IDL:int_data_seq_t:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.int_data_seq_t = int_data_seq_t
_0__GlobalIDL._d_int_data_seq_t  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_long, 0)
_0__GlobalIDL._ad_int_data_seq_t = (omniORB.tcInternal.tv_alias, int_data_seq_t._NP_RepositoryId, "int_data_seq_t", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_long, 0))
_0__GlobalIDL._tc_int_data_seq_t = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_int_data_seq_t)
omniORB.registerType(int_data_seq_t._NP_RepositoryId, _0__GlobalIDL._ad_int_data_seq_t, _0__GlobalIDL._tc_int_data_seq_t)
del int_data_seq_t

# typedef ... float_data_seq_t
class float_data_seq_t:
    _NP_RepositoryId = "IDL:float_data_seq_t:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.float_data_seq_t = float_data_seq_t
_0__GlobalIDL._d_float_data_seq_t  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_float, 0)
_0__GlobalIDL._ad_float_data_seq_t = (omniORB.tcInternal.tv_alias, float_data_seq_t._NP_RepositoryId, "float_data_seq_t", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_float, 0))
_0__GlobalIDL._tc_float_data_seq_t = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_float_data_seq_t)
omniORB.registerType(float_data_seq_t._NP_RepositoryId, _0__GlobalIDL._ad_float_data_seq_t, _0__GlobalIDL._tc_float_data_seq_t)
del float_data_seq_t

# typedef ... int64_data_seq_t
class int64_data_seq_t:
    _NP_RepositoryId = "IDL:int64_data_seq_t:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.int64_data_seq_t = int64_data_seq_t
_0__GlobalIDL._d_int64_data_seq_t  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_longlong, 0)
_0__GlobalIDL._ad_int64_data_seq_t = (omniORB.tcInternal.tv_alias, int64_data_seq_t._NP_RepositoryId, "int64_data_seq_t", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_longlong, 0))
_0__GlobalIDL._tc_int64_data_seq_t = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_int64_data_seq_t)
omniORB.registerType(int64_data_seq_t._NP_RepositoryId, _0__GlobalIDL._ad_int64_data_seq_t, _0__GlobalIDL._tc_int64_data_seq_t)
del int64_data_seq_t

# typedef ... double_data_seq_t
class double_data_seq_t:
    _NP_RepositoryId = "IDL:double_data_seq_t:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.double_data_seq_t = double_data_seq_t
_0__GlobalIDL._d_double_data_seq_t  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_double, 0)
_0__GlobalIDL._ad_double_data_seq_t = (omniORB.tcInternal.tv_alias, double_data_seq_t._NP_RepositoryId, "double_data_seq_t", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_double, 0))
_0__GlobalIDL._tc_double_data_seq_t = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_double_data_seq_t)
omniORB.registerType(double_data_seq_t._NP_RepositoryId, _0__GlobalIDL._ad_double_data_seq_t, _0__GlobalIDL._tc_double_data_seq_t)
del double_data_seq_t

# interface absdev
_0__GlobalIDL._d_absdev = (omniORB.tcInternal.tv_objref, "IDL:absdev:1.0", "absdev")
omniORB.typeMapping["IDL:absdev:1.0"] = _0__GlobalIDL._d_absdev
_0__GlobalIDL.absdev = omniORB.newEmptyClass()
class absdev :
    _NP_RepositoryId = _0__GlobalIDL._d_absdev[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0__GlobalIDL.absdev = absdev
_0__GlobalIDL._tc_absdev = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_absdev)
omniORB.registerType(absdev._NP_RepositoryId, _0__GlobalIDL._d_absdev, _0__GlobalIDL._tc_absdev)

# absdev operations and attributes
absdev._d_init_system_orb = ((omniORB.tcInternal.tv_long, ), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_release_system_orb = ((omniORB.tcInternal.tv_long, ), (omniORB.tcInternal.tv_long, ), None)
absdev._d_init_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, (omniORB.tcInternal.tv_string,0)), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_read_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:module_info_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:module_info_seq_t:1.0"]), None)
absdev._d_drive_module_orb = ((omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:module_info_seq_t:1.0"], omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_load_module_orb = ((omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:module_info_seq_t:1.0"], omniORB.tcInternal.tv_long), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_stop_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_stop_all_orb = ((omniORB.tcInternal.tv_long, ), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_start_acquisition_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_stop_acquisition_orb = ((omniORB.tcInternal.tv_long, ), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_readblock_params_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_char_readblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:char_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:char_data_seq_t:1.0"]), None)
absdev._d_short_readblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:short_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:short_data_seq_t:1.0"]), None)
absdev._d_int_readblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:int_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:int_data_seq_t:1.0"]), None)
absdev._d_int64_readblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:int64_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:int64_data_seq_t:1.0"]), None)
absdev._d_float_readblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:float_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:float_data_seq_t:1.0"]), None)
absdev._d_double_readblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:double_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:double_data_seq_t:1.0"]), None)
absdev._d_char_loadblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:char_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_short_loadblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:short_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_int_loadblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:int_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_int64_loadblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:int64_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_float_loadblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:float_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_double_loadblock_module_orb = ((omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:double_data_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.tcInternal.tv_long), None)
absdev._d_read_allmodules_orb = ((omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:module_info_seq_t:1.0"]), (omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:module_info_seq_t:1.0"]), None)

# absdev object reference
class _objref_absdev (CORBA.Object):
    _NP_RepositoryId = absdev._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def init_system_orb(self, *args):
        return _omnipy.invoke(self, "init_system_orb", _0__GlobalIDL.absdev._d_init_system_orb, args)

    def release_system_orb(self, *args):
        return _omnipy.invoke(self, "release_system_orb", _0__GlobalIDL.absdev._d_release_system_orb, args)

    def init_module_orb(self, *args):
        return _omnipy.invoke(self, "init_module_orb", _0__GlobalIDL.absdev._d_init_module_orb, args)

    def read_module_orb(self, *args):
        return _omnipy.invoke(self, "read_module_orb", _0__GlobalIDL.absdev._d_read_module_orb, args)

    def drive_module_orb(self, *args):
        return _omnipy.invoke(self, "drive_module_orb", _0__GlobalIDL.absdev._d_drive_module_orb, args)

    def load_module_orb(self, *args):
        return _omnipy.invoke(self, "load_module_orb", _0__GlobalIDL.absdev._d_load_module_orb, args)

    def stop_module_orb(self, *args):
        return _omnipy.invoke(self, "stop_module_orb", _0__GlobalIDL.absdev._d_stop_module_orb, args)

    def stop_all_orb(self, *args):
        return _omnipy.invoke(self, "stop_all_orb", _0__GlobalIDL.absdev._d_stop_all_orb, args)

    def start_acquisition_orb(self, *args):
        return _omnipy.invoke(self, "start_acquisition_orb", _0__GlobalIDL.absdev._d_start_acquisition_orb, args)

    def stop_acquisition_orb(self, *args):
        return _omnipy.invoke(self, "stop_acquisition_orb", _0__GlobalIDL.absdev._d_stop_acquisition_orb, args)

    def readblock_params_orb(self, *args):
        return _omnipy.invoke(self, "readblock_params_orb", _0__GlobalIDL.absdev._d_readblock_params_orb, args)

    def char_readblock_module_orb(self, *args):
        return _omnipy.invoke(self, "char_readblock_module_orb", _0__GlobalIDL.absdev._d_char_readblock_module_orb, args)

    def short_readblock_module_orb(self, *args):
        return _omnipy.invoke(self, "short_readblock_module_orb", _0__GlobalIDL.absdev._d_short_readblock_module_orb, args)

    def int_readblock_module_orb(self, *args):
        return _omnipy.invoke(self, "int_readblock_module_orb", _0__GlobalIDL.absdev._d_int_readblock_module_orb, args)

    def int64_readblock_module_orb(self, *args):
        return _omnipy.invoke(self, "int64_readblock_module_orb", _0__GlobalIDL.absdev._d_int64_readblock_module_orb, args)

    def float_readblock_module_orb(self, *args):
        return _omnipy.invoke(self, "float_readblock_module_orb", _0__GlobalIDL.absdev._d_float_readblock_module_orb, args)

    def double_readblock_module_orb(self, *args):
        return _omnipy.invoke(self, "double_readblock_module_orb", _0__GlobalIDL.absdev._d_double_readblock_module_orb, args)

    def char_loadblock_module_orb(self, *args):
        return _omnipy.invoke(self, "char_loadblock_module_orb", _0__GlobalIDL.absdev._d_char_loadblock_module_orb, args)

    def short_loadblock_module_orb(self, *args):
        return _omnipy.invoke(self, "short_loadblock_module_orb", _0__GlobalIDL.absdev._d_short_loadblock_module_orb, args)

    def int_loadblock_module_orb(self, *args):
        return _omnipy.invoke(self, "int_loadblock_module_orb", _0__GlobalIDL.absdev._d_int_loadblock_module_orb, args)

    def int64_loadblock_module_orb(self, *args):
        return _omnipy.invoke(self, "int64_loadblock_module_orb", _0__GlobalIDL.absdev._d_int64_loadblock_module_orb, args)

    def float_loadblock_module_orb(self, *args):
        return _omnipy.invoke(self, "float_loadblock_module_orb", _0__GlobalIDL.absdev._d_float_loadblock_module_orb, args)

    def double_loadblock_module_orb(self, *args):
        return _omnipy.invoke(self, "double_loadblock_module_orb", _0__GlobalIDL.absdev._d_double_loadblock_module_orb, args)

    def read_allmodules_orb(self, *args):
        return _omnipy.invoke(self, "read_allmodules_orb", _0__GlobalIDL.absdev._d_read_allmodules_orb, args)

    __methods__ = ["init_system_orb", "release_system_orb", "init_module_orb", "read_module_orb", "drive_module_orb", "load_module_orb", "stop_module_orb", "stop_all_orb", "start_acquisition_orb", "stop_acquisition_orb", "readblock_params_orb", "char_readblock_module_orb", "short_readblock_module_orb", "int_readblock_module_orb", "int64_readblock_module_orb", "float_readblock_module_orb", "double_readblock_module_orb", "char_loadblock_module_orb", "short_loadblock_module_orb", "int_loadblock_module_orb", "int64_loadblock_module_orb", "float_loadblock_module_orb", "double_loadblock_module_orb", "read_allmodules_orb"] + CORBA.Object.__methods__

omniORB.registerObjref(absdev._NP_RepositoryId, _objref_absdev)
_0__GlobalIDL._objref_absdev = _objref_absdev
del absdev, _objref_absdev

# absdev skeleton
__name__ = "_GlobalIDL__POA"
class absdev (PortableServer.Servant):
    _NP_RepositoryId = _0__GlobalIDL.absdev._NP_RepositoryId


    _omni_op_d = {"init_system_orb": _0__GlobalIDL.absdev._d_init_system_orb, "release_system_orb": _0__GlobalIDL.absdev._d_release_system_orb, "init_module_orb": _0__GlobalIDL.absdev._d_init_module_orb, "read_module_orb": _0__GlobalIDL.absdev._d_read_module_orb, "drive_module_orb": _0__GlobalIDL.absdev._d_drive_module_orb, "load_module_orb": _0__GlobalIDL.absdev._d_load_module_orb, "stop_module_orb": _0__GlobalIDL.absdev._d_stop_module_orb, "stop_all_orb": _0__GlobalIDL.absdev._d_stop_all_orb, "start_acquisition_orb": _0__GlobalIDL.absdev._d_start_acquisition_orb, "stop_acquisition_orb": _0__GlobalIDL.absdev._d_stop_acquisition_orb, "readblock_params_orb": _0__GlobalIDL.absdev._d_readblock_params_orb, "char_readblock_module_orb": _0__GlobalIDL.absdev._d_char_readblock_module_orb, "short_readblock_module_orb": _0__GlobalIDL.absdev._d_short_readblock_module_orb, "int_readblock_module_orb": _0__GlobalIDL.absdev._d_int_readblock_module_orb, "int64_readblock_module_orb": _0__GlobalIDL.absdev._d_int64_readblock_module_orb, "float_readblock_module_orb": _0__GlobalIDL.absdev._d_float_readblock_module_orb, "double_readblock_module_orb": _0__GlobalIDL.absdev._d_double_readblock_module_orb, "char_loadblock_module_orb": _0__GlobalIDL.absdev._d_char_loadblock_module_orb, "short_loadblock_module_orb": _0__GlobalIDL.absdev._d_short_loadblock_module_orb, "int_loadblock_module_orb": _0__GlobalIDL.absdev._d_int_loadblock_module_orb, "int64_loadblock_module_orb": _0__GlobalIDL.absdev._d_int64_loadblock_module_orb, "float_loadblock_module_orb": _0__GlobalIDL.absdev._d_float_loadblock_module_orb, "double_loadblock_module_orb": _0__GlobalIDL.absdev._d_double_loadblock_module_orb, "read_allmodules_orb": _0__GlobalIDL.absdev._d_read_allmodules_orb}

absdev._omni_skeleton = absdev
_0__GlobalIDL__POA.absdev = absdev
omniORB.registerSkeleton(absdev._NP_RepositoryId, absdev)
del absdev
__name__ = "_GlobalIDL"

#
# End of module "_GlobalIDL"
#
__name__ = "nicos.device.vendor.caress.absdev_idl"

_exported_modules = ( "_GlobalIDL", )

# The end.
