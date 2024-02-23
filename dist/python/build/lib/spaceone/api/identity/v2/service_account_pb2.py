# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v2/service_account.proto
# Protobuf Python Version: 4.25.1
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
from spaceone.api.core.v2 import query_pb2 as spaceone_dot_api_dot_core_dot_v2_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.spaceone/api/identity/v2/service_account.proto\x12\x18spaceone.api.identity.v2\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"\x83\x02\n\x1b\x43reateServiceAccountRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x18\n\x10secret_schema_id\x18\x04 \x01(\t\x12,\n\x0bsecret_data\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04tags\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x1a\n\x12trusted_account_id\x18\x15 \x01(\t\x12\x12\n\nproject_id\x18\x16 \x01(\t\"\xa9\x01\n\x1bUpdateServiceAccountRequest\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nproject_id\x18\x17 \x01(\t\"\xa3\x01\n!UpdateServiceAccountSecretRequest\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\x12\x18\n\x10secret_schema_id\x18\x02 \x01(\t\x12,\n\x0bsecret_data\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x1a\n\x12trusted_account_id\x18\x15 \x01(\t\"3\n\x15ServiceAccountRequest\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\"\xb8\x02\n\x12ServiceAccountInfo\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08provider\x18\x04 \x01(\t\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x12\n\nproject_id\x18\x17 \x01(\t\x12\x1a\n\x12trusted_account_id\x18\x18 \x01(\t\x12\x18\n\x10secret_schema_id\x18\x19 \x01(\t\x12\x11\n\tsecret_id\x18\x1a \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\"\xf6\x01\n\x19ServiceAccountSearchQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x1a\n\x12service_account_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08provider\x18\x04 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\x12\x12\n\nproject_id\x18\x17 \x01(\t\x12\x1a\n\x12trusted_account_id\x18\x18 \x01(\t\x12\x18\n\x10secret_schema_id\x18\x19 \x01(\t\x12\x11\n\tsecret_id\x18\x1a \x01(\t\"i\n\x13ServiceAccountsInfo\x12=\n\x07results\x18\x01 \x03(\x0b\x32,.spaceone.api.identity.v2.ServiceAccountInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"O\n\x17ServiceAccountStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery2\xf6\t\n\x0eServiceAccount\x12\x9d\x01\n\x06\x63reate\x12\x35.spaceone.api.identity.v2.CreateServiceAccountRequest\x1a,.spaceone.api.identity.v2.ServiceAccountInfo\".\x82\xd3\xe4\x93\x02(\"#/identity/v2/service-account/create:\x01*\x12\x9d\x01\n\x06update\x12\x35.spaceone.api.identity.v2.UpdateServiceAccountRequest\x1a,.spaceone.api.identity.v2.ServiceAccountInfo\".\x82\xd3\xe4\x93\x02(\"#/identity/v2/service-account/update:\x01*\x12\xbb\x01\n\x12update_secret_data\x12;.spaceone.api.identity.v2.UpdateServiceAccountSecretRequest\x1a,.spaceone.api.identity.v2.ServiceAccountInfo\":\x82\xd3\xe4\x93\x02\x34\"//identity/v2/service-account/update-secret-data:\x01*\x12\xaf\x01\n\x12\x64\x65lete_secret_data\x12/.spaceone.api.identity.v2.ServiceAccountRequest\x1a,.spaceone.api.identity.v2.ServiceAccountInfo\":\x82\xd3\xe4\x93\x02\x34\"//identity/v2/service-account/delete-secret-data:\x01*\x12\x81\x01\n\x06\x64\x65lete\x12/.spaceone.api.identity.v2.ServiceAccountRequest\x1a\x16.google.protobuf.Empty\".\x82\xd3\xe4\x93\x02(\"#/identity/v2/service-account/delete:\x01*\x12\x91\x01\n\x03get\x12/.spaceone.api.identity.v2.ServiceAccountRequest\x1a,.spaceone.api.identity.v2.ServiceAccountInfo\"+\x82\xd3\xe4\x93\x02%\" /identity/v2/service-account/get:\x01*\x12\x98\x01\n\x04list\x12\x33.spaceone.api.identity.v2.ServiceAccountSearchQuery\x1a-.spaceone.api.identity.v2.ServiceAccountsInfo\",\x82\xd3\xe4\x93\x02&\"!/identity/v2/service-account/list:\x01*\x12\x80\x01\n\x04stat\x12\x31.spaceone.api.identity.v2.ServiceAccountStatQuery\x1a\x17.google.protobuf.Struct\",\x82\xd3\xe4\x93\x02&\"!/identity/v2/service-account/stat:\x01*B?Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.identity.v2.service_account_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v2'
  _globals['_SERVICEACCOUNT'].methods_by_name['create']._options = None
  _globals['_SERVICEACCOUNT'].methods_by_name['create']._serialized_options = b'\202\323\344\223\002(\"#/identity/v2/service-account/create:\001*'
  _globals['_SERVICEACCOUNT'].methods_by_name['update']._options = None
  _globals['_SERVICEACCOUNT'].methods_by_name['update']._serialized_options = b'\202\323\344\223\002(\"#/identity/v2/service-account/update:\001*'
  _globals['_SERVICEACCOUNT'].methods_by_name['update_secret_data']._options = None
  _globals['_SERVICEACCOUNT'].methods_by_name['update_secret_data']._serialized_options = b'\202\323\344\223\0024\"//identity/v2/service-account/update-secret-data:\001*'
  _globals['_SERVICEACCOUNT'].methods_by_name['delete_secret_data']._options = None
  _globals['_SERVICEACCOUNT'].methods_by_name['delete_secret_data']._serialized_options = b'\202\323\344\223\0024\"//identity/v2/service-account/delete-secret-data:\001*'
  _globals['_SERVICEACCOUNT'].methods_by_name['delete']._options = None
  _globals['_SERVICEACCOUNT'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\002(\"#/identity/v2/service-account/delete:\001*'
  _globals['_SERVICEACCOUNT'].methods_by_name['get']._options = None
  _globals['_SERVICEACCOUNT'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002%\" /identity/v2/service-account/get:\001*'
  _globals['_SERVICEACCOUNT'].methods_by_name['list']._options = None
  _globals['_SERVICEACCOUNT'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002&\"!/identity/v2/service-account/list:\001*'
  _globals['_SERVICEACCOUNT'].methods_by_name['stat']._options = None
  _globals['_SERVICEACCOUNT'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002&\"!/identity/v2/service-account/stat:\001*'
  _globals['_CREATESERVICEACCOUNTREQUEST']._serialized_start=200
  _globals['_CREATESERVICEACCOUNTREQUEST']._serialized_end=459
  _globals['_UPDATESERVICEACCOUNTREQUEST']._serialized_start=462
  _globals['_UPDATESERVICEACCOUNTREQUEST']._serialized_end=631
  _globals['_UPDATESERVICEACCOUNTSECRETREQUEST']._serialized_start=634
  _globals['_UPDATESERVICEACCOUNTSECRETREQUEST']._serialized_end=797
  _globals['_SERVICEACCOUNTREQUEST']._serialized_start=799
  _globals['_SERVICEACCOUNTREQUEST']._serialized_end=850
  _globals['_SERVICEACCOUNTINFO']._serialized_start=853
  _globals['_SERVICEACCOUNTINFO']._serialized_end=1165
  _globals['_SERVICEACCOUNTSEARCHQUERY']._serialized_start=1168
  _globals['_SERVICEACCOUNTSEARCHQUERY']._serialized_end=1414
  _globals['_SERVICEACCOUNTSINFO']._serialized_start=1416
  _globals['_SERVICEACCOUNTSINFO']._serialized_end=1521
  _globals['_SERVICEACCOUNTSTATQUERY']._serialized_start=1523
  _globals['_SERVICEACCOUNTSTATQUERY']._serialized_end=1602
  _globals['_SERVICEACCOUNT']._serialized_start=1605
  _globals['_SERVICEACCOUNT']._serialized_end=2875
# @@protoc_insertion_point(module_scope)
