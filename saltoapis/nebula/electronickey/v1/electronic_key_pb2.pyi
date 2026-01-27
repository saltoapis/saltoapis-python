from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
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

class ElectronicKey(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_METADATA_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    initialized: bool
    device_id: str
    outdated: bool
    device_metadata: _device_metadata_pb2.DeviceMetadata
    user: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., initialized: _Optional[bool] = ..., device_id: _Optional[str] = ..., outdated: _Optional[bool] = ..., device_metadata: _Optional[_Union[_device_metadata_pb2.DeviceMetadata, _Mapping]] = ..., user: _Optional[str] = ...) -> None: ...

class CreateElectronicKeyRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    electronic_key_id: str
    electronic_key: ElectronicKey
    def __init__(self, parent: _Optional[str] = ..., electronic_key_id: _Optional[str] = ..., electronic_key: _Optional[_Union[ElectronicKey, _Mapping]] = ...) -> None: ...

class GetElectronicKeyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListElectronicKeysRequest(_message.Message):
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

class ListElectronicKeysResponse(_message.Message):
    __slots__ = ()
    ELECTRONIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    electronic_keys: _containers.RepeatedCompositeFieldContainer[ElectronicKey]
    next_page_token: str
    def __init__(self, electronic_keys: _Optional[_Iterable[_Union[ElectronicKey, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateElectronicKeyRequest(_message.Message):
    __slots__ = ()
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    electronic_key: ElectronicKey
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, electronic_key: _Optional[_Union[ElectronicKey, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteElectronicKeyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BindElectronicKeyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_id: str
    def __init__(self, name: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class BindElectronicKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnbindElectronicKeyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: _Optional[bool] = ...) -> None: ...

class UnbindElectronicKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeElectronicKeyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InitializeElectronicKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeElectronicKeyMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigureElectronicKeyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ConfigureElectronicKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigureElectronicKeyMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetElectronicKeyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResetElectronicKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetElectronicKeyMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GenerateAuthorizationTokenRequest(_message.Message):
    __slots__ = ()
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    electronic_key: str
    def __init__(self, electronic_key: _Optional[str] = ...) -> None: ...

class GenerateAuthorizationTokenResponse(_message.Message):
    __slots__ = ()
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorization_token: bytes
    def __init__(self, authorization_token: _Optional[bytes] = ...) -> None: ...

class GenerateFirmwareDownloadUriRequest(_message.Message):
    __slots__ = ()
    ELECTRONIC_KEY_FIELD_NUMBER: _ClassVar[int]
    electronic_key: str
    def __init__(self, electronic_key: _Optional[str] = ...) -> None: ...

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
