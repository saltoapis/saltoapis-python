from google.protobuf import timestamp_pb2 as _timestamp_pb2
from saltoapis.nebula.type import device_type_pb2 as _device_type_pb2
from saltoapis.nebula.type import device_type_pb2 as _device_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Device(_message.Message):
    __slots__ = ("name", "display_name", "device_id", "device_type", "source", "gateway", "extender", "outdated", "connected", "low_battery", "last_event_time", "initialized")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    EXTENDER_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    LOW_BATTERY_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    device_id: str
    device_type: _device_type_pb2.DeviceType
    source: str
    gateway: str
    extender: str
    outdated: bool
    connected: bool
    low_battery: bool
    last_event_time: _timestamp_pb2.Timestamp
    initialized: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., device_id: _Optional[str] = ..., device_type: _Optional[_Union[_device_type_pb2.DeviceType, str]] = ..., source: _Optional[str] = ..., gateway: _Optional[str] = ..., extender: _Optional[str] = ..., outdated: bool = ..., connected: bool = ..., low_battery: bool = ..., last_event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., initialized: bool = ...) -> None: ...

class GetDeviceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDevicesRequest(_message.Message):
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

class ListDevicesResponse(_message.Message):
    __slots__ = ("devices", "next_page_token", "total_size")
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[Device]
    next_page_token: str
    total_size: int
    def __init__(self, devices: _Optional[_Iterable[_Union[Device, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...
