from google.protobuf import struct_pb2 as _struct_pb2
from saltoapis.nebula.accesspoint.v1 import access_point_pb2 as _access_point_pb2
from saltoapis.nebula.accesspoint.v1 import access_point_pb2 as _access_point_pb2
from saltoapis.nebula.accessright.v1 import access_right_pb2 as _access_right_pb2
from saltoapis.nebula.accessright.v1 import access_right_pb2 as _access_right_pb2
from saltoapis.nebula.controller.v1 import controller_pb2 as _controller_pb2
from saltoapis.nebula.controller.v1 import controller_pb2 as _controller_pb2
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
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Principal(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class PreviousValues(_message.Message):
    __slots__ = ()
    class ValuesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, values: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class AccessPointCreated(_message.Message):
    __slots__ = ()
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    actor: Principal
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessPointUpdated(_message.Message):
    __slots__ = ()
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VALUES_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    actor: Principal
    previous_values: PreviousValues
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ..., previous_values: _Optional[_Union[PreviousValues, _Mapping]] = ...) -> None: ...

class AccessPointDeleted(_message.Message):
    __slots__ = ()
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    actor: Principal
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessPointUnlocked(_message.Message):
    __slots__ = ()
    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIRECTION_UNSPECIFIED: _ClassVar[AccessPointUnlocked.Direction]
        ENTRY: _ClassVar[AccessPointUnlocked.Direction]
        EXIT: _ClassVar[AccessPointUnlocked.Direction]
    DIRECTION_UNSPECIFIED: AccessPointUnlocked.Direction
    ENTRY: AccessPointUnlocked.Direction
    EXIT: AccessPointUnlocked.Direction
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    user: _user_pb2.User
    emergency_key: _emergency_key_pb2.EmergencyKey
    card_key: _user_pb2.CardKey
    app_key: _user_pb2.AppKey
    wallet_key: _user_pb2.WalletKey
    passcode: _user_pb2.Passcode
    electronic_key: _user_pb2.ElectronicKey
    direction: AccessPointUnlocked.Direction
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ..., card_key: _Optional[_Union[_user_pb2.CardKey, _Mapping]] = ..., app_key: _Optional[_Union[_user_pb2.AppKey, _Mapping]] = ..., wallet_key: _Optional[_Union[_user_pb2.WalletKey, _Mapping]] = ..., passcode: _Optional[_Union[_user_pb2.Passcode, _Mapping]] = ..., electronic_key: _Optional[_Union[_user_pb2.ElectronicKey, _Mapping]] = ..., direction: _Optional[_Union[AccessPointUnlocked.Direction, str]] = ...) -> None: ...

class AccessPointLocked(_message.Message):
    __slots__ = ()
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    user: _user_pb2.User
    emergency_key: _emergency_key_pb2.EmergencyKey
    card_key: _user_pb2.CardKey
    app_key: _user_pb2.AppKey
    wallet_key: _user_pb2.WalletKey
    passcode: _user_pb2.Passcode
    electronic_key: _user_pb2.ElectronicKey
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ..., card_key: _Optional[_Union[_user_pb2.CardKey, _Mapping]] = ..., app_key: _Optional[_Union[_user_pb2.AppKey, _Mapping]] = ..., wallet_key: _Optional[_Union[_user_pb2.WalletKey, _Mapping]] = ..., passcode: _Optional[_Union[_user_pb2.Passcode, _Mapping]] = ..., electronic_key: _Optional[_Union[_user_pb2.ElectronicKey, _Mapping]] = ...) -> None: ...

class AccessPointForcedOpen(_message.Message):
    __slots__ = ()
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ...) -> None: ...

class AccessPointClosed(_message.Message):
    __slots__ = ()
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ...) -> None: ...

