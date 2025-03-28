# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: salto/nebula/event/v1/types.proto
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
    'salto/nebula/event/v1/types.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from saltoapis.nebula.accesspoint.v1 import access_point_pb2 as salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2
from saltoapis.nebula.accesspoint.v1 import access_point_pb2 as salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2
from saltoapis.nebula.accessright.v1 import access_right_pb2 as salto_dot_nebula_dot_accessright_dot_v1_dot_access__right__pb2
from saltoapis.nebula.accessright.v1 import access_right_pb2 as salto_dot_nebula_dot_accessright_dot_v1_dot_access__right__pb2
from saltoapis.nebula.emergencykey.v1 import emergency_key_pb2 as salto_dot_nebula_dot_emergencykey_dot_v1_dot_emergency__key__pb2
from saltoapis.nebula.emergencykey.v1 import emergency_key_pb2 as salto_dot_nebula_dot_emergencykey_dot_v1_dot_emergency__key__pb2
from saltoapis.nebula.unit.v1 import unit_pb2 as salto_dot_nebula_dot_unit_dot_v1_dot_unit__pb2
from saltoapis.nebula.unit.v1 import unit_pb2 as salto_dot_nebula_dot_unit_dot_v1_dot_unit__pb2
from saltoapis.nebula.user.v1 import user_pb2 as salto_dot_nebula_dot_user_dot_v1_dot_user__pb2
from saltoapis.nebula.user.v1 import user_pb2 as salto_dot_nebula_dot_user_dot_v1_dot_user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!salto/nebula/event/v1/types.proto\x12\x15salto.nebula.event.v1\x1a.salto/nebula/accesspoint/v1/access_point.proto\x1a.salto/nebula/accessright/v1/access_right.proto\x1a\x30salto/nebula/emergencykey/v1/emergency_key.proto\x1a\x1fsalto/nebula/unit/v1/unit.proto\x1a\x1fsalto/nebula/user/v1/user.proto\"T\n\x12\x41\x63\x63\x65ssPointCreated\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x01 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\"T\n\x12\x41\x63\x63\x65ssPointUpdated\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x01 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\"T\n\x12\x41\x63\x63\x65ssPointDeleted\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x01 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\"\xd2\x01\n\x13\x41\x63\x63\x65ssPointUnlocked\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x01 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\x12(\n\x04user\x18\x02 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12\x43\n\remergency_key\x18\x03 \x01(\x0b\x32*.salto.nebula.emergencykey.v1.EmergencyKeyH\x00\x42\x0c\n\ncredential\"\xd0\x01\n\x11\x41\x63\x63\x65ssPointLocked\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x01 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\x12(\n\x04user\x18\x02 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12\x43\n\remergency_key\x18\x03 \x01(\x0b\x32*.salto.nebula.emergencykey.v1.EmergencyKeyH\x00\x42\x0c\n\ncredential\"W\n\x15\x41\x63\x63\x65ssPointForcedOpen\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x01 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\"S\n\x11\x41\x63\x63\x65ssPointClosed\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x01 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\"x\n\x0c\x41\x63\x63\x65ssDenied\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x01 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\x12(\n\x04user\x18\x02 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\"U\n\x13\x41\x63\x63\x65ssPointLeftOpen\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x01 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\"T\n\x12\x41\x63\x63\x65ssRightCreated\x12>\n\x0c\x61\x63\x63\x65ss_right\x18\x01 \x01(\x0b\x32(.salto.nebula.accessright.v1.AccessRight\"T\n\x12\x41\x63\x63\x65ssRightUpdated\x12>\n\x0c\x61\x63\x63\x65ss_right\x18\x01 \x01(\x0b\x32(.salto.nebula.accessright.v1.AccessRight\"T\n\x12\x41\x63\x63\x65ssRightDeleted\x12>\n\x0c\x61\x63\x63\x65ss_right\x18\x01 \x01(\x0b\x32(.salto.nebula.accessright.v1.AccessRight\"\x9f\x01\n\x1d\x41\x63\x63\x65ssRightAccessPointCreated\x12>\n\x0c\x61\x63\x63\x65ss_right\x18\x01 \x01(\x0b\x32(.salto.nebula.accessright.v1.AccessRight\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x02 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\"\xa6\x01\n#AccessRightAccessPointsBatchCreated\x12>\n\x0c\x61\x63\x63\x65ss_right\x18\x01 \x01(\x0b\x32(.salto.nebula.accessright.v1.AccessRight\x12?\n\raccess_points\x18\x02 \x03(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\"\x9f\x01\n\x1d\x41\x63\x63\x65ssRightAccessPointDeleted\x12>\n\x0c\x61\x63\x63\x65ss_right\x18\x01 \x01(\x0b\x32(.salto.nebula.accessright.v1.AccessRight\x12>\n\x0c\x61\x63\x63\x65ss_point\x18\x02 \x01(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\"\xa6\x01\n#AccessRightAccessPointsBatchDeleted\x12>\n\x0c\x61\x63\x63\x65ss_right\x18\x01 \x01(\x0b\x32(.salto.nebula.accessright.v1.AccessRight\x12?\n\raccess_points\x18\x02 \x03(\x0b\x32(.salto.nebula.accesspoint.v1.AccessPoint\"7\n\x0bUserCreated\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\"7\n\x0bUserUpdated\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\"7\n\x0bUserBlocked\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\"9\n\rUserUnblocked\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\"7\n\x0bUserDeleted\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\"\x82\x01\n\x16UserAccessRightCreated\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12>\n\x0c\x61\x63\x63\x65ss_right\x18\x02 \x01(\x0b\x32(.salto.nebula.accessright.v1.AccessRight\"\x82\x01\n\x16UserAccessRightUpdated\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12>\n\x0c\x61\x63\x63\x65ss_right\x18\x02 \x01(\x0b\x32(.salto.nebula.accessright.v1.AccessRight\"\x82\x01\n\x16UserAccessRightDeleted\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12>\n\x0c\x61\x63\x63\x65ss_right\x18\x02 \x01(\x0b\x32(.salto.nebula.accessright.v1.AccessRight\"l\n\x0f\x43\x61rdKeyAssigned\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12/\n\x08\x63\x61rd_key\x18\x02 \x01(\x0b\x32\x1d.salto.nebula.user.v1.CardKey\"l\n\x0f\x43\x61rdKeyCanceled\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12/\n\x08\x63\x61rd_key\x18\x02 \x01(\x0b\x32\x1d.salto.nebula.user.v1.CardKey\"i\n\x0e\x41ppKeyAssigned\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12-\n\x07\x61pp_key\x18\x02 \x01(\x0b\x32\x1c.salto.nebula.user.v1.AppKey\"i\n\x0e\x41ppKeyCanceled\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12-\n\x07\x61pp_key\x18\x02 \x01(\x0b\x32\x1c.salto.nebula.user.v1.AppKey\"r\n\x11WalletKeyAssigned\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12\x33\n\nwallet_key\x18\x02 \x01(\x0b\x32\x1f.salto.nebula.user.v1.WalletKey\"r\n\x11WalletKeyCanceled\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12\x33\n\nwallet_key\x18\x02 \x01(\x0b\x32\x1f.salto.nebula.user.v1.WalletKey\"7\n\x0bUnitMovedIn\x12(\n\x04unit\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.unit.v1.Unit\"8\n\x0cUnitMovedOut\x12(\n\x04unit\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.unit.v1.Unit\"7\n\x0bUnitCreated\x12(\n\x04unit\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.unit.v1.Unit\"7\n\x0bUnitUpdated\x12(\n\x04unit\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.unit.v1.Unit\"7\n\x0bUnitDeleted\x12(\n\x04unit\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.unit.v1.Unit\"X\n\x13\x45mergencyKeyCreated\x12\x41\n\remergency_key\x18\x01 \x01(\x0b\x32*.salto.nebula.emergencykey.v1.EmergencyKey\"X\n\x13\x45mergencyKeyUpdated\x12\x41\n\remergency_key\x18\x01 \x01(\x0b\x32*.salto.nebula.emergencykey.v1.EmergencyKey\"X\n\x13\x45mergencyKeyDeleted\x12\x41\n\remergency_key\x18\x01 \x01(\x0b\x32*.salto.nebula.emergencykey.v1.EmergencyKeyB\xcf\x01\n\x1d\x63om.saltoapis.nebula.event.v1B\nTypesProtoP\x01Z@github.com/saltoapis-internal/saltoapis-go/nebula/event/v1;event\xaa\x02\x19Saltoapis.Nebula.Event.V1\xca\x02\x19Saltoapis\\Nebula\\Event\\V1\xe2\x02%GPBMetadata\\Saltoapis\\Nebula\\Event\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'salto.nebula.event.v1.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.saltoapis.nebula.event.v1B\nTypesProtoP\001Z@github.com/saltoapis-internal/saltoapis-go/nebula/event/v1;event\252\002\031Saltoapis.Nebula.Event.V1\312\002\031Saltoapis\\Nebula\\Event\\V1\342\002%GPBMetadata\\Saltoapis\\Nebula\\Event\\V1'
  _globals['_ACCESSPOINTCREATED']._serialized_start=272
  _globals['_ACCESSPOINTCREATED']._serialized_end=356
  _globals['_ACCESSPOINTUPDATED']._serialized_start=358
  _globals['_ACCESSPOINTUPDATED']._serialized_end=442
  _globals['_ACCESSPOINTDELETED']._serialized_start=444
  _globals['_ACCESSPOINTDELETED']._serialized_end=528
  _globals['_ACCESSPOINTUNLOCKED']._serialized_start=531
  _globals['_ACCESSPOINTUNLOCKED']._serialized_end=741
  _globals['_ACCESSPOINTLOCKED']._serialized_start=744
  _globals['_ACCESSPOINTLOCKED']._serialized_end=952
  _globals['_ACCESSPOINTFORCEDOPEN']._serialized_start=954
  _globals['_ACCESSPOINTFORCEDOPEN']._serialized_end=1041
  _globals['_ACCESSPOINTCLOSED']._serialized_start=1043
  _globals['_ACCESSPOINTCLOSED']._serialized_end=1126
  _globals['_ACCESSDENIED']._serialized_start=1128
  _globals['_ACCESSDENIED']._serialized_end=1248
  _globals['_ACCESSPOINTLEFTOPEN']._serialized_start=1250
  _globals['_ACCESSPOINTLEFTOPEN']._serialized_end=1335
  _globals['_ACCESSRIGHTCREATED']._serialized_start=1337
  _globals['_ACCESSRIGHTCREATED']._serialized_end=1421
  _globals['_ACCESSRIGHTUPDATED']._serialized_start=1423
  _globals['_ACCESSRIGHTUPDATED']._serialized_end=1507
  _globals['_ACCESSRIGHTDELETED']._serialized_start=1509
  _globals['_ACCESSRIGHTDELETED']._serialized_end=1593
  _globals['_ACCESSRIGHTACCESSPOINTCREATED']._serialized_start=1596
  _globals['_ACCESSRIGHTACCESSPOINTCREATED']._serialized_end=1755
  _globals['_ACCESSRIGHTACCESSPOINTSBATCHCREATED']._serialized_start=1758
  _globals['_ACCESSRIGHTACCESSPOINTSBATCHCREATED']._serialized_end=1924
  _globals['_ACCESSRIGHTACCESSPOINTDELETED']._serialized_start=1927
  _globals['_ACCESSRIGHTACCESSPOINTDELETED']._serialized_end=2086
  _globals['_ACCESSRIGHTACCESSPOINTSBATCHDELETED']._serialized_start=2089
  _globals['_ACCESSRIGHTACCESSPOINTSBATCHDELETED']._serialized_end=2255
  _globals['_USERCREATED']._serialized_start=2257
  _globals['_USERCREATED']._serialized_end=2312
  _globals['_USERUPDATED']._serialized_start=2314
  _globals['_USERUPDATED']._serialized_end=2369
  _globals['_USERBLOCKED']._serialized_start=2371
  _globals['_USERBLOCKED']._serialized_end=2426
  _globals['_USERUNBLOCKED']._serialized_start=2428
  _globals['_USERUNBLOCKED']._serialized_end=2485
  _globals['_USERDELETED']._serialized_start=2487
  _globals['_USERDELETED']._serialized_end=2542
  _globals['_USERACCESSRIGHTCREATED']._serialized_start=2545
  _globals['_USERACCESSRIGHTCREATED']._serialized_end=2675
  _globals['_USERACCESSRIGHTUPDATED']._serialized_start=2678
  _globals['_USERACCESSRIGHTUPDATED']._serialized_end=2808
  _globals['_USERACCESSRIGHTDELETED']._serialized_start=2811
  _globals['_USERACCESSRIGHTDELETED']._serialized_end=2941
  _globals['_CARDKEYASSIGNED']._serialized_start=2943
  _globals['_CARDKEYASSIGNED']._serialized_end=3051
  _globals['_CARDKEYCANCELED']._serialized_start=3053
  _globals['_CARDKEYCANCELED']._serialized_end=3161
  _globals['_APPKEYASSIGNED']._serialized_start=3163
  _globals['_APPKEYASSIGNED']._serialized_end=3268
  _globals['_APPKEYCANCELED']._serialized_start=3270
  _globals['_APPKEYCANCELED']._serialized_end=3375
  _globals['_WALLETKEYASSIGNED']._serialized_start=3377
  _globals['_WALLETKEYASSIGNED']._serialized_end=3491
  _globals['_WALLETKEYCANCELED']._serialized_start=3493
  _globals['_WALLETKEYCANCELED']._serialized_end=3607
  _globals['_UNITMOVEDIN']._serialized_start=3609
  _globals['_UNITMOVEDIN']._serialized_end=3664
  _globals['_UNITMOVEDOUT']._serialized_start=3666
  _globals['_UNITMOVEDOUT']._serialized_end=3722
  _globals['_UNITCREATED']._serialized_start=3724
  _globals['_UNITCREATED']._serialized_end=3779
  _globals['_UNITUPDATED']._serialized_start=3781
  _globals['_UNITUPDATED']._serialized_end=3836
  _globals['_UNITDELETED']._serialized_start=3838
  _globals['_UNITDELETED']._serialized_end=3893
  _globals['_EMERGENCYKEYCREATED']._serialized_start=3895
  _globals['_EMERGENCYKEYCREATED']._serialized_end=3983
  _globals['_EMERGENCYKEYUPDATED']._serialized_start=3985
  _globals['_EMERGENCYKEYUPDATED']._serialized_end=4073
  _globals['_EMERGENCYKEYDELETED']._serialized_start=4075
  _globals['_EMERGENCYKEYDELETED']._serialized_end=4163
# @@protoc_insertion_point(module_scope)
