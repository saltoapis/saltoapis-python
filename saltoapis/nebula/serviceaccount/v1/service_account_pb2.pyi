import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceAccount(_message.Message):
    __slots__ = ("name", "display_name", "client_id", "create_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    client_id: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., client_id: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateServiceAccountRequest(_message.Message):
    __slots__ = ("parent", "service_account_id", "service_account")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_account_id: str
    service_account: ServiceAccount
    def __init__(self, parent: _Optional[str] = ..., service_account_id: _Optional[str] = ..., service_account: _Optional[_Union[ServiceAccount, _Mapping]] = ...) -> None: ...

class GetServiceAccountRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListServiceAccountsRequest(_message.Message):
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

class ListServiceAccountsResponse(_message.Message):
    __slots__ = ("service_accounts", "next_page_token")
    SERVICE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    service_accounts: _containers.RepeatedCompositeFieldContainer[ServiceAccount]
    next_page_token: str
    def __init__(self, service_accounts: _Optional[_Iterable[_Union[ServiceAccount, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateServiceAccountRequest(_message.Message):
    __slots__ = ("service_account", "update_mask")
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    service_account: ServiceAccount
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, service_account: _Optional[_Union[ServiceAccount, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteServiceAccountRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ServiceAccountKey(_message.Message):
    __slots__ = ("name", "private_key_data", "public_key_data", "state", "create_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ServiceAccountKey.State]
        STATE_ACTIVE: _ClassVar[ServiceAccountKey.State]
        STATE_DISABLED: _ClassVar[ServiceAccountKey.State]
    STATE_UNSPECIFIED: ServiceAccountKey.State
    STATE_ACTIVE: ServiceAccountKey.State
    STATE_DISABLED: ServiceAccountKey.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    private_key_data: bytes
    public_key_data: bytes
    state: ServiceAccountKey.State
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., private_key_data: _Optional[bytes] = ..., public_key_data: _Optional[bytes] = ..., state: _Optional[_Union[ServiceAccountKey.State, str]] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateServiceAccountKeyRequest(_message.Message):
    __slots__ = ("parent", "service_account_key")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_account_key: ServiceAccountKey
    def __init__(self, parent: _Optional[str] = ..., service_account_key: _Optional[_Union[ServiceAccountKey, _Mapping]] = ...) -> None: ...

class GetServiceAccountKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListServiceAccountKeysRequest(_message.Message):
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

class ListServiceAccountKeysResponse(_message.Message):
    __slots__ = ("service_account_keys", "next_page_token")
    SERVICE_ACCOUNT_KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    service_account_keys: _containers.RepeatedCompositeFieldContainer[ServiceAccountKey]
    next_page_token: str
    def __init__(self, service_account_keys: _Optional[_Iterable[_Union[ServiceAccountKey, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteServiceAccountKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
