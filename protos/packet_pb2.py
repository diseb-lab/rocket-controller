# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/packet.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13protos/packet.proto\x12\x06packet\":\n\x06Packet\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x11\n\tfrom_port\x18\x02 \x01(\r\x12\x0f\n\x07to_port\x18\x03 \x01(\r\")\n\tPacketAck\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\r2@\n\rPacketService\x12/\n\nSendPacket\x12\x0e.packet.Packet\x1a\x11.packet.PacketAckb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.packet_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PACKET']._serialized_start=31
  _globals['_PACKET']._serialized_end=89
  _globals['_PACKETACK']._serialized_start=91
  _globals['_PACKETACK']._serialized_end=132
  _globals['_PACKETSERVICE']._serialized_start=134
  _globals['_PACKETSERVICE']._serialized_end=198
# @@protoc_insertion_point(module_scope)
