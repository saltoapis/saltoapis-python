# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: salto/nebula/gateway/v1/gateway.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%salto/nebula/gateway/v1/gateway.proto\x12\x17salto.nebula.gateway.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a$salto/longrunning/v1/operation.proto\"\xff\x01\n\x07Gateway\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x16\n\tdevice_id\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x0binitialized\x18\x04 \x01(\x08\x12\x11\n\tconnected\x18\x07 \x01(\x08\x12\x44\n\x11\x65thernet_settings\x18\x05 \x01(\x0b\x32).salto.nebula.gateway.v1.EthernetSettings\x12<\n\rwifi_settings\x18\x06 \x01(\x0b\x32%.salto.nebula.gateway.v1.WifiSettingsB\x0c\n\n_device_id\"\x8c\x01\n\x10\x45thernetSettings\x12<\n\ripv4_settings\x18\x01 \x01(\x0b\x32%.salto.nebula.gateway.v1.IPv4Settings\x12:\n\x0c\x64ns_settings\x18\x02 \x01(\x0b\x32$.salto.nebula.gateway.v1.DNSSettings\"\xba\x01\n\x0cWifiSettings\x12<\n\ripv4_settings\x18\x01 \x01(\x0b\x32%.salto.nebula.gateway.v1.IPv4Settings\x12:\n\x0c\x64ns_settings\x18\x02 \x01(\x0b\x32$.salto.nebula.gateway.v1.DNSSettings\x12\x0c\n\x04ssid\x18\x03 \x01(\t\x12\x15\n\x08password\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_password\"\x82\x01\n\x0cIPv4Settings\x12\x17\n\nip_address\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04mask\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1b\n\x0erouter_address\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\r\n\x0b_ip_addressB\x07\n\x05_maskB\x11\n\x0f_router_address\"$\n\x0b\x44NSSettings\x12\x15\n\rdns_addresses\x18\x01 \x03(\t\"\x81\x01\n\x14\x43reateGatewayRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x17\n\ngateway_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x31\n\x07gateway\x18\x03 \x01(\x0b\x32 .salto.nebula.gateway.v1.GatewayB\r\n\x0b_gateway_id\"!\n\x11GetGatewayRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"n\n\x13ListGatewaysRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"c\n\x14ListGatewaysResponse\x12\x32\n\x08gateways\x18\x01 \x03(\x0b\x32 .salto.nebula.gateway.v1.Gateway\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"z\n\x14UpdateGatewayRequest\x12\x31\n\x07gateway\x18\x01 \x01(\x0b\x32 .salto.nebula.gateway.v1.Gateway\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"$\n\x14\x44\x65leteGatewayRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"5\n\x12\x42indGatewayRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdevice_id\x18\x02 \x01(\t\"\x15\n\x13\x42indGatewayResponse\"3\n\x14UnbindGatewayRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\"\x17\n\x15UnbindGatewayResponse\"(\n\x18InitializeGatewayRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1b\n\x19InitializeGatewayResponse\"\x1b\n\x19InitializeGatewayMetadata\"\'\n\x17\x43onfigureGatewayRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1a\n\x18\x43onfigureGatewayResponse\"\x1a\n\x18\x43onfigureGatewayMetadata\"#\n\x13ResetGatewayRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x16\n\x14ResetGatewayResponse\"\x16\n\x14ResetGatewayMetadata\"/\n\x1cUpdateGatewayFirmwareRequest\x12\x0f\n\x07gateway\x18\x01 \x01(\t\"\x1f\n\x1dUpdateGatewayFirmwareResponse\"9\n\x1dUpdateGatewayFirmwareMetadata\x12\x18\n\x10progress_percent\x18\x01 \x01(\x05\"4\n!GenerateAuthorizationTokenRequest\x12\x0f\n\x07gateway\x18\x01 \x01(\t\"A\n\"GenerateAuthorizationTokenResponse\x12\x1b\n\x13\x61uthorization_token\x18\x01 \x01(\x0c\"5\n\"GenerateFirmwareDownloadUriRequest\x12\x0f\n\x07gateway\x18\x01 \x01(\t\"K\n#GenerateFirmwareDownloadUriResponse\x12\x14\n\x0c\x64ownload_uri\x18\x01 \x01(\t\x12\x0e\n\x06\x64igest\x18\x02 \x01(\t\"%\n#GenerateFirmwareDownloadUriMetadata2\x84\x0b\n\x0eGatewayService\x12`\n\rCreateGateway\x12-.salto.nebula.gateway.v1.CreateGatewayRequest\x1a .salto.nebula.gateway.v1.Gateway\x12Z\n\nGetGateway\x12*.salto.nebula.gateway.v1.GetGatewayRequest\x1a .salto.nebula.gateway.v1.Gateway\x12k\n\x0cListGateways\x12,.salto.nebula.gateway.v1.ListGatewaysRequest\x1a-.salto.nebula.gateway.v1.ListGatewaysResponse\x12`\n\rUpdateGateway\x12-.salto.nebula.gateway.v1.UpdateGatewayRequest\x1a .salto.nebula.gateway.v1.Gateway\x12V\n\rDeleteGateway\x12-.salto.nebula.gateway.v1.DeleteGatewayRequest\x1a\x16.google.protobuf.Empty\x12h\n\x0b\x42indGateway\x12+.salto.nebula.gateway.v1.BindGatewayRequest\x1a,.salto.nebula.gateway.v1.BindGatewayResponse\x12n\n\rUnbindGateway\x12-.salto.nebula.gateway.v1.UnbindGatewayRequest\x1a..salto.nebula.gateway.v1.UnbindGatewayResponse\x12g\n\x11InitializeGateway\x12\x31.salto.nebula.gateway.v1.InitializeGatewayRequest\x1a\x1f.salto.longrunning.v1.Operation\x12\x65\n\x10\x43onfigureGateway\x12\x30.salto.nebula.gateway.v1.ConfigureGatewayRequest\x1a\x1f.salto.longrunning.v1.Operation\x12]\n\x0cResetGateway\x12,.salto.nebula.gateway.v1.ResetGatewayRequest\x1a\x1f.salto.longrunning.v1.Operation\x12o\n\x15UpdateGatewayFirmware\x12\x35.salto.nebula.gateway.v1.UpdateGatewayFirmwareRequest\x1a\x1f.salto.longrunning.v1.Operation\x12\x95\x01\n\x1aGenerateAuthorizationToken\x12:.salto.nebula.gateway.v1.GenerateAuthorizationTokenRequest\x1a;.salto.nebula.gateway.v1.GenerateAuthorizationTokenResponse\x12{\n\x1bGenerateFirmwareDownloadUri\x12;.salto.nebula.gateway.v1.GenerateFirmwareDownloadUriRequest\x1a\x1f.salto.longrunning.v1.OperationB\xdd\x01\n\x1f\x63om.saltoapis.nebula.gateway.v1B\x0cGatewayProtoP\x01ZDgithub.com/saltoapis-internal/saltoapis-go/nebula/gateway/v1;gateway\xaa\x02\x1bSaltoapis.Nebula.Gateway.V1\xca\x02\x1bSaltoapis\\Nebula\\Gateway\\V1\xe2\x02\'GPBMetadata\\Saltoapis\\Nebula\\Gateway\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'salto.nebula.gateway.v1.gateway_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.saltoapis.nebula.gateway.v1B\014GatewayProtoP\001ZDgithub.com/saltoapis-internal/saltoapis-go/nebula/gateway/v1;gateway\252\002\033Saltoapis.Nebula.Gateway.V1\312\002\033Saltoapis\\Nebula\\Gateway\\V1\342\002\'GPBMetadata\\Saltoapis\\Nebula\\Gateway\\V1'
  _globals['_GATEWAY']._serialized_start=168
  _globals['_GATEWAY']._serialized_end=423
  _globals['_ETHERNETSETTINGS']._serialized_start=426
  _globals['_ETHERNETSETTINGS']._serialized_end=566
  _globals['_WIFISETTINGS']._serialized_start=569
  _globals['_WIFISETTINGS']._serialized_end=755
  _globals['_IPV4SETTINGS']._serialized_start=758
  _globals['_IPV4SETTINGS']._serialized_end=888
  _globals['_DNSSETTINGS']._serialized_start=890
  _globals['_DNSSETTINGS']._serialized_end=926
  _globals['_CREATEGATEWAYREQUEST']._serialized_start=929
  _globals['_CREATEGATEWAYREQUEST']._serialized_end=1058
  _globals['_GETGATEWAYREQUEST']._serialized_start=1060
  _globals['_GETGATEWAYREQUEST']._serialized_end=1093
  _globals['_LISTGATEWAYSREQUEST']._serialized_start=1095
  _globals['_LISTGATEWAYSREQUEST']._serialized_end=1205
  _globals['_LISTGATEWAYSRESPONSE']._serialized_start=1207
  _globals['_LISTGATEWAYSRESPONSE']._serialized_end=1306
  _globals['_UPDATEGATEWAYREQUEST']._serialized_start=1308
  _globals['_UPDATEGATEWAYREQUEST']._serialized_end=1430
  _globals['_DELETEGATEWAYREQUEST']._serialized_start=1432
  _globals['_DELETEGATEWAYREQUEST']._serialized_end=1468
  _globals['_BINDGATEWAYREQUEST']._serialized_start=1470
  _globals['_BINDGATEWAYREQUEST']._serialized_end=1523
  _globals['_BINDGATEWAYRESPONSE']._serialized_start=1525
  _globals['_BINDGATEWAYRESPONSE']._serialized_end=1546
  _globals['_UNBINDGATEWAYREQUEST']._serialized_start=1548
  _globals['_UNBINDGATEWAYREQUEST']._serialized_end=1599
  _globals['_UNBINDGATEWAYRESPONSE']._serialized_start=1601
  _globals['_UNBINDGATEWAYRESPONSE']._serialized_end=1624
  _globals['_INITIALIZEGATEWAYREQUEST']._serialized_start=1626
  _globals['_INITIALIZEGATEWAYREQUEST']._serialized_end=1666
  _globals['_INITIALIZEGATEWAYRESPONSE']._serialized_start=1668
  _globals['_INITIALIZEGATEWAYRESPONSE']._serialized_end=1695
  _globals['_INITIALIZEGATEWAYMETADATA']._serialized_start=1697
  _globals['_INITIALIZEGATEWAYMETADATA']._serialized_end=1724
  _globals['_CONFIGUREGATEWAYREQUEST']._serialized_start=1726
  _globals['_CONFIGUREGATEWAYREQUEST']._serialized_end=1765
  _globals['_CONFIGUREGATEWAYRESPONSE']._serialized_start=1767
  _globals['_CONFIGUREGATEWAYRESPONSE']._serialized_end=1793
  _globals['_CONFIGUREGATEWAYMETADATA']._serialized_start=1795
  _globals['_CONFIGUREGATEWAYMETADATA']._serialized_end=1821
  _globals['_RESETGATEWAYREQUEST']._serialized_start=1823
  _globals['_RESETGATEWAYREQUEST']._serialized_end=1858
  _globals['_RESETGATEWAYRESPONSE']._serialized_start=1860
  _globals['_RESETGATEWAYRESPONSE']._serialized_end=1882
  _globals['_RESETGATEWAYMETADATA']._serialized_start=1884
  _globals['_RESETGATEWAYMETADATA']._serialized_end=1906
  _globals['_UPDATEGATEWAYFIRMWAREREQUEST']._serialized_start=1908
  _globals['_UPDATEGATEWAYFIRMWAREREQUEST']._serialized_end=1955
  _globals['_UPDATEGATEWAYFIRMWARERESPONSE']._serialized_start=1957
  _globals['_UPDATEGATEWAYFIRMWARERESPONSE']._serialized_end=1988
  _globals['_UPDATEGATEWAYFIRMWAREMETADATA']._serialized_start=1990
  _globals['_UPDATEGATEWAYFIRMWAREMETADATA']._serialized_end=2047
  _globals['_GENERATEAUTHORIZATIONTOKENREQUEST']._serialized_start=2049
  _globals['_GENERATEAUTHORIZATIONTOKENREQUEST']._serialized_end=2101
  _globals['_GENERATEAUTHORIZATIONTOKENRESPONSE']._serialized_start=2103
  _globals['_GENERATEAUTHORIZATIONTOKENRESPONSE']._serialized_end=2168
  _globals['_GENERATEFIRMWAREDOWNLOADURIREQUEST']._serialized_start=2170
  _globals['_GENERATEFIRMWAREDOWNLOADURIREQUEST']._serialized_end=2223
  _globals['_GENERATEFIRMWAREDOWNLOADURIRESPONSE']._serialized_start=2225
  _globals['_GENERATEFIRMWAREDOWNLOADURIRESPONSE']._serialized_end=2300
  _globals['_GENERATEFIRMWAREDOWNLOADURIMETADATA']._serialized_start=2302
  _globals['_GENERATEFIRMWAREDOWNLOADURIMETADATA']._serialized_end=2339
  _globals['_GATEWAYSERVICE']._serialized_start=2342
  _globals['_GATEWAYSERVICE']._serialized_end=3754
# @@protoc_insertion_point(module_scope)
