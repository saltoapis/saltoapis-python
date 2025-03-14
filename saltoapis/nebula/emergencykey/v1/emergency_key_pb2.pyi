from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmergencyKey(_message.Message):
    __slots__ = ("name", "display_name", "uid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    uid: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., uid: _Optional[str] = ...) -> None: ...

class CreateEmergencyKeyRequest(_message.Message):
    __slots__ = ("parent", "emergency_key")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    emergency_key: EmergencyKey
    def __init__(self, parent: _Optional[str] = ..., emergency_key: _Optional[_Union[EmergencyKey, _Mapping]] = ...) -> None: ...

class GetEmergencyKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListEmergencyKeysRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListEmergencyKeysResponse(_message.Message):
    __slots__ = ("emergency_keys", "next_page_token")
    EMERGENCY_KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    emergency_keys: _containers.RepeatedCompositeFieldContainer[EmergencyKey]
    next_page_token: str
    def __init__(self, emergency_keys: _Optional[_Iterable[_Union[EmergencyKey, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateEmergencyKeyRequest(_message.Message):
    __slots__ = ("emergency_key", "update_mask")
    EMERGENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    emergency_key: EmergencyKey
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, emergency_key: _Optional[_Union[EmergencyKey, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteEmergencyKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
