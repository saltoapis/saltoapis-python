from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AppKeyLocalOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APP_KEY_LOCAL_OPERATION_UNSPECIFIED: _ClassVar[AppKeyLocalOperation]
    APP_KEY_LOCAL_OPERATION_UNLOCK: _ClassVar[AppKeyLocalOperation]
    APP_KEY_LOCAL_OPERATION_LOCK: _ClassVar[AppKeyLocalOperation]
APP_KEY_LOCAL_OPERATION_UNSPECIFIED: AppKeyLocalOperation
APP_KEY_LOCAL_OPERATION_UNLOCK: AppKeyLocalOperation
APP_KEY_LOCAL_OPERATION_LOCK: AppKeyLocalOperation
