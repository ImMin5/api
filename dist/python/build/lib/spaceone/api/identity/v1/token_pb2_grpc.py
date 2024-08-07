# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.identity.v1 import token_pb2 as spaceone_dot_api_dot_identity_dot_v1_dot_token__pb2

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
        + f' but the generated code in spaceone/api/identity/v1/token_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class TokenStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.issue = channel.unary_unary(
                '/spaceone.api.identity.v1.Token/issue',
                request_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_token__pb2.IssueTokenRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_token__pb2.TokenInfo.FromString,
                _registered_method=True)
        self.refresh = channel.unary_unary(
                '/spaceone.api.identity.v1.Token/refresh',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_token__pb2.TokenInfo.FromString,
                _registered_method=True)


class TokenServicer(object):
    """Missing associated documentation comment in .proto file."""

    def issue(self, request, context):
        """+noauth
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def refresh(self, request, context):
        """+noauth
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TokenServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'issue': grpc.unary_unary_rpc_method_handler(
                    servicer.issue,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_token__pb2.IssueTokenRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_token__pb2.TokenInfo.SerializeToString,
            ),
            'refresh': grpc.unary_unary_rpc_method_handler(
                    servicer.refresh,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_token__pb2.TokenInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.identity.v1.Token', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.identity.v1.Token', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Token(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def issue(request,
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
            '/spaceone.api.identity.v1.Token/issue',
            spaceone_dot_api_dot_identity_dot_v1_dot_token__pb2.IssueTokenRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v1_dot_token__pb2.TokenInfo.FromString,
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
    def refresh(request,
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
            '/spaceone.api.identity.v1.Token/refresh',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v1_dot_token__pb2.TokenInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
