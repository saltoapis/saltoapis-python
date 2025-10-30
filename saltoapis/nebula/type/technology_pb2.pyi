from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AppKeyTechnology(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APP_KEY_TECHNOLOGY_UNSPECIFIED: _ClassVar[AppKeyTechnology]
    BLE: _ClassVar[AppKeyTechnology]
    NFC_HCE: _ClassVar[AppKeyTechnology]
    NFC_READER: _ClassVar[AppKeyTechnology]
APP_KEY_TECHNOLOGY_UNSPECIFIED: AppKeyTechnology
BLE: AppKeyTechnology
NFC_HCE: AppKeyTechnology
NFC_READER: AppKeyTechnology
