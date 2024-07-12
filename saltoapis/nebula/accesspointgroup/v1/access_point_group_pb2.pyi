from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessPointGroup(_message.Message):
    __slots__ = ("name", "display_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class AccessPointGroupAccessPoint(_message.Message):
    __slots__ = ("name", "access_point", "display_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    access_point: str
    display_name: str
    def __init__(self, name: _Optional[str] = ..., access_point: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class CreateAccessPointGroupRequest(_message.Message):
    __slots__ = ("parent", "access_point_group_id", "access_point_group")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    access_point_group_id: str
    access_point_group: AccessPointGroup
    def __init__(self, parent: _Optional[str] = ..., access_point_group_id: _Optional[str] = ..., access_point_group: _Optional[_Union[AccessPointGroup, _Mapping]] = ...) -> None: ...

class GetAccessPointGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAccessPointGroupsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "show_deleted")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    show_deleted: bool
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., show_deleted: bool = ...) -> None: ...

class ListAccessPointGroupsResponse(_message.Message):
    __slots__ = ("access_point_groups", "next_page_token")
    ACCESS_POINT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_point_groups: _containers.RepeatedCompositeFieldContainer[AccessPointGroup]
    next_page_token: str
    def __init__(self, access_point_groups: _Optional[_Iterable[_Union[AccessPointGroup, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateAccessPointGroupRequest(_message.Message):
    __slots__ = ("access_point_group", "update_mask")
    ACCESS_POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    access_point_group: AccessPointGroup
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, access_point_group: _Optional[_Union[AccessPointGroup, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAccessPointGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateAccessPointGroupAccessPointRequest(_message.Message):
    __slots__ = ("parent", "access_point_group_access_point")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_GROUP_ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    access_point_group_access_point: AccessPointGroupAccessPoint
    def __init__(self, parent: _Optional[str] = ..., access_point_group_access_point: _Optional[_Union[AccessPointGroupAccessPoint, _Mapping]] = ...) -> None: ...

class GetAccessPointGroupAccessPointRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAccessPointGroupAccessPointsRequest(_message.Message):
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

class ListAccessPointGroupAccessPointsResponse(_message.Message):
    __slots__ = ("access_point_group_access_points", "next_page_token")
    ACCESS_POINT_GROUP_ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_point_group_access_points: _containers.RepeatedCompositeFieldContainer[AccessPointGroupAccessPoint]
    next_page_token: str
    def __init__(self, access_point_group_access_points: _Optional[_Iterable[_Union[AccessPointGroupAccessPoint, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateAccessPointGroupAccessPointRequest(_message.Message):
    __slots__ = ("access_point_group_access_point", "update_mask")
    ACCESS_POINT_GROUP_ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    access_point_group_access_point: AccessPointGroupAccessPoint
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, access_point_group_access_point: _Optional[_Union[AccessPointGroupAccessPoint, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAccessPointGroupAccessPointRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
