from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from saltoapis.longrunning.v1 import operation_pb2 as _operation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Gateway(_message.Message):
    __slots__ = ("name", "display_name", "device_id", "initialized", "connected", "ethernet_settings", "wifi_settings")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    WIFI_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    device_id: str
    initialized: bool
    connected: bool
    ethernet_settings: EthernetSettings
    wifi_settings: WifiSettings
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., device_id: _Optional[str] = ..., initialized: bool = ..., connected: bool = ..., ethernet_settings: _Optional[_Union[EthernetSettings, _Mapping]] = ..., wifi_settings: _Optional[_Union[WifiSettings, _Mapping]] = ...) -> None: ...

class EthernetSettings(_message.Message):
    __slots__ = ("ipv4_settings", "dns_settings")
    IPV4_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DNS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ipv4_settings: IPv4Settings
    dns_settings: DNSSettings
    def __init__(self, ipv4_settings: _Optional[_Union[IPv4Settings, _Mapping]] = ..., dns_settings: _Optional[_Union[DNSSettings, _Mapping]] = ...) -> None: ...

class WifiSettings(_message.Message):
    __slots__ = ("ipv4_settings", "dns_settings", "ssid", "password")
    IPV4_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DNS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ipv4_settings: IPv4Settings
    dns_settings: DNSSettings
    ssid: str
    password: str
    def __init__(self, ipv4_settings: _Optional[_Union[IPv4Settings, _Mapping]] = ..., dns_settings: _Optional[_Union[DNSSettings, _Mapping]] = ..., ssid: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class IPv4Settings(_message.Message):
    __slots__ = ("ip_address", "mask", "router_address")
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    ROUTER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    mask: str
    router_address: str
    def __init__(self, ip_address: _Optional[str] = ..., mask: _Optional[str] = ..., router_address: _Optional[str] = ...) -> None: ...

class DNSSettings(_message.Message):
    __slots__ = ("dns_addresses",)
    DNS_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    dns_addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dns_addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateGatewayRequest(_message.Message):
    __slots__ = ("parent", "gateway_id", "gateway")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    gateway_id: str
    gateway: Gateway
    def __init__(self, parent: _Optional[str] = ..., gateway_id: _Optional[str] = ..., gateway: _Optional[_Union[Gateway, _Mapping]] = ...) -> None: ...

class GetGatewayRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListGatewaysRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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

class ListGatewaysResponse(_message.Message):
    __slots__ = ("gateways", "next_page_token")
    GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    gateways: _containers.RepeatedCompositeFieldContainer[Gateway]
    next_page_token: str
    def __init__(self, gateways: _Optional[_Iterable[_Union[Gateway, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateGatewayRequest(_message.Message):
    __slots__ = ("gateway", "update_mask")
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    gateway: Gateway
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, gateway: _Optional[_Union[Gateway, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteGatewayRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BindGatewayRequest(_message.Message):
    __slots__ = ("name", "device_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_id: str
    def __init__(self, name: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class BindGatewayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnbindGatewayRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class UnbindGatewayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeGatewayRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InitializeGatewayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeGatewayMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigureGatewayRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ConfigureGatewayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigureGatewayMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetGatewayRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResetGatewayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetGatewayMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateGatewayFirmwareRequest(_message.Message):
    __slots__ = ("gateway",)
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    gateway: str
    def __init__(self, gateway: _Optional[str] = ...) -> None: ...

class UpdateGatewayFirmwareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateGatewayFirmwareMetadata(_message.Message):
    __slots__ = ("progress_percent",)
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    def __init__(self, progress_percent: _Optional[int] = ...) -> None: ...

class GenerateAuthorizationTokenRequest(_message.Message):
    __slots__ = ("gateway",)
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    gateway: str
    def __init__(self, gateway: _Optional[str] = ...) -> None: ...

class GenerateAuthorizationTokenResponse(_message.Message):
    __slots__ = ("authorization_token",)
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorization_token: bytes
    def __init__(self, authorization_token: _Optional[bytes] = ...) -> None: ...
