from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from saltoapis.nebula.type import schedule_pb2 as _schedule_pb2
from saltoapis.nebula.type import schedule_pb2 as _schedule_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessRight(_message.Message):
    __slots__ = ("name", "display_name", "activate_time", "expire_time", "schedules")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    activate_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    schedules: _containers.RepeatedCompositeFieldContainer[_schedule_pb2.Schedule]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., activate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., schedules: _Optional[_Iterable[_Union[_schedule_pb2.Schedule, _Mapping]]] = ...) -> None: ...

class AccessRightAccessPoint(_message.Message):
    __slots__ = ("name", "access_point", "display_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    access_point: str
    display_name: str
    def __init__(self, name: _Optional[str] = ..., access_point: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class AccessRightAccessPointGroup(_message.Message):
    __slots__ = ("name", "access_point_group", "display_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    access_point_group: str
    display_name: str
    def __init__(self, name: _Optional[str] = ..., access_point_group: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class CreateAccessRightRequest(_message.Message):
    __slots__ = ("parent", "access_right_id", "access_right")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    access_right_id: str
    access_right: AccessRight
    def __init__(self, parent: _Optional[str] = ..., access_right_id: _Optional[str] = ..., access_right: _Optional[_Union[AccessRight, _Mapping]] = ...) -> None: ...

class GetAccessRightRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAccessRightsRequest(_message.Message):
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

class ListAccessRightsResponse(_message.Message):
    __slots__ = ("access_rights", "next_page_token")
    ACCESS_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_rights: _containers.RepeatedCompositeFieldContainer[AccessRight]
    next_page_token: str
    def __init__(self, access_rights: _Optional[_Iterable[_Union[AccessRight, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateAccessRightRequest(_message.Message):
    __slots__ = ("access_right", "update_mask")
    ACCESS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    access_right: AccessRight
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, access_right: _Optional[_Union[AccessRight, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAccessRightRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateAccessRightAccessPointRequest(_message.Message):
    __slots__ = ("parent", "access_right_access_point")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHT_ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    access_right_access_point: AccessRightAccessPoint
    def __init__(self, parent: _Optional[str] = ..., access_right_access_point: _Optional[_Union[AccessRightAccessPoint, _Mapping]] = ...) -> None: ...

class BatchCreateAccessRightAccessPointsRequest(_message.Message):
    __slots__ = ("parent", "requests")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateAccessRightAccessPointRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[CreateAccessRightAccessPointRequest, _Mapping]]] = ...) -> None: ...

class BatchCreateAccessRightAccessPointsResponse(_message.Message):
    __slots__ = ("access_right_access_points",)
    ACCESS_RIGHT_ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    access_right_access_points: _containers.RepeatedCompositeFieldContainer[AccessRightAccessPoint]
    def __init__(self, access_right_access_points: _Optional[_Iterable[_Union[AccessRightAccessPoint, _Mapping]]] = ...) -> None: ...

class GetAccessRightAccessPointRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAccessRightAccessPointsRequest(_message.Message):
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

class ListAccessRightAccessPointsResponse(_message.Message):
    __slots__ = ("access_right_access_points", "next_page_token")
    ACCESS_RIGHT_ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_right_access_points: _containers.RepeatedCompositeFieldContainer[AccessRightAccessPoint]
    next_page_token: str
    def __init__(self, access_right_access_points: _Optional[_Iterable[_Union[AccessRightAccessPoint, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateAccessRightAccessPointRequest(_message.Message):
    __slots__ = ("access_right_access_point", "update_mask")
    ACCESS_RIGHT_ACCESS_POINT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    access_right_access_point: AccessRightAccessPoint
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, access_right_access_point: _Optional[_Union[AccessRightAccessPoint, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAccessRightAccessPointRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateAccessRightAccessPointGroupRequest(_message.Message):
    __slots__ = ("parent", "access_right_access_point_group")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHT_ACCESS_POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    access_right_access_point_group: AccessRightAccessPointGroup
    def __init__(self, parent: _Optional[str] = ..., access_right_access_point_group: _Optional[_Union[AccessRightAccessPointGroup, _Mapping]] = ...) -> None: ...

class BatchCreateAccessRightAccessPointGroupsRequest(_message.Message):
    __slots__ = ("parent", "requests")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateAccessRightAccessPointGroupRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[CreateAccessRightAccessPointGroupRequest, _Mapping]]] = ...) -> None: ...

class BatchCreateAccessRightAccessPointGroupsResponse(_message.Message):
    __slots__ = ("access_right_access_point_groups",)
    ACCESS_RIGHT_ACCESS_POINT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    access_right_access_point_groups: _containers.RepeatedCompositeFieldContainer[AccessRightAccessPointGroup]
    def __init__(self, access_right_access_point_groups: _Optional[_Iterable[_Union[AccessRightAccessPointGroup, _Mapping]]] = ...) -> None: ...

class GetAccessRightAccessPointGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAccessRightAccessPointGroupsRequest(_message.Message):
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

class ListAccessRightAccessPointGroupsResponse(_message.Message):
    __slots__ = ("access_right_access_point_groups", "next_page_token")
    ACCESS_RIGHT_ACCESS_POINT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_right_access_point_groups: _containers.RepeatedCompositeFieldContainer[AccessRightAccessPointGroup]
    next_page_token: str
    def __init__(self, access_right_access_point_groups: _Optional[_Iterable[_Union[AccessRightAccessPointGroup, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateAccessRightAccessPointGroupRequest(_message.Message):
    __slots__ = ("access_right_access_point_group", "update_mask")
    ACCESS_RIGHT_ACCESS_POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    access_right_access_point_group: AccessRightAccessPointGroup
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, access_right_access_point_group: _Optional[_Union[AccessRightAccessPointGroup, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAccessRightAccessPointGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BatchDeleteAccessRightAccessPointGroupsRequest(_message.Message):
    __slots__ = ("parent", "requests")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[DeleteAccessRightAccessPointGroupRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[DeleteAccessRightAccessPointGroupRequest, _Mapping]]] = ...) -> None: ...

class BatchDeleteAccessRightAccessPointGroupsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatchDeleteAccessRightAccessPointsRequest(_message.Message):
    __slots__ = ("parent", "requests")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[DeleteAccessRightAccessPointRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[DeleteAccessRightAccessPointRequest, _Mapping]]] = ...) -> None: ...

class BatchDeleteAccessRightAccessPointsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
