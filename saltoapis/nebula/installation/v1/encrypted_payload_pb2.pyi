from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IngestEncryptedPayloadsRequest(_message.Message):
    __slots__ = ("installation", "encrypted_payloads")
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    installation: str
    encrypted_payloads: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, installation: _Optional[str] = ..., encrypted_payloads: _Optional[_Iterable[bytes]] = ...) -> None: ...

class IngestEncryptedPayloadsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
