# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: salto/nebula/installation/v1/installation.proto
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
    'salto/nebula/installation/v1/installation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from saltoapis.type import color_pb2 as salto_dot_type_dot_color__pb2
from saltoapis.type import color_pb2 as salto_dot_type_dot_color__pb2
from saltoapis.type import date_pb2 as salto_dot_type_dot_date__pb2
from saltoapis.type import date_pb2 as salto_dot_type_dot_date__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/salto/nebula/installation/v1/installation.proto\x12\x1csalto.nebula.installation.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16salto/type/color.proto\x1a\x15salto/type/date.proto\"\x84\x07\n\x0cInstallation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x12\n\x05photo\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x11\n\tphoto_uri\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\x12\x11\n\ttime_zone\x18\x06 \x01(\t\x12Q\n\x0f\x64igital_key_art\x18\x07 \x01(\x0b\x32\x38.salto.nebula.installation.v1.Installation.DigitalKeyArt\x12\x63\n\x18transfer_ownership_state\x18\x08 \x01(\x0b\x32\x41.salto.nebula.installation.v1.Installation.TransferOwnershipState\x12/\n\x0b\x64\x65lete_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12Q\n\x0cpartner_info\x18\t \x01(\x0b\x32\x36.salto.nebula.installation.v1.Installation.PartnerInfoH\x01\x88\x01\x01\x12\x33\n\nblock_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x02\x88\x01\x01\x12\x37\n\x14key_renewal_duration\x18\n \x01(\x0b\x32\x19.google.protobuf.Duration\x1a\x9c\x01\n\rDigitalKeyArt\x12\x1d\n\x10\x62\x61\x63kground_image\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x14\x62\x61\x63kground_image_uri\x18\x02 \x01(\t\x12*\n\ntext_color\x18\x03 \x01(\x0b\x32\x11.salto.type.ColorH\x01\x88\x01\x01\x42\x13\n\x11_background_imageB\r\n\x0b_text_color\x1aX\n\x16TransferOwnershipState\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12/\n\x0b\x65xpire_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x38\n\x0bPartnerInfo\x12\x12\n\npartner_id\x18\x01 \x01(\t\x12\x15\n\rcurrency_code\x18\x02 \x01(\tB\x08\n\x06_photoB\x0f\n\r_partner_infoB\r\n\x0b_block_time\"\xa5\x02\n\x0cSubscription\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x37\n\x0etrial_end_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x12?\n\x0c\x62illing_info\x18\x04 \x01(\x0b\x32).salto.nebula.installation.v1.BillingInfo\x12\x43\n\x0epayment_method\x18\x05 \x01(\x0b\x32+.salto.nebula.installation.v1.PaymentMethod\x12\x35\n\x07\x63oupons\x18\x06 \x03(\x0b\x32$.salto.nebula.installation.v1.CouponB\x11\n\x0f_trial_end_time\"\xbd\x01\n\x0b\x42illingInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x03(\t\x12\x13\n\x0bregion_code\x18\x04 \x01(\t\x12\x0c\n\x04\x63ity\x18\x05 \x01(\t\x12\x17\n\nstate_code\x18\x06 \x01(\tH\x00\x88\x01\x01\x12\x0b\n\x03zip\x18\x07 \x01(\t\x12\x17\n\nvat_number\x18\x08 \x01(\tH\x01\x88\x01\x01\x42\r\n\x0b_state_codeB\r\n\x0b_vat_number\"\xb4\x03\n\rPaymentMethod\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x04\x63\x61rd\x18\x02 \x01(\x0b\x32\x30.salto.nebula.installation.v1.PaymentMethod.CardH\x00\x12O\n\x0c\x64irect_debit\x18\x03 \x01(\x0b\x32\x37.salto.nebula.installation.v1.PaymentMethod.DirectDebitH\x00\x1aO\n\x04\x43\x61rd\x12%\n\x0b\x65xpire_date\x18\x01 \x01(\x0b\x32\x10.salto.type.Date\x12\x11\n\tlast_four\x18\x02 \x01(\t\x12\r\n\x05\x62rand\x18\x03 \x01(\t\x1a\xa6\x01\n\x0b\x44irectDebit\x12L\n\x04sepa\x18\x01 \x01(\x0b\x32<.salto.nebula.installation.v1.PaymentMethod.DirectDebit.SEPAH\x00\x1a?\n\x04SEPA\x12\x11\n\tlast_four\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_holder\x18\x02 \x01(\t\x12\x0c\n\x04iban\x18\x03 \x01(\tB\x08\n\x06schemeB\x08\n\x06method\"\x16\n\x06\x43oupon\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xf3\x02\n\x07Invoice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\nline_items\x18\x04 \x03(\x0b\x32..salto.nebula.installation.v1.Invoice.LineItem\x12\r\n\x05total\x18\x05 \x01(\x03\x12:\n\x05state\x18\x06 \x01(\x0e\x32+.salto.nebula.installation.v1.Invoice.State\x1a\x37\n\x08LineItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\r\n\x05price\x18\x03 \x01(\x03\"4\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06UNPAID\x10\x01\x12\x08\n\x04PAID\x10\x02\"5\n\x06Policy\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06member\x18\x02 \x01(\t\x12\r\n\x05roles\x18\x03 \x03(\t\"\xbd\x01\n\x19\x43reateInstallationRequest\x12\x1c\n\x0finstallation_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12@\n\x0cinstallation\x18\x02 \x01(\x0b\x32*.salto.nebula.installation.v1.Installation\x12\x1a\n\rvalidate_only\x18\x05 \x01(\x08H\x01\x88\x01\x01\x42\x12\n\x10_installation_idB\x10\n\x0e_validate_only\"&\n\x16GetInstallationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"y\n\x18ListInstallationsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cshow_deleted\x18\x05 \x01(\x08\"w\n\x19ListInstallationsResponse\x12\x41\n\rinstallations\x18\x01 \x03(\x0b\x32*.salto.nebula.installation.v1.Installation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x8e\x01\n\x19UpdateInstallationRequest\x12@\n\x0cinstallation\x18\x01 \x01(\x0b\x32*.salto.nebula.installation.v1.Installation\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x81\x01\n\x19\x44\x65leteInstallationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\rvalidate_only\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65lay_hours\x18\x03 \x01(\x05H\x01\x88\x01\x01\x42\x10\n\x0e_validate_onlyB\x0e\n\x0c_delay_hours\"+\n\x1bUndeleteInstallationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"n\n\x13\x43reatePolicyRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpolicy_id\x18\x02 \x01(\t\x12\x34\n\x06policy\x18\x03 \x01(\x0b\x32$.salto.nebula.installation.v1.Policy\" \n\x10GetPolicyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"n\n\x13ListPoliciesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"g\n\x14ListPoliciesResponse\x12\x36\n\x08policies\x18\x01 \x03(\x0b\x32$.salto.nebula.installation.v1.Policy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"|\n\x13UpdatePolicyRequest\x12\x34\n\x06policy\x18\x01 \x01(\x0b\x32$.salto.nebula.installation.v1.Policy\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"#\n\x13\x44\x65letePolicyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"C\n\x16TestPermissionsRequest\x12\x14\n\x0cinstallation\x18\x01 \x01(\t\x12\x13\n\x0bpermissions\x18\x02 \x03(\t\".\n\x17TestPermissionsResponse\x12\x13\n\x0bpermissions\x18\x01 \x03(\t\"K\n$TransferInstallationOwnershipRequest\x12\x14\n\x0cinstallation\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"\'\n%TransferInstallationOwnershipResponse\"\x91\x01\n\"AcceptInstallationOwnershipRequest\x12\x14\n\x0cinstallation\x18\x01 \x01(\t\x12\x44\n\x0c\x62illing_info\x18\x02 \x01(\x0b\x32).salto.nebula.installation.v1.BillingInfoH\x00\x88\x01\x01\x42\x0f\n\r_billing_info\"%\n#AcceptInstallationOwnershipResponse\"&\n\x16GetSubscriptionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"[\n\x18UpdateBillingInfoRequest\x12?\n\x0c\x62illing_info\x18\x01 \x01(\x0b\x32).salto.nebula.installation.v1.BillingInfo\"a\n\x1aUpdatePaymentMethodRequest\x12\x43\n\x0epayment_method\x18\x01 \x01(\x0b\x32+.salto.nebula.installation.v1.PaymentMethod\":\n\x11UpdateCardRequest\x12\x16\n\x0epayment_method\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"\x14\n\x12UpdateCardResponse\"%\n\x13ListInvoicesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\"O\n\x14ListInvoicesResponse\x12\x37\n\x08invoices\x18\x01 \x03(\x0b\x32%.salto.nebula.installation.v1.Invoice\":\n\x12\x41pplyCouponRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t\x12\x0e\n\x06\x63oupon\x18\x02 \x01(\t\"\x15\n\x13\x41pplyCouponResponse\"<\n\x14UnapplyCouponRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t\x12\x0e\n\x06\x63oupon\x18\x02 \x01(\t\"\x17\n\x15UnapplyCouponResponse2\x99\x14\n\x13InstallationService\x12y\n\x12\x43reateInstallation\x12\x37.salto.nebula.installation.v1.CreateInstallationRequest\x1a*.salto.nebula.installation.v1.Installation\x12s\n\x0fGetInstallation\x12\x34.salto.nebula.installation.v1.GetInstallationRequest\x1a*.salto.nebula.installation.v1.Installation\x12\x84\x01\n\x11ListInstallations\x12\x36.salto.nebula.installation.v1.ListInstallationsRequest\x1a\x37.salto.nebula.installation.v1.ListInstallationsResponse\x12y\n\x12UpdateInstallation\x12\x37.salto.nebula.installation.v1.UpdateInstallationRequest\x1a*.salto.nebula.installation.v1.Installation\x12y\n\x12\x44\x65leteInstallation\x12\x37.salto.nebula.installation.v1.DeleteInstallationRequest\x1a*.salto.nebula.installation.v1.Installation\x12}\n\x14UndeleteInstallation\x12\x39.salto.nebula.installation.v1.UndeleteInstallationRequest\x1a*.salto.nebula.installation.v1.Installation\x12g\n\x0c\x43reatePolicy\x12\x31.salto.nebula.installation.v1.CreatePolicyRequest\x1a$.salto.nebula.installation.v1.Policy\x12\x61\n\tGetPolicy\x12..salto.nebula.installation.v1.GetPolicyRequest\x1a$.salto.nebula.installation.v1.Policy\x12u\n\x0cListPolicies\x12\x31.salto.nebula.installation.v1.ListPoliciesRequest\x1a\x32.salto.nebula.installation.v1.ListPoliciesResponse\x12g\n\x0cUpdatePolicy\x12\x31.salto.nebula.installation.v1.UpdatePolicyRequest\x1a$.salto.nebula.installation.v1.Policy\x12Y\n\x0c\x44\x65letePolicy\x12\x31.salto.nebula.installation.v1.DeletePolicyRequest\x1a\x16.google.protobuf.Empty\x12~\n\x0fTestPermissions\x12\x34.salto.nebula.installation.v1.TestPermissionsRequest\x1a\x35.salto.nebula.installation.v1.TestPermissionsResponse\x12\xa8\x01\n\x1dTransferInstallationOwnership\x12\x42.salto.nebula.installation.v1.TransferInstallationOwnershipRequest\x1a\x43.salto.nebula.installation.v1.TransferInstallationOwnershipResponse\x12\xa2\x01\n\x1b\x41\x63\x63\x65ptInstallationOwnership\x12@.salto.nebula.installation.v1.AcceptInstallationOwnershipRequest\x1a\x41.salto.nebula.installation.v1.AcceptInstallationOwnershipResponse\x12s\n\x0fGetSubscription\x12\x34.salto.nebula.installation.v1.GetSubscriptionRequest\x1a*.salto.nebula.installation.v1.Subscription\x12v\n\x11UpdateBillingInfo\x12\x36.salto.nebula.installation.v1.UpdateBillingInfoRequest\x1a).salto.nebula.installation.v1.BillingInfo\x12|\n\x13UpdatePaymentMethod\x12\x38.salto.nebula.installation.v1.UpdatePaymentMethodRequest\x1a+.salto.nebula.installation.v1.PaymentMethod\x12o\n\nUpdateCard\x12/.salto.nebula.installation.v1.UpdateCardRequest\x1a\x30.salto.nebula.installation.v1.UpdateCardResponse\x12u\n\x0cListInvoices\x12\x31.salto.nebula.installation.v1.ListInvoicesRequest\x1a\x32.salto.nebula.installation.v1.ListInvoicesResponse\x12r\n\x0b\x41pplyCoupon\x12\x30.salto.nebula.installation.v1.ApplyCouponRequest\x1a\x31.salto.nebula.installation.v1.ApplyCouponResponse\x12x\n\rUnapplyCoupon\x12\x32.salto.nebula.installation.v1.UnapplyCouponRequest\x1a\x33.salto.nebula.installation.v1.UnapplyCouponResponseB\x80\x02\n$com.saltoapis.nebula.installation.v1B\x11InstallationProtoP\x01ZNgithub.com/saltoapis-internal/saltoapis-go/nebula/installation/v1;installation\xaa\x02 Saltoapis.Nebula.Installation.V1\xca\x02 Saltoapis\\Nebula\\Installation\\V1\xe2\x02,GPBMetadata\\Saltoapis\\Nebula\\Installation\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'salto.nebula.installation.v1.installation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.saltoapis.nebula.installation.v1B\021InstallationProtoP\001ZNgithub.com/saltoapis-internal/saltoapis-go/nebula/installation/v1;installation\252\002 Saltoapis.Nebula.Installation.V1\312\002 Saltoapis\\Nebula\\Installation\\V1\342\002,GPBMetadata\\Saltoapis\\Nebula\\Installation\\V1'
  _globals['_INSTALLATION']._serialized_start=257
  _globals['_INSTALLATION']._serialized_end=1157
  _globals['_INSTALLATION_DIGITALKEYART']._serialized_start=811
  _globals['_INSTALLATION_DIGITALKEYART']._serialized_end=967
  _globals['_INSTALLATION_TRANSFEROWNERSHIPSTATE']._serialized_start=969
  _globals['_INSTALLATION_TRANSFEROWNERSHIPSTATE']._serialized_end=1057
  _globals['_INSTALLATION_PARTNERINFO']._serialized_start=1059
  _globals['_INSTALLATION_PARTNERINFO']._serialized_end=1115
  _globals['_SUBSCRIPTION']._serialized_start=1160
  _globals['_SUBSCRIPTION']._serialized_end=1453
  _globals['_BILLINGINFO']._serialized_start=1456
  _globals['_BILLINGINFO']._serialized_end=1645
  _globals['_PAYMENTMETHOD']._serialized_start=1648
  _globals['_PAYMENTMETHOD']._serialized_end=2084
  _globals['_PAYMENTMETHOD_CARD']._serialized_start=1826
  _globals['_PAYMENTMETHOD_CARD']._serialized_end=1905
  _globals['_PAYMENTMETHOD_DIRECTDEBIT']._serialized_start=1908
  _globals['_PAYMENTMETHOD_DIRECTDEBIT']._serialized_end=2074
  _globals['_PAYMENTMETHOD_DIRECTDEBIT_SEPA']._serialized_start=2001
  _globals['_PAYMENTMETHOD_DIRECTDEBIT_SEPA']._serialized_end=2064
  _globals['_COUPON']._serialized_start=2086
  _globals['_COUPON']._serialized_end=2108
  _globals['_INVOICE']._serialized_start=2111
  _globals['_INVOICE']._serialized_end=2482
  _globals['_INVOICE_LINEITEM']._serialized_start=2373
  _globals['_INVOICE_LINEITEM']._serialized_end=2428
  _globals['_INVOICE_STATE']._serialized_start=2430
  _globals['_INVOICE_STATE']._serialized_end=2482
  _globals['_POLICY']._serialized_start=2484
  _globals['_POLICY']._serialized_end=2537
  _globals['_CREATEINSTALLATIONREQUEST']._serialized_start=2540
  _globals['_CREATEINSTALLATIONREQUEST']._serialized_end=2729
  _globals['_GETINSTALLATIONREQUEST']._serialized_start=2731
  _globals['_GETINSTALLATIONREQUEST']._serialized_end=2769
  _globals['_LISTINSTALLATIONSREQUEST']._serialized_start=2771
  _globals['_LISTINSTALLATIONSREQUEST']._serialized_end=2892
  _globals['_LISTINSTALLATIONSRESPONSE']._serialized_start=2894
  _globals['_LISTINSTALLATIONSRESPONSE']._serialized_end=3013
  _globals['_UPDATEINSTALLATIONREQUEST']._serialized_start=3016
  _globals['_UPDATEINSTALLATIONREQUEST']._serialized_end=3158
  _globals['_DELETEINSTALLATIONREQUEST']._serialized_start=3161
  _globals['_DELETEINSTALLATIONREQUEST']._serialized_end=3290
  _globals['_UNDELETEINSTALLATIONREQUEST']._serialized_start=3292
  _globals['_UNDELETEINSTALLATIONREQUEST']._serialized_end=3335
  _globals['_CREATEPOLICYREQUEST']._serialized_start=3337
  _globals['_CREATEPOLICYREQUEST']._serialized_end=3447
  _globals['_GETPOLICYREQUEST']._serialized_start=3449
  _globals['_GETPOLICYREQUEST']._serialized_end=3481
  _globals['_LISTPOLICIESREQUEST']._serialized_start=3483
  _globals['_LISTPOLICIESREQUEST']._serialized_end=3593
  _globals['_LISTPOLICIESRESPONSE']._serialized_start=3595
  _globals['_LISTPOLICIESRESPONSE']._serialized_end=3698
  _globals['_UPDATEPOLICYREQUEST']._serialized_start=3700
  _globals['_UPDATEPOLICYREQUEST']._serialized_end=3824
  _globals['_DELETEPOLICYREQUEST']._serialized_start=3826
  _globals['_DELETEPOLICYREQUEST']._serialized_end=3861
  _globals['_TESTPERMISSIONSREQUEST']._serialized_start=3863
  _globals['_TESTPERMISSIONSREQUEST']._serialized_end=3930
  _globals['_TESTPERMISSIONSRESPONSE']._serialized_start=3932
  _globals['_TESTPERMISSIONSRESPONSE']._serialized_end=3978
  _globals['_TRANSFERINSTALLATIONOWNERSHIPREQUEST']._serialized_start=3980
  _globals['_TRANSFERINSTALLATIONOWNERSHIPREQUEST']._serialized_end=4055
  _globals['_TRANSFERINSTALLATIONOWNERSHIPRESPONSE']._serialized_start=4057
  _globals['_TRANSFERINSTALLATIONOWNERSHIPRESPONSE']._serialized_end=4096
  _globals['_ACCEPTINSTALLATIONOWNERSHIPREQUEST']._serialized_start=4099
  _globals['_ACCEPTINSTALLATIONOWNERSHIPREQUEST']._serialized_end=4244
  _globals['_ACCEPTINSTALLATIONOWNERSHIPRESPONSE']._serialized_start=4246
  _globals['_ACCEPTINSTALLATIONOWNERSHIPRESPONSE']._serialized_end=4283
  _globals['_GETSUBSCRIPTIONREQUEST']._serialized_start=4285
  _globals['_GETSUBSCRIPTIONREQUEST']._serialized_end=4323
  _globals['_UPDATEBILLINGINFOREQUEST']._serialized_start=4325
  _globals['_UPDATEBILLINGINFOREQUEST']._serialized_end=4416
  _globals['_UPDATEPAYMENTMETHODREQUEST']._serialized_start=4418
  _globals['_UPDATEPAYMENTMETHODREQUEST']._serialized_end=4515
  _globals['_UPDATECARDREQUEST']._serialized_start=4517
  _globals['_UPDATECARDREQUEST']._serialized_end=4575
  _globals['_UPDATECARDRESPONSE']._serialized_start=4577
  _globals['_UPDATECARDRESPONSE']._serialized_end=4597
  _globals['_LISTINVOICESREQUEST']._serialized_start=4599
  _globals['_LISTINVOICESREQUEST']._serialized_end=4636
  _globals['_LISTINVOICESRESPONSE']._serialized_start=4638
  _globals['_LISTINVOICESRESPONSE']._serialized_end=4717
  _globals['_APPLYCOUPONREQUEST']._serialized_start=4719
  _globals['_APPLYCOUPONREQUEST']._serialized_end=4777
  _globals['_APPLYCOUPONRESPONSE']._serialized_start=4779
  _globals['_APPLYCOUPONRESPONSE']._serialized_end=4800
  _globals['_UNAPPLYCOUPONREQUEST']._serialized_start=4802
  _globals['_UNAPPLYCOUPONREQUEST']._serialized_end=4862
  _globals['_UNAPPLYCOUPONRESPONSE']._serialized_start=4864
  _globals['_UNAPPLYCOUPONRESPONSE']._serialized_end=4887
  _globals['_INSTALLATIONSERVICE']._serialized_start=4890
  _globals['_INSTALLATIONSERVICE']._serialized_end=7475
# @@protoc_insertion_point(module_scope)
