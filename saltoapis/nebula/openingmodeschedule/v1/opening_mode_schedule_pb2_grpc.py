# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from saltoapis.nebula.openingmodeschedule.v1 import opening_mode_schedule_pb2 as salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2
from saltoapis.nebula.openingmodeschedule.v1 import opening_mode_schedule_pb2 as salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2


class OpeningModeScheduleServiceStub(object):
    """An opening mode is a type of behavior which can be applied to a specific
    access point or collection of access points. For example: Office or Toggle.
    This service allows you to make a number of different opening modes switch
    automatically and vary across different time periods.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateOpeningModeSchedule = channel.unary_unary(
                '/salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService/CreateOpeningModeSchedule',
                request_serializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.CreateOpeningModeScheduleRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.OpeningModeSchedule.FromString,
                _registered_method=True)
        self.GetOpeningModeSchedule = channel.unary_unary(
                '/salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService/GetOpeningModeSchedule',
                request_serializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.GetOpeningModeScheduleRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.OpeningModeSchedule.FromString,
                _registered_method=True)
        self.ListOpeningModeSchedules = channel.unary_unary(
                '/salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService/ListOpeningModeSchedules',
                request_serializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.ListOpeningModeSchedulesRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.ListOpeningModeSchedulesResponse.FromString,
                _registered_method=True)
        self.UpdateOpeningModeSchedule = channel.unary_unary(
                '/salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService/UpdateOpeningModeSchedule',
                request_serializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.UpdateOpeningModeScheduleRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.OpeningModeSchedule.FromString,
                _registered_method=True)
        self.DeleteOpeningModeSchedule = channel.unary_unary(
                '/salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService/DeleteOpeningModeSchedule',
                request_serializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.DeleteOpeningModeScheduleRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class OpeningModeScheduleServiceServicer(object):
    """An opening mode is a type of behavior which can be applied to a specific
    access point or collection of access points. For example: Office or Toggle.
    This service allows you to make a number of different opening modes switch
    automatically and vary across different time periods.
    """

    def CreateOpeningModeSchedule(self, request, context):
        """Create an opening mode schedule

        Creates an opening mode schedule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOpeningModeSchedule(self, request, context):
        """Get an opening mode schedule

        Gets an existing opening mode schedule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOpeningModeSchedules(self, request, context):
        """List opening mode schedules

        Returns a list of opening mode schedules that have been previously
        created.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOpeningModeSchedule(self, request, context):
        """Update an opening mode schedule

        Updates an existing opening mode schedule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOpeningModeSchedule(self, request, context):
        """Delete an opening mode schedule

        Permanently deletes an opening mode schedule. This cannot be undone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OpeningModeScheduleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateOpeningModeSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOpeningModeSchedule,
                    request_deserializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.CreateOpeningModeScheduleRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.OpeningModeSchedule.SerializeToString,
            ),
            'GetOpeningModeSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOpeningModeSchedule,
                    request_deserializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.GetOpeningModeScheduleRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.OpeningModeSchedule.SerializeToString,
            ),
            'ListOpeningModeSchedules': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOpeningModeSchedules,
                    request_deserializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.ListOpeningModeSchedulesRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.ListOpeningModeSchedulesResponse.SerializeToString,
            ),
            'UpdateOpeningModeSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOpeningModeSchedule,
                    request_deserializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.UpdateOpeningModeScheduleRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.OpeningModeSchedule.SerializeToString,
            ),
            'DeleteOpeningModeSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteOpeningModeSchedule,
                    request_deserializer=salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.DeleteOpeningModeScheduleRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class OpeningModeScheduleService(object):
    """An opening mode is a type of behavior which can be applied to a specific
    access point or collection of access points. For example: Office or Toggle.
    This service allows you to make a number of different opening modes switch
    automatically and vary across different time periods.
    """

    @staticmethod
    def CreateOpeningModeSchedule(request,
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
            '/salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService/CreateOpeningModeSchedule',
            salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.CreateOpeningModeScheduleRequest.SerializeToString,
            salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.OpeningModeSchedule.FromString,
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
    def GetOpeningModeSchedule(request,
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
            '/salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService/GetOpeningModeSchedule',
            salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.GetOpeningModeScheduleRequest.SerializeToString,
            salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.OpeningModeSchedule.FromString,
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
    def ListOpeningModeSchedules(request,
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
            '/salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService/ListOpeningModeSchedules',
            salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.ListOpeningModeSchedulesRequest.SerializeToString,
            salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.ListOpeningModeSchedulesResponse.FromString,
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
    def UpdateOpeningModeSchedule(request,
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
            '/salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService/UpdateOpeningModeSchedule',
            salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.UpdateOpeningModeScheduleRequest.SerializeToString,
            salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.OpeningModeSchedule.FromString,
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
    def DeleteOpeningModeSchedule(request,
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
            '/salto.nebula.openingmodeschedule.v1.OpeningModeScheduleService/DeleteOpeningModeSchedule',
            salto_dot_nebula_dot_openingmodeschedule_dot_v1_dot_opening__mode__schedule__pb2.DeleteOpeningModeScheduleRequest.SerializeToString,
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
