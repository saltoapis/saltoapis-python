from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DayType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DAY_TYPE_UNSPECIFIED: _ClassVar[DayType]
    NORMAL: _ClassVar[DayType]
    HOLIDAY: _ClassVar[DayType]
    SPECIAL_1: _ClassVar[DayType]
    SPECIAL_2: _ClassVar[DayType]
DAY_TYPE_UNSPECIFIED: DayType
NORMAL: DayType
HOLIDAY: DayType
SPECIAL_1: DayType
SPECIAL_2: DayType
