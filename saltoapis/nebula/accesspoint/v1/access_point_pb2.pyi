import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from saltoapis.nebula.type import opening_mode_pb2 as _opening_mode_pb2
from saltoapis.nebula.type import opening_mode_pb2 as _opening_mode_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessPoint(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_UPDATER_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_DURATION_FIELD_NUMBER: _ClassVar[int]
    LEFT_OPEN_FIELD_NUMBER: _ClassVar[int]
    ELECTRONIC_LOCK_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    INTERCOM_ADAPTOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    fixed: _opening_mode_pb2.OpeningMode
    schedule: str
    calendar: str
    card_key_updater: bool
    unlock_duration: _duration_pb2.Duration
    left_open: bool
    electronic_lock: str
    controller: str
    intercom_adaptor: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., fixed: _Optional[_Union[_opening_mode_pb2.OpeningMode, str]] = ..., schedule: _Optional[str] = ..., calendar: _Optional[str] = ..., card_key_updater: _Optional[bool] = ..., unlock_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., left_open: _Optional[bool] = ..., electronic_lock: _Optional[str] = ..., controller: _Optional[str] = ..., intercom_adaptor: _Optional[str] = ...) -> None: ...

class CreateAccessPointRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    access_point_id: str
    access_point: AccessPoint
    def __init__(self, parent: _Optional[str] = ..., access_point_id: _Optional[str] = ..., access_point: _Optional[_Union[AccessPoint, _Mapping]] = ...) -> None: ...

class GetAccessPointRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAccessPointsRequest(_message.Message):
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

class ListAccessPointsResponse(_message.Message):
    __slots__ = ()
    ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    access_points: _containers.RepeatedCompositeFieldContainer[AccessPoint]
    next_page_token: str
    total_size: int
    def __init__(self, access_points: _Optional[_Iterable[_Union[AccessPoint, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateAccessPointRequest(_message.Message):
    __slots__ = ()
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    access_point: AccessPoint
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, access_point: _Optional[_Union[AccessPoint, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAccessPointRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UnlockAccessPointRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UnlockAccessPointResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnlockAccessPointMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockAccessPointRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class LockAccessPointResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockAccessPointMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
