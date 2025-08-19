from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from saltoapis.nebula.type import schedule_pb2 as _schedule_pb2
from saltoapis.nebula.type import schedule_pb2 as _schedule_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("name", "parent", "given_name", "family_name", "display_name", "email", "activate_time", "expire_time", "photo", "photo_uri", "card_key", "app_key", "wallet_key", "passcode", "blocked")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GIVEN_NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    PHOTO_URI_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    given_name: str
    family_name: str
    display_name: str
    email: str
    activate_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    photo: str
    photo_uri: str
    card_key: CardKey
    app_key: AppKey
    wallet_key: WalletKey
    passcode: Passcode
    blocked: bool
    def __init__(self, name: _Optional[str] = ..., parent: _Optional[str] = ..., given_name: _Optional[str] = ..., family_name: _Optional[str] = ..., display_name: _Optional[str] = ..., email: _Optional[str] = ..., activate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., photo: _Optional[str] = ..., photo_uri: _Optional[str] = ..., card_key: _Optional[_Union[CardKey, _Mapping]] = ..., app_key: _Optional[_Union[AppKey, _Mapping]] = ..., wallet_key: _Optional[_Union[WalletKey, _Mapping]] = ..., passcode: _Optional[_Union[Passcode, _Mapping]] = ..., blocked: bool = ...) -> None: ...

class UserAccessRight(_message.Message):
    __slots__ = ("name", "access_right", "display_name", "schedules", "effective_schedules", "activate_time", "expire_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    access_right: str
    display_name: str
    schedules: _containers.RepeatedCompositeFieldContainer[_schedule_pb2.Schedule]
    effective_schedules: _containers.RepeatedCompositeFieldContainer[_schedule_pb2.Schedule]
    activate_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., access_right: _Optional[str] = ..., display_name: _Optional[str] = ..., schedules: _Optional[_Iterable[_Union[_schedule_pb2.Schedule, _Mapping]]] = ..., effective_schedules: _Optional[_Iterable[_Union[_schedule_pb2.Schedule, _Mapping]]] = ..., activate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CardKey(_message.Message):
    __slots__ = ("name", "uid", "state", "outdated")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CardKey.State]
        NOT_ASSIGNED: _ClassVar[CardKey.State]
        PENDING: _ClassVar[CardKey.State]
        ACTIVE: _ClassVar[CardKey.State]
    STATE_UNSPECIFIED: CardKey.State
    NOT_ASSIGNED: CardKey.State
    PENDING: CardKey.State
    ACTIVE: CardKey.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    state: CardKey.State
    outdated: bool
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[str] = ..., state: _Optional[_Union[CardKey.State, str]] = ..., outdated: bool = ...) -> None: ...

class AppKey(_message.Message):
    __slots__ = ("name", "state", "outdated")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AppKey.State]
        NOT_ASSIGNED: _ClassVar[AppKey.State]
        PENDING: _ClassVar[AppKey.State]
        ACTIVE: _ClassVar[AppKey.State]
    STATE_UNSPECIFIED: AppKey.State
    NOT_ASSIGNED: AppKey.State
    PENDING: AppKey.State
    ACTIVE: AppKey.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: AppKey.State
    outdated: bool
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[AppKey.State, str]] = ..., outdated: bool = ...) -> None: ...

class WalletKey(_message.Message):
    __slots__ = ("name", "state", "outdated")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[WalletKey.State]
        NOT_ASSIGNED: _ClassVar[WalletKey.State]
        PENDING: _ClassVar[WalletKey.State]
        ACTIVE: _ClassVar[WalletKey.State]
    STATE_UNSPECIFIED: WalletKey.State
    NOT_ASSIGNED: WalletKey.State
    PENDING: WalletKey.State
    ACTIVE: WalletKey.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: WalletKey.State
    outdated: bool
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[WalletKey.State, str]] = ..., outdated: bool = ...) -> None: ...

class Passcode(_message.Message):
    __slots__ = ("name", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Passcode.State]
        NOT_ASSIGNED: _ClassVar[Passcode.State]
        ACTIVE: _ClassVar[Passcode.State]
    STATE_UNSPECIFIED: Passcode.State
    NOT_ASSIGNED: Passcode.State
    ACTIVE: Passcode.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: Passcode.State
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[Passcode.State, str]] = ...) -> None: ...

