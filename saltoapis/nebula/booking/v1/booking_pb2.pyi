import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Booking(_message.Message):
    __slots__ = ("name", "start_time", "end_time", "state", "check_in_time", "check_out_time", "unit", "access_rights")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Booking.State]
        SCHEDULED: _ClassVar[Booking.State]
        CHECKED_IN: _ClassVar[Booking.State]
        CHECKED_OUT: _ClassVar[Booking.State]
    STATE_UNSPECIFIED: Booking.State
    SCHEDULED: Booking.State
    CHECKED_IN: Booking.State
    CHECKED_OUT: Booking.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CHECK_IN_TIME_FIELD_NUMBER: _ClassVar[int]
    CHECK_OUT_TIME_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: Booking.State
    check_in_time: _timestamp_pb2.Timestamp
    check_out_time: _timestamp_pb2.Timestamp
    unit: str
    access_rights: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[Booking.State, str]] = ..., check_in_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., check_out_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., unit: _Optional[str] = ..., access_rights: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateBookingRequest(_message.Message):
    __slots__ = ("parent", "booking_id", "booking")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    BOOKING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    booking_id: str
    booking: Booking
    def __init__(self, parent: _Optional[str] = ..., booking_id: _Optional[str] = ..., booking: _Optional[_Union[Booking, _Mapping]] = ...) -> None: ...

class GetBookingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListBookingsRequest(_message.Message):
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

class ListBookingsResponse(_message.Message):
    __slots__ = ("bookings", "next_page_token")
    BOOKINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    bookings: _containers.RepeatedCompositeFieldContainer[Booking]
    next_page_token: str
    def __init__(self, bookings: _Optional[_Iterable[_Union[Booking, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateBookingRequest(_message.Message):
    __slots__ = ("booking", "update_mask")
    BOOKING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    booking: Booking
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, booking: _Optional[_Union[Booking, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteBookingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CheckInBookingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CheckOutBookingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BookingUser(_message.Message):
    __slots__ = ("name", "user")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    name: str
    user: str
    def __init__(self, name: _Optional[str] = ..., user: _Optional[str] = ...) -> None: ...

class CreateBookingUserRequest(_message.Message):
    __slots__ = ("parent", "booking_user")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BOOKING_USER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    booking_user: BookingUser
    def __init__(self, parent: _Optional[str] = ..., booking_user: _Optional[_Union[BookingUser, _Mapping]] = ...) -> None: ...

class BatchCreateBookingUsersRequest(_message.Message):
    __slots__ = ("parent", "requests")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateBookingUserRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[CreateBookingUserRequest, _Mapping]]] = ...) -> None: ...

class BatchCreateBookingUsersResponse(_message.Message):
    __slots__ = ("booking_users",)
    BOOKING_USERS_FIELD_NUMBER: _ClassVar[int]
    booking_users: _containers.RepeatedCompositeFieldContainer[BookingUser]
    def __init__(self, booking_users: _Optional[_Iterable[_Union[BookingUser, _Mapping]]] = ...) -> None: ...

class GetBookingUserRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListBookingUsersRequest(_message.Message):
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

class ListBookingUsersResponse(_message.Message):
    __slots__ = ("booking_users", "next_page_token")
    BOOKING_USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    booking_users: _containers.RepeatedCompositeFieldContainer[BookingUser]
    next_page_token: str
    def __init__(self, booking_users: _Optional[_Iterable[_Union[BookingUser, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteBookingUserRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
