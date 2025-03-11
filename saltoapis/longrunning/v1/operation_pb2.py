# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: salto/longrunning/v1/operation.proto
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
    'salto/longrunning/v1/operation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$salto/longrunning/v1/operation.proto\x12\x14salto.longrunning.v1\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto\"\xa8\x01\n\tOperation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x08metadata\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04\x64one\x18\x03 \x01(\x08\x12#\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x12(\n\x08response\x18\x05 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06result\"#\n\x13GetOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"N\n\x15ListOperationsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\"f\n\x16ListOperationsResponse\x12\x33\n\noperations\x18\x01 \x03(\x0b\x32\x1f.salto.longrunning.v1.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"&\n\x16\x44\x65leteOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"&\n\x16\x43\x61ncelOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\x8d\x03\n\x10OperationService\x12Z\n\x0cGetOperation\x12).salto.longrunning.v1.GetOperationRequest\x1a\x1f.salto.longrunning.v1.Operation\x12k\n\x0eListOperations\x12+.salto.longrunning.v1.ListOperationsRequest\x1a,.salto.longrunning.v1.ListOperationsResponse\x12W\n\x0f\x44\x65leteOperation\x12,.salto.longrunning.v1.DeleteOperationRequest\x1a\x16.google.protobuf.Empty\x12W\n\x0f\x43\x61ncelOperation\x12,.salto.longrunning.v1.CancelOperationRequest\x1a\x16.google.protobuf.EmptyB\xd4\x01\n\x1c\x63om.saltoapis.longrunning.v1B\x0eOperationProtoP\x01ZEgithub.com/saltoapis-internal/saltoapis-go/longrunning/v1;longrunning\xaa\x02\x18Saltoapis.Longrunning.V1\xca\x02\x18Saltoapis\\Longrunning\\V1\xe2\x02$GPBMetadata\\Saltoapis\\Longrunning\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'salto.longrunning.v1.operation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.saltoapis.longrunning.v1B\016OperationProtoP\001ZEgithub.com/saltoapis-internal/saltoapis-go/longrunning/v1;longrunning\252\002\030Saltoapis.Longrunning.V1\312\002\030Saltoapis\\Longrunning\\V1\342\002$GPBMetadata\\Saltoapis\\Longrunning\\V1'
  _globals['_OPERATION']._serialized_start=144
  _globals['_OPERATION']._serialized_end=312
  _globals['_GETOPERATIONREQUEST']._serialized_start=314
  _globals['_GETOPERATIONREQUEST']._serialized_end=349
  _globals['_LISTOPERATIONSREQUEST']._serialized_start=351
  _globals['_LISTOPERATIONSREQUEST']._serialized_end=429
  _globals['_LISTOPERATIONSRESPONSE']._serialized_start=431
  _globals['_LISTOPERATIONSRESPONSE']._serialized_end=533
  _globals['_DELETEOPERATIONREQUEST']._serialized_start=535
  _globals['_DELETEOPERATIONREQUEST']._serialized_end=573
  _globals['_CANCELOPERATIONREQUEST']._serialized_start=575
  _globals['_CANCELOPERATIONREQUEST']._serialized_end=613
  _globals['_OPERATIONSERVICE']._serialized_start=616
  _globals['_OPERATIONSERVICE']._serialized_end=1013
# @@protoc_insertion_point(module_scope)
