from saltoapis.type import date_pb2 as _date_pb2
from saltoapis.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceMetadata(_message.Message):
    __slots__ = ("circuit_boards",)
    class CircuitBoard(_message.Message):
        __slots__ = ("manufacture_date", "serial_number", "firmwares")
        class Firmware(_message.Message):
            __slots__ = ("number", "version", "revision")
            NUMBER_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            REVISION_FIELD_NUMBER: _ClassVar[int]
            number: str
            version: str
            revision: str
            def __init__(self, number: _Optional[str] = ..., version: _Optional[str] = ..., revision: _Optional[str] = ...) -> None: ...
        MANUFACTURE_DATE_FIELD_NUMBER: _ClassVar[int]
        SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        FIRMWARES_FIELD_NUMBER: _ClassVar[int]
        manufacture_date: _date_pb2.Date
        serial_number: str
        firmwares: _containers.RepeatedCompositeFieldContainer[DeviceMetadata.CircuitBoard.Firmware]
        def __init__(self, manufacture_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., serial_number: _Optional[str] = ..., firmwares: _Optional[_Iterable[_Union[DeviceMetadata.CircuitBoard.Firmware, _Mapping]]] = ...) -> None: ...
    CIRCUIT_BOARDS_FIELD_NUMBER: _ClassVar[int]
    circuit_boards: _containers.RepeatedCompositeFieldContainer[DeviceMetadata.CircuitBoard]
    def __init__(self, circuit_boards: _Optional[_Iterable[_Union[DeviceMetadata.CircuitBoard, _Mapping]]] = ...) -> None: ...
