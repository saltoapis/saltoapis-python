# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from saltoapis.nebula.calendar.v1 import calendar_pb2 as salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2
from saltoapis.nebula.calendar.v1 import calendar_pb2 as salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2


class CalendarServiceStub(object):
    """The calendar functionality defines your organization's working calendar.
    For example, you can define public holidays, company holidays and company
    shutdowns. This service is responsible for managing calendar resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateCalendar = channel.unary_unary(
                '/salto.nebula.calendar.v1.CalendarService/CreateCalendar',
                request_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.CreateCalendarRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Calendar.FromString,
                _registered_method=True)
        self.GetCalendar = channel.unary_unary(
                '/salto.nebula.calendar.v1.CalendarService/GetCalendar',
                request_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.GetCalendarRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Calendar.FromString,
                _registered_method=True)
        self.ListCalendars = channel.unary_unary(
                '/salto.nebula.calendar.v1.CalendarService/ListCalendars',
                request_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListCalendarsRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListCalendarsResponse.FromString,
                _registered_method=True)
        self.UpdateCalendar = channel.unary_unary(
                '/salto.nebula.calendar.v1.CalendarService/UpdateCalendar',
                request_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.UpdateCalendarRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Calendar.FromString,
                _registered_method=True)
        self.DeleteCalendar = channel.unary_unary(
                '/salto.nebula.calendar.v1.CalendarService/DeleteCalendar',
                request_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.DeleteCalendarRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.CreateEvent = channel.unary_unary(
                '/salto.nebula.calendar.v1.CalendarService/CreateEvent',
                request_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.CreateEventRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Event.FromString,
                _registered_method=True)
        self.GetEvent = channel.unary_unary(
                '/salto.nebula.calendar.v1.CalendarService/GetEvent',
                request_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.GetEventRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Event.FromString,
                _registered_method=True)
        self.ListEvents = channel.unary_unary(
                '/salto.nebula.calendar.v1.CalendarService/ListEvents',
                request_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListEventsRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListEventsResponse.FromString,
                _registered_method=True)
        self.UpdateEvent = channel.unary_unary(
                '/salto.nebula.calendar.v1.CalendarService/UpdateEvent',
                request_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.UpdateEventRequest.SerializeToString,
                response_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Event.FromString,
                _registered_method=True)
        self.DeleteEvent = channel.unary_unary(
                '/salto.nebula.calendar.v1.CalendarService/DeleteEvent',
                request_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.DeleteEventRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class CalendarServiceServicer(object):
    """The calendar functionality defines your organization's working calendar.
    For example, you can define public holidays, company holidays and company
    shutdowns. This service is responsible for managing calendar resources.
    """

    def CreateCalendar(self, request, context):
        """Create a calendar

        Creates a calendar.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCalendar(self, request, context):
        """Get a calendar

        Gets an existing calendar.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCalendars(self, request, context):
        """List calendars

        Returns a list of calendars that have been previously created.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCalendar(self, request, context):
        """Update a calendar

        Updates an existing calendar.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCalendar(self, request, context):
        """Delete a calendar

        Permanently deletes a calendar. This cannot be undone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEvent(self, request, context):
        """Create a calendar event

        Creates a calendar event.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEvent(self, request, context):
        """Get a calendar event

        Gets an existing calendar event.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEvents(self, request, context):
        """List calendar events

        Lists existing calendar events.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEvent(self, request, context):
        """Update a calendar event

        Updates an existing calendar event.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEvent(self, request, context):
        """Delete a calendar event

        Permanently deletes a calendar event. This cannot be undone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalendarServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateCalendar': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCalendar,
                    request_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.CreateCalendarRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Calendar.SerializeToString,
            ),
            'GetCalendar': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCalendar,
                    request_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.GetCalendarRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Calendar.SerializeToString,
            ),
            'ListCalendars': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCalendars,
                    request_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListCalendarsRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListCalendarsResponse.SerializeToString,
            ),
            'UpdateCalendar': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCalendar,
                    request_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.UpdateCalendarRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Calendar.SerializeToString,
            ),
            'DeleteCalendar': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCalendar,
                    request_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.DeleteCalendarRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEvent,
                    request_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.CreateEventRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Event.SerializeToString,
            ),
            'GetEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEvent,
                    request_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.GetEventRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Event.SerializeToString,
            ),
            'ListEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEvents,
                    request_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListEventsRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListEventsResponse.SerializeToString,
            ),
            'UpdateEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEvent,
                    request_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.UpdateEventRequest.FromString,
                    response_serializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Event.SerializeToString,
            ),
            'DeleteEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteEvent,
                    request_deserializer=salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.DeleteEventRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'salto.nebula.calendar.v1.CalendarService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CalendarService(object):
    """The calendar functionality defines your organization's working calendar.
    For example, you can define public holidays, company holidays and company
    shutdowns. This service is responsible for managing calendar resources.
    """

    @staticmethod
    def CreateCalendar(request,
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
            '/salto.nebula.calendar.v1.CalendarService/CreateCalendar',
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.CreateCalendarRequest.SerializeToString,
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Calendar.FromString,
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
    def GetCalendar(request,
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
            '/salto.nebula.calendar.v1.CalendarService/GetCalendar',
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.GetCalendarRequest.SerializeToString,
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Calendar.FromString,
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
    def ListCalendars(request,
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
            '/salto.nebula.calendar.v1.CalendarService/ListCalendars',
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListCalendarsRequest.SerializeToString,
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListCalendarsResponse.FromString,
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
    def UpdateCalendar(request,
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
            '/salto.nebula.calendar.v1.CalendarService/UpdateCalendar',
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.UpdateCalendarRequest.SerializeToString,
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Calendar.FromString,
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
    def DeleteCalendar(request,
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
            '/salto.nebula.calendar.v1.CalendarService/DeleteCalendar',
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.DeleteCalendarRequest.SerializeToString,
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
    def CreateEvent(request,
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
            '/salto.nebula.calendar.v1.CalendarService/CreateEvent',
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.CreateEventRequest.SerializeToString,
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Event.FromString,
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
    def GetEvent(request,
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
            '/salto.nebula.calendar.v1.CalendarService/GetEvent',
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.GetEventRequest.SerializeToString,
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Event.FromString,
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
    def ListEvents(request,
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
            '/salto.nebula.calendar.v1.CalendarService/ListEvents',
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListEventsRequest.SerializeToString,
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.ListEventsResponse.FromString,
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
    def UpdateEvent(request,
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
            '/salto.nebula.calendar.v1.CalendarService/UpdateEvent',
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.UpdateEventRequest.SerializeToString,
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.Event.FromString,
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
    def DeleteEvent(request,
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
            '/salto.nebula.calendar.v1.CalendarService/DeleteEvent',
            salto_dot_nebula_dot_calendar_dot_v1_dot_calendar__pb2.DeleteEventRequest.SerializeToString,
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
