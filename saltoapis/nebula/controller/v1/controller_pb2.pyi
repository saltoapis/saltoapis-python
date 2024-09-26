from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Controller(_message.Message):
    __slots__ = ("name", "display_name", "device_id", "gateway", "extender", "access_points", "initialized", "outdated", "connected", "last_event_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    EXTENDER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    device_id: str
    gateway: str
    extender: str
    access_points: _containers.RepeatedScalarFieldContainer[str]
    initialized: bool
    outdated: bool
    connected: bool
    last_event_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., device_id: _Optional[str] = ..., gateway: _Optional[str] = ..., extender: _Optional[str] = ..., access_points: _Optional[_Iterable[str]] = ..., initialized: bool = ..., outdated: bool = ..., connected: bool = ..., last_event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateControllerRequest(_message.Message):
    __slots__ = ("parent", "controller_id", "controller")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    controller_id: str
    controller: Controller
    def __init__(self, parent: _Optional[str] = ..., controller_id: _Optional[str] = ..., controller: _Optional[_Union[Controller, _Mapping]] = ...) -> None: ...

class GetControllerRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListControllersRequest(_message.Message):
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

class ListControllersResponse(_message.Message):
    __slots__ = ("controllers", "next_page_token")
    CONTROLLERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    controllers: _containers.RepeatedCompositeFieldContainer[Controller]
    next_page_token: str
    def __init__(self, controllers: _Optional[_Iterable[_Union[Controller, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateControllerRequest(_message.Message):
    __slots__ = ("controller", "update_mask")
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    controller: Controller
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, controller: _Optional[_Union[Controller, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteControllerRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BindControllerRequest(_message.Message):
    __slots__ = ("name", "device_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_id: str
    def __init__(self, name: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class BindControllerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnbindControllerRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class UnbindControllerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeControllerRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InitializeControllerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeControllerMetadata(_message.Message):
    __slots__ = ("progress_percent",)
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class ConfigureControllerRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ConfigureControllerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigureControllerMetadata(_message.Message):
    __slots__ = ("progress_percent",)
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class ResetControllerRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResetControllerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetControllerMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateControllerFirmwareRequest(_message.Message):
    __slots__ = ("controller",)
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    controller: str
    def __init__(self, controller: _Optional[str] = ...) -> None: ...

class UpdateControllerFirmwareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateControllerFirmwareMetadata(_message.Message):
    __slots__ = ("progress_percent",)
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class GenerateFirmwareDownloadUriRequest(_message.Message):
    __slots__ = ("controller",)
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    controller: str
    def __init__(self, controller: _Optional[str] = ...) -> None: ...

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
