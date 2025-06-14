# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: salto/nebula/destination/v1/destination.proto
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
    'salto/nebula/destination/v1/destination.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-salto/nebula/destination/v1/destination.proto\x12\x1bsalto.nebula.destination.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"1\n\x0b\x44\x65stination\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\"\x99\x01\n\x18\x43reateDestinationRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x1b\n\x0e\x64\x65stination_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12=\n\x0b\x64\x65stination\x18\x03 \x01(\x0b\x32(.salto.nebula.destination.v1.DestinationB\x11\n\x0f_destination_id\"%\n\x15GetDestinationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x8a\x01\n\x18UpdateDestinationRequest\x12=\n\x0b\x64\x65stination\x18\x01 \x01(\x0b\x32(.salto.nebula.destination.v1.Destination\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"r\n\x17ListDestinationsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"s\n\x18ListDestinationsResponse\x12>\n\x0c\x64\x65stinations\x18\x01 \x03(\x0b\x32(.salto.nebula.destination.v1.Destination\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"(\n\x18\x44\x65leteDestinationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xd5\x04\n\x12\x44\x65stinationService\x12t\n\x11\x43reateDestination\x12\x35.salto.nebula.destination.v1.CreateDestinationRequest\x1a(.salto.nebula.destination.v1.Destination\x12n\n\x0eGetDestination\x12\x32.salto.nebula.destination.v1.GetDestinationRequest\x1a(.salto.nebula.destination.v1.Destination\x12t\n\x11UpdateDestination\x12\x35.salto.nebula.destination.v1.UpdateDestinationRequest\x1a(.salto.nebula.destination.v1.Destination\x12\x7f\n\x10ListDestinations\x12\x34.salto.nebula.destination.v1.ListDestinationsRequest\x1a\x35.salto.nebula.destination.v1.ListDestinationsResponse\x12\x62\n\x11\x44\x65leteDestination\x12\x35.salto.nebula.destination.v1.DeleteDestinationRequest\x1a\x16.google.protobuf.EmptyB\xf9\x01\n#com.saltoapis.nebula.destination.v1B\x10\x44\x65stinationProtoP\x01ZLgithub.com/saltoapis-internal/saltoapis-go/nebula/destination/v1;destination\xaa\x02\x1fSaltoapis.Nebula.Destination.V1\xca\x02\x1fSaltoapis\\Nebula\\Destination\\V1\xe2\x02+GPBMetadata\\Saltoapis\\Nebula\\Destination\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'salto.nebula.destination.v1.destination_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#com.saltoapis.nebula.destination.v1B\020DestinationProtoP\001ZLgithub.com/saltoapis-internal/saltoapis-go/nebula/destination/v1;destination\252\002\037Saltoapis.Nebula.Destination.V1\312\002\037Saltoapis\\Nebula\\Destination\\V1\342\002+GPBMetadata\\Saltoapis\\Nebula\\Destination\\V1'
  _globals['_DESTINATION']._serialized_start=141
  _globals['_DESTINATION']._serialized_end=190
  _globals['_CREATEDESTINATIONREQUEST']._serialized_start=193
  _globals['_CREATEDESTINATIONREQUEST']._serialized_end=346
  _globals['_GETDESTINATIONREQUEST']._serialized_start=348
  _globals['_GETDESTINATIONREQUEST']._serialized_end=385
  _globals['_UPDATEDESTINATIONREQUEST']._serialized_start=388
  _globals['_UPDATEDESTINATIONREQUEST']._serialized_end=526
  _globals['_LISTDESTINATIONSREQUEST']._serialized_start=528
  _globals['_LISTDESTINATIONSREQUEST']._serialized_end=642
  _globals['_LISTDESTINATIONSRESPONSE']._serialized_start=644
  _globals['_LISTDESTINATIONSRESPONSE']._serialized_end=759
  _globals['_DELETEDESTINATIONREQUEST']._serialized_start=761
  _globals['_DELETEDESTINATIONREQUEST']._serialized_end=801
  _globals['_DESTINATIONSERVICE']._serialized_start=804
  _globals['_DESTINATIONSERVICE']._serialized_end=1401
# @@protoc_insertion_point(module_scope)
