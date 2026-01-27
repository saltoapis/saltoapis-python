import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from saltoapis.nebula.type import device_metadata_pb2 as _device_metadata_pb2
from saltoapis.nebula.type import device_metadata_pb2 as _device_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Encoder(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    EXTENDER_FIELD_NUMBER: _ClassVar[int]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_METADATA_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SOUND_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    device_id: str
    gateway: str
    extender: str
    initialized: bool
    device_metadata: _device_metadata_pb2.DeviceMetadata
    connected: bool
    last_event_time: _timestamp_pb2.Timestamp
    outdated: bool
    disable_sound: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., device_id: _Optional[str] = ..., gateway: _Optional[str] = ..., extender: _Optional[str] = ..., initialized: _Optional[bool] = ..., device_metadata: _Optional[_Union[_device_metadata_pb2.DeviceMetadata, _Mapping]] = ..., connected: _Optional[bool] = ..., last_event_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., outdated: _Optional[bool] = ..., disable_sound: _Optional[bool] = ...) -> None: ...

class CreateEncoderRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENCODER_ID_FIELD_NUMBER: _ClassVar[int]
    ENCODER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    encoder_id: str
    encoder: Encoder
    def __init__(self, parent: _Optional[str] = ..., encoder_id: _Optional[str] = ..., encoder: _Optional[_Union[Encoder, _Mapping]] = ...) -> None: ...

class GetEncoderRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListEncodersRequest(_message.Message):
    __slots__ = ()
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

class ListEncodersResponse(_message.Message):
    __slots__ = ()
    ENCODERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    encoders: _containers.RepeatedCompositeFieldContainer[Encoder]
    next_page_token: str
    def __init__(self, encoders: _Optional[_Iterable[_Union[Encoder, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateEncoderRequest(_message.Message):
    __slots__ = ()
    ENCODER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    encoder: Encoder
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, encoder: _Optional[_Union[Encoder, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteEncoderRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BindEncoderRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_id: str
    def __init__(self, name: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class BindEncoderResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnbindEncoderRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: _Optional[bool] = ...) -> None: ...

class UnbindEncoderResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeEncoderRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InitializeEncoderResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeEncoderMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigureEncoderRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ConfigureEncoderResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigureEncoderMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetEncoderRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResetEncoderResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetEncoderMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateEncoderFirmwareRequest(_message.Message):
    __slots__ = ()
    ENCODER_FIELD_NUMBER: _ClassVar[int]
    encoder: str
    def __init__(self, encoder: _Optional[str] = ...) -> None: ...

class UpdateEncoderFirmwareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateEncoderFirmwareMetadata(_message.Message):
    __slots__ = ()
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class ReadKeyRequest(_message.Message):
    __slots__ = ()
    ENCODER_FIELD_NUMBER: _ClassVar[int]
    encoder: str
    def __init__(self, encoder: _Optional[str] = ...) -> None: ...

class ReadKeyResponse(_message.Message):
    __slots__ = ()
    CARD_KEY_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    card_key: str
    electronic_key: str
    uid: str
    device_id: str
    def __init__(self, card_key: _Optional[str] = ..., electronic_key: _Optional[str] = ..., uid: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class ReadKeyMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GenerateAuthorizationTokenRequest(_message.Message):
    __slots__ = ()
    ENCODER_FIELD_NUMBER: _ClassVar[int]
    encoder: str
    def __init__(self, encoder: _Optional[str] = ...) -> None: ...

class GenerateAuthorizationTokenResponse(_message.Message):
    __slots__ = ()
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorization_token: bytes
    def __init__(self, authorization_token: _Optional[bytes] = ...) -> None: ...

class GenerateFirmwareDownloadUriRequest(_message.Message):
    __slots__ = ()
    ENCODER_FIELD_NUMBER: _ClassVar[int]
    encoder: str
    def __init__(self, encoder: _Optional[str] = ...) -> None: ...

class GenerateFirmwareDownloadUriResponse(_message.Message):
    __slots__ = ()
    DOWNLOAD_URI_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    download_uri: str
    digest: str
    def __init__(self, download_uri: _Optional[str] = ..., digest: _Optional[str] = ...) -> None: ...

class GenerateFirmwareDownloadUriMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
