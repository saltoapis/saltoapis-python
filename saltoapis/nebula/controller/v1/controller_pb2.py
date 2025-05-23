# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: salto/nebula/controller/v1/controller.proto
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
    'salto/nebula/controller/v1/controller.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.nebula.type import device_metadata_pb2 as salto_dot_nebula_dot_type_dot_device__metadata__pb2
from saltoapis.nebula.type import device_metadata_pb2 as salto_dot_nebula_dot_type_dot_device__metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+salto/nebula/controller/v1/controller.proto\x12\x1asalto.nebula.controller.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a$salto/longrunning/v1/operation.proto\x1a\'salto/nebula/type/device_metadata.proto\"\xe3\x02\n\nController\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x16\n\tdevice_id\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x07gateway\x18\x04 \x01(\tH\x00\x12\x12\n\x08\x65xtender\x18\x05 \x01(\tH\x00\x12\x15\n\raccess_points\x18\x06 \x03(\t\x12\x13\n\x0binitialized\x18\x07 \x01(\x08\x12:\n\x0f\x64\x65vice_metadata\x18\x0b \x01(\x0b\x32!.salto.nebula.type.DeviceMetadata\x12\x10\n\x08outdated\x18\x08 \x01(\x08\x12\x16\n\tconnected\x18\t \x01(\x08H\x02\x88\x01\x01\x12\x33\n\x0flast_event_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0f\n\rparent_deviceB\x0c\n\n_device_idB\x0c\n\n_connected\"\x93\x01\n\x17\x43reateControllerRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x1a\n\rcontroller_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12:\n\ncontroller\x18\x03 \x01(\x0b\x32&.salto.nebula.controller.v1.ControllerB\x10\n\x0e_controller_id\"$\n\x14GetControllerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"q\n\x16ListControllersRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"o\n\x17ListControllersResponse\x12;\n\x0b\x63ontrollers\x18\x01 \x03(\x0b\x32&.salto.nebula.controller.v1.Controller\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x86\x01\n\x17UpdateControllerRequest\x12:\n\ncontroller\x18\x01 \x01(\x0b\x32&.salto.nebula.controller.v1.Controller\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\'\n\x17\x44\x65leteControllerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"8\n\x15\x42indControllerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdevice_id\x18\x02 \x01(\t\"\x18\n\x16\x42indControllerResponse\"6\n\x17UnbindControllerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\"\x1a\n\x18UnbindControllerResponse\"+\n\x1bInitializeControllerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1e\n\x1cInitializeControllerResponse\"8\n\x1cInitializeControllerMetadata\x12\x18\n\x10progress_percent\x18\x01 \x01(\x05\"*\n\x1a\x43onfigureControllerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\x1b\x43onfigureControllerResponse\"7\n\x1b\x43onfigureControllerMetadata\x12\x18\n\x10progress_percent\x18\x01 \x01(\x05\"&\n\x16ResetControllerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x19\n\x17ResetControllerResponse\"\x19\n\x17ResetControllerMetadata\"5\n\x1fUpdateControllerFirmwareRequest\x12\x12\n\ncontroller\x18\x01 \x01(\t\"\"\n UpdateControllerFirmwareResponse\"<\n UpdateControllerFirmwareMetadata\x12\x18\n\x10progress_percent\x18\x01 \x01(\x05\"7\n!GenerateAuthorizationTokenRequest\x12\x12\n\ncontroller\x18\x01 \x01(\t\"A\n\"GenerateAuthorizationTokenResponse\x12\x1b\n\x13\x61uthorization_token\x18\x01 \x01(\x0c\"8\n\"GenerateFirmwareDownloadUriRequest\x12\x12\n\ncontroller\x18\x01 \x01(\t\"K\n#GenerateFirmwareDownloadUriResponse\x12\x14\n\x0c\x64ownload_uri\x18\x01 \x01(\t\x12\x0e\n\x06\x64igest\x18\x02 \x01(\t\"%\n#GenerateFirmwareDownloadUriMetadata2\x97\x0c\n\x11\x43ontrollerService\x12o\n\x10\x43reateController\x12\x33.salto.nebula.controller.v1.CreateControllerRequest\x1a&.salto.nebula.controller.v1.Controller\x12i\n\rGetController\x12\x30.salto.nebula.controller.v1.GetControllerRequest\x1a&.salto.nebula.controller.v1.Controller\x12z\n\x0fListControllers\x12\x32.salto.nebula.controller.v1.ListControllersRequest\x1a\x33.salto.nebula.controller.v1.ListControllersResponse\x12o\n\x10UpdateController\x12\x33.salto.nebula.controller.v1.UpdateControllerRequest\x1a&.salto.nebula.controller.v1.Controller\x12_\n\x10\x44\x65leteController\x12\x33.salto.nebula.controller.v1.DeleteControllerRequest\x1a\x16.google.protobuf.Empty\x12w\n\x0e\x42indController\x12\x31.salto.nebula.controller.v1.BindControllerRequest\x1a\x32.salto.nebula.controller.v1.BindControllerResponse\x12}\n\x10UnbindController\x12\x33.salto.nebula.controller.v1.UnbindControllerRequest\x1a\x34.salto.nebula.controller.v1.UnbindControllerResponse\x12p\n\x14InitializeController\x12\x37.salto.nebula.controller.v1.InitializeControllerRequest\x1a\x1f.salto.longrunning.v1.Operation\x12n\n\x13\x43onfigureController\x12\x36.salto.nebula.controller.v1.ConfigureControllerRequest\x1a\x1f.salto.longrunning.v1.Operation\x12\x66\n\x0fResetController\x12\x32.salto.nebula.controller.v1.ResetControllerRequest\x1a\x1f.salto.longrunning.v1.Operation\x12x\n\x18UpdateControllerFirmware\x12;.salto.nebula.controller.v1.UpdateControllerFirmwareRequest\x1a\x1f.salto.longrunning.v1.Operation\x12\x9b\x01\n\x1aGenerateAuthorizationToken\x12=.salto.nebula.controller.v1.GenerateAuthorizationTokenRequest\x1a>.salto.nebula.controller.v1.GenerateAuthorizationTokenResponse\x12~\n\x1bGenerateFirmwareDownloadUri\x12>.salto.nebula.controller.v1.GenerateFirmwareDownloadUriRequest\x1a\x1f.salto.longrunning.v1.OperationB\xf2\x01\n\"com.saltoapis.nebula.controller.v1B\x0f\x43ontrollerProtoP\x01ZJgithub.com/saltoapis-internal/saltoapis-go/nebula/controller/v1;controller\xaa\x02\x1eSaltoapis.Nebula.Controller.V1\xca\x02\x1eSaltoapis\\Nebula\\Controller\\V1\xe2\x02*GPBMetadata\\Saltoapis\\Nebula\\Controller\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'salto.nebula.controller.v1.controller_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.saltoapis.nebula.controller.v1B\017ControllerProtoP\001ZJgithub.com/saltoapis-internal/saltoapis-go/nebula/controller/v1;controller\252\002\036Saltoapis.Nebula.Controller.V1\312\002\036Saltoapis\\Nebula\\Controller\\V1\342\002*GPBMetadata\\Saltoapis\\Nebula\\Controller\\V1'
  _globals['_CONTROLLER']._serialized_start=251
  _globals['_CONTROLLER']._serialized_end=606
  _globals['_CREATECONTROLLERREQUEST']._serialized_start=609
  _globals['_CREATECONTROLLERREQUEST']._serialized_end=756
  _globals['_GETCONTROLLERREQUEST']._serialized_start=758
  _globals['_GETCONTROLLERREQUEST']._serialized_end=794
  _globals['_LISTCONTROLLERSREQUEST']._serialized_start=796
  _globals['_LISTCONTROLLERSREQUEST']._serialized_end=909
  _globals['_LISTCONTROLLERSRESPONSE']._serialized_start=911
  _globals['_LISTCONTROLLERSRESPONSE']._serialized_end=1022
  _globals['_UPDATECONTROLLERREQUEST']._serialized_start=1025
  _globals['_UPDATECONTROLLERREQUEST']._serialized_end=1159
  _globals['_DELETECONTROLLERREQUEST']._serialized_start=1161
  _globals['_DELETECONTROLLERREQUEST']._serialized_end=1200
  _globals['_BINDCONTROLLERREQUEST']._serialized_start=1202
  _globals['_BINDCONTROLLERREQUEST']._serialized_end=1258
  _globals['_BINDCONTROLLERRESPONSE']._serialized_start=1260
  _globals['_BINDCONTROLLERRESPONSE']._serialized_end=1284
  _globals['_UNBINDCONTROLLERREQUEST']._serialized_start=1286
  _globals['_UNBINDCONTROLLERREQUEST']._serialized_end=1340
  _globals['_UNBINDCONTROLLERRESPONSE']._serialized_start=1342
  _globals['_UNBINDCONTROLLERRESPONSE']._serialized_end=1368
  _globals['_INITIALIZECONTROLLERREQUEST']._serialized_start=1370
  _globals['_INITIALIZECONTROLLERREQUEST']._serialized_end=1413
  _globals['_INITIALIZECONTROLLERRESPONSE']._serialized_start=1415
  _globals['_INITIALIZECONTROLLERRESPONSE']._serialized_end=1445
  _globals['_INITIALIZECONTROLLERMETADATA']._serialized_start=1447
  _globals['_INITIALIZECONTROLLERMETADATA']._serialized_end=1503
  _globals['_CONFIGURECONTROLLERREQUEST']._serialized_start=1505
  _globals['_CONFIGURECONTROLLERREQUEST']._serialized_end=1547
  _globals['_CONFIGURECONTROLLERRESPONSE']._serialized_start=1549
  _globals['_CONFIGURECONTROLLERRESPONSE']._serialized_end=1578
  _globals['_CONFIGURECONTROLLERMETADATA']._serialized_start=1580
  _globals['_CONFIGURECONTROLLERMETADATA']._serialized_end=1635
  _globals['_RESETCONTROLLERREQUEST']._serialized_start=1637
  _globals['_RESETCONTROLLERREQUEST']._serialized_end=1675
  _globals['_RESETCONTROLLERRESPONSE']._serialized_start=1677
  _globals['_RESETCONTROLLERRESPONSE']._serialized_end=1702
  _globals['_RESETCONTROLLERMETADATA']._serialized_start=1704
  _globals['_RESETCONTROLLERMETADATA']._serialized_end=1729
  _globals['_UPDATECONTROLLERFIRMWAREREQUEST']._serialized_start=1731
  _globals['_UPDATECONTROLLERFIRMWAREREQUEST']._serialized_end=1784
  _globals['_UPDATECONTROLLERFIRMWARERESPONSE']._serialized_start=1786
  _globals['_UPDATECONTROLLERFIRMWARERESPONSE']._serialized_end=1820
  _globals['_UPDATECONTROLLERFIRMWAREMETADATA']._serialized_start=1822
  _globals['_UPDATECONTROLLERFIRMWAREMETADATA']._serialized_end=1882
  _globals['_GENERATEAUTHORIZATIONTOKENREQUEST']._serialized_start=1884
  _globals['_GENERATEAUTHORIZATIONTOKENREQUEST']._serialized_end=1939
  _globals['_GENERATEAUTHORIZATIONTOKENRESPONSE']._serialized_start=1941
  _globals['_GENERATEAUTHORIZATIONTOKENRESPONSE']._serialized_end=2006
  _globals['_GENERATEFIRMWAREDOWNLOADURIREQUEST']._serialized_start=2008
  _globals['_GENERATEFIRMWAREDOWNLOADURIREQUEST']._serialized_end=2064
  _globals['_GENERATEFIRMWAREDOWNLOADURIRESPONSE']._serialized_start=2066
  _globals['_GENERATEFIRMWAREDOWNLOADURIRESPONSE']._serialized_end=2141
  _globals['_GENERATEFIRMWAREDOWNLOADURIMETADATA']._serialized_start=2143
  _globals['_GENERATEFIRMWAREDOWNLOADURIMETADATA']._serialized_end=2180
  _globals['_CONTROLLERSERVICE']._serialized_start=2183
  _globals['_CONTROLLERSERVICE']._serialized_end=3742
# @@protoc_insertion_point(module_scope)
