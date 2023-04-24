# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v1/user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#spaceone/api/identity/v1/user.proto\x12\x18spaceone.api.identity.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\xb8\x02\n\x11\x43reateUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x35\n\tuser_type\x18\x05 \x01(\x0e\x32\".spaceone.api.identity.v1.UserType\x12\x36\n\x07\x62\x61\x63kend\x18\x06 \x01(\x0e\x32%.spaceone.api.identity.v1.UserBackend\x12\x10\n\x08language\x18\x07 \x01(\t\x12\x10\n\x08timezone\x18\x08 \x01(\t\x12%\n\x04tags\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\n \x01(\t\x12\x16\n\x0ereset_password\x18\x0b \x01(\x08\"\xb1\x01\n\x11UpdateUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x10\n\x08language\x18\x07 \x01(\t\x12\x10\n\x08timezone\x18\x08 \x01(\t\x12%\n\x04tags\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\n \x01(\t\"G\n\x12VerifyEmailRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"N\n\x13\x43onfirmEmailRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x13\n\x0bverify_code\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"~\n\x19SetRequiredActionsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12=\n\x07\x61\x63tions\x18\x02 \x03(\x0e\x32,.spaceone.api.identity.v1.UserRequiredAction\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"1\n\x0bUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"B\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\xf6\x01\n\tUserQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x35\n\tuser_type\x18\x06 \x01(\x0e\x32\".spaceone.api.identity.v1.UserType\x12\x36\n\x07\x62\x61\x63kend\x18\x07 \x01(\x0e\x32%.spaceone.api.identity.v1.UserBackend\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"\x87\x04\n\x08UserInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x37\n\x05state\x18\x03 \x01(\x0e\x32(.spaceone.api.identity.v1.UserInfo.State\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x35\n\tuser_type\x18\x05 \x01(\x0e\x32\".spaceone.api.identity.v1.UserType\x12\x36\n\x07\x62\x61\x63kend\x18\x06 \x01(\x0e\x32%.spaceone.api.identity.v1.UserBackend\x12\x10\n\x08language\x18\x07 \x01(\t\x12\x10\n\x08timezone\x18\x08 \x01(\t\x12\x46\n\x10required_actions\x18\t \x03(\x0e\x32,.spaceone.api.identity.v1.UserRequiredAction\x12%\n\x04tags\x18\n \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x18\n\x10last_accessed_at\x18\x0b \x01(\t\x12\x12\n\ncreated_at\x18\x0c \x01(\t\x12\x11\n\tdomain_id\x18\r \x01(\t\x12\x16\n\x0e\x65mail_verified\x18\x0e \x01(\x08\"9\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\x12\x0b\n\x07PENDING\x10\x03\"U\n\tUsersInfo\x12\x33\n\x07results\x18\x01 \x03(\x0b\x32\".spaceone.api.identity.v1.UserInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"X\n\rUserStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"F\n\x0e\x46indUserSearch\x12\x11\n\x07user_id\x18\x01 \x01(\tH\x00\x12\x11\n\x07keyword\x18\x02 \x01(\tH\x00\x42\x0e\n\x0csearch_alias\"\\\n\rFindUserQuery\x12\x38\n\x06search\x18\x01 \x01(\x0b\x32(.spaceone.api.identity.v1.FindUserSearch\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"c\n\x0c\x46indUserInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"]\n\rFindUsersInfo\x12\x37\n\x07results\x18\x01 \x03(\x0b\x32&.spaceone.api.identity.v1.FindUserInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05*8\n\x0bUserBackend\x12\x10\n\x0cNONE_BACKEND\x10\x00\x12\t\n\x05LOCAL\x10\x01\x12\x0c\n\x08\x45XTERNAL\x10\x02*6\n\x08UserType\x12\x12\n\x0eNONE_USER_TYPE\x10\x00\x12\x08\n\x04USER\x10\x01\x12\x0c\n\x08\x41PI_USER\x10\x02*)\n\x12UserRequiredAction\x12\x13\n\x0fUPDATE_PASSWORD\x10\x00\x32\xe7\r\n\x04User\x12~\n\x06\x63reate\x12+.spaceone.api.identity.v1.CreateUserRequest\x1a\".spaceone.api.identity.v1.UserInfo\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/identity/v1/user/create:\x01*\x12}\n\x06update\x12+.spaceone.api.identity.v1.UpdateUserRequest\x1a\".spaceone.api.identity.v1.UserInfo\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17identity/v1/user/update:\x01*\x12~\n\x0cverify_email\x12,.spaceone.api.identity.v1.VerifyEmailRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"\"\x1didentity/v1/user/verify-email:\x01*\x12\x8d\x01\n\rconfirm_email\x12-.spaceone.api.identity.v1.ConfirmEmailRequest\x1a\".spaceone.api.identity.v1.UserInfo\")\x82\xd3\xe4\x93\x02#\"\x1eidentity/v1/user/confirm-email:\x01*\x12{\n\x0ereset_password\x12%.spaceone.api.identity.v1.UserRequest\x1a\x16.google.protobuf.Empty\"*\x82\xd3\xe4\x93\x02$\"\x1fidentity/v1/user/reset-password:\x01*\x12\xa1\x01\n\x14set_required_actions\x12\x33.spaceone.api.identity.v1.SetRequiredActionsRequest\x1a\".spaceone.api.identity.v1.UserInfo\"0\x82\xd3\xe4\x93\x02*\"%identity/v1/user/set-required-actions:\x01*\x12x\n\x06\x65nable\x12%.spaceone.api.identity.v1.UserRequest\x1a\".spaceone.api.identity.v1.UserInfo\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/identity/v1/user/enable:\x01*\x12z\n\x07\x64isable\x12%.spaceone.api.identity.v1.UserRequest\x1a\".spaceone.api.identity.v1.UserInfo\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/identity/v1/user/disable:\x01*\x12l\n\x06\x64\x65lete\x12%.spaceone.api.identity.v1.UserRequest\x1a\x16.google.protobuf.Empty\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/identity/v1/user/delete:\x01*\x12u\n\x03get\x12(.spaceone.api.identity.v1.GetUserRequest\x1a\".spaceone.api.identity.v1.UserInfo\" \x82\xd3\xe4\x93\x02\x1a\"\x15/identity/v1/user/get:\x01*\x12s\n\x04list\x12#.spaceone.api.identity.v1.UserQuery\x1a#.spaceone.api.identity.v1.UsersInfo\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/identity/v1/user/list:\x01*\x12k\n\x04stat\x12\'.spaceone.api.identity.v1.UserStatQuery\x1a\x17.google.protobuf.Struct\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/identity/v1/user/stat:\x01*\x12|\n\x04\x66ind\x12\'.spaceone.api.identity.v1.FindUserQuery\x1a\'.spaceone.api.identity.v1.FindUsersInfo\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/identity/v1/users/find:\x01*\x12t\n\x04sync\x12%.spaceone.api.identity.v1.UserRequest\x1a\".spaceone.api.identity.v1.UserInfo\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/identity/v1/user/sync:\x01*B?Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v1b\x06proto3')

