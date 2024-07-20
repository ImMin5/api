# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/dashboard/v1/public_widget.proto
# Protobuf Python Version: 5.26.1
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-spaceone/api/dashboard/v1/public_widget.proto\x12\x19spaceone.api.dashboard.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"\x82\x03\n\x19\x43reatePublicWidgetRequest\x12\x14\n\x0c\x64\x61shboard_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12I\n\x05state\x18\x03 \x01(\x0e\x32:.spaceone.api.dashboard.v1.CreatePublicWidgetRequest.State\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bwidget_type\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x06 \x01(\t\x12(\n\x07options\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0b\x64\x61ta_tables\x18\x08 \x03(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04tags\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\"?\n\x05State\x12\x0e\n\nSTATE_NONE\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08INACTIVE\x10\x03\"\xda\x02\n\x19UpdatePublicWidgetRequest\x12\x11\n\twidget_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12I\n\x05state\x18\x03 \x01(\x0e\x32:.spaceone.api.dashboard.v1.UpdatePublicWidgetRequest.State\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bwidget_type\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x06 \x01(\t\x12(\n\x07options\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x15\n\rdata_table_id\x18\x08 \x01(\t\x12%\n\x04tags\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\"1\n\x05State\x12\x0e\n\nSTATE_NONE\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02\"(\n\x13PublicWidgetRequest\x12\x11\n\twidget_id\x18\x01 \x01(\t\"\x90\x01\n\x17LoadPublicWidgetRequest\x12\x11\n\twidget_id\x18\x01 \x01(\t\x12;\n\x05query\x18\x02 \x01(\x0b\x32,.spaceone.api.core.v2.TimeSeriesAnalyzeQuery\x12%\n\x04vars\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"v\n\x11PublicWidgetQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x14\n\x0c\x64\x61shboard_id\x18\x02 \x01(\t\x12\x11\n\twidget_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"\xf6\x04\n\x10PublicWidgetInfo\x12\x11\n\twidget_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12@\n\x05state\x18\x03 \x01(\x0e\x32\x31.spaceone.api.dashboard.v1.PublicWidgetInfo.State\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bwidget_type\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x06 \x01(\t\x12(\n\x07options\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04tags\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12Q\n\x0eresource_group\x18\x14 \x01(\x0e\x32\x39.spaceone.api.dashboard.v1.PublicWidgetInfo.ResourceGroup\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x12\n\nproject_id\x18\x17 \x01(\t\x12\x14\n\x0c\x64\x61shboard_id\x18\x18 \x01(\t\x12\x15\n\rdata_table_id\x18\x19 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\x12\x12\n\nupdated_at\x18  \x01(\t\"P\n\rResourceGroup\x12\x17\n\x13RESOURCE_GROUP_NONE\x10\x00\x12\n\n\x06\x44OMAIN\x10\x01\x12\r\n\tWORKSPACE\x10\x02\x12\x0b\n\x07PROJECT\x10\x03\"?\n\x05State\x12\x0e\n\nSTATE_NONE\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08INACTIVE\x10\x03\"f\n\x11PublicWidgetsInfo\x12<\n\x07results\x18\x01 \x03(\x0b\x32+.spaceone.api.dashboard.v1.PublicWidgetInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x32\xef\x06\n\x0cPublicWidget\x12\x9a\x01\n\x06\x63reate\x12\x34.spaceone.api.dashboard.v1.CreatePublicWidgetRequest\x1a+.spaceone.api.dashboard.v1.PublicWidgetInfo\"-\x82\xd3\xe4\x93\x02\'\"\"/dashboard/v1/public-widget/create:\x01*\x12\x9a\x01\n\x06update\x12\x34.spaceone.api.dashboard.v1.UpdatePublicWidgetRequest\x1a+.spaceone.api.dashboard.v1.PublicWidgetInfo\"-\x82\xd3\xe4\x93\x02\'\"\"/dashboard/v1/public-widget/update:\x01*\x12\x7f\n\x06\x64\x65lete\x12..spaceone.api.dashboard.v1.PublicWidgetRequest\x1a\x16.google.protobuf.Empty\"-\x82\xd3\xe4\x93\x02\'\"\"/dashboard/v1/public-widget/delete:\x01*\x12\x80\x01\n\x04load\x12\x32.spaceone.api.dashboard.v1.LoadPublicWidgetRequest\x1a\x17.google.protobuf.Struct\"+\x82\xd3\xe4\x93\x02%\" /dashboard/v1/public-widget/load:\x01*\x12\x8e\x01\n\x03get\x12..spaceone.api.dashboard.v1.PublicWidgetRequest\x1a+.spaceone.api.dashboard.v1.PublicWidgetInfo\"*\x82\xd3\xe4\x93\x02$\"\x1f/dashboard/v1/public-widget/get:\x01*\x12\x8f\x01\n\x04list\x12,.spaceone.api.dashboard.v1.PublicWidgetQuery\x1a,.spaceone.api.dashboard.v1.PublicWidgetsInfo\"+\x82\xd3\xe4\x93\x02%\" /dashboard/v1/public-widget/list:\x01*B@Z>github.com/cloudforet-io/api/dist/go/spaceone/api/dashboard/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.dashboard.v1.public_widget_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z>github.com/cloudforet-io/api/dist/go/spaceone/api/dashboard/v1'
  _globals['_PUBLICWIDGET'].methods_by_name['create']._loaded_options = None
  _globals['_PUBLICWIDGET'].methods_by_name['create']._serialized_options = b'\202\323\344\223\002\'\"\"/dashboard/v1/public-widget/create:\001*'
  _globals['_PUBLICWIDGET'].methods_by_name['update']._loaded_options = None
  _globals['_PUBLICWIDGET'].methods_by_name['update']._serialized_options = b'\202\323\344\223\002\'\"\"/dashboard/v1/public-widget/update:\001*'
  _globals['_PUBLICWIDGET'].methods_by_name['delete']._loaded_options = None
  _globals['_PUBLICWIDGET'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\002\'\"\"/dashboard/v1/public-widget/delete:\001*'
  _globals['_PUBLICWIDGET'].methods_by_name['load']._loaded_options = None
  _globals['_PUBLICWIDGET'].methods_by_name['load']._serialized_options = b'\202\323\344\223\002%\" /dashboard/v1/public-widget/load:\001*'
  _globals['_PUBLICWIDGET'].methods_by_name['get']._loaded_options = None
  _globals['_PUBLICWIDGET'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002$\"\037/dashboard/v1/public-widget/get:\001*'
  _globals['_PUBLICWIDGET'].methods_by_name['list']._loaded_options = None
  _globals['_PUBLICWIDGET'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002%\" /dashboard/v1/public-widget/list:\001*'
  _globals['_CREATEPUBLICWIDGETREQUEST']._serialized_start=200
  _globals['_CREATEPUBLICWIDGETREQUEST']._serialized_end=586
  _globals['_CREATEPUBLICWIDGETREQUEST_STATE']._serialized_start=523
  _globals['_CREATEPUBLICWIDGETREQUEST_STATE']._serialized_end=586
  _globals['_UPDATEPUBLICWIDGETREQUEST']._serialized_start=589
  _globals['_UPDATEPUBLICWIDGETREQUEST']._serialized_end=935
  _globals['_UPDATEPUBLICWIDGETREQUEST_STATE']._serialized_start=886
  _globals['_UPDATEPUBLICWIDGETREQUEST_STATE']._serialized_end=935
  _globals['_PUBLICWIDGETREQUEST']._serialized_start=937
  _globals['_PUBLICWIDGETREQUEST']._serialized_end=977
  _globals['_LOADPUBLICWIDGETREQUEST']._serialized_start=980
  _globals['_LOADPUBLICWIDGETREQUEST']._serialized_end=1124
  _globals['_PUBLICWIDGETQUERY']._serialized_start=1126
  _globals['_PUBLICWIDGETQUERY']._serialized_end=1244
  _globals['_PUBLICWIDGETINFO']._serialized_start=1247
  _globals['_PUBLICWIDGETINFO']._serialized_end=1877
  _globals['_PUBLICWIDGETINFO_RESOURCEGROUP']._serialized_start=1732
  _globals['_PUBLICWIDGETINFO_RESOURCEGROUP']._serialized_end=1812
  _globals['_PUBLICWIDGETINFO_STATE']._serialized_start=523
  _globals['_PUBLICWIDGETINFO_STATE']._serialized_end=586
  _globals['_PUBLICWIDGETSINFO']._serialized_start=1879
  _globals['_PUBLICWIDGETSINFO']._serialized_end=1981
  _globals['_PUBLICWIDGET']._serialized_start=1984
  _globals['_PUBLICWIDGET']._serialized_end=2863
# @@protoc_insertion_point(module_scope)