class AccessDenied(_message.Message):
    __slots__ = ()
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_UNSPECIFIED: _ClassVar[AccessDenied.Reason]
        CREDENTIAL_EXPIRED: _ClassVar[AccessDenied.Reason]
        CREDENTIAL_UNACTIVATED: _ClassVar[AccessDenied.Reason]
        CREDENTIAL_PERMISSION_INSUFFICIENT: _ClassVar[AccessDenied.Reason]
        CREDENTIAL_PERMISSION_OUTSIDE_VALIDITY: _ClassVar[AccessDenied.Reason]
        CREDENTIAL_PERMISSION_OUTSIDE_SCHEDULE: _ClassVar[AccessDenied.Reason]
        INVALID_ACCESS_CODE: _ClassVar[AccessDenied.Reason]
        DEVICE_BATTERY_INSUFFICIENT: _ClassVar[AccessDenied.Reason]
    REASON_UNSPECIFIED: AccessDenied.Reason
    CREDENTIAL_EXPIRED: AccessDenied.Reason
    CREDENTIAL_UNACTIVATED: AccessDenied.Reason
    CREDENTIAL_PERMISSION_INSUFFICIENT: AccessDenied.Reason
    CREDENTIAL_PERMISSION_OUTSIDE_VALIDITY: AccessDenied.Reason
    CREDENTIAL_PERMISSION_OUTSIDE_SCHEDULE: AccessDenied.Reason
    INVALID_ACCESS_CODE: AccessDenied.Reason
    DEVICE_BATTERY_INSUFFICIENT: AccessDenied.Reason
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    controller: _controller_pb2.Controller
    user: _user_pb2.User
    reason: AccessDenied.Reason
    emergency_key: _emergency_key_pb2.EmergencyKey
    card_key: _user_pb2.CardKey
    app_key: _user_pb2.AppKey
    wallet_key: _user_pb2.WalletKey
    passcode: _user_pb2.Passcode
    electronic_key: _user_pb2.ElectronicKey
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., controller: _Optional[_Union[_controller_pb2.Controller, _Mapping]] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., reason: _Optional[_Union[AccessDenied.Reason, str]] = ..., emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ..., card_key: _Optional[_Union[_user_pb2.CardKey, _Mapping]] = ..., app_key: _Optional[_Union[_user_pb2.AppKey, _Mapping]] = ..., wallet_key: _Optional[_Union[_user_pb2.WalletKey, _Mapping]] = ..., passcode: _Optional[_Union[_user_pb2.Passcode, _Mapping]] = ..., electronic_key: _Optional[_Union[_user_pb2.ElectronicKey, _Mapping]] = ...) -> None: ...

class AccessPointLeftOpen(_message.Message):
    __slots__ = ()
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    access_point: _access_point_pb2.AccessPoint
    def __init__(self, access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ...) -> None: ...

class AccessRightCreated(_message.Message):
    __slots__ = ()
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    actor: Principal
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessRightUpdated(_message.Message):
    __slots__ = ()
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VALUES_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    actor: Principal
    previous_values: PreviousValues
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ..., previous_values: _Optional[_Union[PreviousValues, _Mapping]] = ...) -> None: ...

