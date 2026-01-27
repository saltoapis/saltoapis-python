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

class Controller(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    EXTENDER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_METADATA_FIELD_NUMBER: _ClassVar[int]
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
    device_metadata: _device_metadata_pb2.DeviceMetadata
    outdated: bool
    connected: bool
    last_event_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., device_id: _Optional[str] = ..., gateway: _Optional[str] = ..., extender: _Optional[str] = ..., access_points: _Optional[_Iterable[str]] = ..., initialized: _Optional[bool] = ..., device_metadata: _Optional[_Union[_device_metadata_pb2.DeviceMetadata, _Mapping]] = ..., outdated: _Optional[bool] = ..., connected: _Optional[bool] = ..., last_event_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ControllerRelay(_message.Message):
    __slots__ = ()
    class DestinationOutput(_message.Message):
        __slots__ = ()
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        destination: str
        def __init__(self, destination: _Optional[str] = ...) -> None: ...
    class Strike(_message.Message):
        __slots__ = ()
        ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
        access_point: str
        def __init__(self, access_point: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIP_SWITCH_FIELD_NUMBER: _ClassVar[int]
    RELAY_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    STRIKE_FIELD_NUMBER: _ClassVar[int]
    name: str
    dip_switch: int
    relay_id: int
    destination_output: ControllerRelay.DestinationOutput
    strike: ControllerRelay.Strike
    def __init__(self, name: _Optional[str] = ..., dip_switch: _Optional[int] = ..., relay_id: _Optional[int] = ..., destination_output: _Optional[_Union[ControllerRelay.DestinationOutput, _Mapping]] = ..., strike: _Optional[_Union[ControllerRelay.Strike, _Mapping]] = ...) -> None: ...

class CreateControllerRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    controller_id: str
    controller: Controller
    def __init__(self, parent: _Optional[str] = ..., controller_id: _Optional[str] = ..., controller: _Optional[_Union[Controller, _Mapping]] = ...) -> None: ...

class GetControllerRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListControllersRequest(_message.Message):
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

class ListControllersResponse(_message.Message):
    __slots__ = ()
    CONTROLLERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    controllers: _containers.RepeatedCompositeFieldContainer[Controller]
    next_page_token: str
    def __init__(self, controllers: _Optional[_Iterable[_Union[Controller, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateControllerRequest(_message.Message):
    __slots__ = ()
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    controller: Controller
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, controller: _Optional[_Union[Controller, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteControllerRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BindControllerRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_id: str
    def __init__(self, name: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class BindControllerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnbindControllerRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: _Optional[bool] = ...) -> None: ...

class UnbindControllerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeControllerRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InitializeControllerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeControllerMetadata(_message.Message):
    __slots__ = ()
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class ConfigureControllerRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ConfigureControllerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigureControllerMetadata(_message.Message):
    __slots__ = ()
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class ResetControllerRequest(_message.Message):
    __slots__ = ()
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
    __slots__ = ()
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    controller: str
    def __init__(self, controller: _Optional[str] = ...) -> None: ...

class UpdateControllerFirmwareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateControllerFirmwareMetadata(_message.Message):
    __slots__ = ()
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class GenerateAuthorizationTokenRequest(_message.Message):
    __slots__ = ()
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    controller: str
    def __init__(self, controller: _Optional[str] = ...) -> None: ...

class GenerateAuthorizationTokenResponse(_message.Message):
    __slots__ = ()
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorization_token: bytes
    def __init__(self, authorization_token: _Optional[bytes] = ...) -> None: ...

class GenerateFirmwareDownloadUriRequest(_message.Message):
    __slots__ = ()
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    controller: str
    def __init__(self, controller: _Optional[str] = ...) -> None: ...

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

class CreateControllerRelayRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_RELAY_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_RELAY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    controller_relay_id: str
    controller_relay: ControllerRelay
    def __init__(self, parent: _Optional[str] = ..., controller_relay_id: _Optional[str] = ..., controller_relay: _Optional[_Union[ControllerRelay, _Mapping]] = ...) -> None: ...

class GetControllerRelayRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListControllerRelaysRequest(_message.Message):
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

class ListControllerRelaysResponse(_message.Message):
    __slots__ = ()
    CONTROLLER_RELAYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    controller_relays: _containers.RepeatedCompositeFieldContainer[ControllerRelay]
    next_page_token: str
    def __init__(self, controller_relays: _Optional[_Iterable[_Union[ControllerRelay, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateControllerRelayRequest(_message.Message):
    __slots__ = ()
    CONTROLLER_RELAY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    controller_relay: ControllerRelay
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, controller_relay: _Optional[_Union[ControllerRelay, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteControllerRelayRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BatchDeleteControllerRelaysRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[DeleteControllerRelayRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[DeleteControllerRelayRequest, _Mapping]]] = ...) -> None: ...

class BatchDeleteControllerRelaysResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatchCreateControllerRelaysRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateControllerRelayRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[CreateControllerRelayRequest, _Mapping]]] = ...) -> None: ...

class BatchCreateControllerRelaysResponse(_message.Message):
    __slots__ = ()
    CONTROLLER_RELAYS_FIELD_NUMBER: _ClassVar[int]
    controller_relays: _containers.RepeatedCompositeFieldContainer[ControllerRelay]
    def __init__(self, controller_relays: _Optional[_Iterable[_Union[ControllerRelay, _Mapping]]] = ...) -> None: ...

class BatchUpdateControllerRelaysRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[UpdateControllerRelayRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[UpdateControllerRelayRequest, _Mapping]]] = ...) -> None: ...

class BatchUpdateControllerRelaysResponse(_message.Message):
    __slots__ = ()
    CONTROLLER_RELAYS_FIELD_NUMBER: _ClassVar[int]
    controller_relays: _containers.RepeatedCompositeFieldContainer[ControllerRelay]
    def __init__(self, controller_relays: _Optional[_Iterable[_Union[ControllerRelay, _Mapping]]] = ...) -> None: ...
