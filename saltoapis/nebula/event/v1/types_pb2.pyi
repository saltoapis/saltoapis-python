from google.protobuf import struct_pb2 as _struct_pb2
from saltoapis.nebula.accesspoint.v1 import access_point_pb2 as _access_point_pb2
from saltoapis.nebula.accesspoint.v1 import access_point_pb2 as _access_point_pb2
from saltoapis.nebula.accessright.v1 import access_right_pb2 as _access_right_pb2
from saltoapis.nebula.accessright.v1 import access_right_pb2 as _access_right_pb2
from saltoapis.nebula.emergencykey.v1 import emergency_key_pb2 as _emergency_key_pb2
from saltoapis.nebula.emergencykey.v1 import emergency_key_pb2 as _emergency_key_pb2
from saltoapis.nebula.unit.v1 import unit_pb2 as _unit_pb2
from saltoapis.nebula.unit.v1 import unit_pb2 as _unit_pb2
from saltoapis.nebula.user.v1 import user_pb2 as _user_pb2
from saltoapis.nebula.user.v1 import user_pb2 as _user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Principal(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class PreviousValues(_message.Message):
    __slots__ = ("values",)
    class ValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[PreviousValues.ValuesEntry]
    def __init__(self, values: _Optional[_Iterable[_Union[PreviousValues.ValuesEntry, _Mapping]]] = ...) -> None: ...

class AccessPointCreated(_message.Message):
    __slots__ = ("access_point", "actor")
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    actor: Principal
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessPointUpdated(_message.Message):
    __slots__ = ("access_point", "actor")
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    actor: Principal
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessPointDeleted(_message.Message):
    __slots__ = ("access_point", "actor")
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    actor: Principal
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessPointUnlocked(_message.Message):
    __slots__ = ("access_point", "user", "emergency_key", "card_key", "app_key", "wallet_key", "passcode")
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    user: _user_pb2.User
    emergency_key: _emergency_key_pb2.EmergencyKey
    card_key: _user_pb2.CardKey
    app_key: _user_pb2.AppKey
    wallet_key: _user_pb2.WalletKey
    passcode: _user_pb2.Passcode
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ..., card_key: _Optional[_Union[_user_pb2.CardKey, _Mapping]] = ..., app_key: _Optional[_Union[_user_pb2.AppKey, _Mapping]] = ..., wallet_key: _Optional[_Union[_user_pb2.WalletKey, _Mapping]] = ..., passcode: _Optional[_Union[_user_pb2.Passcode, _Mapping]] = ...) -> None: ...

class AccessPointLocked(_message.Message):
    __slots__ = ("access_point", "user", "emergency_key", "card_key", "app_key", "wallet_key", "passcode")
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    user: _user_pb2.User
    emergency_key: _emergency_key_pb2.EmergencyKey
    card_key: _user_pb2.CardKey
    app_key: _user_pb2.AppKey
    wallet_key: _user_pb2.WalletKey
    passcode: _user_pb2.Passcode
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ..., card_key: _Optional[_Union[_user_pb2.CardKey, _Mapping]] = ..., app_key: _Optional[_Union[_user_pb2.AppKey, _Mapping]] = ..., wallet_key: _Optional[_Union[_user_pb2.WalletKey, _Mapping]] = ..., passcode: _Optional[_Union[_user_pb2.Passcode, _Mapping]] = ...) -> None: ...

class AccessPointForcedOpen(_message.Message):
    __slots__ = ("access_point",)
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ...) -> None: ...

class AccessPointClosed(_message.Message):
    __slots__ = ("access_point",)
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ...) -> None: ...

class AccessDenied(_message.Message):
    __slots__ = ("access_point", "user", "reason", "emergency_key", "card_key", "app_key", "wallet_key", "passcode")
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_UNSPECIFIED: _ClassVar[AccessDenied.Reason]
        CREDENTIAL_EXPIRED: _ClassVar[AccessDenied.Reason]
    REASON_UNSPECIFIED: AccessDenied.Reason
    CREDENTIAL_EXPIRED: AccessDenied.Reason
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    user: _user_pb2.User
    reason: AccessDenied.Reason
    emergency_key: _emergency_key_pb2.EmergencyKey
    card_key: _user_pb2.CardKey
    app_key: _user_pb2.AppKey
    wallet_key: _user_pb2.WalletKey
    passcode: _user_pb2.Passcode
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., reason: _Optional[_Union[AccessDenied.Reason, str]] = ..., emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ..., card_key: _Optional[_Union[_user_pb2.CardKey, _Mapping]] = ..., app_key: _Optional[_Union[_user_pb2.AppKey, _Mapping]] = ..., wallet_key: _Optional[_Union[_user_pb2.WalletKey, _Mapping]] = ..., passcode: _Optional[_Union[_user_pb2.Passcode, _Mapping]] = ...) -> None: ...

class AccessPointLeftOpen(_message.Message):
    __slots__ = ("access_point",)
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ...) -> None: ...

class AccessRightCreated(_message.Message):
    __slots__ = ("access_right", "actor")
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    actor: Principal
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessRightUpdated(_message.Message):
    __slots__ = ("access_right", "actor")
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    actor: Principal
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessRightDeleted(_message.Message):
    __slots__ = ("access_right", "actor")
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    actor: Principal
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessRightAccessPointCreated(_message.Message):
    __slots__ = ("access_right", "access_point")
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    access_point: _access_point_pb2.AccessPoint
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ...) -> None: ...

class AccessRightAccessPointsBatchCreated(_message.Message):
    __slots__ = ("access_right", "access_points")
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    access_points: _containers.RepeatedCompositeFieldContainer[_access_point_pb2.AccessPoint]
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., access_points: _Optional[_Iterable[_Union[_access_point_pb2.AccessPoint, _Mapping]]] = ...) -> None: ...

