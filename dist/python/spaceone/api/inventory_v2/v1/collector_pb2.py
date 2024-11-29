# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/inventory_v2/v1/collector.proto
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
from spaceone.api.inventory_v2.v1 import job_pb2 as spaceone_dot_api_dot_inventory__v2_dot_v1_dot_job__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,spaceone/api/inventory_v2/v1/collector.proto\x12\x1cspaceone.api.inventory_v2.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\x1a&spaceone/api/inventory_v2/v1/job.proto\"\x98\x01\n\tScheduled\x12\x45\n\x05state\x18\x01 \x01(\x0e\x32\x36.spaceone.api.inventory_v2.v1.Scheduled.ScheduledState\x12\r\n\x05hours\x18\x02 \x03(\x05\"5\n\x0eScheduledState\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\xa5\x02\n\x0cSecretFilter\x12K\n\x05state\x18\x01 \x01(\x0e\x32<.spaceone.api.inventory_v2.v1.SecretFilter.SecretFilterState\x12\x0f\n\x07secrets\x18\x02 \x03(\t\x12\x18\n\x10service_accounts\x18\x03 \x03(\t\x12\x0f\n\x07schemas\x18\x04 \x03(\t\x12\x17\n\x0f\x65xclude_secrets\x18\x05 \x03(\t\x12 \n\x18\x65xclude_service_accounts\x18\x06 \x03(\t\x12\x17\n\x0f\x65xclude_schemas\x18\x07 \x03(\t\"8\n\x11SecretFilterState\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\x80\x02\n\nPluginInfo\x12\x11\n\tplugin_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12(\n\x07options\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\n \x01(\x0b\x32\x17.google.protobuf.Struct\x12J\n\x0cupgrade_mode\x18\x0b \x01(\x0e\x32\x34.spaceone.api.inventory_v2.v1.PluginInfo.UpgradeMode\"-\n\x0bUpgradeMode\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06MANUAL\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\"\xd3\x03\n\x16\x43reateCollectorRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12=\n\x0bplugin_info\x18\x02 \x01(\x0b\x32(.spaceone.api.inventory_v2.v1.PluginInfo\x12\x39\n\x08schedule\x18\x03 \x01(\x0b\x32\'.spaceone.api.inventory_v2.v1.Scheduled\x12\x10\n\x08provider\x18\x04 \x01(\t\x12\x41\n\rsecret_filter\x18\x05 \x01(\x0b\x32*.spaceone.api.inventory_v2.v1.SecretFilter\x12%\n\x04tags\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12Z\n\x0eresource_group\x18\x14 \x01(\x0e\x32\x42.spaceone.api.inventory_v2.v1.CreateCollectorRequest.ResourceGroup\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\"C\n\rResourceGroup\x12\x17\n\x13RESOURCE_GROUP_NONE\x10\x00\x12\n\n\x06\x44OMAIN\x10\x01\x12\r\n\tWORKSPACE\x10\x02\"\xe1\x01\n\x16UpdateCollectorRequest\x12\x14\n\x0c\x63ollector_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x39\n\x08schedule\x18\x05 \x01(\x0b\x32\'.spaceone.api.inventory_v2.v1.Scheduled\x12\x41\n\rsecret_filter\x18\x06 \x01(\x0b\x32*.spaceone.api.inventory_v2.v1.SecretFilter\x12%\n\x04tags\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xea\x01\n\x13UpdatePluginRequest\x12\x14\n\x0c\x63ollector_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12(\n\x07options\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12S\n\x0cupgrade_mode\x18\x05 \x01(\x0e\x32=.spaceone.api.inventory_v2.v1.UpdatePluginRequest.UpgradeMode\"-\n\x0bUpgradeMode\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06MANUAL\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\"(\n\x10\x43ollectorRequest\x12\x14\n\x0c\x63ollector_id\x18\x01 \x01(\t\"\xda\x02\n\x0e\x43ollectorQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x14\n\x0c\x63ollector_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12O\n\x13secret_filter_state\x18\x04 \x01(\x0e\x32\x32.spaceone.api.inventory_v2.v1.CollectorQuery.State\x12J\n\x0eschedule_state\x18\x05 \x01(\x0e\x32\x32.spaceone.api.inventory_v2.v1.CollectorQuery.State\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\x12\x11\n\tplugin_id\x18\x16 \x01(\t\"2\n\x05State\x12\x0e\n\nSTATE_NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"9\n\x0e\x43ollectRequest\x12\x14\n\x0c\x63ollector_id\x18\x01 \x01(\t\x12\x11\n\tsecret_id\x18\x02 \x01(\t\">\n\x13VerifyPluginRequest\x12\x14\n\x0c\x63ollector_id\x18\x01 \x01(\t\x12\x11\n\tsecret_id\x18\x02 \x01(\t\"\xdb\x04\n\rCollectorInfo\x12\x14\n\x0c\x63ollector_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x41\n\rsecret_filter\x18\x04 \x01(\x0b\x32*.spaceone.api.inventory_v2.v1.SecretFilter\x12=\n\x0bplugin_info\x18\x05 \x01(\x0b\x32(.spaceone.api.inventory_v2.v1.PluginInfo\x12\x39\n\x08schedule\x18\x06 \x01(\x0b\x32\'.spaceone.api.inventory_v2.v1.Scheduled\x12%\n\x04tags\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12Q\n\x0eresource_group\x18\x14 \x01(\x0e\x32\x39.spaceone.api.inventory_v2.v1.CollectorInfo.ResourceGroup\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\x12\x12\n\nupdated_at\x18  \x01(\t\x12\x19\n\x11last_collected_at\x18! \x01(\t\",\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"C\n\rResourceGroup\x12\x17\n\x13RESOURCE_GROUP_NONE\x10\x00\x12\n\n\x06\x44OMAIN\x10\x01\x12\r\n\tWORKSPACE\x10\x02\"c\n\x0e\x43ollectorsInfo\x12<\n\x07results\x18\x01 \x03(\x0b\x32+.spaceone.api.inventory_v2.v1.CollectorInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"J\n\x12\x43ollectorStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery2\xac\n\n\tCollector\x12\x99\x01\n\x06\x63reate\x12\x34.spaceone.api.inventory_v2.v1.CreateCollectorRequest\x1a+.spaceone.api.inventory_v2.v1.CollectorInfo\",\x82\xd3\xe4\x93\x02&\"!/inventory-v2/v1/collector/create:\x01*\x12\x99\x01\n\x06update\x12\x34.spaceone.api.inventory_v2.v1.UpdateCollectorRequest\x1a+.spaceone.api.inventory_v2.v1.CollectorInfo\",\x82\xd3\xe4\x93\x02&\"!/inventory-v2/v1/collector/update:\x01*\x12\xa4\x01\n\rupdate_plugin\x12\x31.spaceone.api.inventory_v2.v1.UpdatePluginRequest\x1a+.spaceone.api.inventory_v2.v1.CollectorInfo\"3\x82\xd3\xe4\x93\x02-\"(/inventory-v2/v1/collector/update-plugin:\x01*\x12\x8f\x01\n\rverify_plugin\x12\x31.spaceone.api.inventory_v2.v1.VerifyPluginRequest\x1a\x16.google.protobuf.Empty\"3\x82\xd3\xe4\x93\x02-\"(/inventory-v2/v1/collector/verify-plugin:\x01*\x12~\n\x06\x64\x65lete\x12..spaceone.api.inventory_v2.v1.CollectorRequest\x1a\x16.google.protobuf.Empty\",\x82\xd3\xe4\x93\x02&\"!/inventory-v2/v1/collector/delete:\x01*\x12\x8d\x01\n\x03get\x12..spaceone.api.inventory_v2.v1.CollectorRequest\x1a+.spaceone.api.inventory_v2.v1.CollectorInfo\")\x82\xd3\xe4\x93\x02#\"\x1e/inventory-v2/v1/collector/get:\x01*\x12\x8e\x01\n\x04list\x12,.spaceone.api.inventory_v2.v1.CollectorQuery\x1a,.spaceone.api.inventory_v2.v1.CollectorsInfo\"*\x82\xd3\xe4\x93\x02$\"\x1f/inventory-v2/v1/collector/list:\x01*\x12}\n\x04stat\x12\x30.spaceone.api.inventory_v2.v1.CollectorStatQuery\x1a\x17.google.protobuf.Struct\"*\x82\xd3\xe4\x93\x02$\"\x1f/inventory-v2/v1/collector/stat:\x01*\x12\x8d\x01\n\x07\x63ollect\x12,.spaceone.api.inventory_v2.v1.CollectRequest\x1a%.spaceone.api.inventory_v2.v1.JobInfo\"-\x82\xd3\xe4\x93\x02\'\"\"/inventory-v2/v1/collector/collect:\x01*BCZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/inventory-v2/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.inventory_v2.v1.collector_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/inventory-v2/v1'
  _globals['_COLLECTOR'].methods_by_name['create']._loaded_options = None
  _globals['_COLLECTOR'].methods_by_name['create']._serialized_options = b'\202\323\344\223\002&\"!/inventory-v2/v1/collector/create:\001*'
  _globals['_COLLECTOR'].methods_by_name['update']._loaded_options = None
  _globals['_COLLECTOR'].methods_by_name['update']._serialized_options = b'\202\323\344\223\002&\"!/inventory-v2/v1/collector/update:\001*'
  _globals['_COLLECTOR'].methods_by_name['update_plugin']._loaded_options = None
  _globals['_COLLECTOR'].methods_by_name['update_plugin']._serialized_options = b'\202\323\344\223\002-\"(/inventory-v2/v1/collector/update-plugin:\001*'
  _globals['_COLLECTOR'].methods_by_name['verify_plugin']._loaded_options = None
  _globals['_COLLECTOR'].methods_by_name['verify_plugin']._serialized_options = b'\202\323\344\223\002-\"(/inventory-v2/v1/collector/verify-plugin:\001*'
  _globals['_COLLECTOR'].methods_by_name['delete']._loaded_options = None
  _globals['_COLLECTOR'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\002&\"!/inventory-v2/v1/collector/delete:\001*'
  _globals['_COLLECTOR'].methods_by_name['get']._loaded_options = None
  _globals['_COLLECTOR'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002#\"\036/inventory-v2/v1/collector/get:\001*'
  _globals['_COLLECTOR'].methods_by_name['list']._loaded_options = None
  _globals['_COLLECTOR'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002$\"\037/inventory-v2/v1/collector/list:\001*'
  _globals['_COLLECTOR'].methods_by_name['stat']._loaded_options = None
  _globals['_COLLECTOR'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002$\"\037/inventory-v2/v1/collector/stat:\001*'
  _globals['_COLLECTOR'].methods_by_name['collect']._loaded_options = None
  _globals['_COLLECTOR'].methods_by_name['collect']._serialized_options = b'\202\323\344\223\002\'\"\"/inventory-v2/v1/collector/collect:\001*'
  _globals['_SCHEDULED']._serialized_start=242
  _globals['_SCHEDULED']._serialized_end=394
  _globals['_SCHEDULED_SCHEDULEDSTATE']._serialized_start=341
  _globals['_SCHEDULED_SCHEDULEDSTATE']._serialized_end=394
  _globals['_SECRETFILTER']._serialized_start=397
  _globals['_SECRETFILTER']._serialized_end=690
  _globals['_SECRETFILTER_SECRETFILTERSTATE']._serialized_start=634
  _globals['_SECRETFILTER_SECRETFILTERSTATE']._serialized_end=690
  _globals['_PLUGININFO']._serialized_start=693
  _globals['_PLUGININFO']._serialized_end=949
  _globals['_PLUGININFO_UPGRADEMODE']._serialized_start=904
  _globals['_PLUGININFO_UPGRADEMODE']._serialized_end=949
  _globals['_CREATECOLLECTORREQUEST']._serialized_start=952
  _globals['_CREATECOLLECTORREQUEST']._serialized_end=1419
  _globals['_CREATECOLLECTORREQUEST_RESOURCEGROUP']._serialized_start=1352
  _globals['_CREATECOLLECTORREQUEST_RESOURCEGROUP']._serialized_end=1419
  _globals['_UPDATECOLLECTORREQUEST']._serialized_start=1422
  _globals['_UPDATECOLLECTORREQUEST']._serialized_end=1647
  _globals['_UPDATEPLUGINREQUEST']._serialized_start=1650
  _globals['_UPDATEPLUGINREQUEST']._serialized_end=1884
  _globals['_UPDATEPLUGINREQUEST_UPGRADEMODE']._serialized_start=904
  _globals['_UPDATEPLUGINREQUEST_UPGRADEMODE']._serialized_end=949
  _globals['_COLLECTORREQUEST']._serialized_start=1886
  _globals['_COLLECTORREQUEST']._serialized_end=1926
  _globals['_COLLECTORQUERY']._serialized_start=1929
  _globals['_COLLECTORQUERY']._serialized_end=2275
  _globals['_COLLECTORQUERY_STATE']._serialized_start=2225
  _globals['_COLLECTORQUERY_STATE']._serialized_end=2275
  _globals['_COLLECTREQUEST']._serialized_start=2277
  _globals['_COLLECTREQUEST']._serialized_end=2334
  _globals['_VERIFYPLUGINREQUEST']._serialized_start=2336
  _globals['_VERIFYPLUGINREQUEST']._serialized_end=2398
  _globals['_COLLECTORINFO']._serialized_start=2401
  _globals['_COLLECTORINFO']._serialized_end=3004
  _globals['_COLLECTORINFO_STATE']._serialized_start=2891
  _globals['_COLLECTORINFO_STATE']._serialized_end=2935
  _globals['_COLLECTORINFO_RESOURCEGROUP']._serialized_start=1352
  _globals['_COLLECTORINFO_RESOURCEGROUP']._serialized_end=1419
  _globals['_COLLECTORSINFO']._serialized_start=3006
  _globals['_COLLECTORSINFO']._serialized_end=3105
  _globals['_COLLECTORSTATQUERY']._serialized_start=3107
  _globals['_COLLECTORSTATQUERY']._serialized_end=3181
  _globals['_COLLECTOR']._serialized_start=3184
  _globals['_COLLECTOR']._serialized_end=4508
# @@protoc_insertion_point(module_scope)