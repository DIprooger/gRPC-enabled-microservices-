# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/user/protos/user.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fservices/user/protos/user.proto\x12\x04user\"<\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x05\"\x14\n\x06UserId\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1f\n\x0cUserResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x8b\x01\n\x0bUserService\x12)\n\x07\x41\x64\x64User\x12\n.user.User\x1a\x12.user.UserResponse\x12#\n\x07GetUser\x12\x0c.user.UserId\x1a\n.user.User\x12,\n\nUpdateUser\x12\n.user.User\x1a\x12.user.UserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.user.protos.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USER']._serialized_start=41
  _globals['_USER']._serialized_end=101
  _globals['_USERID']._serialized_start=103
  _globals['_USERID']._serialized_end=123
  _globals['_USERRESPONSE']._serialized_start=125
  _globals['_USERRESPONSE']._serialized_end=156
  _globals['_USERSERVICE']._serialized_start=159
  _globals['_USERSERVICE']._serialized_end=298
# @@protoc_insertion_point(module_scope)
