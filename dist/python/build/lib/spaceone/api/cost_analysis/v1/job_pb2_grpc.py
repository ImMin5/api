# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.cost_analysis.v1 import job_pb2 as spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2


class JobStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.cancel = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.Job/cancel',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobInfo.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.Job/get',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.GetJobRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.Job/list',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobsInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.Job/stat',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class JobServicer(object):
    """Missing associated documentation comment in .proto file."""

    def cancel(self, request, context):
        """
        desc: Cancels a specific Job. You can manually cease a Job in run with this method.
        request_example: >-
        {
        "job_id": "job-07994c7c9021"
        }
        response_example: >-
        {
        "job_id": "job-07994c7c9021",
        "status": "CANCELED",
        "options": {
        "no_preload_cache": false,
        "start": "2021-01-01T00:00:00Z"
        },
        "total_tasks": 2,
        "remained_tasks": 2,
        "data_source_id": "ds-fcba92ca73b1",
        "domain_id": "domain-58010aa2e451",
        "created_at": "2022-04-02T09:17:44.031Z",
        "updated_at": "2022-04-02T09:19:47.715Z",
        "finished_at": "2022-04-02T09:19:47.715Z",
        "changed": [
        {
        "start": "2021-01-01T00:00:00.000Z"
        }
        ]
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """
        desc: Gets a specific Job. Prints detailed information about the Job, including the plugin used, operation time, and `status`.
        request_example: >-
        {
        "job_id": "job-85cf2c385252"
        }
        response_example: >-
        {
        "job_id": "job-85cf2c385252",
        "status": "SUCCESS",
        "options": {
        "no_preload_cache": false,
        "start": null
        },
        "total_tasks": 1,
        "data_source_id": "ds-c96609f5afeb",
        "domain_id": "domain-58010aa2e451",
        "created_at": "2022-07-17T16:00:08.254Z",
        "updated_at": "2022-07-17T16:01:30.637Z",
        "finished_at": "2022-07-17T16:01:30.637Z",
        "changed": [
        {
        "start": "2022-07-01T00:00:00.000Z"
        }
        ]
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """
        desc: Gets a list of all Jobs. You can use a query to get a filtered list of Jobs.
        request_example: >-
        {
        "query": {}
        }
        response_example: >-
        {
        "results": [
        {
        "job_id": "job-85cf2c385252",
        "status": "SUCCESS",
        "options": {
        "start": null,
        "no_preload_cache": false
        },
        "total_tasks": 1,
        "data_source_id": "ds-c96609f5afeb",
        "domain_id": "domain-58010aa2e451",
        "created_at": "2022-07-17T16:00:08.254Z",
        "updated_at": "2022-07-17T16:01:30.637Z",
        "finished_at": "2022-07-17T16:01:30.637Z",
        "changed": [
        {
        "start": "2022-07-01T00:00:00.000Z"
        }
        ]
        },
        {
        "job_id": "job-6b6765f757a9",
        "status": "SUCCESS",
        "options": {
        "start": null,
        "no_preload_cache": false
        },
        "total_tasks": 2,
        "data_source_id": "ds-fcba92ca73b1",
        "domain_id": "domain-58010aa2e451",
        "created_at": "2022-07-17T16:00:05.077Z",
        "updated_at": "2022-07-17T16:01:28.206Z",
        "finished_at": "2022-07-17T16:01:28.206Z",
        "changed": [
        {
        "start": "2022-07-01T00:00:00.000Z"
        }
        ]
        }
        ],
        "total_count": 372
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


def add_JobServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'cancel': grpc.unary_unary_rpc_method_handler(
                    servicer.cancel,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobInfo.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.GetJobRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.cost_analysis.v1.Job', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Job(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def cancel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_analysis.v1.Job/cancel',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobRequest.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_analysis.v1.Job/get',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.GetJobRequest.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_analysis.v1.Job/list',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobQuery.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobsInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_analysis.v1.Job/stat',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2.JobStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
