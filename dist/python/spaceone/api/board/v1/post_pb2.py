# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/board/v1/post.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n spaceone/api/board/v1/post.proto\x12\x15spaceone.api.board.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\xb4\x01\n\x11\x43reatePostRequest\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x10\n\x08\x63ontents\x18\x04 \x01(\t\x12(\n\x07options\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06writer\x18\x06 \x01(\t\x12\r\n\x05\x66iles\x18\x07 \x03(\t\x12\x11\n\tdomain_id\x18\n \x01(\t\"\xc5\x01\n\x11UpdatePostRequest\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x0f\n\x07post_id\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x10\n\x08\x63ontents\x18\x05 \x01(\t\x12(\n\x07options\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06writer\x18\x07 \x01(\t\x12\r\n\x05\x66iles\x18\x08 \x03(\t\x12\x11\n\tdomain_id\x18\n \x01(\t\"O\n\x17SendNotificationRequest\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x0f\n\x07post_id\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"C\n\x0bPostRequest\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x0f\n\x07post_id\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"T\n\x0eGetPostRequest\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x0f\n\x07post_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\x12\x11\n\tdomain_id\x18\x07 \x01(\t\"\x98\x03\n\tPostQuery\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x0f\n\x07post_id\x18\x02 \x01(\t\x12<\n\tpost_type\x18\x03 \x01(\x0e\x32).spaceone.api.board.v1.PostQuery.PostType\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\x0e\n\x06writer\x18\x05 \x01(\t\x12\x35\n\x05scope\x18\x06 \x01(\x0e\x32&.spaceone.api.board.v1.PostQuery.Scope\x12\x0f\n\x07user_id\x18\x07 \x01(\t\x12\x16\n\x0euser_domain_id\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\t \x01(\t\x12*\n\x05query\x18\n \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\"/\n\x05Scope\x12\x0e\n\nSCOPE_NONE\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\n\n\x06\x44OMAIN\x10\x02\"8\n\x08PostType\x12\x12\n\x0ePOST_TYPE_NONE\x10\x00\x12\n\n\x06SYSTEM\x10\x01\x12\x0c\n\x08INTERNAL\x10\x02\"X\n\rPostStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"\x9b\x04\n\x08PostInfo\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x0f\n\x07post_id\x18\x02 \x01(\t\x12;\n\tpost_type\x18\x03 \x01(\x0e\x32(.spaceone.api.board.v1.PostInfo.PostType\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x10\n\x08\x63ontents\x18\x06 \x01(\t\x12(\n\x07options\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nview_count\x18\x08 \x01(\x05\x12\x0e\n\x06writer\x18\t \x01(\t\x12\x34\n\x05scope\x18\n \x01(\x0e\x32%.spaceone.api.board.v1.PostInfo.Scope\x12)\n\x05\x66iles\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x0f\n\x07user_id\x18\x16 \x01(\t\x12\x16\n\x0euser_domain_id\x18\x17 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\x12\x12\n\nupdated_at\x18  \x01(\t\"/\n\x05Scope\x12\x0e\n\nSCOPE_NONE\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\n\n\x06\x44OMAIN\x10\x02\"8\n\x08PostType\x12\x12\n\x0ePOST_TYPE_NONE\x10\x00\x12\n\n\x06SYSTEM\x10\x01\x12\x0c\n\x08INTERNAL\x10\x02\"R\n\tPostsInfo\x12\x30\n\x07results\x18\x01 \x03(\x0b\x32\x1f.spaceone.api.board.v1.PostInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x32\xaf\x06\n\x04Post\x12v\n\x06\x63reate\x12(.spaceone.api.board.v1.CreatePostRequest\x1a\x1f.spaceone.api.board.v1.PostInfo\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/board/v1/board/create:\x01*\x12v\n\x06update\x12(.spaceone.api.board.v1.UpdatePostRequest\x1a\x1f.spaceone.api.board.v1.PostInfo\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/board/v1/board/update:\x01*\x12\x89\x01\n\x11send_notification\x12..spaceone.api.board.v1.SendNotificationRequest\x1a\x16.google.protobuf.Empty\",\x82\xd3\xe4\x93\x02&\"!/board/v1/board/send-notification:\x01*\x12g\n\x06\x64\x65lete\x12\".spaceone.api.board.v1.PostRequest\x1a\x16.google.protobuf.Empty\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/board/v1/board/delete:\x01*\x12m\n\x03get\x12%.spaceone.api.board.v1.GetPostRequest\x1a\x1f.spaceone.api.board.v1.PostInfo\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/board/v1/board/get:\x01*\x12k\n\x04list\x12 .spaceone.api.board.v1.PostQuery\x1a .spaceone.api.board.v1.PostsInfo\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/board/v1/board/list:\x01*\x12\x66\n\x04stat\x12$.spaceone.api.board.v1.PostStatQuery\x1a\x17.google.protobuf.Struct\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/board/v1/board/stat:\x01*B<Z:github.com/cloudforet-io/api/dist/go/spaceone/api/board/v1b\x06proto3')



