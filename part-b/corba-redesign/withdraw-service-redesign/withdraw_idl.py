# Python stubs generated by omniidl from withdraw.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "Withdraw"
#
__name__ = "Withdraw"
_0_Withdraw = omniORB.openModule("Withdraw", r"withdraw.idl")
_0_Withdraw__POA = omniORB.openModule("Withdraw__POA", r"withdraw.idl")


# interface BankingServer
_0_Withdraw._d_BankingServer = (omniORB.tcInternal.tv_objref, "IDL:Withdraw/BankingServer:1.0", "BankingServer")
omniORB.typeMapping["IDL:Withdraw/BankingServer:1.0"] = _0_Withdraw._d_BankingServer
_0_Withdraw.BankingServer = omniORB.newEmptyClass()
class BankingServer :
    _NP_RepositoryId = _0_Withdraw._d_BankingServer[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Withdraw.BankingServer = BankingServer
_0_Withdraw._tc_BankingServer = omniORB.tcInternal.createTypeCode(_0_Withdraw._d_BankingServer)
omniORB.registerType(BankingServer._NP_RepositoryId, _0_Withdraw._d_BankingServer, _0_Withdraw._tc_BankingServer)

# BankingServer operations and attributes
BankingServer._d_withdraw = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_octet), ((omniORB.tcInternal.tv_string,0), ), None)

# BankingServer object reference
class _objref_BankingServer (CORBA.Object):
    _NP_RepositoryId = BankingServer._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def withdraw(self, *args):
        return self._obj.invoke("withdraw", _0_Withdraw.BankingServer._d_withdraw, args)

omniORB.registerObjref(BankingServer._NP_RepositoryId, _objref_BankingServer)
_0_Withdraw._objref_BankingServer = _objref_BankingServer
del BankingServer, _objref_BankingServer

# BankingServer skeleton
__name__ = "Withdraw__POA"
class BankingServer (PortableServer.Servant):
    _NP_RepositoryId = _0_Withdraw.BankingServer._NP_RepositoryId


    _omni_op_d = {"withdraw": _0_Withdraw.BankingServer._d_withdraw}

BankingServer._omni_skeleton = BankingServer
_0_Withdraw__POA.BankingServer = BankingServer
omniORB.registerSkeleton(BankingServer._NP_RepositoryId, BankingServer)
del BankingServer
__name__ = "Withdraw"

#
# End of module "Withdraw"
#
__name__ = "withdraw_idl"

_exported_modules = ( "Withdraw", )

# The end.