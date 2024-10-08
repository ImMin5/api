# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.dashboard.v1 import public_folder_pb2 as spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in spaceone/api/dashboard/v1/public_folder_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class PublicFolderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicFolder/create',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.CreatePublicFolderRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicFolder/update',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.UpdatePublicFolderRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.FromString,
                _registered_method=True)
        self.share = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicFolder/share',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.SharePublicFolderRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.FromString,
                _registered_method=True)
        self.unshare = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicFolder/unshare',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicFolder/delete',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicFolder/get',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicFolder/list',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFoldersInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicFolder/stat',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class PublicFolderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def share(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def unshare(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
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

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PublicFolderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.CreatePublicFolderRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.UpdatePublicFolderRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.SerializeToString,
            ),
            'share': grpc.unary_unary_rpc_method_handler(
                    servicer.share,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.SharePublicFolderRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.SerializeToString,
            ),
            'unshare': grpc.unary_unary_rpc_method_handler(
                    servicer.unshare,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFoldersInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.dashboard.v1.PublicFolder', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.dashboard.v1.PublicFolder', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PublicFolder(object):
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
            '/spaceone.api.dashboard.v1.PublicFolder/create',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.CreatePublicFolderRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.FromString,
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
            '/spaceone.api.dashboard.v1.PublicFolder/update',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.UpdatePublicFolderRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.FromString,
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
    def share(request,
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
            '/spaceone.api.dashboard.v1.PublicFolder/share',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.SharePublicFolderRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.FromString,
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
    def unshare(request,
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
            '/spaceone.api.dashboard.v1.PublicFolder/unshare',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.FromString,
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
            '/spaceone.api.dashboard.v1.PublicFolder/delete',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderRequest.SerializeToString,
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
            '/spaceone.api.dashboard.v1.PublicFolder/get',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderInfo.FromString,
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
            '/spaceone.api.dashboard.v1.PublicFolder/list',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderQuery.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFoldersInfo.FromString,
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
            '/spaceone.api.dashboard.v1.PublicFolder/stat',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__folder__pb2.PublicFolderStatQuery.SerializeToString,
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
