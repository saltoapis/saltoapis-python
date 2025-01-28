# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: salto/nebula/digitalkey/v1/digital_key.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.type import color_pb2 as salto_dot_type_dot_color__pb2
from saltoapis.type import color_pb2 as salto_dot_type_dot_color__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,salto/nebula/digitalkey/v1/digital_key.proto\x12\x1asalto.nebula.digitalkey.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a$salto/longrunning/v1/operation.proto\x1a\x16salto/type/color.proto\"\xe1\x08\n\nDigitalKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x07\x61pp_key\x18\x02 \x01(\x0b\x32-.salto.nebula.digitalkey.v1.DigitalKey.AppKeyH\x00\x12\x46\n\nwallet_key\x18\x03 \x01(\x0b\x32\x30.salto.nebula.digitalkey.v1.DigitalKey.WalletKeyH\x00\x1av\n\x08Metadata\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x11\n\tphoto_uri\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12%\n\ntext_color\x18\x05 \x01(\x0b\x32\x11.salto.type.Color\x1a\xea\x03\n\x06\x41ppKey\x12\x41\n\x08metadata\x18\x01 \x01(\x0b\x32/.salto.nebula.digitalkey.v1.DigitalKey.Metadata\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x14\n\x0cinstallation\x18\x05 \x01(\t\x12\x11\n\x04unit\x18\x06 \x01(\tH\x00\x88\x01\x01\x12\x17\n\x0finstallation_id\x18\x03 \x01(\t\x12\x14\n\x07unit_id\x18\x04 \x01(\tH\x01\x88\x01\x01\x12;\n\x17\x61\x63\x63\x65ss_points_sync_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x65\n\x18\x61\x63\x63\x65ss_points_sync_state\x18\x08 \x01(\x0e\x32\x43.salto.nebula.digitalkey.v1.DigitalKey.AppKey.AccessPointsSyncState\"~\n\x15\x41\x63\x63\x65ssPointsSyncState\x12(\n$ACCESS_POINTS_SYNC_STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bINVALIDATED\x10\x03\x12\x0b\n\x07SYNCING\x10\x01\x12\n\n\x06SYNCED\x10\x02\x12\x11\n\rNOT_SUPPORTED\x10\x04\x42\x07\n\x05_unitB\n\n\x08_unit_id\x1a\xcd\x02\n\tWalletKey\x12\x41\n\x08metadata\x18\x01 \x01(\x0b\x32/.salto.nebula.digitalkey.v1.DigitalKey.Metadata\x12Z\n\x10hydra_credential\x18\x02 \x01(\x0b\x32@.salto.nebula.digitalkey.v1.DigitalKey.WalletKey.HydraCredential\x1a\xa0\x01\n\x0fHydraCredential\x12\x15\n\rcredential_id\x18\x01 \x01(\t\x12\x1b\n\x13sharing_instance_id\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63ount_hash\x18\x03 \x01(\t\x12\x13\n\x0btemplate_id\x18\x04 \x01(\t\x12\x18\n\x10relying_party_id\x18\x05 \x01(\t\x12\x14\n\x0creference_id\x18\x06 \x01(\tB\x06\n\x04type\"$\n\x14GetDigitalKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"a\n\x16ListDigitalKeysRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\"p\n\x17ListDigitalKeysResponse\x12<\n\x0c\x64igital_keys\x18\x01 \x03(\x0b\x32&.salto.nebula.digitalkey.v1.DigitalKey\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"N\n\x15\x44igitalKeyAccessPoint\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x11\n\tdevice_id\x18\x03 \x01(\t\"/\n\x1fGetDigitalKeyAccessPointRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"j\n!ListDigitalKeyAccessPointsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\"\x93\x01\n\"ListDigitalKeyAccessPointsResponse\x12T\n\x19\x64igital_key_access_points\x18\x01 \x03(\x0b\x32\x31.salto.nebula.digitalkey.v1.DigitalKeyAccessPoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"1\n!SyncDigitalKeyAccessPointsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"$\n\"SyncDigitalKeyAccessPointsResponse\"$\n\"SyncDigitalKeyAccessPointsMetadata\"2\n\"UnlockDigitalKeyAccessPointRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"%\n#UnlockDigitalKeyAccessPointResponse\"%\n#UnlockDigitalKeyAccessPointMetadata2\xa3\x06\n\x11\x44igitalKeyService\x12i\n\rGetDigitalKey\x12\x30.salto.nebula.digitalkey.v1.GetDigitalKeyRequest\x1a&.salto.nebula.digitalkey.v1.DigitalKey\x12z\n\x0fListDigitalKeys\x12\x32.salto.nebula.digitalkey.v1.ListDigitalKeysRequest\x1a\x33.salto.nebula.digitalkey.v1.ListDigitalKeysResponse\x12\x8a\x01\n\x18GetDigitalKeyAccessPoint\x12;.salto.nebula.digitalkey.v1.GetDigitalKeyAccessPointRequest\x1a\x31.salto.nebula.digitalkey.v1.DigitalKeyAccessPoint\x12\x9b\x01\n\x1aListDigitalKeyAccessPoints\x12=.salto.nebula.digitalkey.v1.ListDigitalKeyAccessPointsRequest\x1a>.salto.nebula.digitalkey.v1.ListDigitalKeyAccessPointsResponse\x12|\n\x1aSyncDigitalKeyAccessPoints\x12=.salto.nebula.digitalkey.v1.SyncDigitalKeyAccessPointsRequest\x1a\x1f.salto.longrunning.v1.Operation\x12~\n\x1bUnlockDigitalKeyAccessPoint\x12>.salto.nebula.digitalkey.v1.UnlockDigitalKeyAccessPointRequest\x1a\x1f.salto.longrunning.v1.OperationB\xf2\x01\n\"com.saltoapis.nebula.digitalkey.v1B\x0f\x44igitalKeyProtoP\x01ZJgithub.com/saltoapis-internal/saltoapis-go/nebula/digitalkey/v1;digitalkey\xaa\x02\x1eSaltoapis.Nebula.DigitalKey.V1\xca\x02\x1eSaltoapis\\Nebula\\DigitalKey\\V1\xe2\x02*GPBMetadata\\Saltoapis\\Nebula\\DigitalKey\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'salto.nebula.digitalkey.v1.digital_key_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.saltoapis.nebula.digitalkey.v1B\017DigitalKeyProtoP\001ZJgithub.com/saltoapis-internal/saltoapis-go/nebula/digitalkey/v1;digitalkey\252\002\036Saltoapis.Nebula.DigitalKey.V1\312\002\036Saltoapis\\Nebula\\DigitalKey\\V1\342\002*GPBMetadata\\Saltoapis\\Nebula\\DigitalKey\\V1'
  _globals['_DIGITALKEY']._serialized_start=172
  _globals['_DIGITALKEY']._serialized_end=1293
  _globals['_DIGITALKEY_METADATA']._serialized_start=338
  _globals['_DIGITALKEY_METADATA']._serialized_end=456
  _globals['_DIGITALKEY_APPKEY']._serialized_start=459
  _globals['_DIGITALKEY_APPKEY']._serialized_end=949
  _globals['_DIGITALKEY_APPKEY_ACCESSPOINTSSYNCSTATE']._serialized_start=802
  _globals['_DIGITALKEY_APPKEY_ACCESSPOINTSSYNCSTATE']._serialized_end=928
  _globals['_DIGITALKEY_WALLETKEY']._serialized_start=952
  _globals['_DIGITALKEY_WALLETKEY']._serialized_end=1285
  _globals['_DIGITALKEY_WALLETKEY_HYDRACREDENTIAL']._serialized_start=1125
  _globals['_DIGITALKEY_WALLETKEY_HYDRACREDENTIAL']._serialized_end=1285
  _globals['_GETDIGITALKEYREQUEST']._serialized_start=1295
  _globals['_GETDIGITALKEYREQUEST']._serialized_end=1331
  _globals['_LISTDIGITALKEYSREQUEST']._serialized_start=1333
  _globals['_LISTDIGITALKEYSREQUEST']._serialized_end=1430
  _globals['_LISTDIGITALKEYSRESPONSE']._serialized_start=1432
  _globals['_LISTDIGITALKEYSRESPONSE']._serialized_end=1544
  _globals['_DIGITALKEYACCESSPOINT']._serialized_start=1546
  _globals['_DIGITALKEYACCESSPOINT']._serialized_end=1624
  _globals['_GETDIGITALKEYACCESSPOINTREQUEST']._serialized_start=1626
  _globals['_GETDIGITALKEYACCESSPOINTREQUEST']._serialized_end=1673
  _globals['_LISTDIGITALKEYACCESSPOINTSREQUEST']._serialized_start=1675
  _globals['_LISTDIGITALKEYACCESSPOINTSREQUEST']._serialized_end=1781
  _globals['_LISTDIGITALKEYACCESSPOINTSRESPONSE']._serialized_start=1784
  _globals['_LISTDIGITALKEYACCESSPOINTSRESPONSE']._serialized_end=1931
  _globals['_SYNCDIGITALKEYACCESSPOINTSREQUEST']._serialized_start=1933
  _globals['_SYNCDIGITALKEYACCESSPOINTSREQUEST']._serialized_end=1982
  _globals['_SYNCDIGITALKEYACCESSPOINTSRESPONSE']._serialized_start=1984
  _globals['_SYNCDIGITALKEYACCESSPOINTSRESPONSE']._serialized_end=2020
  _globals['_SYNCDIGITALKEYACCESSPOINTSMETADATA']._serialized_start=2022
  _globals['_SYNCDIGITALKEYACCESSPOINTSMETADATA']._serialized_end=2058
  _globals['_UNLOCKDIGITALKEYACCESSPOINTREQUEST']._serialized_start=2060
  _globals['_UNLOCKDIGITALKEYACCESSPOINTREQUEST']._serialized_end=2110
  _globals['_UNLOCKDIGITALKEYACCESSPOINTRESPONSE']._serialized_start=2112
  _globals['_UNLOCKDIGITALKEYACCESSPOINTRESPONSE']._serialized_end=2149
  _globals['_UNLOCKDIGITALKEYACCESSPOINTMETADATA']._serialized_start=2151
  _globals['_UNLOCKDIGITALKEYACCESSPOINTMETADATA']._serialized_end=2188
  _globals['_DIGITALKEYSERVICE']._serialized_start=2191
  _globals['_DIGITALKEYSERVICE']._serialized_end=2994
# @@protoc_insertion_point(module_scope)
