# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/board/v1/board.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!spaceone/api/board/v1/board.proto\x12\x15spaceone.api.board.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"]\n\x12\x43reateBoardRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncategories\x18\x02 \x03(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"[\n\x12UpdateBoardRequest\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"A\n\x19SetBoardCategoriesRequest\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x12\n\ncategories\x18\x02 \x03(\t\" \n\x0c\x42oardRequest\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\"1\n\x0fGetBoardRequest\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"X\n\nBoardQuery\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\x05query\x18\x03 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\"F\n\x0e\x42oardStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\"z\n\tBoardInfo\x12\x10\n\x08\x62oard_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ncategories\x18\x03 \x03(\t\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\ncreated_at\x18\x0b \x01(\t\"T\n\nBoardsInfo\x12\x31\n\x07results\x18\x01 \x03(\x0b\x32 .spaceone.api.board.v1.BoardInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x32\xc0\x06\n\x05\x42oard\x12x\n\x06\x63reate\x12).spaceone.api.board.v1.CreateBoardRequest\x1a .spaceone.api.board.v1.BoardInfo\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/board/v1/board/create:\x01*\x12x\n\x06update\x12).spaceone.api.board.v1.UpdateBoardRequest\x1a .spaceone.api.board.v1.BoardInfo\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/board/v1/board/update:\x01*\x12\x8f\x01\n\x0eset_categories\x12\x30.spaceone.api.board.v1.SetBoardCategoriesRequest\x1a .spaceone.api.board.v1.BoardInfo\")\x82\xd3\xe4\x93\x02#\"\x1e/board/v1/board/set-categories:\x01*\x12h\n\x06\x64\x65lete\x12#.spaceone.api.board.v1.BoardRequest\x1a\x16.google.protobuf.Empty\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/board/v1/board/delete:\x01*\x12o\n\x03get\x12&.spaceone.api.board.v1.GetBoardRequest\x1a .spaceone.api.board.v1.BoardInfo\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/board/v1/board/get:\x01*\x12m\n\x04list\x12!.spaceone.api.board.v1.BoardQuery\x1a!.spaceone.api.board.v1.BoardsInfo\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/board/v1/board/list:\x01*\x12g\n\x04stat\x12%.spaceone.api.board.v1.BoardStatQuery\x1a\x17.google.protobuf.Struct\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/board/v1/board/stat:\x01*B<Z:github.com/cloudforet-io/api/dist/go/spaceone/api/board/v1b\x06proto3')



_CREATEBOARDREQUEST = DESCRIPTOR.message_types_by_name['CreateBoardRequest']
_UPDATEBOARDREQUEST = DESCRIPTOR.message_types_by_name['UpdateBoardRequest']
_SETBOARDCATEGORIESREQUEST = DESCRIPTOR.message_types_by_name['SetBoardCategoriesRequest']
_BOARDREQUEST = DESCRIPTOR.message_types_by_name['BoardRequest']
_GETBOARDREQUEST = DESCRIPTOR.message_types_by_name['GetBoardRequest']
_BOARDQUERY = DESCRIPTOR.message_types_by_name['BoardQuery']
_BOARDSTATQUERY = DESCRIPTOR.message_types_by_name['BoardStatQuery']
_BOARDINFO = DESCRIPTOR.message_types_by_name['BoardInfo']
_BOARDSINFO = DESCRIPTOR.message_types_by_name['BoardsInfo']
CreateBoardRequest = _reflection.GeneratedProtocolMessageType('CreateBoardRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBOARDREQUEST,
  '__module__' : 'spaceone.api.board.v1.board_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.CreateBoardRequest)
  })
_sym_db.RegisterMessage(CreateBoardRequest)

UpdateBoardRequest = _reflection.GeneratedProtocolMessageType('UpdateBoardRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBOARDREQUEST,
  '__module__' : 'spaceone.api.board.v1.board_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.UpdateBoardRequest)
  })
_sym_db.RegisterMessage(UpdateBoardRequest)

SetBoardCategoriesRequest = _reflection.GeneratedProtocolMessageType('SetBoardCategoriesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETBOARDCATEGORIESREQUEST,
  '__module__' : 'spaceone.api.board.v1.board_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.SetBoardCategoriesRequest)
  })
_sym_db.RegisterMessage(SetBoardCategoriesRequest)

