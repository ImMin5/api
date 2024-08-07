# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.repository.v1 import dashboard_template_pb2 as spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2

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
        + f' but the generated code in spaceone/api/repository/v1/dashboard_template_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class DashboardTemplateStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.register = channel.unary_unary(
                '/spaceone.api.repository.v1.DashboardTemplate/register',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.RegisterDashboardTemplateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.repository.v1.DashboardTemplate/update',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.UpdateDashboardTemplateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.FromString,
                _registered_method=True)
        self.deregister = channel.unary_unary(
                '/spaceone.api.repository.v1.DashboardTemplate/deregister',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.enable = channel.unary_unary(
                '/spaceone.api.repository.v1.DashboardTemplate/enable',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.FromString,
                _registered_method=True)
        self.disable = channel.unary_unary(
                '/spaceone.api.repository.v1.DashboardTemplate/disable',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.repository.v1.DashboardTemplate/get',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.RepositoryDashboardTemplateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.repository.v1.DashboardTemplate/list',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplatesInfo.FromString,
                _registered_method=True)


class DashboardTemplateServicer(object):
    """Missing associated documentation comment in .proto file."""

    def register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deregister(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def enable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DashboardTemplateServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'register': grpc.unary_unary_rpc_method_handler(
                    servicer.register,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.RegisterDashboardTemplateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.UpdateDashboardTemplateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.SerializeToString,
            ),
            'deregister': grpc.unary_unary_rpc_method_handler(
                    servicer.deregister,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'enable': grpc.unary_unary_rpc_method_handler(
                    servicer.enable,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.SerializeToString,
            ),
            'disable': grpc.unary_unary_rpc_method_handler(
                    servicer.disable,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.RepositoryDashboardTemplateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplatesInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.repository.v1.DashboardTemplate', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.repository.v1.DashboardTemplate', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DashboardTemplate(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def register(request,
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
            '/spaceone.api.repository.v1.DashboardTemplate/register',
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.RegisterDashboardTemplateRequest.SerializeToString,
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.FromString,
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
            '/spaceone.api.repository.v1.DashboardTemplate/update',
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.UpdateDashboardTemplateRequest.SerializeToString,
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.FromString,
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
    def deregister(request,
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
            '/spaceone.api.repository.v1.DashboardTemplate/deregister',
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateRequest.SerializeToString,
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
    def enable(request,
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
            '/spaceone.api.repository.v1.DashboardTemplate/enable',
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateRequest.SerializeToString,
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.FromString,
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
    def disable(request,
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
            '/spaceone.api.repository.v1.DashboardTemplate/disable',
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateRequest.SerializeToString,
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.FromString,
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
            '/spaceone.api.repository.v1.DashboardTemplate/get',
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.RepositoryDashboardTemplateRequest.SerializeToString,
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateInfo.FromString,
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
            '/spaceone.api.repository.v1.DashboardTemplate/list',
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplateQuery.SerializeToString,
            spaceone_dot_api_dot_repository_dot_v1_dot_dashboard__template__pb2.DashboardTemplatesInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
