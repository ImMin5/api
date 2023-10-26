# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/inventory/v1/cloud_service_query_set.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7spaceone/api/inventory/v1/cloud_service_query_set.proto\x12\x19spaceone.api.inventory.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\x98\x02\n!CreateCloudServiceQuerySetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x39\n\rquery_options\x18\x02 \x01(\x0b\x32\".spaceone.api.core.v1.AnalyzeQuery\x12%\n\x04unit\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08provider\x18\x04 \x01(\t\x12\x1b\n\x13\x63loud_service_group\x18\x05 \x01(\t\x12\x1a\n\x12\x63loud_service_type\x18\x06 \x01(\t\x12%\n\x04tags\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"\xe3\x01\n!UpdateCloudServiceQuerySetRequest\x12\x14\n\x0cquery_set_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x39\n\rquery_options\x18\x03 \x01(\x0b\x32\".spaceone.api.core.v1.AnalyzeQuery\x12%\n\x04unit\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04tags\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"F\n\x1b\x43loudServiceQuerySetRequest\x12\x14\n\x0cquery_set_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"W\n\x1eGetCloudServiceQuerySetRequest\x12\x14\n\x0cquery_set_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\xd7\x03\n\x19\x43loudServiceQuerySetQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x14\n\x0cquery_set_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12I\n\x05state\x18\x04 \x01(\x0e\x32:.spaceone.api.inventory.v1.CloudServiceQuerySetQuery.State\x12R\n\nquery_type\x18\x05 \x01(\x0e\x32>.spaceone.api.inventory.v1.CloudServiceQuerySetQuery.QueryType\x12\x10\n\x08provider\x18\x06 \x01(\t\x12\x1b\n\x13\x63loud_service_group\x18\x07 \x01(\t\x12\x1a\n\x12\x63loud_service_type\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"2\n\x05State\x12\x0e\n\nNONE_STATE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"9\n\tQueryType\x12\x13\n\x0fNONE_QUERY_TYPE\x10\x00\x12\x0b\n\x07MANAGED\x10\x01\x12\n\n\x06\x43USTOM\x10\x02\"\x85\x05\n\x18\x43loudServiceQuerySetInfo\x12\x14\n\x0cquery_set_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12H\n\x05state\x18\x03 \x01(\x0e\x32\x39.spaceone.api.inventory.v1.CloudServiceQuerySetInfo.State\x12\x39\n\rquery_options\x18\x04 \x01(\x0b\x32\".spaceone.api.core.v1.AnalyzeQuery\x12Q\n\nquery_type\x18\x05 \x01(\x0e\x32=.spaceone.api.inventory.v1.CloudServiceQuerySetInfo.QueryType\x12%\n\x04unit\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0c\n\x04keys\x18\x07 \x03(\t\x12\x1c\n\x14\x61\x64\x64itional_info_keys\x18\x08 \x03(\t\x12\x10\n\x08provider\x18\t \x01(\t\x12\x1b\n\x13\x63loud_service_group\x18\n \x01(\t\x12\x1a\n\x12\x63loud_service_type\x18\x0b \x01(\t\x12%\n\x04tags\x18\x15 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x1f \x01(\t\x12\x12\n\ncreated_at\x18) \x01(\t\x12\x12\n\nupdated_at\x18* \x01(\t\"2\n\x05State\x12\x0e\n\nNONE_STATE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"9\n\tQueryType\x12\x13\n\x0fNONE_QUERY_TYPE\x10\x00\x12\x0b\n\x07MANAGED\x10\x01\x12\n\n\x06\x43USTOM\x10\x02\"v\n\x19\x43loudServiceQuerySetsInfo\x12\x44\n\x07results\x18\x01 \x03(\x0b\x32\x33.spaceone.api.inventory.v1.CloudServiceQuerySetInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"h\n\x1d\x43loudServiceQuerySetStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\x88\r\n\x14\x43loudServiceQuerySet\x12\xb4\x01\n\x06\x63reate\x12<.spaceone.api.inventory.v1.CreateCloudServiceQuerySetRequest\x1a\x33.spaceone.api.inventory.v1.CloudServiceQuerySetInfo\"7\x82\xd3\xe4\x93\x02\x31\",/inventory/v1/cloud-service-query-set/create:\x01*\x12\xb4\x01\n\x06update\x12<.spaceone.api.inventory.v1.UpdateCloudServiceQuerySetRequest\x1a\x33.spaceone.api.inventory.v1.CloudServiceQuerySetInfo\"7\x82\xd3\xe4\x93\x02\x31\",/inventory/v1/cloud-service-query-set/update:\x01*\x12\x91\x01\n\x06\x64\x65lete\x12\x36.spaceone.api.inventory.v1.CloudServiceQuerySetRequest\x1a\x16.google.protobuf.Empty\"7\x82\xd3\xe4\x93\x02\x31\",/inventory/v1/cloud-service-query-set/delete:\x01*\x12\x8b\x01\n\x03run\x12\x36.spaceone.api.inventory.v1.CloudServiceQuerySetRequest\x1a\x16.google.protobuf.Empty\"4\x82\xd3\xe4\x93\x02.\")/inventory/v1/cloud-service-query-set/run:\x01*\x12\x8e\x01\n\x04test\x12\x36.spaceone.api.inventory.v1.CloudServiceQuerySetRequest\x1a\x17.google.protobuf.Struct\"5\x82\xd3\xe4\x93\x02/\"*/inventory/v1/cloud-service-query-set/test:\x01*\x12\xae\x01\n\x06\x65nable\x12\x36.spaceone.api.inventory.v1.CloudServiceQuerySetRequest\x1a\x33.spaceone.api.inventory.v1.CloudServiceQuerySetInfo\"7\x82\xd3\xe4\x93\x02\x31\",/inventory/v1/cloud-service-query-set/enable:\x01*\x12\xb0\x01\n\x07\x64isable\x12\x36.spaceone.api.inventory.v1.CloudServiceQuerySetRequest\x1a\x33.spaceone.api.inventory.v1.CloudServiceQuerySetInfo\"8\x82\xd3\xe4\x93\x02\x32\"-/inventory/v1/cloud-service-query-set/disable:\x01*\x12\xab\x01\n\x03get\x12\x39.spaceone.api.inventory.v1.GetCloudServiceQuerySetRequest\x1a\x33.spaceone.api.inventory.v1.CloudServiceQuerySetInfo\"4\x82\xd3\xe4\x93\x02.\")/inventory/v1/cloud-service-query-set/get:\x01*\x12\xa9\x01\n\x04list\x12\x34.spaceone.api.inventory.v1.CloudServiceQuerySetQuery\x1a\x34.spaceone.api.inventory.v1.CloudServiceQuerySetsInfo\"5\x82\xd3\xe4\x93\x02/\"*/inventory/v1/cloud-service-query-set/list:\x01*\x12\x90\x01\n\x04stat\x12\x38.spaceone.api.inventory.v1.CloudServiceQuerySetStatQuery\x1a\x17.google.protobuf.Struct\"5\x82\xd3\xe4\x93\x02/\"*/inventory/v1/cloud-service-query-set/stat:\x01*B@Z>github.com/cloudforet-io/api/dist/go/spaceone/api/inventory/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.inventory.v1.cloud_service_query_set_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z>github.com/cloudforet-io/api/dist/go/spaceone/api/inventory/v1'
  _CLOUDSERVICEQUERYSET.methods_by_name['create']._options = None
  _CLOUDSERVICEQUERYSET.methods_by_name['create']._serialized_options = b'\202\323\344\223\0021\",/inventory/v1/cloud-service-query-set/create:\001*'
  _CLOUDSERVICEQUERYSET.methods_by_name['update']._options = None
  _CLOUDSERVICEQUERYSET.methods_by_name['update']._serialized_options = b'\202\323\344\223\0021\",/inventory/v1/cloud-service-query-set/update:\001*'
  _CLOUDSERVICEQUERYSET.methods_by_name['delete']._options = None
  _CLOUDSERVICEQUERYSET.methods_by_name['delete']._serialized_options = b'\202\323\344\223\0021\",/inventory/v1/cloud-service-query-set/delete:\001*'
  _CLOUDSERVICEQUERYSET.methods_by_name['run']._options = None
  _CLOUDSERVICEQUERYSET.methods_by_name['run']._serialized_options = b'\202\323\344\223\002.\")/inventory/v1/cloud-service-query-set/run:\001*'
  _CLOUDSERVICEQUERYSET.methods_by_name['test']._options = None
  _CLOUDSERVICEQUERYSET.methods_by_name['test']._serialized_options = b'\202\323\344\223\002/\"*/inventory/v1/cloud-service-query-set/test:\001*'
  _CLOUDSERVICEQUERYSET.methods_by_name['enable']._options = None
  _CLOUDSERVICEQUERYSET.methods_by_name['enable']._serialized_options = b'\202\323\344\223\0021\",/inventory/v1/cloud-service-query-set/enable:\001*'
  _CLOUDSERVICEQUERYSET.methods_by_name['disable']._options = None
  _CLOUDSERVICEQUERYSET.methods_by_name['disable']._serialized_options = b'\202\323\344\223\0022\"-/inventory/v1/cloud-service-query-set/disable:\001*'
  _CLOUDSERVICEQUERYSET.methods_by_name['get']._options = None
  _CLOUDSERVICEQUERYSET.methods_by_name['get']._serialized_options = b'\202\323\344\223\002.\")/inventory/v1/cloud-service-query-set/get:\001*'
  _CLOUDSERVICEQUERYSET.methods_by_name['list']._options = None
  _CLOUDSERVICEQUERYSET.methods_by_name['list']._serialized_options = b'\202\323\344\223\002/\"*/inventory/v1/cloud-service-query-set/list:\001*'
  _CLOUDSERVICEQUERYSET.methods_by_name['stat']._options = None
  _CLOUDSERVICEQUERYSET.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002/\"*/inventory/v1/cloud-service-query-set/stat:\001*'
  _globals['_CREATECLOUDSERVICEQUERYSETREQUEST']._serialized_start=210
  _globals['_CREATECLOUDSERVICEQUERYSETREQUEST']._serialized_end=490
  _globals['_UPDATECLOUDSERVICEQUERYSETREQUEST']._serialized_start=493
  _globals['_UPDATECLOUDSERVICEQUERYSETREQUEST']._serialized_end=720
  _globals['_CLOUDSERVICEQUERYSETREQUEST']._serialized_start=722
  _globals['_CLOUDSERVICEQUERYSETREQUEST']._serialized_end=792
  _globals['_GETCLOUDSERVICEQUERYSETREQUEST']._serialized_start=794
  _globals['_GETCLOUDSERVICEQUERYSETREQUEST']._serialized_end=881
  _globals['_CLOUDSERVICEQUERYSETQUERY']._serialized_start=884
  _globals['_CLOUDSERVICEQUERYSETQUERY']._serialized_end=1355
  _globals['_CLOUDSERVICEQUERYSETQUERY_STATE']._serialized_start=1246
  _globals['_CLOUDSERVICEQUERYSETQUERY_STATE']._serialized_end=1296
  _globals['_CLOUDSERVICEQUERYSETQUERY_QUERYTYPE']._serialized_start=1298
  _globals['_CLOUDSERVICEQUERYSETQUERY_QUERYTYPE']._serialized_end=1355
  _globals['_CLOUDSERVICEQUERYSETINFO']._serialized_start=1358
  _globals['_CLOUDSERVICEQUERYSETINFO']._serialized_end=2003
  _globals['_CLOUDSERVICEQUERYSETINFO_STATE']._serialized_start=1246
  _globals['_CLOUDSERVICEQUERYSETINFO_STATE']._serialized_end=1296
  _globals['_CLOUDSERVICEQUERYSETINFO_QUERYTYPE']._serialized_start=1298
  _globals['_CLOUDSERVICEQUERYSETINFO_QUERYTYPE']._serialized_end=1355
  _globals['_CLOUDSERVICEQUERYSETSINFO']._serialized_start=2005
  _globals['_CLOUDSERVICEQUERYSETSINFO']._serialized_end=2123
  _globals['_CLOUDSERVICEQUERYSETSTATQUERY']._serialized_start=2125
  _globals['_CLOUDSERVICEQUERYSETSTATQUERY']._serialized_end=2229
  _globals['_CLOUDSERVICEQUERYSET']._serialized_start=2232
  _globals['_CLOUDSERVICEQUERYSET']._serialized_end=3904
# @@protoc_insertion_point(module_scope)
