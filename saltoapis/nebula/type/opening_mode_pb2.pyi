from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class OpeningMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPENING_MODE_UNSPECIFIED: _ClassVar[OpeningMode]
    OFFICE: _ClassVar[OpeningMode]
    TOGGLE: _ClassVar[OpeningMode]
OPENING_MODE_UNSPECIFIED: OpeningMode
OFFICE: OpeningMode
TOGGLE: OpeningMode
