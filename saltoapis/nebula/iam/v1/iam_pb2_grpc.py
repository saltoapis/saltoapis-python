# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from saltoapis.nebula.iam.v1 import iam_pb2 as salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2
from saltoapis.nebula.iam.v1 import iam_pb2 as salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2


class IAMServiceStub(object):
    """Identity and Access Management (IAM) is a service that allows you to securely
    control user access to specific resources. IAM gives you full control and
    visibility to manage resources centrally. You grant roles to users by
    creating an IAM policy which is a collection of permissions that define who
    has what type of access.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRole = channel.unary_unary(
                '/salto.nebula.iam.v1.IAMService/GetRole',
                request_serializer=salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.GetRoleRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.Role.FromString,
                _registered_method=True)
        self.ListRoles = channel.unary_unary(
                '/salto.nebula.iam.v1.IAMService/ListRoles',
                request_serializer=salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.ListRolesRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.ListRolesResponse.FromString,
                _registered_method=True)


class IAMServiceServicer(object):
    """Identity and Access Management (IAM) is a service that allows you to securely
    control user access to specific resources. IAM gives you full control and
    visibility to manage resources centrally. You grant roles to users by
    creating an IAM policy which is a collection of permissions that define who
    has what type of access.
    """

    def GetRole(self, request, context):
        """Get a role

        Gets an existing role.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRoles(self, request, context):
        """List roles

        Returns a list of roles that have been previously created.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IAMServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetRole': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRole,
                    request_deserializer=salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.GetRoleRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.Role.SerializeToString,
            ),
            'ListRoles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRoles,
                    request_deserializer=salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.ListRolesRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.ListRolesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'salto.nebula.iam.v1.IAMService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IAMService(object):
    """Identity and Access Management (IAM) is a service that allows you to securely
    control user access to specific resources. IAM gives you full control and
    visibility to manage resources centrally. You grant roles to users by
    creating an IAM policy which is a collection of permissions that define who
    has what type of access.
    """

    @staticmethod
    def GetRole(request,
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
            '/salto.nebula.iam.v1.IAMService/GetRole',
            salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.GetRoleRequest.SerializeToString,
            salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.Role.FromString,
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
    def ListRoles(request,
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
            '/salto.nebula.iam.v1.IAMService/ListRoles',
            salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.ListRolesRequest.SerializeToString,
            salto_dot_nebula_dot_iam_dot_v1_dot_iam__pb2.ListRolesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
