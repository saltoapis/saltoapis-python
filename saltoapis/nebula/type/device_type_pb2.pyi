from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_TYPE_UNSPECIFIED: _ClassVar[DeviceType]
    ELECTRONIC_LOCK: _ClassVar[DeviceType]
    GATEWAY: _ClassVar[DeviceType]
    EXTENDER: _ClassVar[DeviceType]
    ENCODER: _ClassVar[DeviceType]
    CONTROLLER: _ClassVar[DeviceType]
    INTERCOM_ADAPTOR: _ClassVar[DeviceType]
    ELECTRONIC_KEY: _ClassVar[DeviceType]
DEVICE_TYPE_UNSPECIFIED: DeviceType
ELECTRONIC_LOCK: DeviceType
GATEWAY: DeviceType
EXTENDER: DeviceType
ENCODER: DeviceType
CONTROLLER: DeviceType
INTERCOM_ADAPTOR: DeviceType
ELECTRONIC_KEY: DeviceType