_USERBACKEND = DESCRIPTOR.enum_types_by_name['UserBackend']
UserBackend = enum_type_wrapper.EnumTypeWrapper(_USERBACKEND)
_USERTYPE = DESCRIPTOR.enum_types_by_name['UserType']
UserType = enum_type_wrapper.EnumTypeWrapper(_USERTYPE)
_USERREQUIREDACTION = DESCRIPTOR.enum_types_by_name['UserRequiredAction']
UserRequiredAction = enum_type_wrapper.EnumTypeWrapper(_USERREQUIREDACTION)
NONE_BACKEND = 0
LOCAL = 1
EXTERNAL = 2
NONE_USER_TYPE = 0
USER = 1
API_USER = 2
UPDATE_PASSWORD = 0


_CREATEUSERREQUEST = DESCRIPTOR.message_types_by_name['CreateUserRequest']
_UPDATEUSERREQUEST = DESCRIPTOR.message_types_by_name['UpdateUserRequest']
_VERIFYEMAILREQUEST = DESCRIPTOR.message_types_by_name['VerifyEmailRequest']
_CONFIRMEMAILREQUEST = DESCRIPTOR.message_types_by_name['ConfirmEmailRequest']
_SETREQUIREDACTIONSREQUEST = DESCRIPTOR.message_types_by_name['SetRequiredActionsRequest']
_USERREQUEST = DESCRIPTOR.message_types_by_name['UserRequest']
_GETUSERREQUEST = DESCRIPTOR.message_types_by_name['GetUserRequest']
_USERQUERY = DESCRIPTOR.message_types_by_name['UserQuery']
_USERINFO = DESCRIPTOR.message_types_by_name['UserInfo']
_USERSINFO = DESCRIPTOR.message_types_by_name['UsersInfo']
_USERSTATQUERY = DESCRIPTOR.message_types_by_name['UserStatQuery']
_FINDUSERSEARCH = DESCRIPTOR.message_types_by_name['FindUserSearch']
_FINDUSERQUERY = DESCRIPTOR.message_types_by_name['FindUserQuery']
_FINDUSERINFO = DESCRIPTOR.message_types_by_name['FindUserInfo']
_FINDUSERSINFO = DESCRIPTOR.message_types_by_name['FindUsersInfo']
_USERINFO_STATE = _USERINFO.enum_types_by_name['State']
CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERREQUEST,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.UpdateUserRequest)
  })
