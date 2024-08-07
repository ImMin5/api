# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.identity.v2 import job_pb2 as spaceone_dot_api_dot_identity_dot_v2_dot_job__pb2
from spaceone.api.identity.v2 import trusted_account_pb2 as spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2

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
        + f' but the generated code in spaceone/api/identity/v2/trusted_account_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class TrustedAccountStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.identity.v2.TrustedAccount/create',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.CreateTrustedAccountRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.identity.v2.TrustedAccount/update',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.UpdateTrustedAccountRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.FromString,
                _registered_method=True)
        self.update_secret_data = channel.unary_unary(
                '/spaceone.api.identity.v2.TrustedAccount/update_secret_data',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.UpdateTrustedAccountSecretRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.identity.v2.TrustedAccount/delete',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.sync = channel.unary_unary(
                '/spaceone.api.identity.v2.TrustedAccount/sync',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_job__pb2.JobInfo.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.identity.v2.TrustedAccount/get',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.identity.v2.TrustedAccount/list',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountSearchQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountsInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.identity.v2.TrustedAccount/stat',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class TrustedAccountServicer(object):
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

    def update_secret_data(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sync(self, request, context):
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


def add_TrustedAccountServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.CreateTrustedAccountRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.UpdateTrustedAccountRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.SerializeToString,
            ),
            'update_secret_data': grpc.unary_unary_rpc_method_handler(
                    servicer.update_secret_data,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.UpdateTrustedAccountSecretRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'sync': grpc.unary_unary_rpc_method_handler(
                    servicer.sync,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_job__pb2.JobInfo.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountSearchQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.identity.v2.TrustedAccount', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.identity.v2.TrustedAccount', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TrustedAccount(object):
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
            '/spaceone.api.identity.v2.TrustedAccount/create',
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.CreateTrustedAccountRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.FromString,
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
            '/spaceone.api.identity.v2.TrustedAccount/update',
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.UpdateTrustedAccountRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.FromString,
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
    def update_secret_data(request,
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
            '/spaceone.api.identity.v2.TrustedAccount/update_secret_data',
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.UpdateTrustedAccountSecretRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.FromString,
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
            '/spaceone.api.identity.v2.TrustedAccount/delete',
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountRequest.SerializeToString,
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
    def sync(request,
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
            '/spaceone.api.identity.v2.TrustedAccount/sync',
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_job__pb2.JobInfo.FromString,
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
            '/spaceone.api.identity.v2.TrustedAccount/get',
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountInfo.FromString,
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
            '/spaceone.api.identity.v2.TrustedAccount/list',
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountSearchQuery.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountsInfo.FromString,
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
            '/spaceone.api.identity.v2.TrustedAccount/stat',
            spaceone_dot_api_dot_identity_dot_v2_dot_trusted__account__pb2.TrustedAccountStatQuery.SerializeToString,
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
