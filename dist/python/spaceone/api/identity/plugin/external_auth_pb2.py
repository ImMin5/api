# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/plugin/external_auth.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0spaceone/api/identity/plugin/external_auth.proto\x12\x1cspaceone.api.identity.plugin\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"J\n\x0bInitRequest\x12(\n\x07options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"\xe9\x01\n\x10\x41uthorizeRequest\x12(\n\x07options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tschema_id\x18\x02 \x01(\t\x12,\n\x0bsecret_data\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0b\x63redentials\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"\xd4\x01\n\x08UserInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06mobile\x18\x04 \x01(\t\x12\r\n\x05group\x18\x05 \x01(\t\x12;\n\x05state\x18\x06 \x01(\x0e\x32,.spaceone.api.identity.plugin.UserInfo.State\">\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\x12\x10\n\x0cUNIDENTIFIED\x10\x03\"7\n\nPluginInfo\x12)\n\x08metadata\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct2\xd4\x01\n\x0c\x45xternalAuth\x12]\n\x04init\x12).spaceone.api.identity.plugin.InitRequest\x1a(.spaceone.api.identity.plugin.PluginInfo\"\x00\x12\x65\n\tauthorize\x12..spaceone.api.identity.plugin.AuthorizeRequest\x1a&.spaceone.api.identity.plugin.UserInfo\"\x00\x42\x43ZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/identity/pluginb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.identity.plugin.external_auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/identity/plugin'
  _globals['_INITREQUEST']._serialized_start=141
  _globals['_INITREQUEST']._serialized_end=215
  _globals['_AUTHORIZEREQUEST']._serialized_start=218
  _globals['_AUTHORIZEREQUEST']._serialized_end=451
  _globals['_USERINFO']._serialized_start=454
  _globals['_USERINFO']._serialized_end=666
  _globals['_USERINFO_STATE']._serialized_start=604
  _globals['_USERINFO_STATE']._serialized_end=666
  _globals['_PLUGININFO']._serialized_start=668
  _globals['_PLUGININFO']._serialized_end=723
  _globals['_EXTERNALAUTH']._serialized_start=726
  _globals['_EXTERNALAUTH']._serialized_end=938
# @@protoc_insertion_point(module_scope)
