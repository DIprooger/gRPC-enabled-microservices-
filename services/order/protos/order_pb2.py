# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/order/protos/order.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!services/order/protos/order.proto\x12\x05order\"H\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"\x15\n\x07OrderId\x12\n\n\x02id\x18\x01 \x01(\x05\" \n\rOrderResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x9b\x01\n\x0cOrderService\x12.\n\x08\x41\x64\x64Order\x12\x0c.order.Order\x1a\x14.order.OrderResponse\x12(\n\x08GetOrder\x12\x0e.order.OrderId\x1a\x0c.order.Order\x12\x31\n\x0bUpdateOrder\x12\x0c.order.Order\x1a\x14.order.OrderResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.order.protos.order_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ORDER']._serialized_start=44
  _globals['_ORDER']._serialized_end=116
  _globals['_ORDERID']._serialized_start=118
  _globals['_ORDERID']._serialized_end=139
  _globals['_ORDERRESPONSE']._serialized_start=141
  _globals['_ORDERRESPONSE']._serialized_end=173
  _globals['_ORDERSERVICE']._serialized_start=176
  _globals['_ORDERSERVICE']._serialized_end=331
# @@protoc_insertion_point(module_scope)
