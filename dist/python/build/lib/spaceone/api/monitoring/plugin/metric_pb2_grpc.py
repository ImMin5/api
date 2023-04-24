# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from spaceone.api.monitoring.plugin import metric_pb2 as spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2


class MetricStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.list = channel.unary_unary(
                '/spaceone.api.monitoring.plugin.Metric/list',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricsInfo.FromString,
                )
        self.get_data = channel.unary_unary(
                '/spaceone.api.monitoring.plugin.Metric/get_data',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricDataRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricDataInfo.FromString,
                )


class MetricServicer(object):
    """Missing associated documentation comment in .proto file."""

    def list(self, request, context):
        """
        desc: Gets a list of all Metrics from a specific cloud service. You can use the method to list up the Metrics to collect before using the `get_data` method to collect the Metrics.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_data(self, request, context):
        """
        desc: Gets a Metric from a specific cloud service resource `instance`. By specifying the time period to collect the Metric, the Metric data value of the `instance` during the period is returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetricServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricsInfo.SerializeToString,
            ),
            'get_data': grpc.unary_unary_rpc_method_handler(
                    servicer.get_data,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricDataRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricDataInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.monitoring.plugin.Metric', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Metric(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.plugin.Metric/list',
            spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricsInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_data(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.plugin.Metric/get_data',
            spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricDataRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricDataInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