_CREATEPOSTREQUEST = DESCRIPTOR.message_types_by_name['CreatePostRequest']
_UPDATEPOSTREQUEST = DESCRIPTOR.message_types_by_name['UpdatePostRequest']
_SENDNOTIFICATIONREQUEST = DESCRIPTOR.message_types_by_name['SendNotificationRequest']
_POSTREQUEST = DESCRIPTOR.message_types_by_name['PostRequest']
_GETPOSTREQUEST = DESCRIPTOR.message_types_by_name['GetPostRequest']
_POSTQUERY = DESCRIPTOR.message_types_by_name['PostQuery']
_POSTSTATQUERY = DESCRIPTOR.message_types_by_name['PostStatQuery']
_POSTINFO = DESCRIPTOR.message_types_by_name['PostInfo']
_POSTSINFO = DESCRIPTOR.message_types_by_name['PostsInfo']
_POSTQUERY_SCOPE = _POSTQUERY.enum_types_by_name['Scope']
_POSTQUERY_POSTTYPE = _POSTQUERY.enum_types_by_name['PostType']
_POSTINFO_SCOPE = _POSTINFO.enum_types_by_name['Scope']
_POSTINFO_POSTTYPE = _POSTINFO.enum_types_by_name['PostType']
CreatePostRequest = _reflection.GeneratedProtocolMessageType('CreatePostRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPOSTREQUEST,
  '__module__' : 'spaceone.api.board.v1.post_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.CreatePostRequest)
  })
_sym_db.RegisterMessage(CreatePostRequest)

UpdatePostRequest = _reflection.GeneratedProtocolMessageType('UpdatePostRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPOSTREQUEST,
  '__module__' : 'spaceone.api.board.v1.post_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.UpdatePostRequest)
  })
_sym_db.RegisterMessage(UpdatePostRequest)

SendNotificationRequest = _reflection.GeneratedProtocolMessageType('SendNotificationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDNOTIFICATIONREQUEST,
  '__module__' : 'spaceone.api.board.v1.post_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.SendNotificationRequest)
  })
_sym_db.RegisterMessage(SendNotificationRequest)

PostRequest = _reflection.GeneratedProtocolMessageType('PostRequest', (_message.Message,), {
  'DESCRIPTOR' : _POSTREQUEST,
  '__module__' : 'spaceone.api.board.v1.post_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.PostRequest)
  })
_sym_db.RegisterMessage(PostRequest)

GetPostRequest = _reflection.GeneratedProtocolMessageType('GetPostRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPOSTREQUEST,
  '__module__' : 'spaceone.api.board.v1.post_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.GetPostRequest)
  })
_sym_db.RegisterMessage(GetPostRequest)

PostQuery = _reflection.GeneratedProtocolMessageType('PostQuery', (_message.Message,), {
  'DESCRIPTOR' : _POSTQUERY,
  '__module__' : 'spaceone.api.board.v1.post_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.PostQuery)
  })
