from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from saltoapis.nebula.type import day_type_pb2 as _day_type_pb2
from saltoapis.nebula.type import day_type_pb2 as _day_type_pb2
from saltoapis.type import date_pb2 as _date_pb2
from saltoapis.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Calendar(_message.Message):
    __slots__ = ("name", "display_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("name", "day_type", "start_date", "end_date")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    day_type: _day_type_pb2.DayType
    start_date: _date_pb2.Date
    end_date: _date_pb2.Date
    def __init__(self, name: _Optional[str] = ..., day_type: _Optional[_Union[_day_type_pb2.DayType, str]] = ..., start_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...

class CreateCalendarRequest(_message.Message):
    __slots__ = ("parent", "calendar_id", "calendar")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_ID_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_FIELD_NUMBER: _ClassVar[int]
    parent: str
    calendar_id: str
    calendar: Calendar
    def __init__(self, parent: _Optional[str] = ..., calendar_id: _Optional[str] = ..., calendar: _Optional[_Union[Calendar, _Mapping]] = ...) -> None: ...

class GetCalendarRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListCalendarsRequest(_message.Message):
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

class ListCalendarsResponse(_message.Message):
    __slots__ = ("calendars", "next_page_token")
    CALENDARS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    calendars: _containers.RepeatedCompositeFieldContainer[Calendar]
    next_page_token: str
    def __init__(self, calendars: _Optional[_Iterable[_Union[Calendar, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateCalendarRequest(_message.Message):
    __slots__ = ("calendar", "update_mask")
    CALENDAR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    calendar: Calendar
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, calendar: _Optional[_Union[Calendar, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteCalendarRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateEventRequest(_message.Message):
    __slots__ = ("parent", "event_id", "event")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    event_id: str
    event: Event
    def __init__(self, parent: _Optional[str] = ..., event_id: _Optional[str] = ..., event: _Optional[_Union[Event, _Mapping]] = ...) -> None: ...

class GetEventRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListEventsRequest(_message.Message):
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

class ListEventsResponse(_message.Message):
    __slots__ = ("events", "next_page_token")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    next_page_token: str
    def __init__(self, events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateEventRequest(_message.Message):
    __slots__ = ("event", "update_mask")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    event: Event
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, event: _Optional[_Union[Event, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteEventRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
