# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.nebula.extender.v1 import extender_pb2 as salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2
from saltoapis.nebula.extender.v1 import extender_pb2 as salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2


class ExtenderServiceStub(object):
    """An extender allows the distance between the a gateway and an electronic lock
    to be extended. It forwards signals between an access point (lock) and a
    gateway. This service is responsible for managing extender resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateExtender = channel.unary_unary(
                '/salto.nebula.extender.v1.ExtenderService/CreateExtender',
                request_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.CreateExtenderRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.Extender.FromString,
                _registered_method=True)
        self.GetExtender = channel.unary_unary(
                '/salto.nebula.extender.v1.ExtenderService/GetExtender',
                request_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.GetExtenderRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.Extender.FromString,
                _registered_method=True)
        self.ListExtenders = channel.unary_unary(
                '/salto.nebula.extender.v1.ExtenderService/ListExtenders',
                request_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.ListExtendersRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.ListExtendersResponse.FromString,
                _registered_method=True)
        self.UpdateExtender = channel.unary_unary(
                '/salto.nebula.extender.v1.ExtenderService/UpdateExtender',
                request_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UpdateExtenderRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.Extender.FromString,
                _registered_method=True)
        self.DeleteExtender = channel.unary_unary(
                '/salto.nebula.extender.v1.ExtenderService/DeleteExtender',
                request_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.DeleteExtenderRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.BindExtender = channel.unary_unary(
                '/salto.nebula.extender.v1.ExtenderService/BindExtender',
                request_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.BindExtenderRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.BindExtenderResponse.FromString,
                _registered_method=True)
        self.UnbindExtender = channel.unary_unary(
                '/salto.nebula.extender.v1.ExtenderService/UnbindExtender',
                request_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UnbindExtenderRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UnbindExtenderResponse.FromString,
                _registered_method=True)
        self.UpdateExtenderFirmware = channel.unary_unary(
                '/salto.nebula.extender.v1.ExtenderService/UpdateExtenderFirmware',
                request_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UpdateExtenderFirmwareRequest.SerializeToString,
                response_deserializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ResetExtender = channel.unary_unary(
                '/salto.nebula.extender.v1.ExtenderService/ResetExtender',
                request_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.ResetExtenderRequest.SerializeToString,
                response_deserializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.GenerateFirmwareDownloadUri = channel.unary_unary(
                '/salto.nebula.extender.v1.ExtenderService/GenerateFirmwareDownloadUri',
                request_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.GenerateFirmwareDownloadUriRequest.SerializeToString,
                response_deserializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class ExtenderServiceServicer(object):
    """An extender allows the distance between the a gateway and an electronic lock
    to be extended. It forwards signals between an access point (lock) and a
    gateway. This service is responsible for managing extender resources.
    """

    def CreateExtender(self, request, context):
        """Create an extender

        Creates a new extender
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExtender(self, request, context):
        """Get an extender

        Gets an existing extender.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExtenders(self, request, context):
        """List extenders

        Returns a list of extenders that have been previously created.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateExtender(self, request, context):
        """Update an extender

        Updates an existing extender.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteExtender(self, request, context):
        """Delete an extender

        Permanently deletes an extender. This cannot be undone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BindExtender(self, request, context):
        """Bind an extender

        Binds an extender. Binding an extender assigns a device
        identifier to the extender.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnbindExtender(self, request, context):
        """Unbind an extender

        Unbinds an extender. Unbinding an extender removes the
        device identifier from the extender.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateExtenderFirmware(self, request, context):
        """Update extender firmware

        Updates an extender's firmware. SALTO provides firmware updates when
        new functionality is available or when we fix a bug.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetExtender(self, request, context):
        """Reset an extender

        Resetting a device such as an extender means returning it to its
        factory settings. Resetting is the process of removing the identity as
        well as all the associated information of an already configured device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateFirmwareDownloadUri(self, request, context):
        """Generate extender firmware download URI

        Provides the download URI for the latest firmware bundle for the
        extender. The returned URI can be used to bring the extender firmwares up
        to latest.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExtenderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateExtender': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateExtender,
                    request_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.CreateExtenderRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.Extender.SerializeToString,
            ),
            'GetExtender': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExtender,
                    request_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.GetExtenderRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.Extender.SerializeToString,
            ),
            'ListExtenders': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExtenders,
                    request_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.ListExtendersRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.ListExtendersResponse.SerializeToString,
            ),
            'UpdateExtender': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateExtender,
                    request_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UpdateExtenderRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.Extender.SerializeToString,
            ),
            'DeleteExtender': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteExtender,
                    request_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.DeleteExtenderRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'BindExtender': grpc.unary_unary_rpc_method_handler(
                    servicer.BindExtender,
                    request_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.BindExtenderRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.BindExtenderResponse.SerializeToString,
            ),
            'UnbindExtender': grpc.unary_unary_rpc_method_handler(
                    servicer.UnbindExtender,
                    request_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UnbindExtenderRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UnbindExtenderResponse.SerializeToString,
            ),
            'UpdateExtenderFirmware': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateExtenderFirmware,
                    request_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UpdateExtenderFirmwareRequest.FromString,
                    response_serializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ResetExtender': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetExtender,
                    request_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.ResetExtenderRequest.FromString,
                    response_serializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GenerateFirmwareDownloadUri': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateFirmwareDownloadUri,
                    request_deserializer=salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.GenerateFirmwareDownloadUriRequest.FromString,
                    response_serializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'salto.nebula.extender.v1.ExtenderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExtenderService(object):
    """An extender allows the distance between the a gateway and an electronic lock
    to be extended. It forwards signals between an access point (lock) and a
    gateway. This service is responsible for managing extender resources.
    """

    @staticmethod
    def CreateExtender(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/salto.nebula.extender.v1.ExtenderService/CreateExtender',
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.CreateExtenderRequest.SerializeToString,
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.Extender.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetExtender(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/salto.nebula.extender.v1.ExtenderService/GetExtender',
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.GetExtenderRequest.SerializeToString,
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.Extender.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListExtenders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/salto.nebula.extender.v1.ExtenderService/ListExtenders',
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.ListExtendersRequest.SerializeToString,
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.ListExtendersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateExtender(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/salto.nebula.extender.v1.ExtenderService/UpdateExtender',
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UpdateExtenderRequest.SerializeToString,
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.Extender.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteExtender(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/salto.nebula.extender.v1.ExtenderService/DeleteExtender',
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.DeleteExtenderRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BindExtender(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/salto.nebula.extender.v1.ExtenderService/BindExtender',
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.BindExtenderRequest.SerializeToString,
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.BindExtenderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UnbindExtender(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/salto.nebula.extender.v1.ExtenderService/UnbindExtender',
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UnbindExtenderRequest.SerializeToString,
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UnbindExtenderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateExtenderFirmware(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/salto.nebula.extender.v1.ExtenderService/UpdateExtenderFirmware',
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.UpdateExtenderFirmwareRequest.SerializeToString,
            salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ResetExtender(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/salto.nebula.extender.v1.ExtenderService/ResetExtender',
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.ResetExtenderRequest.SerializeToString,
            salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GenerateFirmwareDownloadUri(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/salto.nebula.extender.v1.ExtenderService/GenerateFirmwareDownloadUri',
            salto_dot_nebula_dot_extender_dot_v1_dot_extender__pb2.GenerateFirmwareDownloadUriRequest.SerializeToString,
            salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
