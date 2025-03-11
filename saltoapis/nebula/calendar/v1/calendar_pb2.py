# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: salto/nebula/calendar/v1/calendar.proto
# Protobuf Python Version: 5.29.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    2,
    '',
    'salto/nebula/calendar/v1/calendar.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from saltoapis.nebula.type import day_type_pb2 as salto_dot_nebula_dot_type_dot_day__type__pb2
from saltoapis.nebula.type import day_type_pb2 as salto_dot_nebula_dot_type_dot_day__type__pb2
from saltoapis.type import date_pb2 as salto_dot_type_dot_date__pb2
from saltoapis.type import date_pb2 as salto_dot_type_dot_date__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'salto/nebula/calendar/v1/calendar.proto\x12\x18salto.nebula.calendar.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a salto/nebula/type/day_type.proto\x1a\x15salto/type/date.proto\".\n\x08\x43\x61lendar\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\"\x8d\x01\n\x05\x45vent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x08\x64\x61y_type\x18\x02 \x01(\x0e\x32\x1a.salto.nebula.type.DayType\x12$\n\nstart_date\x18\x03 \x01(\x0b\x32\x10.salto.type.Date\x12\"\n\x08\x65nd_date\x18\x04 \x01(\x0b\x32\x10.salto.type.Date\"\x87\x01\n\x15\x43reateCalendarRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x18\n\x0b\x63\x61lendar_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x34\n\x08\x63\x61lendar\x18\x03 \x01(\x0b\x32\".salto.nebula.calendar.v1.CalendarB\x0e\n\x0c_calendar_id\"\"\n\x12GetCalendarRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"o\n\x14ListCalendarsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"g\n\x15ListCalendarsResponse\x12\x35\n\tcalendars\x18\x01 \x03(\x0b\x32\".salto.nebula.calendar.v1.Calendar\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"~\n\x15UpdateCalendarRequest\x12\x34\n\x08\x63\x61lendar\x18\x01 \x01(\x0b\x32\".salto.nebula.calendar.v1.Calendar\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"%\n\x15\x44\x65leteCalendarRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"x\n\x12\x43reateEventRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x15\n\x08\x65vent_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12.\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x1f.salto.nebula.calendar.v1.EventB\x0b\n\t_event_id\"\x1f\n\x0fGetEventRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"l\n\x11ListEventsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"^\n\x12ListEventsResponse\x12/\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x1f.salto.nebula.calendar.v1.Event\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"u\n\x12UpdateEventRequest\x12.\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1f.salto.nebula.calendar.v1.Event\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\"\n\x12\x44\x65leteEventRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xdf\x07\n\x0f\x43\x61lendarService\x12\x65\n\x0e\x43reateCalendar\x12/.salto.nebula.calendar.v1.CreateCalendarRequest\x1a\".salto.nebula.calendar.v1.Calendar\x12_\n\x0bGetCalendar\x12,.salto.nebula.calendar.v1.GetCalendarRequest\x1a\".salto.nebula.calendar.v1.Calendar\x12p\n\rListCalendars\x12..salto.nebula.calendar.v1.ListCalendarsRequest\x1a/.salto.nebula.calendar.v1.ListCalendarsResponse\x12\x65\n\x0eUpdateCalendar\x12/.salto.nebula.calendar.v1.UpdateCalendarRequest\x1a\".salto.nebula.calendar.v1.Calendar\x12Y\n\x0e\x44\x65leteCalendar\x12/.salto.nebula.calendar.v1.DeleteCalendarRequest\x1a\x16.google.protobuf.Empty\x12\\\n\x0b\x43reateEvent\x12,.salto.nebula.calendar.v1.CreateEventRequest\x1a\x1f.salto.nebula.calendar.v1.Event\x12V\n\x08GetEvent\x12).salto.nebula.calendar.v1.GetEventRequest\x1a\x1f.salto.nebula.calendar.v1.Event\x12g\n\nListEvents\x12+.salto.nebula.calendar.v1.ListEventsRequest\x1a,.salto.nebula.calendar.v1.ListEventsResponse\x12\\\n\x0bUpdateEvent\x12,.salto.nebula.calendar.v1.UpdateEventRequest\x1a\x1f.salto.nebula.calendar.v1.Event\x12S\n\x0b\x44\x65leteEvent\x12,.salto.nebula.calendar.v1.DeleteEventRequest\x1a\x16.google.protobuf.EmptyB\xe4\x01\n com.saltoapis.nebula.calendar.v1B\rCalendarProtoP\x01ZFgithub.com/saltoapis-internal/saltoapis-go/nebula/calendar/v1;calendar\xaa\x02\x1cSaltoapis.Nebula.Calendar.V1\xca\x02\x1cSaltoapis\\Nebula\\Calendar\\V1\xe2\x02(GPBMetadata\\Saltoapis\\Nebula\\Calendar\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'salto.nebula.calendar.v1.calendar_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.saltoapis.nebula.calendar.v1B\rCalendarProtoP\001ZFgithub.com/saltoapis-internal/saltoapis-go/nebula/calendar/v1;calendar\252\002\034Saltoapis.Nebula.Calendar.V1\312\002\034Saltoapis\\Nebula\\Calendar\\V1\342\002(GPBMetadata\\Saltoapis\\Nebula\\Calendar\\V1'
  _globals['_CALENDAR']._serialized_start=189
  _globals['_CALENDAR']._serialized_end=235
  _globals['_EVENT']._serialized_start=238
  _globals['_EVENT']._serialized_end=379
  _globals['_CREATECALENDARREQUEST']._serialized_start=382
  _globals['_CREATECALENDARREQUEST']._serialized_end=517
  _globals['_GETCALENDARREQUEST']._serialized_start=519
  _globals['_GETCALENDARREQUEST']._serialized_end=553
  _globals['_LISTCALENDARSREQUEST']._serialized_start=555
  _globals['_LISTCALENDARSREQUEST']._serialized_end=666
  _globals['_LISTCALENDARSRESPONSE']._serialized_start=668
  _globals['_LISTCALENDARSRESPONSE']._serialized_end=771
  _globals['_UPDATECALENDARREQUEST']._serialized_start=773
  _globals['_UPDATECALENDARREQUEST']._serialized_end=899
  _globals['_DELETECALENDARREQUEST']._serialized_start=901
  _globals['_DELETECALENDARREQUEST']._serialized_end=938
  _globals['_CREATEEVENTREQUEST']._serialized_start=940
  _globals['_CREATEEVENTREQUEST']._serialized_end=1060
  _globals['_GETEVENTREQUEST']._serialized_start=1062
  _globals['_GETEVENTREQUEST']._serialized_end=1093
  _globals['_LISTEVENTSREQUEST']._serialized_start=1095
  _globals['_LISTEVENTSREQUEST']._serialized_end=1203
  _globals['_LISTEVENTSRESPONSE']._serialized_start=1205
  _globals['_LISTEVENTSRESPONSE']._serialized_end=1299
  _globals['_UPDATEEVENTREQUEST']._serialized_start=1301
  _globals['_UPDATEEVENTREQUEST']._serialized_end=1418
  _globals['_DELETEEVENTREQUEST']._serialized_start=1420
  _globals['_DELETEEVENTREQUEST']._serialized_end=1454
  _globals['_CALENDARSERVICE']._serialized_start=1457
  _globals['_CALENDARSERVICE']._serialized_end=2448
# @@protoc_insertion_point(module_scope)