_sym_db.RegisterMessage(PostQuery)

PostStatQuery = _reflection.GeneratedProtocolMessageType('PostStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _POSTSTATQUERY,
  '__module__' : 'spaceone.api.board.v1.post_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.PostStatQuery)
  })
_sym_db.RegisterMessage(PostStatQuery)

PostInfo = _reflection.GeneratedProtocolMessageType('PostInfo', (_message.Message,), {
  'DESCRIPTOR' : _POSTINFO,
  '__module__' : 'spaceone.api.board.v1.post_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.PostInfo)
  })
_sym_db.RegisterMessage(PostInfo)

PostsInfo = _reflection.GeneratedProtocolMessageType('PostsInfo', (_message.Message,), {
  'DESCRIPTOR' : _POSTSINFO,
  '__module__' : 'spaceone.api.board.v1.post_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.PostsInfo)
  })
_sym_db.RegisterMessage(PostsInfo)

_POST = DESCRIPTOR.services_by_name['Post']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z:github.com/cloudforet-io/api/dist/go/spaceone/api/board/v1'
  _POST.methods_by_name['create']._options = None
  _POST.methods_by_name['create']._serialized_options = b'\202\323\344\223\002\033\"\026/board/v1/board/create:\001*'
  _POST.methods_by_name['update']._options = None
  _POST.methods_by_name['update']._serialized_options = b'\202\323\344\223\002\033\"\026/board/v1/board/update:\001*'
  _POST.methods_by_name['send_notification']._options = None
  _POST.methods_by_name['send_notification']._serialized_options = b'\202\323\344\223\002&\"!/board/v1/board/send-notification:\001*'
  _POST.methods_by_name['delete']._options = None
  _POST.methods_by_name['delete']._serialized_options = b'\202\323\344\223\002\033\"\026/board/v1/board/delete:\001*'
  _POST.methods_by_name['get']._options = None
  _POST.methods_by_name['get']._serialized_options = b'\202\323\344\223\002\030\"\023/board/v1/board/get:\001*'
  _POST.methods_by_name['list']._options = None
  _POST.methods_by_name['list']._serialized_options = b'\202\323\344\223\002\031\"\024/board/v1/board/list:\001*'
  _POST.methods_by_name['stat']._options = None
  _POST.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\031\"\024/board/v1/board/stat:\001*'
  _CREATEPOSTREQUEST._serialized_start=183
  _CREATEPOSTREQUEST._serialized_end=363
  _UPDATEPOSTREQUEST._serialized_start=366
  _UPDATEPOSTREQUEST._serialized_end=563
  _SENDNOTIFICATIONREQUEST._serialized_start=565
  _SENDNOTIFICATIONREQUEST._serialized_end=644
  _POSTREQUEST._serialized_start=646
  _POSTREQUEST._serialized_end=713
  _GETPOSTREQUEST._serialized_start=715
  _GETPOSTREQUEST._serialized_end=799
  _POSTQUERY._serialized_start=802
  _POSTQUERY._serialized_end=1210
  _POSTQUERY_SCOPE._serialized_start=1105
  _POSTQUERY_SCOPE._serialized_end=1152
  _POSTQUERY_POSTTYPE._serialized_start=1154
  _POSTQUERY_POSTTYPE._serialized_end=1210
  _POSTSTATQUERY._serialized_start=1212
  _POSTSTATQUERY._serialized_end=1300
  _POSTINFO._serialized_start=1303
  _POSTINFO._serialized_end=1842
  _POSTINFO_SCOPE._serialized_start=1105
  _POSTINFO_SCOPE._serialized_end=1152
  _POSTINFO_POSTTYPE._serialized_start=1154
  _POSTINFO_POSTTYPE._serialized_end=1210
  _POSTSINFO._serialized_start=1844
  _POSTSINFO._serialized_end=1926
  _POST._serialized_start=1929
  _POST._serialized_end=2744
# @@protoc_insertion_point(module_scope)
