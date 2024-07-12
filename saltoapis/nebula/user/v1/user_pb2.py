# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: salto/nebula/user/v1/user.proto
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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.nebula.type import schedule_pb2 as salto_dot_nebula_dot_type_dot_schedule__pb2
from saltoapis.nebula.type import schedule_pb2 as salto_dot_nebula_dot_type_dot_schedule__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsalto/nebula/user/v1/user.proto\x12\x14salto.nebula.user.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a$salto/longrunning/v1/operation.proto\x1a salto/nebula/type/schedule.proto\"\x93\x04\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x06parent\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\ngiven_name\x18\x03 \x01(\t\x12\x18\n\x0b\x66\x61mily_name\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x0c\x64isplay_name\x18\x05 \x01(\t\x12\x12\n\x05\x65mail\x18\x06 \x01(\tH\x02\x88\x01\x01\x12\x31\n\ractivate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x65xpire_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\x05photo\x18\t \x01(\tH\x03\x88\x01\x01\x12\x11\n\tphoto_uri\x18\n \x01(\t\x12/\n\x08\x63\x61rd_key\x18\x0b \x01(\x0b\x32\x1d.salto.nebula.user.v1.CardKey\x12-\n\x07\x61pp_key\x18\x0c \x01(\x0b\x32\x1c.salto.nebula.user.v1.AppKey\x12\x33\n\nwallet_key\x18\r \x01(\x0b\x32\x1f.salto.nebula.user.v1.WalletKey\x12\x30\n\x08passcode\x18\x0f \x01(\x0b\x32\x1e.salto.nebula.user.v1.Passcode\x12\x0f\n\x07\x62locked\x18\x0e \x01(\x08\x42\t\n\x07_parentB\x0e\n\x0c_family_nameB\x08\n\x06_emailB\x08\n\x06_photo\"\xb5\x01\n\x0fUserAccessRight\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_right\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12.\n\tschedules\x18\x04 \x03(\x0b\x32\x1b.salto.nebula.type.Schedule\x12\x38\n\x13\x65\x66\x66\x65\x63tive_schedules\x18\x05 \x03(\x0b\x32\x1b.salto.nebula.type.Schedule\"\xc2\x01\n\x07\x43\x61rdKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x03uid\x18\x02 \x01(\tH\x00\x12\x32\n\x05state\x18\x03 \x01(\x0e\x32#.salto.nebula.user.v1.CardKey.State\x12\x10\n\x08outdated\x18\x04 \x01(\x08\"I\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_ASSIGNED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\n\n\x06\x41\x43TIVE\x10\x03\x42\t\n\x07\x63\x61rd_id\"\xa6\x01\n\x06\x41ppKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x05state\x18\x02 \x01(\x0e\x32\".salto.nebula.user.v1.AppKey.State\x12\x10\n\x08outdated\x18\x03 \x01(\x08\"I\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_ASSIGNED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\n\n\x06\x41\x43TIVE\x10\x03\"\xac\x01\n\tWalletKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x05state\x18\x02 \x01(\x0e\x32%.salto.nebula.user.v1.WalletKey.State\x12\x10\n\x08outdated\x18\x03 \x01(\x08\"I\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_ASSIGNED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\n\n\x06\x41\x43TIVE\x10\x03\"\x8b\x01\n\x08Passcode\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x33\n\x05state\x18\x02 \x01(\x0e\x32$.salto.nebula.user.v1.Passcode.State\"<\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_ASSIGNED\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\"o\n\x11\x43reateUserRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x14\n\x07user_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12(\n\x04user\x18\x03 \x01(\x0b\x32\x1a.salto.nebula.user.v1.UserB\n\n\x08_user_id\"\x1e\n\x0eGetUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"k\n\x10ListUsersRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"k\n\x11ListUsersResponse\x12)\n\x05users\x18\x01 \x03(\x0b\x32\x1a.salto.nebula.user.v1.User\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05\"n\n\x11UpdateUserRequest\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.salto.nebula.user.v1.User\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"!\n\x11\x44\x65leteUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\x10\x42lockUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x13\n\x11\x42lockUserResponse\"\"\n\x12UnblockUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x15\n\x13UnblockUserResponse\"p\n\x1c\x43reateUserAccessRightRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12@\n\x11user_access_right\x18\x02 \x01(\x0b\x32%.salto.nebula.user.v1.UserAccessRight\")\n\x19GetUserAccessRightRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"v\n\x1bListUserAccessRightsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"z\n\x1cListUserAccessRightsResponse\x12\x41\n\x12user_access_rights\x18\x01 \x03(\x0b\x32%.salto.nebula.user.v1.UserAccessRight\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x91\x01\n\x1cUpdateUserAccessRightRequest\x12@\n\x11user_access_right\x18\x01 \x01(\x0b\x32%.salto.nebula.user.v1.UserAccessRight\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\",\n\x1c\x44\x65leteUserAccessRightRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\">\n\x14\x41ssignCardKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x03uid\x18\x02 \x01(\tH\x00\x42\t\n\x07\x63\x61rd_id\"$\n\x14\x43\x61ncelCardKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"r\n\x14\x45ncodeCardKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x07\x65ncoder\x18\x02 \x01(\tH\x00\x12\x19\n\x0f\x65lectronic_lock\x18\x03 \x01(\tH\x00\x12\x14\n\ncontroller\x18\x04 \x01(\tH\x00\x42\x08\n\x06\x64\x65vice\"\x17\n\x15\x45ncodeCardKeyResponse\"\x17\n\x15\x45ncodeCardKeyMetadata\"#\n\x13\x41ssignAppKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"#\n\x13\x43\x61ncelAppKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"(\n\x18\x43omputeAppKeyDataRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\")\n\x19\x43omputeAppKeyDataResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"&\n\x16\x41ssignWalletKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"b\n\x17\x41ssignWalletKeyResponse\x12\x33\n\nwallet_key\x18\x01 \x01(\x0b\x32\x1f.salto.nebula.user.v1.WalletKey\x12\x12\n\naccess_uri\x18\x02 \x01(\t\"&\n\x16\x43\x61ncelWalletKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"N\n\x17\x43\x61ncelWalletKeyResponse\x12\x33\n\nwallet_key\x18\x01 \x01(\x0b\x32\x1f.salto.nebula.user.v1.WalletKey\"%\n\x15\x41ssignPasscodeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"Y\n\x16\x41ssignPasscodeResponse\x12\x30\n\x08passcode\x18\x01 \x01(\x0b\x32\x1e.salto.nebula.user.v1.Passcode\x12\r\n\x05value\x18\x02 \x01(\t\"%\n\x15\x43\x61ncelPasscodeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"J\n\x16\x43\x61ncelPasscodeResponse\x12\x30\n\x08passcode\x18\x01 \x01(\x0b\x32\x1e.salto.nebula.user.v1.Passcode2\xa1\x11\n\x0bUserService\x12Q\n\nCreateUser\x12\'.salto.nebula.user.v1.CreateUserRequest\x1a\x1a.salto.nebula.user.v1.User\x12K\n\x07GetUser\x12$.salto.nebula.user.v1.GetUserRequest\x1a\x1a.salto.nebula.user.v1.User\x12\\\n\tListUsers\x12&.salto.nebula.user.v1.ListUsersRequest\x1a\'.salto.nebula.user.v1.ListUsersResponse\x12Q\n\nUpdateUser\x12\'.salto.nebula.user.v1.UpdateUserRequest\x1a\x1a.salto.nebula.user.v1.User\x12M\n\nDeleteUser\x12\'.salto.nebula.user.v1.DeleteUserRequest\x1a\x16.google.protobuf.Empty\x12\\\n\tBlockUser\x12&.salto.nebula.user.v1.BlockUserRequest\x1a\'.salto.nebula.user.v1.BlockUserResponse\x12\x62\n\x0bUnblockUser\x12(.salto.nebula.user.v1.UnblockUserRequest\x1a).salto.nebula.user.v1.UnblockUserResponse\x12r\n\x15\x43reateUserAccessRight\x12\x32.salto.nebula.user.v1.CreateUserAccessRightRequest\x1a%.salto.nebula.user.v1.UserAccessRight\x12l\n\x12GetUserAccessRight\x12/.salto.nebula.user.v1.GetUserAccessRightRequest\x1a%.salto.nebula.user.v1.UserAccessRight\x12}\n\x14ListUserAccessRights\x12\x31.salto.nebula.user.v1.ListUserAccessRightsRequest\x1a\x32.salto.nebula.user.v1.ListUserAccessRightsResponse\x12r\n\x15UpdateUserAccessRight\x12\x32.salto.nebula.user.v1.UpdateUserAccessRightRequest\x1a%.salto.nebula.user.v1.UserAccessRight\x12\x63\n\x15\x44\x65leteUserAccessRight\x12\x32.salto.nebula.user.v1.DeleteUserAccessRightRequest\x1a\x16.google.protobuf.Empty\x12Z\n\rAssignCardKey\x12*.salto.nebula.user.v1.AssignCardKeyRequest\x1a\x1d.salto.nebula.user.v1.CardKey\x12Z\n\rCancelCardKey\x12*.salto.nebula.user.v1.CancelCardKeyRequest\x1a\x1d.salto.nebula.user.v1.CardKey\x12\\\n\rEncodeCardKey\x12*.salto.nebula.user.v1.EncodeCardKeyRequest\x1a\x1f.salto.longrunning.v1.Operation\x12W\n\x0c\x41ssignAppKey\x12).salto.nebula.user.v1.AssignAppKeyRequest\x1a\x1c.salto.nebula.user.v1.AppKey\x12W\n\x0c\x43\x61ncelAppKey\x12).salto.nebula.user.v1.CancelAppKeyRequest\x1a\x1c.salto.nebula.user.v1.AppKey\x12t\n\x11\x43omputeAppKeyData\x12..salto.nebula.user.v1.ComputeAppKeyDataRequest\x1a/.salto.nebula.user.v1.ComputeAppKeyDataResponse\x12n\n\x0f\x41ssignWalletKey\x12,.salto.nebula.user.v1.AssignWalletKeyRequest\x1a-.salto.nebula.user.v1.AssignWalletKeyResponse\x12n\n\x0f\x43\x61ncelWalletKey\x12,.salto.nebula.user.v1.CancelWalletKeyRequest\x1a-.salto.nebula.user.v1.CancelWalletKeyResponse\x12k\n\x0e\x41ssignPasscode\x12+.salto.nebula.user.v1.AssignPasscodeRequest\x1a,.salto.nebula.user.v1.AssignPasscodeResponse\x12k\n\x0e\x43\x61ncelPasscode\x12+.salto.nebula.user.v1.CancelPasscodeRequest\x1a,.salto.nebula.user.v1.CancelPasscodeResponseB\xc8\x01\n\x1c\x63om.saltoapis.nebula.user.v1B\tUserProtoP\x01Z>github.com/saltoapis-internal/saltoapis-go/nebula/user/v1;user\xaa\x02\x18Saltoapis.Nebula.User.V1\xca\x02\x18Saltoapis\\Nebula\\User\\V1\xe2\x02$GPBMetadata\\Saltoapis\\Nebula\\User\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'salto.nebula.user.v1.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.saltoapis.nebula.user.v1B\tUserProtoP\001Z>github.com/saltoapis-internal/saltoapis-go/nebula/user/v1;user\252\002\030Saltoapis.Nebula.User.V1\312\002\030Saltoapis\\Nebula\\User\\V1\342\002$GPBMetadata\\Saltoapis\\Nebula\\User\\V1'
  _globals['_USER']._serialized_start=226
  _globals['_USER']._serialized_end=757
  _globals['_USERACCESSRIGHT']._serialized_start=760
  _globals['_USERACCESSRIGHT']._serialized_end=941
  _globals['_CARDKEY']._serialized_start=944
  _globals['_CARDKEY']._serialized_end=1138
  _globals['_CARDKEY_STATE']._serialized_start=1054
  _globals['_CARDKEY_STATE']._serialized_end=1127
  _globals['_APPKEY']._serialized_start=1141
  _globals['_APPKEY']._serialized_end=1307
  _globals['_APPKEY_STATE']._serialized_start=1054
  _globals['_APPKEY_STATE']._serialized_end=1127
  _globals['_WALLETKEY']._serialized_start=1310
  _globals['_WALLETKEY']._serialized_end=1482
  _globals['_WALLETKEY_STATE']._serialized_start=1054
  _globals['_WALLETKEY_STATE']._serialized_end=1127
  _globals['_PASSCODE']._serialized_start=1485
  _globals['_PASSCODE']._serialized_end=1624
  _globals['_PASSCODE_STATE']._serialized_start=1564
  _globals['_PASSCODE_STATE']._serialized_end=1624
  _globals['_CREATEUSERREQUEST']._serialized_start=1626
  _globals['_CREATEUSERREQUEST']._serialized_end=1737
  _globals['_GETUSERREQUEST']._serialized_start=1739
  _globals['_GETUSERREQUEST']._serialized_end=1769
  _globals['_LISTUSERSREQUEST']._serialized_start=1771
  _globals['_LISTUSERSREQUEST']._serialized_end=1878
  _globals['_LISTUSERSRESPONSE']._serialized_start=1880
  _globals['_LISTUSERSRESPONSE']._serialized_end=1987
  _globals['_UPDATEUSERREQUEST']._serialized_start=1989
  _globals['_UPDATEUSERREQUEST']._serialized_end=2099
  _globals['_DELETEUSERREQUEST']._serialized_start=2101
  _globals['_DELETEUSERREQUEST']._serialized_end=2134
  _globals['_BLOCKUSERREQUEST']._serialized_start=2136
  _globals['_BLOCKUSERREQUEST']._serialized_end=2168
  _globals['_BLOCKUSERRESPONSE']._serialized_start=2170
  _globals['_BLOCKUSERRESPONSE']._serialized_end=2189
  _globals['_UNBLOCKUSERREQUEST']._serialized_start=2191
  _globals['_UNBLOCKUSERREQUEST']._serialized_end=2225
  _globals['_UNBLOCKUSERRESPONSE']._serialized_start=2227
  _globals['_UNBLOCKUSERRESPONSE']._serialized_end=2248
  _globals['_CREATEUSERACCESSRIGHTREQUEST']._serialized_start=2250
  _globals['_CREATEUSERACCESSRIGHTREQUEST']._serialized_end=2362
  _globals['_GETUSERACCESSRIGHTREQUEST']._serialized_start=2364
  _globals['_GETUSERACCESSRIGHTREQUEST']._serialized_end=2405
  _globals['_LISTUSERACCESSRIGHTSREQUEST']._serialized_start=2407
  _globals['_LISTUSERACCESSRIGHTSREQUEST']._serialized_end=2525
  _globals['_LISTUSERACCESSRIGHTSRESPONSE']._serialized_start=2527
  _globals['_LISTUSERACCESSRIGHTSRESPONSE']._serialized_end=2649
  _globals['_UPDATEUSERACCESSRIGHTREQUEST']._serialized_start=2652
  _globals['_UPDATEUSERACCESSRIGHTREQUEST']._serialized_end=2797
  _globals['_DELETEUSERACCESSRIGHTREQUEST']._serialized_start=2799
  _globals['_DELETEUSERACCESSRIGHTREQUEST']._serialized_end=2843
  _globals['_ASSIGNCARDKEYREQUEST']._serialized_start=2845
  _globals['_ASSIGNCARDKEYREQUEST']._serialized_end=2907
  _globals['_CANCELCARDKEYREQUEST']._serialized_start=2909
  _globals['_CANCELCARDKEYREQUEST']._serialized_end=2945
  _globals['_ENCODECARDKEYREQUEST']._serialized_start=2947
  _globals['_ENCODECARDKEYREQUEST']._serialized_end=3061
  _globals['_ENCODECARDKEYRESPONSE']._serialized_start=3063
  _globals['_ENCODECARDKEYRESPONSE']._serialized_end=3086
  _globals['_ENCODECARDKEYMETADATA']._serialized_start=3088
  _globals['_ENCODECARDKEYMETADATA']._serialized_end=3111
  _globals['_ASSIGNAPPKEYREQUEST']._serialized_start=3113
  _globals['_ASSIGNAPPKEYREQUEST']._serialized_end=3148
  _globals['_CANCELAPPKEYREQUEST']._serialized_start=3150
  _globals['_CANCELAPPKEYREQUEST']._serialized_end=3185
  _globals['_COMPUTEAPPKEYDATAREQUEST']._serialized_start=3187
  _globals['_COMPUTEAPPKEYDATAREQUEST']._serialized_end=3227
  _globals['_COMPUTEAPPKEYDATARESPONSE']._serialized_start=3229
  _globals['_COMPUTEAPPKEYDATARESPONSE']._serialized_end=3270
  _globals['_ASSIGNWALLETKEYREQUEST']._serialized_start=3272
  _globals['_ASSIGNWALLETKEYREQUEST']._serialized_end=3310
  _globals['_ASSIGNWALLETKEYRESPONSE']._serialized_start=3312
  _globals['_ASSIGNWALLETKEYRESPONSE']._serialized_end=3410
  _globals['_CANCELWALLETKEYREQUEST']._serialized_start=3412
  _globals['_CANCELWALLETKEYREQUEST']._serialized_end=3450
  _globals['_CANCELWALLETKEYRESPONSE']._serialized_start=3452
  _globals['_CANCELWALLETKEYRESPONSE']._serialized_end=3530
  _globals['_ASSIGNPASSCODEREQUEST']._serialized_start=3532
  _globals['_ASSIGNPASSCODEREQUEST']._serialized_end=3569
  _globals['_ASSIGNPASSCODERESPONSE']._serialized_start=3571
  _globals['_ASSIGNPASSCODERESPONSE']._serialized_end=3660
  _globals['_CANCELPASSCODEREQUEST']._serialized_start=3662
  _globals['_CANCELPASSCODEREQUEST']._serialized_end=3699
  _globals['_CANCELPASSCODERESPONSE']._serialized_start=3701
  _globals['_CANCELPASSCODERESPONSE']._serialized_end=3775
  _globals['_USERSERVICE']._serialized_start=3778
  _globals['_USERSERVICE']._serialized_end=5987
# @@protoc_insertion_point(module_scope)
