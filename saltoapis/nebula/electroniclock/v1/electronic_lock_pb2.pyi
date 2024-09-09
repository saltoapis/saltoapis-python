from google.protobuf import duration_pb2 as _duration_pb2
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

class ElectronicLock(_message.Message):
    __slots__ = ("name", "display_name", "device_id", "gateway", "extender", "access_point", "initialized", "outdated", "connected", "low_battery", "last_event_time", "calibration_settings", "force_rotate_carriage_end", "hold_back_latch_duration")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    EXTENDER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    LOW_BATTERY_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FORCE_ROTATE_CARRIAGE_END_FIELD_NUMBER: _ClassVar[int]
    HOLD_BACK_LATCH_DURATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    device_id: str
    gateway: str
    extender: str
    access_point: str
    initialized: bool
    outdated: bool
    connected: bool
    low_battery: bool
    last_event_time: _timestamp_pb2.Timestamp
    calibration_settings: bytes
    force_rotate_carriage_end: bool
    hold_back_latch_duration: _duration_pb2.Duration
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., device_id: _Optional[str] = ..., gateway: _Optional[str] = ..., extender: _Optional[str] = ..., access_point: _Optional[str] = ..., initialized: bool = ..., outdated: bool = ..., connected: bool = ..., low_battery: bool = ..., last_event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., calibration_settings: _Optional[bytes] = ..., force_rotate_carriage_end: bool = ..., hold_back_latch_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class CreateElectronicLockRequest(_message.Message):
    __slots__ = ("parent", "electronic_lock_id", "electronic_lock")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_LOCK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    electronic_lock_id: str
    electronic_lock: ElectronicLock
    def __init__(self, parent: _Optional[str] = ..., electronic_lock_id: _Optional[str] = ..., electronic_lock: _Optional[_Union[ElectronicLock, _Mapping]] = ...) -> None: ...

class GetElectronicLockRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListElectronicLocksRequest(_message.Message):
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

class ListElectronicLocksResponse(_message.Message):
    __slots__ = ("electronic_locks", "next_page_token")
    ELECTRONIC_LOCKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    electronic_locks: _containers.RepeatedCompositeFieldContainer[ElectronicLock]
    next_page_token: str
    def __init__(self, electronic_locks: _Optional[_Iterable[_Union[ElectronicLock, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateElectronicLockRequest(_message.Message):
    __slots__ = ("electronic_lock", "update_mask")
    ELECTRONIC_LOCK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    electronic_lock: ElectronicLock
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, electronic_lock: _Optional[_Union[ElectronicLock, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteElectronicLockRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BindElectronicLockRequest(_message.Message):
    __slots__ = ("name", "device_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_id: str
    def __init__(self, name: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class BindElectronicLockResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnbindElectronicLockRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class UnbindElectronicLockResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeElectronicLockRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InitializeElectronicLockResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeElectronicLockMetadata(_message.Message):
    __slots__ = ("progress_percent",)
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class ConfigureElectronicLockRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ConfigureElectronicLockResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigureElectronicLockMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetElectronicLockRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResetElectronicLockResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetElectronicLockMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateElectronicLockFirmwareRequest(_message.Message):
    __slots__ = ("electronic_lock",)
    ELECTRONIC_LOCK_FIELD_NUMBER: _ClassVar[int]
    electronic_lock: str
    def __init__(self, electronic_lock: _Optional[str] = ...) -> None: ...

class UpdateElectronicLockFirmwareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateElectronicLockFirmwareMetadata(_message.Message):
    __slots__ = ("progress_percent",)
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class GenerateAuthorizationTokenRequest(_message.Message):
    __slots__ = ("electronic_lock",)
    ELECTRONIC_LOCK_FIELD_NUMBER: _ClassVar[int]
    electronic_lock: str
    def __init__(self, electronic_lock: _Optional[str] = ...) -> None: ...

class GenerateAuthorizationTokenResponse(_message.Message):
    __slots__ = ("authorization_token",)
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorization_token: bytes
    def __init__(self, authorization_token: _Optional[bytes] = ...) -> None: ...

class GenerateFirmwareDownloadUriRequest(_message.Message):
    __slots__ = ("electronic_lock",)
    ELECTRONIC_LOCK_FIELD_NUMBER: _ClassVar[int]
    electronic_lock: str
    def __init__(self, electronic_lock: _Optional[str] = ...) -> None: ...

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
