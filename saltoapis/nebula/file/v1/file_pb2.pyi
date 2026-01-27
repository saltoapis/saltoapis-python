from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_URI_FIELD_NUMBER: _ClassVar[int]
    name: str
    upload_uri: str
    def __init__(self, name: _Optional[str] = ..., upload_uri: _Optional[str] = ...) -> None: ...

class CreateFileRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...