_sym_db.RegisterMessage(UpdateUserRequest)

VerifyEmailRequest = _reflection.GeneratedProtocolMessageType('VerifyEmailRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYEMAILREQUEST,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.VerifyEmailRequest)
  })
_sym_db.RegisterMessage(VerifyEmailRequest)

ConfirmEmailRequest = _reflection.GeneratedProtocolMessageType('ConfirmEmailRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONFIRMEMAILREQUEST,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ConfirmEmailRequest)
  })
_sym_db.RegisterMessage(ConfirmEmailRequest)

SetRequiredActionsRequest = _reflection.GeneratedProtocolMessageType('SetRequiredActionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETREQUIREDACTIONSREQUEST,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.SetRequiredActionsRequest)
  })
_sym_db.RegisterMessage(SetRequiredActionsRequest)

UserRequest = _reflection.GeneratedProtocolMessageType('UserRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERREQUEST,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.UserRequest)
  })
_sym_db.RegisterMessage(UserRequest)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

UserQuery = _reflection.GeneratedProtocolMessageType('UserQuery', (_message.Message,), {
  'DESCRIPTOR' : _USERQUERY,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.UserQuery)
  })
_sym_db.RegisterMessage(UserQuery)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

UsersInfo = _reflection.GeneratedProtocolMessageType('UsersInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERSINFO,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.UsersInfo)
  })
_sym_db.RegisterMessage(UsersInfo)

UserStatQuery = _reflection.GeneratedProtocolMessageType('UserStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _USERSTATQUERY,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.UserStatQuery)
  })
_sym_db.RegisterMessage(UserStatQuery)

FindUserSearch = _reflection.GeneratedProtocolMessageType('FindUserSearch', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERSEARCH,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.FindUserSearch)
  })
_sym_db.RegisterMessage(FindUserSearch)

FindUserQuery = _reflection.GeneratedProtocolMessageType('FindUserQuery', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERQUERY,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.FindUserQuery)
  })
_sym_db.RegisterMessage(FindUserQuery)

FindUserInfo = _reflection.GeneratedProtocolMessageType('FindUserInfo', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERINFO,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.FindUserInfo)
  })
_sym_db.RegisterMessage(FindUserInfo)

FindUsersInfo = _reflection.GeneratedProtocolMessageType('FindUsersInfo', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERSINFO,
  '__module__' : 'spaceone.api.identity.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.FindUsersInfo)
  })
_sym_db.RegisterMessage(FindUsersInfo)

