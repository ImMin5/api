# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/statistics/v1/history.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(spaceone/api/statistics/v1/history.proto\x12\x1aspaceone.api.statistics.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\">\n\x14\x43reateHistoryRequest\x12\x13\n\x0bschedule_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"c\n\x13QueryHistoryRequest\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"q\n\x10HistoryValueInfo\x12\r\n\x05topic\x18\x01 \x01(\t\x12\'\n\x06values\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x03 \x01(\t\x12\x12\n\ncreated_at\x18\x04 \x01(\t\"a\n\x0bHistoryInfo\x12=\n\x07results\x18\x01 \x03(\x0b\x32,.spaceone.api.statistics.v1.HistoryValueInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"l\n\x12HistoryStatRequest\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t2\x8b\x03\n\x07History\x12|\n\x06\x63reate\x12\x30.spaceone.api.statistics.v1.CreateHistoryRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"\"\x1d/statistics/v1/history/create:\x01*\x12\x88\x01\n\x04list\x12/.spaceone.api.statistics.v1.QueryHistoryRequest\x1a\'.spaceone.api.statistics.v1.HistoryInfo\"&\x82\xd3\xe4\x93\x02 \"\x1b/statistics/v1/history/list:\x01*\x12w\n\x04stat\x12..spaceone.api.statistics.v1.HistoryStatRequest\x1a\x17.google.protobuf.Struct\"&\x82\xd3\xe4\x93\x02 \"\x1b/statistics/v1/history/stat:\x01*BAZ?github.com/cloudforet-io/api/dist/go/spaceone/api/statistics/v1b\x06proto3')



_CREATEHISTORYREQUEST = DESCRIPTOR.message_types_by_name['CreateHistoryRequest']
_QUERYHISTORYREQUEST = DESCRIPTOR.message_types_by_name['QueryHistoryRequest']
_HISTORYVALUEINFO = DESCRIPTOR.message_types_by_name['HistoryValueInfo']
_HISTORYINFO = DESCRIPTOR.message_types_by_name['HistoryInfo']
_HISTORYSTATREQUEST = DESCRIPTOR.message_types_by_name['HistoryStatRequest']
CreateHistoryRequest = _reflection.GeneratedProtocolMessageType('CreateHistoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEHISTORYREQUEST,
  '__module__' : 'spaceone.api.statistics.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.statistics.v1.CreateHistoryRequest)
  })
_sym_db.RegisterMessage(CreateHistoryRequest)

QueryHistoryRequest = _reflection.GeneratedProtocolMessageType('QueryHistoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYHISTORYREQUEST,
  '__module__' : 'spaceone.api.statistics.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.statistics.v1.QueryHistoryRequest)
  })
_sym_db.RegisterMessage(QueryHistoryRequest)

HistoryValueInfo = _reflection.GeneratedProtocolMessageType('HistoryValueInfo', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYVALUEINFO,
  '__module__' : 'spaceone.api.statistics.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.statistics.v1.HistoryValueInfo)
  })
_sym_db.RegisterMessage(HistoryValueInfo)

HistoryInfo = _reflection.GeneratedProtocolMessageType('HistoryInfo', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYINFO,
  '__module__' : 'spaceone.api.statistics.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.statistics.v1.HistoryInfo)
  })
_sym_db.RegisterMessage(HistoryInfo)

HistoryStatRequest = _reflection.GeneratedProtocolMessageType('HistoryStatRequest', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYSTATREQUEST,
  '__module__' : 'spaceone.api.statistics.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.statistics.v1.HistoryStatRequest)
  })
_sym_db.RegisterMessage(HistoryStatRequest)

_HISTORY = DESCRIPTOR.services_by_name['History']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z?github.com/cloudforet-io/api/dist/go/spaceone/api/statistics/v1'
  _HISTORY.methods_by_name['create']._options = None
  _HISTORY.methods_by_name['create']._serialized_options = b'\202\323\344\223\002\"\"\035/statistics/v1/history/create:\001*'
  _HISTORY.methods_by_name['list']._options = None
  _HISTORY.methods_by_name['list']._serialized_options = b'\202\323\344\223\002 \"\033/statistics/v1/history/list:\001*'
  _HISTORY.methods_by_name['stat']._options = None
  _HISTORY.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002 \"\033/statistics/v1/history/stat:\001*'
  _CREATEHISTORYREQUEST._serialized_start=195
  _CREATEHISTORYREQUEST._serialized_end=257
  _QUERYHISTORYREQUEST._serialized_start=259
  _QUERYHISTORYREQUEST._serialized_end=358
  _HISTORYVALUEINFO._serialized_start=360
  _HISTORYVALUEINFO._serialized_end=473
  _HISTORYINFO._serialized_start=475
  _HISTORYINFO._serialized_end=572
  _HISTORYSTATREQUEST._serialized_start=574
  _HISTORYSTATREQUEST._serialized_end=682
  _HISTORY._serialized_start=685
  _HISTORY._serialized_end=1080
# @@protoc_insertion_point(module_scope)
