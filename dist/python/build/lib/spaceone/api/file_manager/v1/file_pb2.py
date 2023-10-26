# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/file_manager/v1/file.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'spaceone/api/file_manager/v1/file.proto\x12\x1cspaceone.api.file_manager.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\";\n\rFileReference\x12\x15\n\rresource_type\x18\x01 \x01(\t\x12\x13\n\x0bresource_id\x18\x02 \x01(\t\"\x9b\x01\n\x11\x43reateFileRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04tags\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12>\n\treference\x18\x03 \x01(\x0b\x32+.spaceone.api.file_manager.v1.FileReference\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"\x9e\x01\n\x11UpdateFileRequest\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12%\n\x04tags\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12>\n\treference\x18\x03 \x01(\x0b\x32+.spaceone.api.file_manager.v1.FileReference\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"1\n\x0b\x46ileRequest\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"B\n\x0eGetFileRequest\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\xb0\x02\n\tFileQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x0f\n\x07\x66ile_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x36\n\x05state\x18\x04 \x01(\x0e\x32\'.spaceone.api.file_manager.v1.FileState\x12\x36\n\x05scope\x18\x05 \x01(\x0e\x32\'.spaceone.api.file_manager.v1.FileScope\x12\x11\n\tfile_type\x18\x06 \x01(\t\x12\x15\n\rresource_type\x18\x07 \x01(\t\x12\x13\n\x0bresource_id\x18\x08 \x01(\t\x12\x16\n\x0euser_domain_id\x18\x0b \x01(\t\x12\x11\n\tdomain_id\x18\x0c \x01(\t\"\xbe\x03\n\x08\x46ileInfo\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x36\n\x05state\x18\x03 \x01(\x0e\x32\'.spaceone.api.file_manager.v1.FileState\x12\x36\n\x05scope\x18\x04 \x01(\x0e\x32\'.spaceone.api.file_manager.v1.FileScope\x12\x11\n\tfile_type\x18\x05 \x01(\t\x12\x12\n\nupload_url\x18\x06 \x01(\t\x12/\n\x0eupload_options\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x14\n\x0c\x64ownload_url\x18\x08 \x01(\t\x12%\n\x04tags\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x12>\n\treference\x18\n \x01(\x0b\x32+.spaceone.api.file_manager.v1.FileReference\x12\x0f\n\x07user_id\x18\x0b \x01(\t\x12\x16\n\x0euser_domain_id\x18\x0c \x01(\t\x12\x11\n\tdomain_id\x18\r \x01(\t\x12\x12\n\ncreated_at\x18\x15 \x01(\t\"Y\n\tFilesInfo\x12\x37\n\x07results\x18\x01 \x03(\x0b\x32&.spaceone.api.file_manager.v1.FileInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"X\n\rFileStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t*2\n\tFileState\x12\x0e\n\nSTATE_NONE\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x08\n\x04\x44ONE\x10\x02*3\n\tFileScope\x12\x0e\n\nSCOPE_NONE\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\n\n\x06\x44OMAIN\x10\x02\x32\xa5\x07\n\x04\x46ile\x12\x84\x01\n\x03\x61\x64\x64\x12/.spaceone.api.file_manager.v1.CreateFileRequest\x1a&.spaceone.api.file_manager.v1.FileInfo\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/file-manager/v1/file/add:\x01*\x12\x8a\x01\n\x06update\x12/.spaceone.api.file_manager.v1.UpdateFileRequest\x1a&.spaceone.api.file_manager.v1.FileInfo\"\'\x82\xd3\xe4\x93\x02!\"\x1c/file-manager/v1/file/update:\x01*\x12t\n\x06\x64\x65lete\x12).spaceone.api.file_manager.v1.FileRequest\x1a\x16.google.protobuf.Empty\"\'\x82\xd3\xe4\x93\x02!\"\x1c/file-manager/v1/file/delete:\x01*\x12\x98\x01\n\x10get_download_url\x12).spaceone.api.file_manager.v1.FileRequest\x1a&.spaceone.api.file_manager.v1.FileInfo\"1\x82\xd3\xe4\x93\x02+\"&/file-manager/v1/file/get-download-url:\x01*\x12\x81\x01\n\x03get\x12,.spaceone.api.file_manager.v1.GetFileRequest\x1a&.spaceone.api.file_manager.v1.FileInfo\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/file-manager/v1/file/get:\x01*\x12\x7f\n\x04list\x12\'.spaceone.api.file_manager.v1.FileQuery\x1a\'.spaceone.api.file_manager.v1.FilesInfo\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/file-manager/v1/file/list:\x01*\x12s\n\x04stat\x12+.spaceone.api.file_manager.v1.FileStatQuery\x1a\x17.google.protobuf.Struct\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/file-manager/v1/file/stat:\x01*BCZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/file_manager/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.file_manager.v1.file_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/file_manager/v1'
  _FILE.methods_by_name['add']._options = None
  _FILE.methods_by_name['add']._serialized_options = b'\202\323\344\223\002\036\"\031/file-manager/v1/file/add:\001*'
  _FILE.methods_by_name['update']._options = None
  _FILE.methods_by_name['update']._serialized_options = b'\202\323\344\223\002!\"\034/file-manager/v1/file/update:\001*'
  _FILE.methods_by_name['delete']._options = None
  _FILE.methods_by_name['delete']._serialized_options = b'\202\323\344\223\002!\"\034/file-manager/v1/file/delete:\001*'
  _FILE.methods_by_name['get_download_url']._options = None
  _FILE.methods_by_name['get_download_url']._serialized_options = b'\202\323\344\223\002+\"&/file-manager/v1/file/get-download-url:\001*'
  _FILE.methods_by_name['get']._options = None
  _FILE.methods_by_name['get']._serialized_options = b'\202\323\344\223\002\036\"\031/file-manager/v1/file/get:\001*'
  _FILE.methods_by_name['list']._options = None
  _FILE.methods_by_name['list']._serialized_options = b'\202\323\344\223\002\037\"\032/file-manager/v1/file/list:\001*'
  _FILE.methods_by_name['stat']._options = None
  _FILE.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\037\"\032/file-manager/v1/file/stat:\001*'
  _globals['_FILESTATE']._serialized_start=1632
  _globals['_FILESTATE']._serialized_end=1682
  _globals['_FILESCOPE']._serialized_start=1684
  _globals['_FILESCOPE']._serialized_end=1735
  _globals['_FILEREFERENCE']._serialized_start=196
  _globals['_FILEREFERENCE']._serialized_end=255
  _globals['_CREATEFILEREQUEST']._serialized_start=258
  _globals['_CREATEFILEREQUEST']._serialized_end=413
  _globals['_UPDATEFILEREQUEST']._serialized_start=416
  _globals['_UPDATEFILEREQUEST']._serialized_end=574
  _globals['_FILEREQUEST']._serialized_start=576
  _globals['_FILEREQUEST']._serialized_end=625
  _globals['_GETFILEREQUEST']._serialized_start=627
  _globals['_GETFILEREQUEST']._serialized_end=693
  _globals['_FILEQUERY']._serialized_start=696
  _globals['_FILEQUERY']._serialized_end=1000
  _globals['_FILEINFO']._serialized_start=1003
  _globals['_FILEINFO']._serialized_end=1449
  _globals['_FILESINFO']._serialized_start=1451
  _globals['_FILESINFO']._serialized_end=1540
  _globals['_FILESTATQUERY']._serialized_start=1542
  _globals['_FILESTATQUERY']._serialized_end=1630
  _globals['_FILE']._serialized_start=1738
  _globals['_FILE']._serialized_end=2671
# @@protoc_insertion_point(module_scope)
