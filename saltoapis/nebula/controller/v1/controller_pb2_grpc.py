# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.nebula.controller.v1 import controller_pb2 as salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2
from saltoapis.nebula.controller.v1 import controller_pb2 as salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2


class ControllerServiceStub(object):
    """Controllers are mains-wired hardware devices that can be used to control access where
    a standalone lock cannot be fitted. For example, on car park barriers, turnstiles or
    sliding doors. They allow the management of multiple accesses from a single device.
    For example, one single controller could control access to both the entrance and exit
    of a building via a turnstile. This service is responsible for managing controllers
    resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateController = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/CreateController',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.CreateControllerRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.Controller.FromString,
                _registered_method=True)
        self.GetController = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/GetController',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GetControllerRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.Controller.FromString,
                _registered_method=True)
        self.ListControllers = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/ListControllers',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ListControllersRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ListControllersResponse.FromString,
                _registered_method=True)
        self.UpdateController = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/UpdateController',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UpdateControllerRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.Controller.FromString,
                _registered_method=True)
        self.DeleteController = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/DeleteController',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.DeleteControllerRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.BindController = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/BindController',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.BindControllerRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.BindControllerResponse.FromString,
                _registered_method=True)
        self.UnbindController = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/UnbindController',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UnbindControllerRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UnbindControllerResponse.FromString,
                _registered_method=True)
        self.InitializeController = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/InitializeController',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.InitializeControllerRequest.SerializeToString,
                response_deserializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ConfigureController = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/ConfigureController',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ConfigureControllerRequest.SerializeToString,
                response_deserializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ResetController = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/ResetController',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ResetControllerRequest.SerializeToString,
                response_deserializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.UpdateControllerFirmware = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/UpdateControllerFirmware',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UpdateControllerFirmwareRequest.SerializeToString,
                response_deserializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.GenerateAuthorizationToken = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/GenerateAuthorizationToken',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GenerateAuthorizationTokenRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GenerateAuthorizationTokenResponse.FromString,
                _registered_method=True)
        self.GenerateFirmwareDownloadUri = channel.unary_unary(
                '/salto.nebula.controller.v1.ControllerService/GenerateFirmwareDownloadUri',
                request_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GenerateFirmwareDownloadUriRequest.SerializeToString,
                response_deserializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class ControllerServiceServicer(object):
    """Controllers are mains-wired hardware devices that can be used to control access where
    a standalone lock cannot be fitted. For example, on car park barriers, turnstiles or
    sliding doors. They allow the management of multiple accesses from a single device.
    For example, one single controller could control access to both the entrance and exit
    of a building via a turnstile. This service is responsible for managing controllers
    resources.
    """

    def CreateController(self, request, context):
        """Create a controller

        Creates a new controller
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetController(self, request, context):
        """Get a controller

        Gets an existing controller.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListControllers(self, request, context):
        """List controllers

        Returns a list of controllers that have been previously created.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateController(self, request, context):
        """Update a controller

        Updates an existing controller.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteController(self, request, context):
        """Delete a controller

        Permanently deletes a controller. This cannot be undone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BindController(self, request, context):
        """Bind a controller

        Binds a controller. Binding a controller assigns a device
        identifier to the controller. After binding, the device can then be
        initialized or configured.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnbindController(self, request, context):
        """Unbind a controller

        Unbinds a controller. Unbinding a controller removes the
        device identifier from the controller. This may be required in some
        cases where the controller is not available anymore because, for
        example, it's broken or damaged. Unbinding allows the initialization of
        the replacement device without removing it from the installation. It also
        means the device keeps all the information associated with it, such as
        events.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitializeController(self, request, context):
        """Initialize a controller

        Initializes a controller. Controllers need to be initialized
        before you can start to use them.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureController(self, request, context):
        """Configure a controller

        Configures a controller. Configuring a controller implies
        adding some information to the controller such as setting the time
        zone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetController(self, request, context):
        """Reset a controller

        Resetting a device such as a controller means returning it to its
        factory settings. Resetting is the process of removing the identity as
        well as all the associated information of an already configured device.
        Once a device has been reset, you need to reconfigure it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateControllerFirmware(self, request, context):
        """Update controller firmware

        Updates a controller's firmware. SALTO provides firmware updates
        when new functionality is available or when we fix a bug.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateAuthorizationToken(self, request, context):
        """Generates an authorization token for a controller

        Generates an authorization token that allows to connect, authenticate and
        authorize against a controller.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateFirmwareDownloadUri(self, request, context):
        """Generate controller firmware download URI

        Provides the download URI for the latest firmware bundle for the
        controller. The returned URI can be used to bring the controller
        firmwares up to latest.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControllerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateController': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateController,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.CreateControllerRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.Controller.SerializeToString,
            ),
            'GetController': grpc.unary_unary_rpc_method_handler(
                    servicer.GetController,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GetControllerRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.Controller.SerializeToString,
            ),
            'ListControllers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListControllers,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ListControllersRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ListControllersResponse.SerializeToString,
            ),
            'UpdateController': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateController,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UpdateControllerRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.Controller.SerializeToString,
            ),
            'DeleteController': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteController,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.DeleteControllerRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'BindController': grpc.unary_unary_rpc_method_handler(
                    servicer.BindController,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.BindControllerRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.BindControllerResponse.SerializeToString,
            ),
            'UnbindController': grpc.unary_unary_rpc_method_handler(
                    servicer.UnbindController,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UnbindControllerRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UnbindControllerResponse.SerializeToString,
            ),
            'InitializeController': grpc.unary_unary_rpc_method_handler(
                    servicer.InitializeController,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.InitializeControllerRequest.FromString,
                    response_serializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ConfigureController': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureController,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ConfigureControllerRequest.FromString,
                    response_serializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ResetController': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetController,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ResetControllerRequest.FromString,
                    response_serializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateControllerFirmware': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateControllerFirmware,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UpdateControllerFirmwareRequest.FromString,
                    response_serializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GenerateAuthorizationToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateAuthorizationToken,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GenerateAuthorizationTokenRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GenerateAuthorizationTokenResponse.SerializeToString,
            ),
            'GenerateFirmwareDownloadUri': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateFirmwareDownloadUri,
                    request_deserializer=salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GenerateFirmwareDownloadUriRequest.FromString,
                    response_serializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'salto.nebula.controller.v1.ControllerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('salto.nebula.controller.v1.ControllerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ControllerService(object):
    """Controllers are mains-wired hardware devices that can be used to control access where
    a standalone lock cannot be fitted. For example, on car park barriers, turnstiles or
    sliding doors. They allow the management of multiple accesses from a single device.
    For example, one single controller could control access to both the entrance and exit
    of a building via a turnstile. This service is responsible for managing controllers
    resources.
    """

    @staticmethod
    def CreateController(request,
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
            '/salto.nebula.controller.v1.ControllerService/CreateController',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.CreateControllerRequest.SerializeToString,
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.Controller.FromString,
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
    def GetController(request,
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
            '/salto.nebula.controller.v1.ControllerService/GetController',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GetControllerRequest.SerializeToString,
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.Controller.FromString,
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
    def ListControllers(request,
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
            '/salto.nebula.controller.v1.ControllerService/ListControllers',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ListControllersRequest.SerializeToString,
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ListControllersResponse.FromString,
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
    def UpdateController(request,
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
            '/salto.nebula.controller.v1.ControllerService/UpdateController',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UpdateControllerRequest.SerializeToString,
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.Controller.FromString,
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
    def DeleteController(request,
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
            '/salto.nebula.controller.v1.ControllerService/DeleteController',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.DeleteControllerRequest.SerializeToString,
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
    def BindController(request,
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
            '/salto.nebula.controller.v1.ControllerService/BindController',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.BindControllerRequest.SerializeToString,
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.BindControllerResponse.FromString,
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
    def UnbindController(request,
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
            '/salto.nebula.controller.v1.ControllerService/UnbindController',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UnbindControllerRequest.SerializeToString,
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UnbindControllerResponse.FromString,
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
    def InitializeController(request,
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
            '/salto.nebula.controller.v1.ControllerService/InitializeController',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.InitializeControllerRequest.SerializeToString,
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
    def ConfigureController(request,
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
            '/salto.nebula.controller.v1.ControllerService/ConfigureController',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ConfigureControllerRequest.SerializeToString,
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
    def ResetController(request,
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
            '/salto.nebula.controller.v1.ControllerService/ResetController',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.ResetControllerRequest.SerializeToString,
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
    def UpdateControllerFirmware(request,
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
            '/salto.nebula.controller.v1.ControllerService/UpdateControllerFirmware',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.UpdateControllerFirmwareRequest.SerializeToString,
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
    def GenerateAuthorizationToken(request,
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
            '/salto.nebula.controller.v1.ControllerService/GenerateAuthorizationToken',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GenerateAuthorizationTokenRequest.SerializeToString,
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GenerateAuthorizationTokenResponse.FromString,
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
            '/salto.nebula.controller.v1.ControllerService/GenerateFirmwareDownloadUri',
            salto_dot_nebula_dot_controller_dot_v1_dot_controller__pb2.GenerateFirmwareDownloadUriRequest.SerializeToString,
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
