# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.monitoring.v1 import alert_pb2 as spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2


class AlertStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/create',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.CreateAlertRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
                )
        self.update = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/update',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.UpdateAlertRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
                )
        self.update_state = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/update_state',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.UpdateAlertStateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
                )
        self.merge = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/merge',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.MergeAlertRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
                )
        self.snooze = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/snooze',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.SnoozeAlertRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
                )
        self.add_responder = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/add_responder',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertResponderRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
                )
        self.remove_responder = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/remove_responder',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertResponderRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
                )
        self.add_project_dependency = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/add_project_dependency',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertProjectDependencyRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
                )
        self.remove_project_dependency = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/remove_project_dependency',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertProjectDependencyRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
                )
        self.delete = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/delete',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/get',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.GetAlertRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/list',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertsInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Alert/stat',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class AlertServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """
        desc: Creates a new Alert. Alerts generated with `create` method are made in a manual way. Manually made Alerts can be used for Notifications.
        request_example: >-
        {
        "title": "sample test",
        "description": "This is a description of sample.",
        "urgency": "HIGH",
        "project_id": "project-123456789012",
        "domain_id": "domain-123456789012"
        }
        response_example: >-
        {
        "alert_number": 104053,
        "alert_id": "alert-123456789012",
        "title": "sample test",
        "state": "TRIGGERED",
        "description": "This is a description of sample.",
        "urgency": "HIGH",
        "severity": "NONE",
        "escalation_step": 1,
        "additional_info": {},
        "triggered_by": "user1@email.com",
        "escalation_policy_id": "ep-123456789012",
        "project_id": "project-123456789012",
        "domain_id": "domain-123456789012",
        "created_at": "2022-01-01T01:43:08.566Z",
        "updated_at": "2022-01-01T01:43:08.566Z",
        "escalated_at": "2022-01-01T01:43:54.464Z"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """
        desc: Updates a specific Alert. You can make changes in Alert settings, including the `title`, `description`, `responder`, `state`, and `urgency`. The `responder` of the Alert is a User who is assigned to respond to the Alert.
        request_example: >-
        {
        "alert_id": "alert-123456789012",
        "state": "ACKNOWLEDGED",
        "urgency": "LOW",
        "description": "[updating]This is a description of sample.",
        "domain_id": "domain-123456789012"
        }
        response_example: >-
        {
        "alert_number": 104053,
        "alert_id": "alert-123456789012",
        "title": "sample test",
        "state": "ACKNOWLEDGED",
        "description": "[updating]This is a description of sample. ",
        "urgency": "LOW",
        "severity": "NONE",
        "escalation_step": 1,
        "additional_info": {},
        "triggered_by": "user1@email.com",
        "escalation_policy_id": "ep-123456789012",
        "project_id": "project-123456789012",
        "domain_id": "domain-123456789012",
        "created_at": "2022-01-01T01:43:08.566Z",
        "updated_at": "2022-01-01T01:43:08.566Z",
        "acknowledged_at": "2022-01-01T01:48:52.799Z",
        "escalated_at": "2022-01-01T01:43:54.464Z"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_state(self, request, context):
        """
        desc: Updates the state of an Alert via callback URL by creating a temporary `access_key` while generating a Notification about the Alert.
        request_example: >-
        {
        "alert_id": "alert-123456789012",
        "access_key": "1q2w3e4r5t6y7u8i9o0p",
        "domain_id": "domain-123456789012"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def merge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def snooze(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def add_responder(self, request, context):
        """
        desc: Adds a responder who receives a Notification about an Alert.
        request_example: >-
        {
        "alert_id": "alert-123456789012",
        "resource_type": "identity.User",
        "resource_id": "user2@email.com",
        "domain_id": "domain-123456789012"
        }
        response_example: >-
        {
        "alert_number": 104053,
        "alert_id": "alert-123456789012",
        "title": "sample test",
        "state": "ACKNOWLEDGED",
        "description": "[updating]This is a description of sample. ",
        "urgency": "LOW",
        "severity": "NONE",
        "escalation_step": 1,
        "responders": [
        {
        "resource_type": "identity.User",
        "resource_id": "user2@email.com"
        }
        ],
        "additional_info": {},
        "triggered_by": "user1@email.com",
        "escalation_policy_id": "ep-123456789012",
        "project_id": "project-123456789012",
        "domain_id": "domain-123456789012",
        "created_at": "2022-01-01T01:43:08.566Z",
        "updated_at": "2022-01-01T01:43:08.566Z",
        "acknowledged_at": "2022-01-01T02:24:12.051Z",
        "escalated_at": "2022-01-01T01:43:54.464Z"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove_responder(self, request, context):
        """
        desc: Deletes a responder who receives a Notification about an Alert.
        request_example: >-
        {
        "alert_id": "alert-123456789012",
        "resource_type": "identity.User",
        "resource_id": "user2@email.com",
        "domain_id": "domain-123456789012"
        }
        response_example: >-
        {
        "alert_number": 104053,
        "alert_id": "alert-123456789012",
        "title": "sample test",
        "state": "ACKNOWLEDGED",
        "description": "[updating]This is a description of sample. ",
        "urgency": "LOW",
        "severity": "NONE",
        "escalation_step": 1,
        "additional_info": {},
        "triggered_by": "user1@email.com",
        "escalation_policy_id": "ep-123456789012",
        "project_id": "project-123456789012",
        "domain_id": "domain-123456789012",
        "created_at": "2022-01-01T01:43:08.566Z",
        "updated_at": "2022-01-01T01:43:08.566Z",
        "acknowledged_at": "2022-01-01T01:48:52.799Z",
        "escalated_at": "2022-01-01T01:43:54.464Z"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def add_project_dependency(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove_project_dependency(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """
        desc: Deletes a specific Alert and remove it from the list of Alerts. You must specify the `alert_id` of the Alert to delete.
        request_example: >-
        {
        "alert_id": "alert-123456789012",
        "domain_id": "domain-123456789012"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """
        desc: Gets a specific Alert. Prints detailed information about the Alert.
        request_example: >-
        {
        "alert_id": "alert-123456789012",
        "domain_id": "domain-123456789012"
        }
        response_example: >-
        {
        "alert_number": 104053,
        "alert_id": "alert-123456789012",
        "title": "sample test",
        "state": "ACKNOWLEDGED",
        "description": "[updating]This is a description of sample. ",
        "urgency": "LOW",
        "severity": "NONE",
        "escalation_step": 1,
        "additional_info": {},
        "triggered_by": "user1@email.com",
        "escalation_policy_id": "ep-123456789012",
        "project_id": "project-123456789012",
        "domain_id": "domain-123456789012",
        "created_at": "2022-01-01T01:43:08.566Z",
        "updated_at": "2022-01-01T01:43:08.566Z",
        "acknowledged_at": "2022-01-01T01:48:52.799Z",
        "escalated_at": "2022-01-01T01:43:54.464Z"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """
        desc: Gets a list of all Alerts. You can use a query to get a filtered list of Alerts.
        request_example: >-
        {
        "query": {},
        "domain_id": "domain-123456789012"
        }
        response_example: >-
        {
        "results": [
        {
        "alert_number": 104057,
        "alert_id": "alert-987654321098",
        "title": "Notification of access to the bastion Host",
        "state": "TRIGGERED",
        "description": "SSH Access to stargate-dev from adm",
        "urgency": "LOW",
        "severity": "INFO",
        "resource": {
        "resource_id": "server-123456789012",
        "resource_type": "inventory.Server",
        "name": "stargate-dev"
        },
        "escalation_step": 1,
        "escalation_ttl": 1,
        "additional_info": {
        "host": "[]",
        "user": "user1"
        },
        "triggered_by": "webhook-123456789012",
        "webhook_id": "webhook-123456789012",
        "escalation_policy_id": "ep-123456789012",
        "project_id": "project-123456789012",
        "domain_id": "domain-123456789012",
        "created_at": "2022-01-01T02:46:35.934Z",
        "updated_at": "2022-01-01T02:46:35.934Z",
        "escalated_at": "2022-01-01T02:46:35.979Z"
        },
        {
        "alert_number": 104056,
        "alert_id": "alert-123456789999",
        "title": "Notification of access to the bastion Host",
        "state": "TRIGGERED",
        "description": "SSH Access to stargate-dev from user3@email.com",
        "urgency": "LOW",
        "severity": "INFO",
        "resource": {
        "resource_id": "server-123456789012",
        "resource_type": "inventory.Server",
        "name": "stargate-dev"
        },
        "escalation_step": 1,
        "escalation_ttl": 1,
        "additional_info": {
        "user": "user3@email.com",
        "host": "['111.111.111.11']"
        },
        "triggered_by": "webhook-123456789012",
        "webhook_id": "webhook-123456789012",
        "escalation_policy_id": "ep-123456789012",
        "project_id": "project-123456789012",
        "domain_id": "domain-123456789012",
        "created_at": "2022-01-01T02:46:31.391Z",
        "updated_at": "2022-01-01T02:46:31.391Z",
        "escalated_at": "2022-01-01T02:46:31.553Z"
        }
        ],
        "total_count": 21283
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AlertServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.CreateAlertRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.UpdateAlertRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.SerializeToString,
            ),
            'update_state': grpc.unary_unary_rpc_method_handler(
                    servicer.update_state,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.UpdateAlertStateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.SerializeToString,
            ),
            'merge': grpc.unary_unary_rpc_method_handler(
                    servicer.merge,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.MergeAlertRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.SerializeToString,
            ),
            'snooze': grpc.unary_unary_rpc_method_handler(
                    servicer.snooze,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.SnoozeAlertRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.SerializeToString,
            ),
            'add_responder': grpc.unary_unary_rpc_method_handler(
                    servicer.add_responder,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertResponderRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.SerializeToString,
            ),
            'remove_responder': grpc.unary_unary_rpc_method_handler(
                    servicer.remove_responder,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertResponderRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.SerializeToString,
            ),
            'add_project_dependency': grpc.unary_unary_rpc_method_handler(
                    servicer.add_project_dependency,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertProjectDependencyRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.SerializeToString,
            ),
            'remove_project_dependency': grpc.unary_unary_rpc_method_handler(
                    servicer.remove_project_dependency,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertProjectDependencyRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.GetAlertRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.monitoring.v1.Alert', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Alert(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/create',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.CreateAlertRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/update',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.UpdateAlertRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/update_state',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.UpdateAlertStateRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def merge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/merge',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.MergeAlertRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def snooze(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/snooze',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.SnoozeAlertRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def add_responder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/add_responder',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertResponderRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def remove_responder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/remove_responder',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertResponderRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def add_project_dependency(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/add_project_dependency',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertProjectDependencyRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def remove_project_dependency(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/remove_project_dependency',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertProjectDependencyRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/delete',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/get',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.GetAlertRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/list',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertQuery.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertsInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Alert/stat',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_alert__pb2.AlertStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
