# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/plugin/account_collector.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4spaceone/api/identity/plugin/account_collector.proto\x12\x1cspaceone.api.identity.plugin\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"J\n\x0bInitRequest\x12(\n\x07options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"\x8b\x01\n\x0bSyncRequest\x12(\n\x07options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tschema_id\x18\x02 \x01(\t\x12,\n\x0bsecret_data\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"\xf1\x01\n\x0b\x41\x63\x63ountInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0bresource_id\x18\x03 \x01(\t\x12\x18\n\x10secret_schema_id\x18\x04 \x01(\t\x12,\n\x0bsecret_data\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04tags\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08location\x18\x07 \x03(\x0b\x32\x17.google.protobuf.Struct\"J\n\x0c\x41\x63\x63ountsInfo\x12:\n\x07results\x18\x01 \x03(\x0b\x32).spaceone.api.identity.plugin.AccountInfo\"7\n\nPluginInfo\x12)\n\x08metadata\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct2\xd2\x01\n\x10\x41\x63\x63ountCollector\x12]\n\x04init\x12).spaceone.api.identity.plugin.InitRequest\x1a(.spaceone.api.identity.plugin.PluginInfo\"\x00\x12_\n\x04sync\x12).spaceone.api.identity.plugin.SyncRequest\x1a*.spaceone.api.identity.plugin.AccountsInfo\"\x00\x42\x43ZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/identity/pluginb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.identity.plugin.account_collector_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/identity/plugin'
  _globals['_INITREQUEST']._serialized_start=145
  _globals['_INITREQUEST']._serialized_end=219
  _globals['_SYNCREQUEST']._serialized_start=222
  _globals['_SYNCREQUEST']._serialized_end=361
  _globals['_ACCOUNTINFO']._serialized_start=364
  _globals['_ACCOUNTINFO']._serialized_end=605
  _globals['_ACCOUNTSINFO']._serialized_start=607
  _globals['_ACCOUNTSINFO']._serialized_end=681
  _globals['_PLUGININFO']._serialized_start=683
  _globals['_PLUGININFO']._serialized_end=738
  _globals['_ACCOUNTCOLLECTOR']._serialized_start=741
  _globals['_ACCOUNTCOLLECTOR']._serialized_end=951
# @@protoc_insertion_point(module_scope)
