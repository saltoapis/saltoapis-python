from saltoapis.nebula.type import day_type_pb2 as _day_type_pb2
from saltoapis.nebula.type import day_type_pb2 as _day_type_pb2
from saltoapis.type import day_of_week_pb2 as _day_of_week_pb2
from saltoapis.type import day_of_week_pb2 as _day_of_week_pb2
from saltoapis.type import time_of_day_pb2 as _time_of_day_pb2
from saltoapis.type import time_of_day_pb2 as _time_of_day_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Schedule(_message.Message):
    __slots__ = ()
    class Day(_message.Message):
        __slots__ = ()
        DAY_TYPE_FIELD_NUMBER: _ClassVar[int]
        DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
        day_type: _day_type_pb2.DayType
        day_of_week: _day_of_week_pb2.DayOfWeek
        def __init__(self, day_type: _Optional[_Union[_day_type_pb2.DayType, str]] = ..., day_of_week: _Optional[_Union[_day_of_week_pb2.DayOfWeek, str]] = ...) -> None: ...
    DAYS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    days: _containers.RepeatedCompositeFieldContainer[Schedule.Day]
    start_time: _time_of_day_pb2.TimeOfDay
    end_time: _time_of_day_pb2.TimeOfDay
    def __init__(self, days: _Optional[_Iterable[_Union[Schedule.Day, _Mapping]]] = ..., start_time: _Optional[_Union[_time_of_day_pb2.TimeOfDay, _Mapping]] = ..., end_time: _Optional[_Union[_time_of_day_pb2.TimeOfDay, _Mapping]] = ...) -> None: ...
