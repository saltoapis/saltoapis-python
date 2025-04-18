# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: salto/nebula/openingmodeschedule/v1/opening_mode_schedule.proto
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
    'salto/nebula/openingmodeschedule/v1/opening_mode_schedule.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from saltoapis.nebula.type import day_type_pb2 as salto_dot_nebula_dot_type_dot_day__type__pb2
from saltoapis.nebula.type import day_type_pb2 as salto_dot_nebula_dot_type_dot_day__type__pb2
from saltoapis.nebula.type import opening_mode_pb2 as salto_dot_nebula_dot_type_dot_opening__mode__pb2
from saltoapis.nebula.type import opening_mode_pb2 as salto_dot_nebula_dot_type_dot_opening__mode__pb2
from saltoapis.type import day_of_week_pb2 as salto_dot_type_dot_day__of__week__pb2
from saltoapis.type import day_of_week_pb2 as salto_dot_type_dot_day__of__week__pb2
from saltoapis.type import time_of_day_pb2 as salto_dot_type_dot_time__of__day__pb2
from saltoapis.type import time_of_day_pb2 as salto_dot_type_dot_time__of__day__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?salto/nebula/openingmodeschedule/v1/opening_mode_schedule.proto\x12#salto.nebula.openingmodeschedule.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a salto/nebula/type/day_type.proto\x1a$salto/nebula/type/opening_mode.proto\x1a\x1csalto/type/day_of_week.proto\x1a\x1csalto/type/time_of_day.proto\"\xcc\x03\n\x13OpeningModeSchedule\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12J\n\x04\x64\x61ys\x18\x03 \x03(\x0b\x32<.salto.nebula.openingmodeschedule.v1.OpeningModeSchedule.Day\x1a\xc4\x02\n\x03\x44\x61y\x12,\n\x08\x64\x61y_type\x18\x01 \x01(\x0e\x32\x1a.salto.nebula.type.DayType\x12*\n\x0b\x64\x61y_of_week\x18\x02 \x01(\x0e\x32\x15.salto.type.DayOfWeek\x12P\n\x05slots\x18\x03 \x03(\x0b\x32\x41.salto.nebula.openingmodeschedule.v1.OpeningModeSchedule.Day.Slot\x1a\x90\x01\n\x04Slot\x12\x34\n\x0copening_mode\x18\x01 \x01(\x0e\x32\x1e.salto.nebula.type.OpeningMode\x12)\n\nstart_time\x18\x02 \x01(\x0b\x32\x15.salto.type.TimeOfDay\x12\'\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x15.salto.type.TimeOfDay\"\xad\x01\n CreateOpeningModeScheduleRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12 \n\x18opening_mode_schedule_id\x18\x02 \x01(\t\x12W\n\x15opening_mode_schedule\x18\x03 \x01(\x0b\x32\x38.salto.nebula.openingmodeschedule.v1.OpeningModeSchedule\"-\n\x1dGetOpeningModeScheduleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"z\n\x1fListOpeningModeSchedulesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"\x95\x01\n ListOpeningModeSchedulesResponse\x12X\n\x16opening_mode_schedules\x18\x01 \x03(\x0b\x32\x38.salto.nebula.openingmodeschedule.v1.OpeningModeSchedule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xac\x01\n UpdateOpeningModeScheduleRequest\x12W\n\x15opening_mode_schedule\x18\x01 \x01(\x0b\x32\x38.salto.nebula.openingmodeschedule.v1.OpeningModeSchedule\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"0\n DeleteOpeningModeScheduleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\x99\x06\n\x1aOpeningModeScheduleService\x12\x9c\x01\n\x19\x43reateOpeningModeSchedule\x12\x45.salto.nebula.openingmodeschedule.v1.CreateOpeningModeScheduleRequest\x1a\x38.salto.nebula.openingmodeschedule.v1.OpeningModeSchedule\x12\x96\x01\n\x16GetOpeningModeSchedule\x12\x42.salto.nebula.openingmodeschedule.v1.GetOpeningModeScheduleRequest\x1a\x38.salto.nebula.openingmodeschedule.v1.OpeningModeSchedule\x12\xa7\x01\n\x18ListOpeningModeSchedules\x12\x44.salto.nebula.openingmodeschedule.v1.ListOpeningModeSchedulesRequest\x1a\x45.salto.nebula.openingmodeschedule.v1.ListOpeningModeSchedulesResponse\x12\x9c\x01\n\x19UpdateOpeningModeSchedule\x12\x45.salto.nebula.openingmodeschedule.v1.UpdateOpeningModeScheduleRequest\x1a\x38.salto.nebula.openingmodeschedule.v1.OpeningModeSchedule\x12z\n\x19\x44\x65leteOpeningModeSchedule\x12\x45.salto.nebula.openingmodeschedule.v1.DeleteOpeningModeScheduleRequest\x1a\x16.google.protobuf.EmptyB\xb1\x02\n+com.saltoapis.nebula.openingmodeschedule.v1B\x18OpeningModeScheduleProtoP\x01Z\\github.com/saltoapis-internal/saltoapis-go/nebula/openingmodeschedule/v1;openingmodeschedule\xaa\x02\'Saltoapis.Nebula.OpeningModeSchedule.V1\xca\x02\'Saltoapis\\Nebula\\OpeningModeSchedule\\V1\xe2\x02\x33GPBMetadata\\Saltoapis\\Nebula\\OpeningModeSchedule\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'salto.nebula.openingmodeschedule.v1.opening_mode_schedule_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n+com.saltoapis.nebula.openingmodeschedule.v1B\030OpeningModeScheduleProtoP\001Z\\github.com/saltoapis-internal/saltoapis-go/nebula/openingmodeschedule/v1;openingmodeschedule\252\002\'Saltoapis.Nebula.OpeningModeSchedule.V1\312\002\'Saltoapis\\Nebula\\OpeningModeSchedule\\V1\342\0023GPBMetadata\\Saltoapis\\Nebula\\OpeningModeSchedule\\V1'
  _globals['_OPENINGMODESCHEDULE']._serialized_start=300
  _globals['_OPENINGMODESCHEDULE']._serialized_end=760
  _globals['_OPENINGMODESCHEDULE_DAY']._serialized_start=436
  _globals['_OPENINGMODESCHEDULE_DAY']._serialized_end=760
  _globals['_OPENINGMODESCHEDULE_DAY_SLOT']._serialized_start=616
  _globals['_OPENINGMODESCHEDULE_DAY_SLOT']._serialized_end=760
  _globals['_CREATEOPENINGMODESCHEDULEREQUEST']._serialized_start=763
  _globals['_CREATEOPENINGMODESCHEDULEREQUEST']._serialized_end=936
  _globals['_GETOPENINGMODESCHEDULEREQUEST']._serialized_start=938
  _globals['_GETOPENINGMODESCHEDULEREQUEST']._serialized_end=983
  _globals['_LISTOPENINGMODESCHEDULESREQUEST']._serialized_start=985
  _globals['_LISTOPENINGMODESCHEDULESREQUEST']._serialized_end=1107
  _globals['_LISTOPENINGMODESCHEDULESRESPONSE']._serialized_start=1110
  _globals['_LISTOPENINGMODESCHEDULESRESPONSE']._serialized_end=1259
  _globals['_UPDATEOPENINGMODESCHEDULEREQUEST']._serialized_start=1262
  _globals['_UPDATEOPENINGMODESCHEDULEREQUEST']._serialized_end=1434
  _globals['_DELETEOPENINGMODESCHEDULEREQUEST']._serialized_start=1436
  _globals['_DELETEOPENINGMODESCHEDULEREQUEST']._serialized_end=1484
  _globals['_OPENINGMODESCHEDULESERVICE']._serialized_start=1487
  _globals['_OPENINGMODESCHEDULESERVICE']._serialized_end=2280
# @@protoc_insertion_point(module_scope)