_USER = DESCRIPTOR.services_by_name['User']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v1'
  _USER.methods_by_name['create']._options = None
  _USER.methods_by_name['create']._serialized_options = b'\202\323\344\223\002\035\"\030/identity/v1/user/create:\001*'
  _USER.methods_by_name['update']._options = None
  _USER.methods_by_name['update']._serialized_options = b'\202\323\344\223\002\034\"\027identity/v1/user/update:\001*'
  _USER.methods_by_name['verify_email']._options = None
  _USER.methods_by_name['verify_email']._serialized_options = b'\202\323\344\223\002\"\"\035identity/v1/user/verify-email:\001*'
  _USER.methods_by_name['confirm_email']._options = None
  _USER.methods_by_name['confirm_email']._serialized_options = b'\202\323\344\223\002#\"\036identity/v1/user/confirm-email:\001*'
  _USER.methods_by_name['reset_password']._options = None
  _USER.methods_by_name['reset_password']._serialized_options = b'\202\323\344\223\002$\"\037identity/v1/user/reset-password:\001*'
  _USER.methods_by_name['set_required_actions']._options = None
  _USER.methods_by_name['set_required_actions']._serialized_options = b'\202\323\344\223\002*\"%identity/v1/user/set-required-actions:\001*'
  _USER.methods_by_name['enable']._options = None
  _USER.methods_by_name['enable']._serialized_options = b'\202\323\344\223\002\035\"\030/identity/v1/user/enable:\001*'
  _USER.methods_by_name['disable']._options = None
  _USER.methods_by_name['disable']._serialized_options = b'\202\323\344\223\002\036\"\031/identity/v1/user/disable:\001*'
  _USER.methods_by_name['delete']._options = None
  _USER.methods_by_name['delete']._serialized_options = b'\202\323\344\223\002\035\"\030/identity/v1/user/delete:\001*'
  _USER.methods_by_name['get']._options = None
  _USER.methods_by_name['get']._serialized_options = b'\202\323\344\223\002\032\"\025/identity/v1/user/get:\001*'
  _USER.methods_by_name['list']._options = None
  _USER.methods_by_name['list']._serialized_options = b'\202\323\344\223\002\033\"\026/identity/v1/user/list:\001*'
  _USER.methods_by_name['stat']._options = None
  _USER.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\033\"\026/identity/v1/user/stat:\001*'
  _USER.methods_by_name['find']._options = None
  _USER.methods_by_name['find']._serialized_options = b'\202\323\344\223\002\034\"\027/identity/v1/users/find:\001*'
  _USER.methods_by_name['sync']._options = None
  _USER.methods_by_name['sync']._serialized_options = b'\202\323\344\223\002\033\"\026/identity/v1/user/sync:\001*'
  _USERBACKEND._serialized_start=2393
  _USERBACKEND._serialized_end=2449
  _USERTYPE._serialized_start=2451
  _USERTYPE._serialized_end=2505
  _USERREQUIREDACTION._serialized_start=2507
  _USERREQUIREDACTION._serialized_end=2548
  _CREATEUSERREQUEST._serialized_start=189
  _CREATEUSERREQUEST._serialized_end=501
  _UPDATEUSERREQUEST._serialized_start=504
  _UPDATEUSERREQUEST._serialized_end=681
  _VERIFYEMAILREQUEST._serialized_start=683
  _VERIFYEMAILREQUEST._serialized_end=754
  _CONFIRMEMAILREQUEST._serialized_start=756
  _CONFIRMEMAILREQUEST._serialized_end=834
  _SETREQUIREDACTIONSREQUEST._serialized_start=836
  _SETREQUIREDACTIONSREQUEST._serialized_end=962
  _USERREQUEST._serialized_start=964
  _USERREQUEST._serialized_end=1013
  _GETUSERREQUEST._serialized_start=1015
  _GETUSERREQUEST._serialized_end=1081
  _USERQUERY._serialized_start=1084
  _USERQUERY._serialized_end=1330
  _USERINFO._serialized_start=1333
  _USERINFO._serialized_end=1852
  _USERINFO_STATE._serialized_start=1795
  _USERINFO_STATE._serialized_end=1852
  _USERSINFO._serialized_start=1854
  _USERSINFO._serialized_end=1939
  _USERSTATQUERY._serialized_start=1941
  _USERSTATQUERY._serialized_end=2029
  _FINDUSERSEARCH._serialized_start=2031
  _FINDUSERSEARCH._serialized_end=2101
  _FINDUSERQUERY._serialized_start=2103
  _FINDUSERQUERY._serialized_end=2195
  _FINDUSERINFO._serialized_start=2197
  _FINDUSERINFO._serialized_end=2296
  _FINDUSERSINFO._serialized_start=2298
  _FINDUSERSINFO._serialized_end=2391
  _USER._serialized_start=2551
  _USER._serialized_end=4318
# @@protoc_insertion_point(module_scope)
