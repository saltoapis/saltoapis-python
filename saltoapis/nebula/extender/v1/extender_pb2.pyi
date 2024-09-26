from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Extender(_message.Message):
    __slots__ = ("name", "display_name", "device_id", "gateway", "extender")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    EXTENDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    device_id: str
    gateway: str
    extender: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., device_id: _Optional[str] = ..., gateway: _Optional[str] = ..., extender: _Optional[str] = ...) -> None: ...

class CreateExtenderRequest(_message.Message):
    __slots__ = ("parent", "extender_id", "extender")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXTENDER_ID_FIELD_NUMBER: _ClassVar[int]
    EXTENDER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    extender_id: str
    extender: Extender
    def __init__(self, parent: _Optional[str] = ..., extender_id: _Optional[str] = ..., extender: _Optional[_Union[Extender, _Mapping]] = ...) -> None: ...

class GetExtenderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListExtendersRequest(_message.Message):
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

class ListExtendersResponse(_message.Message):
    __slots__ = ("extenders", "next_page_token")
    EXTENDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    extenders: _containers.RepeatedCompositeFieldContainer[Extender]
    next_page_token: str
    def __init__(self, extenders: _Optional[_Iterable[_Union[Extender, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateExtenderRequest(_message.Message):
    __slots__ = ("extender", "update_mask")
    EXTENDER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    extender: Extender
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, extender: _Optional[_Union[Extender, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteExtenderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BindExtenderRequest(_message.Message):
    __slots__ = ("name", "device_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_id: str
    def __init__(self, name: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class BindExtenderResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnbindExtenderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UnbindExtenderResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateExtenderFirmwareRequest(_message.Message):
    __slots__ = ("extender",)
    EXTENDER_FIELD_NUMBER: _ClassVar[int]
    extender: str
    def __init__(self, extender: _Optional[str] = ...) -> None: ...

class UpdateExtenderFirmwareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateExtenderFirmwareMetadata(_message.Message):
    __slots__ = ("progress_percent",)
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class ResetExtenderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResetExtenderResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetExtenderMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GenerateFirmwareDownloadUriRequest(_message.Message):
    __slots__ = ("extender",)
    EXTENDER_FIELD_NUMBER: _ClassVar[int]
    extender: str
    def __init__(self, extender: _Optional[str] = ...) -> None: ...

class GenerateFirmwareDownloadUriResponse(_message.Message):
    __slots__ = ("download_uri", "digest")
    DOWNLOAD_URI_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    download_uri: str
    digest: str
    def __init__(self, download_uri: _Optional[str] = ..., digest: _Optional[str] = ...) -> None: ...

class GenerateFirmwareDownloadUriMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
