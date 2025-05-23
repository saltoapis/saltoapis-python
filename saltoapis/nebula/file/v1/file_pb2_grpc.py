# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from saltoapis.nebula.file.v1 import file_pb2 as salto_dot_nebula_dot_file_dot_v1_dot_file__pb2
from saltoapis.nebula.file.v1 import file_pb2 as salto_dot_nebula_dot_file_dot_v1_dot_file__pb2


class FileServiceStub(object):
    """A file represents an object that serves as a reference for files
    stored elsewhere. This service is responsible for managing file resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateFile = channel.unary_unary(
                '/salto.nebula.file.v1.FileService/CreateFile',
                request_serializer=salto_dot_nebula_dot_file_dot_v1_dot_file__pb2.CreateFileRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_file_dot_v1_dot_file__pb2.File.FromString,
                _registered_method=True)


class FileServiceServicer(object):
    """A file represents an object that serves as a reference for files
    stored elsewhere. This service is responsible for managing file resources.
    """

    def CreateFile(self, request, context):
        """Create a file

        Creates a new file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=salto_dot_nebula_dot_file_dot_v1_dot_file__pb2.CreateFileRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_file_dot_v1_dot_file__pb2.File.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'salto.nebula.file.v1.FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('salto.nebula.file.v1.FileService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """A file represents an object that serves as a reference for files
    stored elsewhere. This service is responsible for managing file resources.
    """

    @staticmethod
    def CreateFile(request,
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
            '/salto.nebula.file.v1.FileService/CreateFile',
            salto_dot_nebula_dot_file_dot_v1_dot_file__pb2.CreateFileRequest.SerializeToString,
            salto_dot_nebula_dot_file_dot_v1_dot_file__pb2.File.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
