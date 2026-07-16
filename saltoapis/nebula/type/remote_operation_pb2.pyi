from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AppKeyRemoteOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APP_KEY_REMOTE_OPERATION_UNSPECIFIED: _ClassVar[AppKeyRemoteOperation]
    LOCK: _ClassVar[AppKeyRemoteOperation]
    UNLOCK: _ClassVar[AppKeyRemoteOperation]
APP_KEY_REMOTE_OPERATION_UNSPECIFIED: AppKeyRemoteOperation
LOCK: AppKeyRemoteOperation
UNLOCK: AppKeyRemoteOperation
