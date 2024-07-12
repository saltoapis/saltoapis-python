from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from saltoapis.nebula.type import day_type_pb2 as _day_type_pb2
from saltoapis.nebula.type import day_type_pb2 as _day_type_pb2
from saltoapis.nebula.type import opening_mode_pb2 as _opening_mode_pb2
from saltoapis.nebula.type import opening_mode_pb2 as _opening_mode_pb2
from saltoapis.type import day_of_week_pb2 as _day_of_week_pb2
from saltoapis.type import day_of_week_pb2 as _day_of_week_pb2
from saltoapis.type import time_of_day_pb2 as _time_of_day_pb2
from saltoapis.type import time_of_day_pb2 as _time_of_day_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OpeningModeSchedule(_message.Message):
    __slots__ = ("name", "display_name", "days")
    class Day(_message.Message):
        __slots__ = ("day_type", "day_of_week", "slots")
        class Slot(_message.Message):
            __slots__ = ("opening_mode", "start_time", "end_time")
            OPENING_MODE_FIELD_NUMBER: _ClassVar[int]
            START_TIME_FIELD_NUMBER: _ClassVar[int]
            END_TIME_FIELD_NUMBER: _ClassVar[int]
            opening_mode: _opening_mode_pb2.OpeningMode
            start_time: _time_of_day_pb2.TimeOfDay
            end_time: _time_of_day_pb2.TimeOfDay
            def __init__(self, opening_mode: _Optional[_Union[_opening_mode_pb2.OpeningMode, str]] = ..., start_time: _Optional[_Union[_time_of_day_pb2.TimeOfDay, _Mapping]] = ..., end_time: _Optional[_Union[_time_of_day_pb2.TimeOfDay, _Mapping]] = ...) -> None: ...
        DAY_TYPE_FIELD_NUMBER: _ClassVar[int]
        DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
        SLOTS_FIELD_NUMBER: _ClassVar[int]
        day_type: _day_type_pb2.DayType
        day_of_week: _day_of_week_pb2.DayOfWeek
        slots: _containers.RepeatedCompositeFieldContainer[OpeningModeSchedule.Day.Slot]
        def __init__(self, day_type: _Optional[_Union[_day_type_pb2.DayType, str]] = ..., day_of_week: _Optional[_Union[_day_of_week_pb2.DayOfWeek, str]] = ..., slots: _Optional[_Iterable[_Union[OpeningModeSchedule.Day.Slot, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    days: _containers.RepeatedCompositeFieldContainer[OpeningModeSchedule.Day]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., days: _Optional[_Iterable[_Union[OpeningModeSchedule.Day, _Mapping]]] = ...) -> None: ...

class CreateOpeningModeScheduleRequest(_message.Message):
    __slots__ = ("parent", "opening_mode_schedule_id", "opening_mode_schedule")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPENING_MODE_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    OPENING_MODE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    opening_mode_schedule_id: str
    opening_mode_schedule: OpeningModeSchedule
    def __init__(self, parent: _Optional[str] = ..., opening_mode_schedule_id: _Optional[str] = ..., opening_mode_schedule: _Optional[_Union[OpeningModeSchedule, _Mapping]] = ...) -> None: ...

class GetOpeningModeScheduleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListOpeningModeSchedulesRequest(_message.Message):
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

class ListOpeningModeSchedulesResponse(_message.Message):
    __slots__ = ("opening_mode_schedules", "next_page_token")
    OPENING_MODE_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    opening_mode_schedules: _containers.RepeatedCompositeFieldContainer[OpeningModeSchedule]
    next_page_token: str
    def __init__(self, opening_mode_schedules: _Optional[_Iterable[_Union[OpeningModeSchedule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateOpeningModeScheduleRequest(_message.Message):
    __slots__ = ("opening_mode_schedule", "update_mask")
    OPENING_MODE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    opening_mode_schedule: OpeningModeSchedule
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, opening_mode_schedule: _Optional[_Union[OpeningModeSchedule, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteOpeningModeScheduleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
