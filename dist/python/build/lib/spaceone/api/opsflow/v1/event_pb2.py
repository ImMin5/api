# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/opsflow/v1/event.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v2 import query_pb2 as spaceone_dot_api_dot_core_dot_v2_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#spaceone/api/opsflow/v1/event.proto\x12\x17spaceone.api.opsflow.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"\xf1\x01\n\x10\x45ventSearchQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12@\n\nevent_type\x18\x03 \x01(\x0e\x32,.spaceone.api.opsflow.v1.EventInfo.EventType\x12\x11\n\tuser_type\x18\x04 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x05 \x01(\t\x12\x0f\n\x07user_id\x18\x06 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x07 \x01(\t\x12\x12\n\nproject_id\x18\x08 \x01(\t\"\xf9\x02\n\tEventInfo\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12@\n\nevent_type\x18\x02 \x01(\x0e\x32,.spaceone.api.opsflow.v1.EventInfo.EventType\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x11\n\tuser_type\x18\x05 \x01(\t\x12\x0f\n\x07user_id\x18\x06 \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x12\n\nproject_id\x18\x17 \x01(\t\x12\x0f\n\x07task_id\x18\x18 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\x12\x12\n\nupdated_at\x18  \x01(\t\"[\n\tEventType\x12\x12\n\x0eSELECTION_NONE\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\x0b\n\x07UPDATED\x10\x02\x12\x11\n\rCHANGE_STATUS\x10\x03\x12\r\n\tCOMMENTED\x10\x04\"V\n\nEventsInfo\x12\x33\n\x07results\x18\x01 \x03(\x0b\x32\".spaceone.api.opsflow.v1.EventInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"F\n\x0e\x45ventStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery2\xef\x01\n\x05\x45vent\x12y\n\x04list\x12).spaceone.api.opsflow.v1.EventSearchQuery\x1a#.spaceone.api.opsflow.v1.EventsInfo\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/opsflow/v1/event/list:\x01*\x12k\n\x04stat\x12\'.spaceone.api.opsflow.v1.EventStatQuery\x1a\x17.google.protobuf.Struct\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/opsflow/v1/event/stat:\x01*B>Z<github.com/cloudforet-io/api/dist/go/spaceone/api/opsflow/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.opsflow.v1.event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/cloudforet-io/api/dist/go/spaceone/api/opsflow/v1'
  _globals['_EVENT'].methods_by_name['list']._loaded_options = None
  _globals['_EVENT'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002\033\"\026/opsflow/v1/event/list:\001*'
  _globals['_EVENT'].methods_by_name['stat']._loaded_options = None
  _globals['_EVENT'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\033\"\026/opsflow/v1/event/stat:\001*'
  _globals['_EVENTSEARCHQUERY']._serialized_start=159
  _globals['_EVENTSEARCHQUERY']._serialized_end=400
  _globals['_EVENTINFO']._serialized_start=403
  _globals['_EVENTINFO']._serialized_end=780
  _globals['_EVENTINFO_EVENTTYPE']._serialized_start=689
  _globals['_EVENTINFO_EVENTTYPE']._serialized_end=780
  _globals['_EVENTSINFO']._serialized_start=782
  _globals['_EVENTSINFO']._serialized_end=868
  _globals['_EVENTSTATQUERY']._serialized_start=870
  _globals['_EVENTSTATQUERY']._serialized_end=940
  _globals['_EVENT']._serialized_start=943
  _globals['_EVENT']._serialized_end=1182
# @@protoc_insertion_point(module_scope)
