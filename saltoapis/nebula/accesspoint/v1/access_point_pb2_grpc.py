# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.longrunning.v1 import operation_pb2 as salto_dot_longrunning_dot_v1_dot_operation__pb2
from saltoapis.nebula.accesspoint.v1 import access_point_pb2 as salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2
from saltoapis.nebula.accesspoint.v1 import access_point_pb2 as salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2


class AccessPointServiceStub(object):
    """An access point is a smart electronic locking device capable of granting or
    denying access to a secured area. This service is responsible for managing
    access point resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateAccessPoint = channel.unary_unary(
                '/salto.nebula.accesspoint.v1.AccessPointService/CreateAccessPoint',
                request_serializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.CreateAccessPointRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.AccessPoint.FromString,
                _registered_method=True)
        self.GetAccessPoint = channel.unary_unary(
                '/salto.nebula.accesspoint.v1.AccessPointService/GetAccessPoint',
                request_serializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.GetAccessPointRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.AccessPoint.FromString,
                _registered_method=True)
        self.ListAccessPoints = channel.unary_unary(
                '/salto.nebula.accesspoint.v1.AccessPointService/ListAccessPoints',
                request_serializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.ListAccessPointsRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.ListAccessPointsResponse.FromString,
                _registered_method=True)
        self.UpdateAccessPoint = channel.unary_unary(
                '/salto.nebula.accesspoint.v1.AccessPointService/UpdateAccessPoint',
                request_serializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.UpdateAccessPointRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.AccessPoint.FromString,
                _registered_method=True)
        self.DeleteAccessPoint = channel.unary_unary(
                '/salto.nebula.accesspoint.v1.AccessPointService/DeleteAccessPoint',
                request_serializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.DeleteAccessPointRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.UnlockAccessPoint = channel.unary_unary(
                '/salto.nebula.accesspoint.v1.AccessPointService/UnlockAccessPoint',
                request_serializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.UnlockAccessPointRequest.SerializeToString,
                response_deserializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class AccessPointServiceServicer(object):
    """An access point is a smart electronic locking device capable of granting or
    denying access to a secured area. This service is responsible for managing
    access point resources.
    """

    def CreateAccessPoint(self, request, context):
        """Create an access point

        Creates a new access point.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccessPoint(self, request, context):
        """Get an access point

        Retrieves an existing access point.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessPoints(self, request, context):
        """List access points

        Returns a list of access points that have been previously created.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessPoint(self, request, context):
        """Update an access point

        Updates an existing access point.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAccessPoint(self, request, context):
        """Delete an access point

        Permanently deletes an access point. This cannot be undone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnlockAccessPoint(self, request, context):
        """Unlock an access point

        Remotely unlocks an access point. This can be run against those access
        points where their associated devices are online and connected.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccessPointServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateAccessPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAccessPoint,
                    request_deserializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.CreateAccessPointRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.AccessPoint.SerializeToString,
            ),
            'GetAccessPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccessPoint,
                    request_deserializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.GetAccessPointRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.AccessPoint.SerializeToString,
            ),
            'ListAccessPoints': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccessPoints,
                    request_deserializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.ListAccessPointsRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.ListAccessPointsResponse.SerializeToString,
            ),
            'UpdateAccessPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccessPoint,
                    request_deserializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.UpdateAccessPointRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.AccessPoint.SerializeToString,
            ),
            'DeleteAccessPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAccessPoint,
                    request_deserializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.DeleteAccessPointRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UnlockAccessPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.UnlockAccessPoint,
                    request_deserializer=salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.UnlockAccessPointRequest.FromString,
                    response_serializer=salto_dot_longrunning_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'salto.nebula.accesspoint.v1.AccessPointService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccessPointService(object):
    """An access point is a smart electronic locking device capable of granting or
    denying access to a secured area. This service is responsible for managing
    access point resources.
    """

    @staticmethod
    def CreateAccessPoint(request,
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
            '/salto.nebula.accesspoint.v1.AccessPointService/CreateAccessPoint',
            salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.CreateAccessPointRequest.SerializeToString,
            salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.AccessPoint.FromString,
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
    def GetAccessPoint(request,
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
            '/salto.nebula.accesspoint.v1.AccessPointService/GetAccessPoint',
            salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.GetAccessPointRequest.SerializeToString,
            salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.AccessPoint.FromString,
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
    def ListAccessPoints(request,
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
            '/salto.nebula.accesspoint.v1.AccessPointService/ListAccessPoints',
            salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.ListAccessPointsRequest.SerializeToString,
            salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.ListAccessPointsResponse.FromString,
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
    def UpdateAccessPoint(request,
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
            '/salto.nebula.accesspoint.v1.AccessPointService/UpdateAccessPoint',
            salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.UpdateAccessPointRequest.SerializeToString,
            salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.AccessPoint.FromString,
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
    def DeleteAccessPoint(request,
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
            '/salto.nebula.accesspoint.v1.AccessPointService/DeleteAccessPoint',
            salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.DeleteAccessPointRequest.SerializeToString,
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
    def UnlockAccessPoint(request,
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
            '/salto.nebula.accesspoint.v1.AccessPointService/UnlockAccessPoint',
            salto_dot_nebula_dot_accesspoint_dot_v1_dot_access__point__pb2.UnlockAccessPointRequest.SerializeToString,
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
