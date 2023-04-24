# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from spaceone.api.cost_analysis.v1 import exchange_rate_pb2 as spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2


class ExchangeRateStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.set = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.ExchangeRate/set',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.SetExchangeRateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.FromString,
                )
        self.reset = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.ExchangeRate/reset',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.FromString,
                )
        self.enable = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.ExchangeRate/enable',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.FromString,
                )
        self.disable = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.ExchangeRate/disable',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.ExchangeRate/get',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.ExchangeRate/list',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRatesInfo.FromString,
                )


class ExchangeRateServicer(object):
    """Missing associated documentation comment in .proto file."""

    def set(self, request, context):
        """
        desc: Overrides a value of a specific ExchangeRate. This method is used to change the ExchangeRate in a specific domain. You can set the `currency` and `rate` of the resource.
        request_example: >-
        {
        "currency": "KRW",
        "rate": 1300
        }
        response_example: >-
        {
        "currency": "KRW",
        "rate": 1300.0,
        "state": "ENABLED",
        "is_default": true
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def reset(self, request, context):
        """
        desc: Resets a value of a specific ExchangeRate and changes the ExchangeRate to the ExchangeRate of the `default` domain.
        request_example: >-
        {
        "currency": "KRW"
        }
        response_example: >-
        {
        "currency": "KRW",
        "rate": 1242.7,
        "state": "ENABLED",
        "is_default": true,
        "domain_id": "domain-58010aa2e451"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def enable(self, request, context):
        """
        desc: ''
        request_example: >-
        {
        }
        response_example: >-
        {

        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disable(self, request, context):
        """
        desc: ''
        request_example: >-
        {

        }
        response_example: >-
        {

        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """
        desc: Gets a specific ExchangeRate. Prints detailed information about the ExchangeRate, including  `currency` and `rate`.
        request_example: >-
        {
        "currency": "KRW"
        }
        response_example: >-
        {
        "currency": "KRW",
        "rate": 1242.7,
        "state": "ENABLED",
        "is_default": true,
        "domain_id": "domain-58010aa2e451"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """
        desc: Gets a list of all ExchangeRates. You can use a query to get a filtered list of ExchangeRates.
        request_example: >-
        {
        }
        response_example: >-
        {
        "results": [
        {
        "currency": "JPY",
        "rate": 129.8,
        "state": "ENABLED",
        "is_default": true,
        "domain_id": "domain-58010aa2e451"
        },
        {
        "currency": "KRW",
        "rate": 1242.7,
        "state": "ENABLED",
        "is_default": true,
        "domain_id": "domain-58010aa2e451"
        }
        ],
        "total_count": 2
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExchangeRateServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'set': grpc.unary_unary_rpc_method_handler(
                    servicer.set,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.SetExchangeRateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.SerializeToString,
            ),
            'reset': grpc.unary_unary_rpc_method_handler(
                    servicer.reset,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.SerializeToString,
            ),
            'enable': grpc.unary_unary_rpc_method_handler(
                    servicer.enable,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.SerializeToString,
            ),
            'disable': grpc.unary_unary_rpc_method_handler(
                    servicer.disable,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRatesInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.cost_analysis.v1.ExchangeRate', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExchangeRate(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_analysis.v1.ExchangeRate/set',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.SetExchangeRateRequest.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_analysis.v1.ExchangeRate/reset',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_analysis.v1.ExchangeRate/enable',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_analysis.v1.ExchangeRate/disable',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_analysis.v1.ExchangeRate/get',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateRequest.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_analysis.v1.ExchangeRate/list',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRateQuery.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_exchange__rate__pb2.ExchangeRatesInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