class AccessRightDeleted(_message.Message):
    __slots__ = ()
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    actor: Principal
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessRightAccessPointCreated(_message.Message):
    __slots__ = ()
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    access_point: _access_point_pb2.AccessPoint
    actor: Principal
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessRightAccessPointsBatchCreated(_message.Message):
    __slots__ = ()
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    access_points: _containers.RepeatedCompositeFieldContainer[_access_point_pb2.AccessPoint]
    actor: Principal
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., access_points: _Optional[_Iterable[_Union[_access_point_pb2.AccessPoint, _Mapping]]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessRightAccessPointDeleted(_message.Message):
    __slots__ = ()
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    access_point: _access_point_pb2.AccessPoint
    actor: Principal
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., access_point: _Optional[_Union[_access_point_pb2.AccessPoint, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessRightAccessPointsBatchDeleted(_message.Message):
    __slots__ = ()
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    access_right: _access_right_pb2.AccessRight
    access_points: _containers.RepeatedCompositeFieldContainer[_access_point_pb2.AccessPoint]
    actor: Principal
    def __init__(self, access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., access_points: _Optional[_Iterable[_Union[_access_point_pb2.AccessPoint, _Mapping]]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class UserCreated(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class UserUpdated(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VALUES_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    actor: Principal
    previous_values: PreviousValues
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ..., previous_values: _Optional[_Union[PreviousValues, _Mapping]] = ...) -> None: ...

class UserBlocked(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class UserUnblocked(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class UserDeleted(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class UserAccessRightCreated(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    access_right: _access_right_pb2.AccessRight
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class UserAccessRightUpdated(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    access_right: _access_right_pb2.AccessRight
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class UserAccessRightDeleted(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    access_right: _access_right_pb2.AccessRight
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., access_right: _Optional[_Union[_access_right_pb2.AccessRight, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class CardKeyAssigned(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    card_key: _user_pb2.CardKey
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., card_key: _Optional[_Union[_user_pb2.CardKey, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class CardKeyCanceled(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    card_key: _user_pb2.CardKey
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., card_key: _Optional[_Union[_user_pb2.CardKey, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AppKeyAssigned(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    app_key: _user_pb2.AppKey
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., app_key: _Optional[_Union[_user_pb2.AppKey, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AppKeyCanceled(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    app_key: _user_pb2.AppKey
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., app_key: _Optional[_Union[_user_pb2.AppKey, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class WalletKeyAssigned(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    wallet_key: _user_pb2.WalletKey
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., wallet_key: _Optional[_Union[_user_pb2.WalletKey, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class WalletKeyCanceled(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    wallet_key: _user_pb2.WalletKey
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., wallet_key: _Optional[_Union[_user_pb2.WalletKey, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class UnitMovedIn(_message.Message):
    __slots__ = ()
    UNIT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    unit: _unit_pb2.Unit
    actor: Principal
    def __init__(self, unit: _Optional[_Union[_unit_pb2.Unit, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class UnitMovedOut(_message.Message):
    __slots__ = ()
    UNIT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    unit: _unit_pb2.Unit
    actor: Principal
    def __init__(self, unit: _Optional[_Union[_unit_pb2.Unit, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class UnitCreated(_message.Message):
    __slots__ = ()
    UNIT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    unit: _unit_pb2.Unit
    actor: Principal
    def __init__(self, unit: _Optional[_Union[_unit_pb2.Unit, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class UnitUpdated(_message.Message):
    __slots__ = ()
    UNIT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VALUES_FIELD_NUMBER: _ClassVar[int]
    unit: _unit_pb2.Unit
    actor: Principal
    previous_values: PreviousValues
    def __init__(self, unit: _Optional[_Union[_unit_pb2.Unit, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ..., previous_values: _Optional[_Union[PreviousValues, _Mapping]] = ...) -> None: ...

class UnitDeleted(_message.Message):
    __slots__ = ()
    UNIT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    unit: _unit_pb2.Unit
    actor: Principal
    def __init__(self, unit: _Optional[_Union[_unit_pb2.Unit, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class EmergencyKeyCreated(_message.Message):
    __slots__ = ()
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    emergency_key: _emergency_key_pb2.EmergencyKey
    actor: Principal
    def __init__(self, emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class EmergencyKeyUpdated(_message.Message):
    __slots__ = ()
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VALUES_FIELD_NUMBER: _ClassVar[int]
    emergency_key: _emergency_key_pb2.EmergencyKey
    actor: Principal
    previous_values: PreviousValues
    def __init__(self, emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ..., previous_values: _Optional[_Union[PreviousValues, _Mapping]] = ...) -> None: ...

class EmergencyKeyDeleted(_message.Message):
    __slots__ = ()
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    emergency_key: _emergency_key_pb2.EmergencyKey
    actor: Principal
    def __init__(self, emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class ElectronicKeyAssigned(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    electronic_key: _user_pb2.ElectronicKey
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., electronic_key: _Optional[_Union[_user_pb2.ElectronicKey, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class ElectronicKeyCanceled(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    electronic_key: _user_pb2.ElectronicKey
    actor: Principal
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., electronic_key: _Optional[_Union[_user_pb2.ElectronicKey, _Mapping]] = ..., actor: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class AccessGranted(_message.Message):
    __slots__ = ()
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    controller: _controller_pb2.Controller
    user: _user_pb2.User
    emergency_key: _emergency_key_pb2.EmergencyKey
    card_key: _user_pb2.CardKey
    app_key: _user_pb2.AppKey
    wallet_key: _user_pb2.WalletKey
    passcode: _user_pb2.Passcode
    electronic_key: _user_pb2.ElectronicKey
    def __init__(self, controller: _Optional[_Union[_controller_pb2.Controller, _Mapping]] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., emergency_key: _Optional[_Union[_emergency_key_pb2.EmergencyKey, _Mapping]] = ..., card_key: _Optional[_Union[_user_pb2.CardKey, _Mapping]] = ..., app_key: _Optional[_Union[_user_pb2.AppKey, _Mapping]] = ..., wallet_key: _Optional[_Union[_user_pb2.WalletKey, _Mapping]] = ..., passcode: _Optional[_Union[_user_pb2.Passcode, _Mapping]] = ..., electronic_key: _Optional[_Union[_user_pb2.ElectronicKey, _Mapping]] = ...) -> None: ...
