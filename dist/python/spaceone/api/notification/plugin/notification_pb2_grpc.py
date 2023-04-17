# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.notification.plugin import notification_pb2 as spaceone_dot_api_dot_notification_dot_plugin_dot_notification__pb2


class NotificationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.dispatch = channel.unary_unary(
                '/spaceone.api.notification.plugin.Notification/dispatch',
                request_serializer=spaceone_dot_api_dot_notification_dot_plugin_dot_notification__pb2.PluginDispatchRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class NotificationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def dispatch(self, request, context):
        """
        desc: Dispatches data from Cloudforet to a specific notification Protocol. When dispatching data, data input by a User is included in the `options` parameter, and `notification` information to be delivered is included in the `message` parameter. Also, data dispatched includes basic information such as `notification_type` and `secret_data`.
        request_example: >-
        {
        "options": {},
        "message": {
        "tags": [
        {
        "key": "Alert Number",
        "options": {"short": true},
        "value": "#108664"
        },
        {
        "options": {"short": true},
        "key": "State",
        "value": "TRIGGERED"
        },
        {
        "value": "LOW",
        "options": {"short": true},
        "key": "Urgency"
        },
        {
        "value": "kubectl-webhook",
        "key": "Triggered by",
        "options": {"short": true}
        },
        {
        "value": "SpaceONE > Project1",
        "key": "Project"
        },
        {
        "value": "spaceone-api",
        "key": "Resource"
        }
        ],
        "occurred_at": "2022-06-27T09:22:57.967Z",
        "callbacks": [{
        "url": "https://monitoring-webhook.dev.spaceone.dev/monitoring/v1/alert/alert-x1v2c3v456/8f2ede36213dqw4d7d5awe07ds32d883/ACKNOWLEDGED",
        "label": "Acknowledge Alerts"}],
        "link": "https://spaceone.console.dev.spaceone.dev/alert-manager/alert/alert-x1v2c3v456",
        "title": "[Alerting] Notification of access to the SpaceONE",
        "description": "SSH Access to spaceone-api from admin"},
        "notification_type": "INFO",
        "secret_data": "********",
        "channel_data": {"email": "test5@test.com"}
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotificationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'dispatch': grpc.unary_unary_rpc_method_handler(
                    servicer.dispatch,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_plugin_dot_notification__pb2.PluginDispatchRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.notification.plugin.Notification', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Notification(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def dispatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.notification.plugin.Notification/dispatch',
            spaceone_dot_api_dot_notification_dot_plugin_dot_notification__pb2.PluginDispatchRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