class ElectronicKey(_message.Message):
    __slots__ = ("name", "device_id", "state", "outdated")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ElectronicKey.State]
        NOT_ASSIGNED: _ClassVar[ElectronicKey.State]
        PENDING: _ClassVar[ElectronicKey.State]
        ACTIVE: _ClassVar[ElectronicKey.State]
    STATE_UNSPECIFIED: ElectronicKey.State
    NOT_ASSIGNED: ElectronicKey.State
    PENDING: ElectronicKey.State
    ACTIVE: ElectronicKey.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_id: str
    state: ElectronicKey.State
    outdated: bool
    def __init__(self, name: _Optional[str] = ..., device_id: _Optional[str] = ..., state: _Optional[_Union[ElectronicKey.State, str]] = ..., outdated: bool = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("parent", "user_id", "user")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_id: str
    user: User
    def __init__(self, parent: _Optional[str] = ..., user_id: _Optional[str] = ..., user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("users", "next_page_token", "total_size")
    USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    next_page_token: str
    total_size: int
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("user", "update_mask")
    USER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    user: User
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BlockUserRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BlockUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnblockUserRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UnblockUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateUserAccessRightRequest(_message.Message):
    __slots__ = ("parent", "user_access_right")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_access_right: UserAccessRight
    def __init__(self, parent: _Optional[str] = ..., user_access_right: _Optional[_Union[UserAccessRight, _Mapping]] = ...) -> None: ...

class GetUserAccessRightRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListUserAccessRightsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListUserAccessRightsResponse(_message.Message):
    __slots__ = ("user_access_rights", "next_page_token")
    USER_ACCESS_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_access_rights: _containers.RepeatedCompositeFieldContainer[UserAccessRight]
    next_page_token: str
    def __init__(self, user_access_rights: _Optional[_Iterable[_Union[UserAccessRight, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateUserAccessRightRequest(_message.Message):
    __slots__ = ("user_access_right", "update_mask")
    USER_ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    user_access_right: UserAccessRight
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, user_access_right: _Optional[_Union[UserAccessRight, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteUserAccessRightRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AssignCardKeyRequest(_message.Message):
    __slots__ = ("name", "uid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[str] = ...) -> None: ...

class CancelCardKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class EncodeCardKeyRequest(_message.Message):
    __slots__ = ("name", "encoder", "electronic_lock", "controller")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENCODER_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_LOCK_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    name: str
    encoder: str
    electronic_lock: str
    controller: str
    def __init__(self, name: _Optional[str] = ..., encoder: _Optional[str] = ..., electronic_lock: _Optional[str] = ..., controller: _Optional[str] = ...) -> None: ...

class EncodeCardKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EncodeCardKeyMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignAppKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CancelAppKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ComputeAppKeyDataRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ComputeAppKeyDataResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class AssignWalletKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AssignWalletKeyResponse(_message.Message):
    __slots__ = ("wallet_key", "access_uri")
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_URI_FIELD_NUMBER: _ClassVar[int]
    wallet_key: WalletKey
    access_uri: str
    def __init__(self, wallet_key: _Optional[_Union[WalletKey, _Mapping]] = ..., access_uri: _Optional[str] = ...) -> None: ...

class CancelWalletKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CancelWalletKeyResponse(_message.Message):
    __slots__ = ("wallet_key",)
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    wallet_key: WalletKey
    def __init__(self, wallet_key: _Optional[_Union[WalletKey, _Mapping]] = ...) -> None: ...

class AssignPasscodeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AssignPasscodeResponse(_message.Message):
    __slots__ = ("passcode", "value")
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    passcode: Passcode
    value: str
    def __init__(self, passcode: _Optional[_Union[Passcode, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...

class CancelPasscodeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CancelPasscodeResponse(_message.Message):
    __slots__ = ("passcode",)
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    passcode: Passcode
    def __init__(self, passcode: _Optional[_Union[Passcode, _Mapping]] = ...) -> None: ...

class AssignElectronicKeyRequest(_message.Message):
    __slots__ = ("name", "device_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_id: str
    def __init__(self, name: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class AssignElectronicKeyResponse(_message.Message):
    __slots__ = ("electronic_key",)
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    electronic_key: ElectronicKey
    def __init__(self, electronic_key: _Optional[_Union[ElectronicKey, _Mapping]] = ...) -> None: ...

class CancelElectronicKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CancelElectronicKeyResponse(_message.Message):
    __slots__ = ("electronic_key",)
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    electronic_key: ElectronicKey
    def __init__(self, electronic_key: _Optional[_Union[ElectronicKey, _Mapping]] = ...) -> None: ...

class EncodeElectronicKeyRequest(_message.Message):
    __slots__ = ("name", "encoder", "electronic_lock", "controller")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENCODER_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_LOCK_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    name: str
    encoder: str
    electronic_lock: str
    controller: str
    def __init__(self, name: _Optional[str] = ..., encoder: _Optional[str] = ..., electronic_lock: _Optional[str] = ..., controller: _Optional[str] = ...) -> None: ...

class EncodeElectronicKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EncodeElectronicKeyMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
