# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: salto/nebula/accesspoint/v1/access_point.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.nebula.type import opening_mode_pb2 as salto_dot_nebula_dot_type_dot_opening__mode__pb2
from saltoapis.nebula.type import opening_mode_pb2 as salto_dot_nebula_dot_type_dot_opening__mode__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.salto/nebula/accesspoint/v1/access_point.proto\x12\x1bsalto.nebula.accesspoint.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a$salto/longrunning/v1/operation.proto\x1a$salto/nebula/type/opening_mode.proto\"\xab\x02\n\x0b\x41\x63\x63\x65ssPoint\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12/\n\x05\x66ixed\x18\x03 \x01(\x0e\x32\x1e.salto.nebula.type.OpeningModeH\x00\x12\x12\n\x08schedule\x18\x04 \x01(\tH\x00\x12\x15\n\x08\x63\x61lendar\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x1d\n\x10\x63\x61rd_key_updater\x18\x06 \x01(\x08H\x02\x88\x01\x01\x12\x37\n\x0funlock_duration\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationH\x03\x88\x01\x01\x42\x0e\n\x0copening_modeB\x0b\n\t_calendarB\x13\n\x11_card_key_updaterB\x12\n\x10_unlock_duration\"\x9c\x01\n\x18\x43reateAccessPointRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x1c\n\x0f\x61\x63\x63\x65ss_point_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x03 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPointB\x12\n\x10_access_point_id\"%\n\x15GetAccessPointRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"r\n\x17ListAccessPointsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"\x88\x01\n\x18ListAccessPointsResponse\x12?\n\raccess_points\x18\x01 \x03(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05\"\x8b\x01\n\x18UpdateAccessPointRequest\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x01 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"(\n\x18\x44\x65leteAccessPointRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"(\n\x18UnlockAccessPointRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1b\n\x19UnlockAccessPointResponse\"\x1b\n\x19UnlockAccessPointMetadata2\xc2\x05\n\x12\x41\x63\x63\x65ssPointService\x12t\n\x11\x43reateAccessPoint\x12\x35.salto.nebula.accesspoint.v1.CreateAccessPointRequest\x1a(.salto.nebula.accesspoint.v1.AccessPoint\x12n\n\x0eGetAccessPoint\x12\x32.salto.nebula.accesspoint.v1.GetAccessPointRequest\x1a(.salto.nebula.accesspoint.v1.AccessPoint\x12\x7f\n\x10ListAccessPoints\x12\x34.salto.nebula.accesspoint.v1.ListAccessPointsRequest\x1a\x35.salto.nebula.accesspoint.v1.ListAccessPointsResponse\x12t\n\x11UpdateAccessPoint\x12\x35.salto.nebula.accesspoint.v1.UpdateAccessPointRequest\x1a(.salto.nebula.accesspoint.v1.AccessPoint\x12\x62\n\x11\x44\x65leteAccessPoint\x12\x35.salto.nebula.accesspoint.v1.DeleteAccessPointRequest\x1a\x16.google.protobuf.Empty\x12k\n\x11UnlockAccessPoint\x12\x35.salto.nebula.accesspoint.v1.UnlockAccessPointRequest\x1a\x1f.salto.longrunning.v1.OperationB\xf9\x01\n#com.saltoapis.nebula.accesspoint.v1B\x10\x41\x63\x63\x65ssPointProtoP\x01ZLgithub.com/saltoapis-internal/saltoapis-go/nebula/accesspoint/v1;accesspoint\xaa\x02\x1fSaltoapis.Nebula.AccessPoint.V1\xca\x02\x1fSaltoapis\\Nebula\\AccessPoint\\V1\xe2\x02+GPBMetadata\\Saltoapis\\Nebula\\AccessPoint\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'salto.nebula.accesspoint.v1.access_point_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#com.saltoapis.nebula.accesspoint.v1B\020AccessPointProtoP\001ZLgithub.com/saltoapis-internal/saltoapis-go/nebula/accesspoint/v1;accesspoint\252\002\037Saltoapis.Nebula.AccessPoint.V1\312\002\037Saltoapis\\Nebula\\AccessPoint\\V1\342\002+GPBMetadata\\Saltoapis\\Nebula\\AccessPoint\\V1'
  _globals['_ACCESSPOINT']._serialized_start=251
  _globals['_ACCESSPOINT']._serialized_end=550
  _globals['_CREATEACCESSPOINTREQUEST']._serialized_start=553
  _globals['_CREATEACCESSPOINTREQUEST']._serialized_end=709
  _globals['_GETACCESSPOINTREQUEST']._serialized_start=711
  _globals['_GETACCESSPOINTREQUEST']._serialized_end=748
  _globals['_LISTACCESSPOINTSREQUEST']._serialized_start=750
  _globals['_LISTACCESSPOINTSREQUEST']._serialized_end=864
  _globals['_LISTACCESSPOINTSRESPONSE']._serialized_start=867
  _globals['_LISTACCESSPOINTSRESPONSE']._serialized_end=1003
  _globals['_UPDATEACCESSPOINTREQUEST']._serialized_start=1006
  _globals['_UPDATEACCESSPOINTREQUEST']._serialized_end=1145
  _globals['_DELETEACCESSPOINTREQUEST']._serialized_start=1147
  _globals['_DELETEACCESSPOINTREQUEST']._serialized_end=1187
  _globals['_UNLOCKACCESSPOINTREQUEST']._serialized_start=1189
  _globals['_UNLOCKACCESSPOINTREQUEST']._serialized_end=1229
  _globals['_UNLOCKACCESSPOINTRESPONSE']._serialized_start=1231
  _globals['_UNLOCKACCESSPOINTRESPONSE']._serialized_end=1258
  _globals['_UNLOCKACCESSPOINTMETADATA']._serialized_start=1260
  _globals['_UNLOCKACCESSPOINTMETADATA']._serialized_end=1287
  _globals['_ACCESSPOINTSERVICE']._serialized_start=1290
  _globals['_ACCESSPOINTSERVICE']._serialized_end=1996
# @@protoc_insertion_point(module_scope)
