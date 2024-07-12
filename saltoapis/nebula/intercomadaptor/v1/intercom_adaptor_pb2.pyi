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

class IntercomAdaptor(_message.Message):
    __slots__ = ("name", "display_name", "device_id", "gateway", "extender", "access_points", "initialized", "outdated", "connected", "low_battery", "last_event_time", "intercom", "photos", "photo_uris", "readings")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    EXTENDER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    LOW_BATTERY_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    INTERCOM_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    PHOTO_URIS_FIELD_NUMBER: _ClassVar[int]
    READINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    device_id: str
    gateway: str
    extender: str
    access_points: _containers.RepeatedCompositeFieldContainer[IntercomAdaptorAccessPoint]
    initialized: bool
    outdated: bool
    connected: bool
    low_battery: bool
    last_event_time: _timestamp_pb2.Timestamp
    intercom: str
    photos: _containers.RepeatedScalarFieldContainer[str]
    photo_uris: _containers.RepeatedScalarFieldContainer[str]
    readings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., device_id: _Optional[str] = ..., gateway: _Optional[str] = ..., extender: _Optional[str] = ..., access_points: _Optional[_Iterable[_Union[IntercomAdaptorAccessPoint, _Mapping]]] = ..., initialized: bool = ..., outdated: bool = ..., connected: bool = ..., low_battery: bool = ..., last_event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., intercom: _Optional[str] = ..., photos: _Optional[_Iterable[str]] = ..., photo_uris: _Optional[_Iterable[str]] = ..., readings: _Optional[_Iterable[str]] = ...) -> None: ...

class IntercomAdaptorAccessPoint(_message.Message):
    __slots__ = ("access_point", "frame_settings")
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    FRAME_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    access_point: str
    frame_settings: bytes
    def __init__(self, access_point: _Optional[str] = ..., frame_settings: _Optional[bytes] = ...) -> None: ...

class CreateIntercomAdaptorRequest(_message.Message):
    __slots__ = ("parent", "intercom_adaptor_id", "intercom_adaptor")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INTERCOM_ADAPTOR_ID_FIELD_NUMBER: _ClassVar[int]
    INTERCOM_ADAPTOR_FIELD_NUMBER: _ClassVar[int]
    parent: str
    intercom_adaptor_id: str
    intercom_adaptor: IntercomAdaptor
    def __init__(self, parent: _Optional[str] = ..., intercom_adaptor_id: _Optional[str] = ..., intercom_adaptor: _Optional[_Union[IntercomAdaptor, _Mapping]] = ...) -> None: ...

class GetIntercomAdaptorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListIntercomAdaptorsRequest(_message.Message):
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

class ListIntercomAdaptorsResponse(_message.Message):
    __slots__ = ("intercom_adaptors", "next_page_token")
    INTERCOM_ADAPTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    intercom_adaptors: _containers.RepeatedCompositeFieldContainer[IntercomAdaptor]
    next_page_token: str
    def __init__(self, intercom_adaptors: _Optional[_Iterable[_Union[IntercomAdaptor, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateIntercomAdaptorRequest(_message.Message):
    __slots__ = ("intercom_adaptor", "update_mask")
    INTERCOM_ADAPTOR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    intercom_adaptor: IntercomAdaptor
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, intercom_adaptor: _Optional[_Union[IntercomAdaptor, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteIntercomAdaptorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BindIntercomAdaptorRequest(_message.Message):
    __slots__ = ("name", "device_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_id: str
    def __init__(self, name: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class BindIntercomAdaptorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnbindIntercomAdaptorRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class UnbindIntercomAdaptorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeIntercomAdaptorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InitializeIntercomAdaptorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeIntercomAdaptorMetadata(_message.Message):
    __slots__ = ("progress_percent",)
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class ConfigureIntercomAdaptorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ConfigureIntercomAdaptorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigureIntercomAdaptorMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetIntercomAdaptorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResetIntercomAdaptorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetIntercomAdaptorMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateIntercomAdaptorFirmwareRequest(_message.Message):
    __slots__ = ("intercom_adaptor",)
    INTERCOM_ADAPTOR_FIELD_NUMBER: _ClassVar[int]
    intercom_adaptor: str
    def __init__(self, intercom_adaptor: _Optional[str] = ...) -> None: ...

class UpdateIntercomAdaptorFirmwareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateIntercomAdaptorFirmwareMetadata(_message.Message):
    __slots__ = ("progress_percent",)
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class GenerateAuthorizationTokenRequest(_message.Message):
    __slots__ = ("intercom_adaptor",)
    INTERCOM_ADAPTOR_FIELD_NUMBER: _ClassVar[int]
    intercom_adaptor: str
    def __init__(self, intercom_adaptor: _Optional[str] = ...) -> None: ...

class GenerateAuthorizationTokenResponse(_message.Message):
    __slots__ = ("authorization_token",)
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorization_token: bytes
    def __init__(self, authorization_token: _Optional[bytes] = ...) -> None: ...
