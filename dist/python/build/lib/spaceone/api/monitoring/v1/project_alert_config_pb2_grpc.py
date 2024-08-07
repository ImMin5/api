# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.monitoring.v1 import project_alert_config_pb2 as spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2

GRPC_GENERATED_VERSION = '1.65.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in spaceone/api/monitoring/v1/project_alert_config_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ProjectAlertConfigStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.monitoring.v1.ProjectAlertConfig/create',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.CreateProjectAlertConfigRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.monitoring.v1.ProjectAlertConfig/update',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.UpdateProjectAlertConfigRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.monitoring.v1.ProjectAlertConfig/delete',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.monitoring.v1.ProjectAlertConfig/get',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.monitoring.v1.ProjectAlertConfig/list',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigsInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.monitoring.v1.ProjectAlertConfig/stat',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class ProjectAlertConfigServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Creates a new ProjectAlertConfig in a specific Project. When creating a ProjectAlertConfig, validation of the Project is preceded. After the validation is done, ProjectAlertConfig enables EscalationPolicy to be set in the Project, or enables `enum` type `recovery_mode` and `notification_urgency` to be set through the `options` parameter.  The parameter `recovery_mode` is for changing the state of the Alert to `resolved` if the external monitoring solution sends the resolved Alert. The parameter `notification_urgency` is used to choose whether you will get all Alerts or only urgent ones.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Updates a specific ProjectAlertConfig. You can make changes in ProjectAlertConfig settings, including the EscalationPolicy to apply. You can also change `notification_urgency` and `recovery_mode` by modifying the `options` parameter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Deletes a specific ProjectAlertConfig. Deletes alert configuration data in a Project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Gets a specific ProjectAlertConfig. Prints detailed information about the ProjectAlertConfig, including EscalationPolicy, recovery mode, and notification urgency.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Gets a list of all ProjectAlertConfigs from all projects configured in the same domain. You can use a query to get a filtered list of ProjectAlertConfigs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectAlertConfigServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.CreateProjectAlertConfigRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.UpdateProjectAlertConfigRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.monitoring.v1.ProjectAlertConfig', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.monitoring.v1.ProjectAlertConfig', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ProjectAlertConfig(object):
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.ProjectAlertConfig/create',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.CreateProjectAlertConfigRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigInfo.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.ProjectAlertConfig/update',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.UpdateProjectAlertConfigRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigInfo.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.ProjectAlertConfig/delete',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.ProjectAlertConfig/get',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigInfo.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.ProjectAlertConfig/list',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigQuery.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigsInfo.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.ProjectAlertConfig/stat',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_project__alert__config__pb2.ProjectAlertConfigStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