BoardRequest = _reflection.GeneratedProtocolMessageType('BoardRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOARDREQUEST,
  '__module__' : 'spaceone.api.board.v1.board_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.BoardRequest)
  })
_sym_db.RegisterMessage(BoardRequest)

GetBoardRequest = _reflection.GeneratedProtocolMessageType('GetBoardRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBOARDREQUEST,
  '__module__' : 'spaceone.api.board.v1.board_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.GetBoardRequest)
  })
_sym_db.RegisterMessage(GetBoardRequest)

BoardQuery = _reflection.GeneratedProtocolMessageType('BoardQuery', (_message.Message,), {
  'DESCRIPTOR' : _BOARDQUERY,
  '__module__' : 'spaceone.api.board.v1.board_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.BoardQuery)
  })
_sym_db.RegisterMessage(BoardQuery)

BoardStatQuery = _reflection.GeneratedProtocolMessageType('BoardStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _BOARDSTATQUERY,
  '__module__' : 'spaceone.api.board.v1.board_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.BoardStatQuery)
  })
_sym_db.RegisterMessage(BoardStatQuery)

BoardInfo = _reflection.GeneratedProtocolMessageType('BoardInfo', (_message.Message,), {
  'DESCRIPTOR' : _BOARDINFO,
  '__module__' : 'spaceone.api.board.v1.board_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.BoardInfo)
  })
_sym_db.RegisterMessage(BoardInfo)

BoardsInfo = _reflection.GeneratedProtocolMessageType('BoardsInfo', (_message.Message,), {
  'DESCRIPTOR' : _BOARDSINFO,
  '__module__' : 'spaceone.api.board.v1.board_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.board.v1.BoardsInfo)
  })
_sym_db.RegisterMessage(BoardsInfo)

_BOARD = DESCRIPTOR.services_by_name['Board']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z:github.com/cloudforet-io/api/dist/go/spaceone/api/board/v1'
  _BOARD.methods_by_name['create']._options = None
  _BOARD.methods_by_name['create']._serialized_options = b'\202\323\344\223\002\033\"\026/board/v1/board/create:\001*'
  _BOARD.methods_by_name['update']._options = None
  _BOARD.methods_by_name['update']._serialized_options = b'\202\323\344\223\002\033\"\026/board/v1/board/update:\001*'
  _BOARD.methods_by_name['set_categories']._options = None
  _BOARD.methods_by_name['set_categories']._serialized_options = b'\202\323\344\223\002#\"\036/board/v1/board/set-categories:\001*'
  _BOARD.methods_by_name['delete']._options = None
  _BOARD.methods_by_name['delete']._serialized_options = b'\202\323\344\223\002\033\"\026/board/v1/board/delete:\001*'
  _BOARD.methods_by_name['get']._options = None
  _BOARD.methods_by_name['get']._serialized_options = b'\202\323\344\223\002\030\"\023/board/v1/board/get:\001*'
  _BOARD.methods_by_name['list']._options = None
  _BOARD.methods_by_name['list']._serialized_options = b'\202\323\344\223\002\031\"\024/board/v1/board/list:\001*'
  _BOARD.methods_by_name['stat']._options = None
  _BOARD.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\031\"\024/board/v1/board/stat:\001*'
  _CREATEBOARDREQUEST._serialized_start=183
  _CREATEBOARDREQUEST._serialized_end=276
  _UPDATEBOARDREQUEST._serialized_start=278
  _UPDATEBOARDREQUEST._serialized_end=369
  _SETBOARDCATEGORIESREQUEST._serialized_start=371
  _SETBOARDCATEGORIESREQUEST._serialized_end=436
  _BOARDREQUEST._serialized_start=438
  _BOARDREQUEST._serialized_end=470
  _GETBOARDREQUEST._serialized_start=472
  _GETBOARDREQUEST._serialized_end=521
  _BOARDQUERY._serialized_start=523
  _BOARDQUERY._serialized_end=611
  _BOARDSTATQUERY._serialized_start=613
  _BOARDSTATQUERY._serialized_end=683
  _BOARDINFO._serialized_start=685
  _BOARDINFO._serialized_end=807
  _BOARDSINFO._serialized_start=809
  _BOARDSINFO._serialized_end=893
  _BOARD._serialized_start=896
  _BOARD._serialized_end=1728
# @@protoc_insertion_point(module_scope)