class AccessRightAccessPointDeleted(_message.Message):
    __slots__ = ("access_right", "access_point")
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    access_point: _access_point_pb2.AccessPoint
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ...) -> None: ...

class AccessRightAccessPointsBatchDeleted(_message.Message):
    __slots__ = ("access_right", "access_points")
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    access_points: _containers.RepeatedCompositeFieldContainer[_access_point_pb2.AccessPoint]
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., access_points: _Optional[_Iterable[_Union[_access_point_pb2.AccessPoint, _Mapping]]] = ...) -> None: ...

class UserCreated(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class UserUpdated(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class UserBlocked(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class UserUnblocked(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class UserDeleted(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class UserAccessRightCreated(_message.Message):
    __slots__ = ("user", "access_right")
    USER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    access_right: _access_right_pb2.AccessRight
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ...) -> None: ...

class UserAccessRightUpdated(_message.Message):
    __slots__ = ("user", "access_right")
    USER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    access_right: _access_right_pb2.AccessRight
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ...) -> None: ...

class UserAccessRightDeleted(_message.Message):
    __slots__ = ("user", "access_right")
    USER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    access_right: _access_right_pb2.AccessRight
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ...) -> None: ...

class CardKeyAssigned(_message.Message):
    __slots__ = ("user", "card_key")
    USER_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    card_key: _user_pb2.CardKey
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., card_key: _Optional[_Union[_user_pb2.CardKey, _Mapping]] = ...) -> None: ...

class CardKeyCanceled(_message.Message):
    __slots__ = ("user", "card_key")
    USER_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    card_key: _user_pb2.CardKey
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., card_key: _Optional[_Union[_user_pb2.CardKey, _Mapping]] = ...) -> None: ...

class AppKeyAssigned(_message.Message):
    __slots__ = ("user", "app_key")
    USER_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    app_key: _user_pb2.AppKey
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., app_key: _Optional[_Union[_user_pb2.AppKey, _Mapping]] = ...) -> None: ...

class AppKeyCanceled(_message.Message):
    __slots__ = ("user", "app_key")
    USER_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    app_key: _user_pb2.AppKey
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., app_key: _Optional[_Union[_user_pb2.AppKey, _Mapping]] = ...) -> None: ...

class WalletKeyAssigned(_message.Message):
    __slots__ = ("user", "wallet_key")
    USER_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    wallet_key: _user_pb2.WalletKey
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., wallet_key: _Optional[_Union[_user_pb2.WalletKey, _Mapping]] = ...) -> None: ...

class WalletKeyCanceled(_message.Message):
    __slots__ = ("user", "wallet_key")
    USER_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    wallet_key: _user_pb2.WalletKey
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., wallet_key: _Optional[_Union[_user_pb2.WalletKey, _Mapping]] = ...) -> None: ...

class UnitMovedIn(_message.Message):
    __slots__ = ("unit",)
    UNIT_FIELD_NUMBER: _ClassVar[int]
    unit: _unit_pb2.Unit
    def __init__(self, unit: _Optional[_Union[_unit_pb2.Unit, _Mapping]] = ...) -> None: ...

class UnitMovedOut(_message.Message):
    __slots__ = ("unit",)
    UNIT_FIELD_NUMBER: _ClassVar[int]
    unit: _unit_pb2.Unit
    def __init__(self, unit: _Optional[_Union[_unit_pb2.Unit, _Mapping]] = ...) -> None: ...

class UnitCreated(_message.Message):
    __slots__ = ("unit",)
    UNIT_FIELD_NUMBER: _ClassVar[int]
    unit: _unit_pb2.Unit
    def __init__(self, unit: _Optional[_Union[_unit_pb2.Unit, _Mapping]] = ...) -> None: ...

class UnitUpdated(_message.Message):
    __slots__ = ("unit",)
    UNIT_FIELD_NUMBER: _ClassVar[int]
    unit: _unit_pb2.Unit
    def __init__(self, unit: _Optional[_Union[_unit_pb2.Unit, _Mapping]] = ...) -> None: ...

class UnitDeleted(_message.Message):
    __slots__ = ("unit",)
    UNIT_FIELD_NUMBER: _ClassVar[int]
    unit: _unit_pb2.Unit
    def __init__(self, unit: _Optional[_Union[_unit_pb2.Unit, _Mapping]] = ...) -> None: ...

class EmergencyKeyCreated(_message.Message):
    __slots__ = ("emergency_key",)
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    emergency_key: _emergency_key_pb2.EmergencyKey
    def __init__(self, emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ...) -> None: ...

class EmergencyKeyUpdated(_message.Message):
    __slots__ = ("emergency_key",)
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    emergency_key: _emergency_key_pb2.EmergencyKey
    def __init__(self, emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ...) -> None: ...

class EmergencyKeyDeleted(_message.Message):
    __slots__ = ("emergency_key",)
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    emergency_key: _emergency_key_pb2.EmergencyKey
    def __init__(self, emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ...) -> None: ...

class ElectronicKeyAssigned(_message.Message):
    __slots__ = ("user", "electronic_key")
    USER_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    electronic_key: _user_pb2.ElectronicKey
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., electronic_key: _Optional[_Union[_user_pb2.ElectronicKey, _Mapping]] = ...) -> None: ...

class ElectronicKeyCanceled(_message.Message):
    __slots__ = ("user", "electronic_key")
    USER_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    electronic_key: _user_pb2.ElectronicKey
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., electronic_key: _Optional[_Union[_user_pb2.ElectronicKey, _Mapping]] = ...) -> None: ...
