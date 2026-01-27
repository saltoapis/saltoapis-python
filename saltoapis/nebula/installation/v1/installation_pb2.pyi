import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from saltoapis.type import color_pb2 as _color_pb2
from saltoapis.type import color_pb2 as _color_pb2
from saltoapis.type import date_pb2 as _date_pb2
from saltoapis.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Installation(_message.Message):
    __slots__ = ()
    class DigitalKeyArt(_message.Message):
        __slots__ = ()
        BACKGROUND_IMAGE_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
        TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
        background_image: str
        background_image_uri: str
        text_color: _color_pb2.Color
        def __init__(self, background_image: _Optional[str] = ..., background_image_uri: _Optional[str] = ..., text_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ...) -> None: ...
    class TransferOwnershipState(_message.Message):
        __slots__ = ()
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
        email: str
        expire_time: _timestamp_pb2.Timestamp
        def __init__(self, email: _Optional[str] = ..., expire_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class PartnerInfo(_message.Message):
        __slots__ = ()
        PARTNER_ID_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
        partner_id: str
        currency_code: str
        def __init__(self, partner_id: _Optional[str] = ..., currency_code: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    PHOTO_URI_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_KEY_ART_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OWNERSHIP_STATE_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    PARTNER_INFO_FIELD_NUMBER: _ClassVar[int]
    BLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    KEY_RENEWAL_DURATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    photo: str
    photo_uri: str
    address: str
    time_zone: str
    digital_key_art: Installation.DigitalKeyArt
    transfer_ownership_state: Installation.TransferOwnershipState
    delete_time: _timestamp_pb2.Timestamp
    partner_info: Installation.PartnerInfo
    block_time: _timestamp_pb2.Timestamp
    key_renewal_duration: _duration_pb2.Duration
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., photo: _Optional[str] = ..., photo_uri: _Optional[str] = ..., address: _Optional[str] = ..., time_zone: _Optional[str] = ..., digital_key_art: _Optional[_Union[Installation.DigitalKeyArt, _Mapping]] = ..., transfer_ownership_state: _Optional[_Union[Installation.TransferOwnershipState, _Mapping]] = ..., delete_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., partner_info: _Optional[_Union[Installation.PartnerInfo, _Mapping]] = ..., block_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., key_renewal_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class Subscription(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRIAL_END_TIME_FIELD_NUMBER: _ClassVar[int]
    BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    COUPONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    trial_end_time: _timestamp_pb2.Timestamp
    billing_info: BillingInfo
    payment_method: PaymentMethod
    coupons: _containers.RepeatedCompositeFieldContainer[Coupon]
    def __init__(self, name: _Optional[str] = ..., trial_end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., billing_info: _Optional[_Union[BillingInfo, _Mapping]] = ..., payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ..., coupons: _Optional[_Iterable[_Union[Coupon, _Mapping]]] = ...) -> None: ...

class BillingInfo(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_CODE_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    VAT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    name: str
    company: str
    address: _containers.RepeatedScalarFieldContainer[str]
    region_code: str
    city: str
    state_code: str
    zip: str
    vat_number: str
    def __init__(self, name: _Optional[str] = ..., company: _Optional[str] = ..., address: _Optional[_Iterable[str]] = ..., region_code: _Optional[str] = ..., city: _Optional[str] = ..., state_code: _Optional[str] = ..., zip: _Optional[str] = ..., vat_number: _Optional[str] = ...) -> None: ...

class PaymentMethod(_message.Message):
    __slots__ = ()
    class Card(_message.Message):
        __slots__ = ()
        EXPIRE_DATE_FIELD_NUMBER: _ClassVar[int]
        LAST_FOUR_FIELD_NUMBER: _ClassVar[int]
        BRAND_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
        expire_date: _date_pb2.Date
        last_four: str
        brand: str
        payment_authorization: str
        def __init__(self, expire_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., last_four: _Optional[str] = ..., brand: _Optional[str] = ..., payment_authorization: _Optional[str] = ...) -> None: ...
    class DirectDebit(_message.Message):
        __slots__ = ()
        class SEPA(_message.Message):
            __slots__ = ()
            LAST_FOUR_FIELD_NUMBER: _ClassVar[int]
            ACCOUNT_HOLDER_FIELD_NUMBER: _ClassVar[int]
            IBAN_FIELD_NUMBER: _ClassVar[int]
            last_four: str
            account_holder: str
            iban: str
            def __init__(self, last_four: _Optional[str] = ..., account_holder: _Optional[str] = ..., iban: _Optional[str] = ...) -> None: ...
        SEPA_FIELD_NUMBER: _ClassVar[int]
        sepa: PaymentMethod.DirectDebit.SEPA
        def __init__(self, sepa: _Optional[_Union[PaymentMethod.DirectDebit.SEPA, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    DIRECT_DEBIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    card: PaymentMethod.Card
    direct_debit: PaymentMethod.DirectDebit
    def __init__(self, name: _Optional[str] = ..., card: _Optional[_Union[PaymentMethod.Card, _Mapping]] = ..., direct_debit: _Optional[_Union[PaymentMethod.DirectDebit, _Mapping]] = ...) -> None: ...

class PaymentAuthorization(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Coupon(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Invoice(_message.Message):
    __slots__ = ()
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Invoice.State]
        UNPAID: _ClassVar[Invoice.State]
        PAID: _ClassVar[Invoice.State]
    STATE_UNSPECIFIED: Invoice.State
    UNPAID: Invoice.State
    PAID: Invoice.State
    class LineItem(_message.Message):
        __slots__ = ()
        ID_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        id: str
        quantity: int
        price: int
        def __init__(self, id: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    line_items: _containers.RepeatedCompositeFieldContainer[Invoice.LineItem]
    total: int
    state: Invoice.State
    def __init__(self, name: _Optional[str] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., line_items: _Optional[_Iterable[_Union[Invoice.LineItem, _Mapping]]] = ..., total: _Optional[int] = ..., state: _Optional[_Union[Invoice.State, str]] = ...) -> None: ...

class Policy(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    member: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., member: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateInstallationRequest(_message.Message):
    __slots__ = ()
    INSTALLATION_ID_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    installation_id: str
    installation: Installation
    validate_only: bool
    def __init__(self, installation_id: _Optional[str] = ..., installation: _Optional[_Union[Installation, _Mapping]] = ..., validate_only: _Optional[bool] = ...) -> None: ...

class GetInstallationRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListInstallationsRequest(_message.Message):
    __slots__ = ()
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str
    order_by: str
    show_deleted: bool
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., show_deleted: _Optional[bool] = ...) -> None: ...

class ListInstallationsResponse(_message.Message):
    __slots__ = ()
    INSTALLATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    installations: _containers.RepeatedCompositeFieldContainer[Installation]
    next_page_token: str
    def __init__(self, installations: _Optional[_Iterable[_Union[Installation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateInstallationRequest(_message.Message):
    __slots__ = ()
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    installation: Installation
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, installation: _Optional[_Union[Installation, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteInstallationRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    DELAY_HOURS_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    delay_hours: int
    def __init__(self, name: _Optional[str] = ..., validate_only: _Optional[bool] = ..., delay_hours: _Optional[int] = ...) -> None: ...

class UndeleteInstallationRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreatePolicyRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    policy_id: str
    policy: Policy
    def __init__(self, parent: _Optional[str] = ..., policy_id: _Optional[str] = ..., policy: _Optional[_Union[Policy, _Mapping]] = ...) -> None: ...

class GetPolicyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListPoliciesRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListPoliciesResponse(_message.Message):
    __slots__ = ()
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[Policy]
    next_page_token: str
    def __init__(self, policies: _Optional[_Iterable[_Union[Policy, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdatePolicyRequest(_message.Message):
    __slots__ = ()
    POLICY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    policy: Policy
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, policy: _Optional[_Union[Policy, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeletePolicyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class TestPermissionsRequest(_message.Message):
    __slots__ = ()
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    installation: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, installation: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class TestPermissionsResponse(_message.Message):
    __slots__ = ()
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class TransferInstallationOwnershipRequest(_message.Message):
    __slots__ = ()
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    installation: str
    email: str
    def __init__(self, installation: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class TransferInstallationOwnershipResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AcceptInstallationOwnershipRequest(_message.Message):
    __slots__ = ()
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    installation: str
    billing_info: BillingInfo
    def __init__(self, installation: _Optional[str] = ..., billing_info: _Optional[_Union[BillingInfo, _Mapping]] = ...) -> None: ...

class AcceptInstallationOwnershipResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSubscriptionRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateBillingInfoRequest(_message.Message):
    __slots__ = ()
    BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    billing_info: BillingInfo
    def __init__(self, billing_info: _Optional[_Union[BillingInfo, _Mapping]] = ...) -> None: ...

class UpdatePaymentMethodRequest(_message.Message):
    __slots__ = ()
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...

class UpdateCardRequest(_message.Message):
    __slots__ = ()
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    payment_method: str
    token: str
    def __init__(self, payment_method: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class UpdateCardResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreatePaymentAuthorizationRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    payment_authorization: PaymentAuthorization
    def __init__(self, parent: _Optional[str] = ..., payment_authorization: _Optional[_Union[PaymentAuthorization, _Mapping]] = ...) -> None: ...

class ListInvoicesRequest(_message.Message):
    __slots__ = ()
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListInvoicesResponse(_message.Message):
    __slots__ = ()
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    invoices: _containers.RepeatedCompositeFieldContainer[Invoice]
    def __init__(self, invoices: _Optional[_Iterable[_Union[Invoice, _Mapping]]] = ...) -> None: ...

class ApplyCouponRequest(_message.Message):
    __slots__ = ()
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COUPON_FIELD_NUMBER: _ClassVar[int]
    subscription: str
    coupon: str
    def __init__(self, subscription: _Optional[str] = ..., coupon: _Optional[str] = ...) -> None: ...

class ApplyCouponResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnapplyCouponRequest(_message.Message):
    __slots__ = ()
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COUPON_FIELD_NUMBER: _ClassVar[int]
    subscription: str
    coupon: str
    def __init__(self, subscription: _Optional[str] = ..., coupon: _Optional[str] = ...) -> None: ...

class UnapplyCouponResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GenerateAuthorizationTokenRequest(_message.Message):
    __slots__ = ()
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    installation: str
    def __init__(self, installation: _Optional[str] = ...) -> None: ...

class GenerateAuthorizationTokenResponse(_message.Message):
    __slots__ = ()
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorization_token: bytes
    def __init__(self, authorization_token: _Optional[bytes] = ...) -> None: ...
