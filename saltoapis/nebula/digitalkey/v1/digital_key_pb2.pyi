from google.protobuf import timestamp_pb2 as _timestamp_pb2
from saltoapis.type import color_pb2 as _color_pb2
from saltoapis.type import color_pb2 as _color_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DigitalKey(_message.Message):
    __slots__ = ("name", "app_key", "wallet_key")
    class Metadata(_message.Message):
        __slots__ = ("title", "subtitle", "photo_uri", "address", "text_color")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        PHOTO_URI_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        photo_uri: str
        address: str
        text_color: _color_pb2.Color
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., photo_uri: _Optional[str] = ..., address: _Optional[str] = ..., text_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ...) -> None: ...
    class AppKey(_message.Message):
        __slots__ = ("metadata", "data", "installation", "unit", "installation_id", "unit_id", "access_points_sync_time", "access_points_sync_state")
        class AccessPointsSyncState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACCESS_POINTS_SYNC_STATE_UNSPECIFIED: _ClassVar[DigitalKey.AppKey.AccessPointsSyncState]
            INVALIDATED: _ClassVar[DigitalKey.AppKey.AccessPointsSyncState]
            SYNCING: _ClassVar[DigitalKey.AppKey.AccessPointsSyncState]
            SYNCED: _ClassVar[DigitalKey.AppKey.AccessPointsSyncState]
            NOT_SUPPORTED: _ClassVar[DigitalKey.AppKey.AccessPointsSyncState]
        ACCESS_POINTS_SYNC_STATE_UNSPECIFIED: DigitalKey.AppKey.AccessPointsSyncState
        INVALIDATED: DigitalKey.AppKey.AccessPointsSyncState
        SYNCING: DigitalKey.AppKey.AccessPointsSyncState
        SYNCED: DigitalKey.AppKey.AccessPointsSyncState
        NOT_SUPPORTED: DigitalKey.AppKey.AccessPointsSyncState
        METADATA_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        INSTALLATION_FIELD_NUMBER: _ClassVar[int]
        UNIT_FIELD_NUMBER: _ClassVar[int]
        INSTALLATION_ID_FIELD_NUMBER: _ClassVar[int]
        UNIT_ID_FIELD_NUMBER: _ClassVar[int]
        ACCESS_POINTS_SYNC_TIME_FIELD_NUMBER: _ClassVar[int]
        ACCESS_POINTS_SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
        metadata: DigitalKey.Metadata
        data: bytes
        installation: str
        unit: str
        installation_id: str
        unit_id: str
        access_points_sync_time: _timestamp_pb2.Timestamp
        access_points_sync_state: DigitalKey.AppKey.AccessPointsSyncState
        def __init__(self, metadata: _Optional[_Union[DigitalKey.Metadata, _Mapping]] = ..., data: _Optional[bytes] = ..., installation: _Optional[str] = ..., unit: _Optional[str] = ..., installation_id: _Optional[str] = ..., unit_id: _Optional[str] = ..., access_points_sync_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., access_points_sync_state: _Optional[_Union[DigitalKey.AppKey.AccessPointsSyncState, str]] = ...) -> None: ...
    class WalletKey(_message.Message):
        __slots__ = ("metadata", "hydra_credential")
        class HydraCredential(_message.Message):
            __slots__ = ("credential_id", "sharing_instance_id", "account_hash", "template_id", "relying_party_id", "reference_id")
            CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
            SHARING_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
            ACCOUNT_HASH_FIELD_NUMBER: _ClassVar[int]
            TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
            RELYING_PARTY_ID_FIELD_NUMBER: _ClassVar[int]
            REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
            credential_id: str
            sharing_instance_id: str
            account_hash: str
            template_id: str
            relying_party_id: str
            reference_id: str
            def __init__(self, credential_id: _Optional[str] = ..., sharing_instance_id: _Optional[str] = ..., account_hash: _Optional[str] = ..., template_id: _Optional[str] = ..., relying_party_id: _Optional[str] = ..., reference_id: _Optional[str] = ...) -> None: ...
        METADATA_FIELD_NUMBER: _ClassVar[int]
        HYDRA_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
        metadata: DigitalKey.Metadata
        hydra_credential: DigitalKey.WalletKey.HydraCredential
        def __init__(self, metadata: _Optional[_Union[DigitalKey.Metadata, _Mapping]] = ..., hydra_credential: _Optional[_Union[DigitalKey.WalletKey.HydraCredential, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    WALLET_KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    app_key: DigitalKey.AppKey
    wallet_key: DigitalKey.WalletKey
    def __init__(self, name: _Optional[str] = ..., app_key: _Optional[_Union[DigitalKey.AppKey, _Mapping]] = ..., wallet_key: _Optional[_Union[DigitalKey.WalletKey, _Mapping]] = ...) -> None: ...

class GetDigitalKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDigitalKeysRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "filter", "order_by")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListDigitalKeysResponse(_message.Message):
    __slots__ = ("digital_keys", "next_page_token")
    DIGITAL_KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    digital_keys: _containers.RepeatedCompositeFieldContainer[DigitalKey]
    next_page_token: str
    def __init__(self, digital_keys: _Optional[_Iterable[_Union[DigitalKey, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DigitalKeyAccessPoint(_message.Message):
    __slots__ = ("name", "display_name", "device_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    device_id: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class GetDigitalKeyAccessPointRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDigitalKeyAccessPointsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDigitalKeyAccessPointsResponse(_message.Message):
    __slots__ = ("digital_key_access_points", "next_page_token")
    DIGITAL_KEY_ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    digital_key_access_points: _containers.RepeatedCompositeFieldContainer[DigitalKeyAccessPoint]
    next_page_token: str
    def __init__(self, digital_key_access_points: _Optional[_Iterable[_Union[DigitalKeyAccessPoint, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
