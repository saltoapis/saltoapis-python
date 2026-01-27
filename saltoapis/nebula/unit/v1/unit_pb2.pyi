import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Unit(_message.Message):
    __slots__ = ()
    class PrivacySettings(_message.Message):
        __slots__ = ()
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: _Optional[bool] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MOVE_IN_TIME_FIELD_NUMBER: _ClassVar[int]
    MOVE_OUT_TIME_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    move_in_time: _timestamp_pb2.Timestamp
    move_out_time: _timestamp_pb2.Timestamp
    privacy_settings: Unit.PrivacySettings
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., move_in_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., move_out_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., privacy_settings: _Optional[_Union[Unit.PrivacySettings, _Mapping]] = ...) -> None: ...

class Policy(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    member: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., member: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateUnitRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UNIT_ID_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    unit_id: str
    unit: Unit
    def __init__(self, parent: _Optional[str] = ..., unit_id: _Optional[str] = ..., unit: _Optional[_Union[Unit, _Mapping]] = ...) -> None: ...

class GetUnitRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListUnitsRequest(_message.Message):
    __slots__ = ()
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

class ListUnitsResponse(_message.Message):
    __slots__ = ()
    UNITS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedCompositeFieldContainer[Unit]
    next_page_token: str
    def __init__(self, units: _Optional[_Iterable[_Union[Unit, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateUnitRequest(_message.Message):
    __slots__ = ()
    UNIT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    unit: Unit
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, unit: _Optional[_Union[Unit, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteUnitRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CleanOutUnitRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CleanOutUnitResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MoveInUnitRequest(_message.Message):
    __slots__ = ()
    class Occupant(_message.Message):
        __slots__ = ()
        GIVEN_NAME_FIELD_NUMBER: _ClassVar[int]
        FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        ACCESS_RIGHTS_FIELD_NUMBER: _ClassVar[int]
        IAM_ROLES_FIELD_NUMBER: _ClassVar[int]
        given_name: str
        family_name: str
        email: str
        access_rights: _containers.RepeatedScalarFieldContainer[str]
        iam_roles: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, given_name: _Optional[str] = ..., family_name: _Optional[str] = ..., email: _Optional[str] = ..., access_rights: _Optional[_Iterable[str]] = ..., iam_roles: _Optional[_Iterable[str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    OCCUPANTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    occupants: _containers.RepeatedCompositeFieldContainer[MoveInUnitRequest.Occupant]
    def __init__(self, name: _Optional[str] = ..., occupants: _Optional[_Iterable[_Union[MoveInUnitRequest.Occupant, _Mapping]]] = ...) -> None: ...

class MoveInUnitResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MoveOutUnitRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class MoveOutUnitResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreatePolicyRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    policy_id: str
    policy: Policy
    def __init__(self, parent: _Optional[str] = ..., policy_id: _Optional[str] = ..., policy: _Optional[_Union[Policy, _Mapping]] = ...) -> None: ...

class GetPolicyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListPoliciesRequest(_message.Message):
    __slots__ = ()
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

class ListPoliciesResponse(_message.Message):
    __slots__ = ()
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[Policy]
    next_page_token: str
    def __init__(self, policies: _Optional[_Iterable[_Union[Policy, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdatePolicyRequest(_message.Message):
    __slots__ = ()
    POLICY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    policy: Policy
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, policy: _Optional[_Union[Policy, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeletePolicyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class TestPermissionsRequest(_message.Message):
    __slots__ = ()
    UNIT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    unit: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, unit: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class TestPermissionsResponse(_message.Message):
    __slots__ = ()
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permissions: _Optional[_Iterable[str]] = ...) -> None: ...
