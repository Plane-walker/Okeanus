# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dci/dci.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import interface.gogo_pb2 as gogoproto_dot_gogo__pb2
import interface.common.id_pb2 as common_dot_id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dci/dci.proto',
  package='dci',
  syntax='proto3',
  serialized_options=b'Z+github.com/tendermint/tendermint/abci/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rdci/dci.proto\x12\x03\x64\x63i\x1a\x14gogoproto/gogo.proto\x1a\x0f\x63ommon/id.proto\"j\n\x10RequestDeliverTx\x12\n\n\x02tx\x18\x01 \x01(\x0c\x12\x1d\n\x06source\x18\x02 \x01(\x0b\x32\r.common.Chain\x12\x1d\n\x06target\x18\x03 \x01(\x0b\x32\r.common.Chain\x12\x0c\n\x04\x66lag\x18\x04 \x01(\t\"\x1f\n\x11RequestRouterInfo\x12\n\n\x02tx\x18\x01 \x01(\r\"\x80\x01\n\x15RequestRouterTransmit\x12\x1d\n\x06source\x18\x01 \x01(\x0b\x32\r.common.Chain\x12\x1d\n\x06target\x18\x02 \x01(\x0b\x32\r.common.Chain\x12\x0b\n\x03ttl\x18\x03 \x01(\r\x12\x1c\n\x05paths\x18\x04 \x03(\x0b\x32\r.common.Chain\"w\n\x19RequestRouterPathCallback\x12\x1d\n\x06source\x18\x01 \x01(\x0b\x32\r.common.Chain\x12\x1d\n\x06target\x18\x02 \x01(\x0b\x32\r.common.Chain\x12\x1c\n\x05paths\x18\x03 \x03(\x0b\x32\r.common.Chain\"2\n\x16RequestSwitchCommunity\x12\x18\n\x10target_community\x18\x01 \x01(\t\"*\n\x14RequestCommunityInfo\x12\x12\n\ninfo_level\x18\x01 \x01(\x05\"Y\n\x16RequestCommunityConfig\x12\x13\n\x0b\x61uto_switch\x18\x01 \x01(\x08\x12\x17\n\x0fmax_peer_number\x18\x02 \x01(\x05\x12\x11\n\talgorithm\x18\x03 \x01(\t\"\\\n\x05\x45vent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x45\n\nattributes\x18\x02 \x03(\x0b\x32\x13.dci.EventAttributeB\x1c\xc8\xde\x1f\x00\xea\xde\x1f\x14\x61ttributes,omitempty\";\n\x0e\x45ventAttribute\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\r\n\x05index\x18\x03 \x01(\x08\"!\n\x11ResponseDeliverTx\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\">\n\x12ResponseRouterInfo\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0c\n\x04info\x18\x03 \x01(\t\"4\n\x16ResponseRouterTransmit\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0c\n\x04info\x18\x02 \x01(\t\"8\n\x1aResponseRouterPathCallback\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0c\n\x04info\x18\x02 \x01(\t\"5\n\x17ResponseSwitchCommunity\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0c\n\x04info\x18\x02 \x01(\x0c\">\n\x15ResponseCommunityInfo\x12\x14\n\x0c\x63ommunity_id\x18\x01 \x01(\t\x12\x0f\n\x07node_id\x18\x02 \x01(\t\"5\n\x17ResponseCommunityConfig\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0c\n\x04info\x18\x02 \x01(\t*9\n\x0b\x43heckTxType\x12\x10\n\x03NEW\x10\x00\x1a\x07\x8a\x9d \x03New\x12\x18\n\x07RECHECK\x10\x01\x1a\x0b\x8a\x9d \x07Recheck2\x8f\x04\n\x04\x44ock\x12<\n\tDeliverTx\x12\x15.dci.RequestDeliverTx\x1a\x16.dci.ResponseDeliverTx0\x01\x12?\n\nRouterInfo\x12\x16.dci.RequestRouterInfo\x1a\x17.dci.ResponseRouterInfo0\x01\x12K\n\x0eRouterTransmit\x12\x1a.dci.RequestRouterTransmit\x1a\x1b.dci.ResponseRouterTransmit0\x01\x12W\n\x12RouterPathCallback\x12\x1e.dci.RequestRouterPathCallback\x1a\x1f.dci.ResponseRouterPathCallback0\x01\x12L\n\x0fSwitchCommunity\x12\x1b.dci.RequestSwitchCommunity\x1a\x1c.dci.ResponseSwitchCommunity\x12\x46\n\rCommunityInfo\x12\x19.dci.RequestCommunityInfo\x1a\x1a.dci.ResponseCommunityInfo\x12L\n\x0f\x43ommunityConfig\x12\x1b.dci.RequestCommunityConfig\x1a\x1c.dci.ResponseCommunityConfigB-Z+github.com/tendermint/tendermint/abci/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,common_dot_id__pb2.DESCRIPTOR,])

_CHECKTXTYPE = _descriptor.EnumDescriptor(
  name='CheckTxType',
  full_name='dci.CheckTxType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEW', index=0, number=0,
      serialized_options=b'\212\235 \003New',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RECHECK', index=1, number=1,
      serialized_options=b'\212\235 \007Recheck',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1181,
  serialized_end=1238,
)
_sym_db.RegisterEnumDescriptor(_CHECKTXTYPE)

CheckTxType = enum_type_wrapper.EnumTypeWrapper(_CHECKTXTYPE)
NEW = 0
RECHECK = 1



_REQUESTDELIVERTX = _descriptor.Descriptor(
  name='RequestDeliverTx',
  full_name='dci.RequestDeliverTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx', full_name='dci.RequestDeliverTx.tx', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='dci.RequestDeliverTx.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='dci.RequestDeliverTx.target', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flag', full_name='dci.RequestDeliverTx.flag', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=167,
)


_REQUESTROUTERINFO = _descriptor.Descriptor(
  name='RequestRouterInfo',
  full_name='dci.RequestRouterInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx', full_name='dci.RequestRouterInfo.tx', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=200,
)


_REQUESTROUTERTRANSMIT = _descriptor.Descriptor(
  name='RequestRouterTransmit',
  full_name='dci.RequestRouterTransmit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='dci.RequestRouterTransmit.source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='dci.RequestRouterTransmit.target', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='dci.RequestRouterTransmit.ttl', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paths', full_name='dci.RequestRouterTransmit.paths', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=331,
)


_REQUESTROUTERPATHCALLBACK = _descriptor.Descriptor(
  name='RequestRouterPathCallback',
  full_name='dci.RequestRouterPathCallback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='dci.RequestRouterPathCallback.source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='dci.RequestRouterPathCallback.target', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paths', full_name='dci.RequestRouterPathCallback.paths', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=452,
)


_REQUESTSWITCHCOMMUNITY = _descriptor.Descriptor(
  name='RequestSwitchCommunity',
  full_name='dci.RequestSwitchCommunity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_community', full_name='dci.RequestSwitchCommunity.target_community', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=454,
  serialized_end=504,
)


_REQUESTCOMMUNITYINFO = _descriptor.Descriptor(
  name='RequestCommunityInfo',
  full_name='dci.RequestCommunityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='info_level', full_name='dci.RequestCommunityInfo.info_level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=548,
)


_REQUESTCOMMUNITYCONFIG = _descriptor.Descriptor(
  name='RequestCommunityConfig',
  full_name='dci.RequestCommunityConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auto_switch', full_name='dci.RequestCommunityConfig.auto_switch', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_peer_number', full_name='dci.RequestCommunityConfig.max_peer_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='dci.RequestCommunityConfig.algorithm', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=550,
  serialized_end=639,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='dci.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='dci.Event.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='dci.Event.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\352\336\037\024attributes,omitempty', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=641,
  serialized_end=733,
)


_EVENTATTRIBUTE = _descriptor.Descriptor(
  name='EventAttribute',
  full_name='dci.EventAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dci.EventAttribute.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dci.EventAttribute.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='dci.EventAttribute.index', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=735,
  serialized_end=794,
)


_RESPONSEDELIVERTX = _descriptor.Descriptor(
  name='ResponseDeliverTx',
  full_name='dci.ResponseDeliverTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dci.ResponseDeliverTx.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=796,
  serialized_end=829,
)


_RESPONSEROUTERINFO = _descriptor.Descriptor(
  name='ResponseRouterInfo',
  full_name='dci.ResponseRouterInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dci.ResponseRouterInfo.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='dci.ResponseRouterInfo.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='dci.ResponseRouterInfo.info', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=831,
  serialized_end=893,
)


_RESPONSEROUTERTRANSMIT = _descriptor.Descriptor(
  name='ResponseRouterTransmit',
  full_name='dci.ResponseRouterTransmit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dci.ResponseRouterTransmit.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='dci.ResponseRouterTransmit.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=895,
  serialized_end=947,
)


_RESPONSEROUTERPATHCALLBACK = _descriptor.Descriptor(
  name='ResponseRouterPathCallback',
  full_name='dci.ResponseRouterPathCallback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dci.ResponseRouterPathCallback.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='dci.ResponseRouterPathCallback.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=949,
  serialized_end=1005,
)


_RESPONSESWITCHCOMMUNITY = _descriptor.Descriptor(
  name='ResponseSwitchCommunity',
  full_name='dci.ResponseSwitchCommunity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dci.ResponseSwitchCommunity.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='dci.ResponseSwitchCommunity.info', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1007,
  serialized_end=1060,
)


_RESPONSECOMMUNITYINFO = _descriptor.Descriptor(
  name='ResponseCommunityInfo',
  full_name='dci.ResponseCommunityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='community_id', full_name='dci.ResponseCommunityInfo.community_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='dci.ResponseCommunityInfo.node_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1062,
  serialized_end=1124,
)


_RESPONSECOMMUNITYCONFIG = _descriptor.Descriptor(
  name='ResponseCommunityConfig',
  full_name='dci.ResponseCommunityConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dci.ResponseCommunityConfig.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='dci.ResponseCommunityConfig.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1126,
  serialized_end=1179,
)

_REQUESTDELIVERTX.fields_by_name['source'].message_type = common_dot_id__pb2._CHAIN
_REQUESTDELIVERTX.fields_by_name['target'].message_type = common_dot_id__pb2._CHAIN
_REQUESTROUTERTRANSMIT.fields_by_name['source'].message_type = common_dot_id__pb2._CHAIN
_REQUESTROUTERTRANSMIT.fields_by_name['target'].message_type = common_dot_id__pb2._CHAIN
_REQUESTROUTERTRANSMIT.fields_by_name['paths'].message_type = common_dot_id__pb2._CHAIN
_REQUESTROUTERPATHCALLBACK.fields_by_name['source'].message_type = common_dot_id__pb2._CHAIN
_REQUESTROUTERPATHCALLBACK.fields_by_name['target'].message_type = common_dot_id__pb2._CHAIN
_REQUESTROUTERPATHCALLBACK.fields_by_name['paths'].message_type = common_dot_id__pb2._CHAIN
_EVENT.fields_by_name['attributes'].message_type = _EVENTATTRIBUTE
DESCRIPTOR.message_types_by_name['RequestDeliverTx'] = _REQUESTDELIVERTX
DESCRIPTOR.message_types_by_name['RequestRouterInfo'] = _REQUESTROUTERINFO
DESCRIPTOR.message_types_by_name['RequestRouterTransmit'] = _REQUESTROUTERTRANSMIT
DESCRIPTOR.message_types_by_name['RequestRouterPathCallback'] = _REQUESTROUTERPATHCALLBACK
DESCRIPTOR.message_types_by_name['RequestSwitchCommunity'] = _REQUESTSWITCHCOMMUNITY
DESCRIPTOR.message_types_by_name['RequestCommunityInfo'] = _REQUESTCOMMUNITYINFO
DESCRIPTOR.message_types_by_name['RequestCommunityConfig'] = _REQUESTCOMMUNITYCONFIG
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['EventAttribute'] = _EVENTATTRIBUTE
DESCRIPTOR.message_types_by_name['ResponseDeliverTx'] = _RESPONSEDELIVERTX
DESCRIPTOR.message_types_by_name['ResponseRouterInfo'] = _RESPONSEROUTERINFO
DESCRIPTOR.message_types_by_name['ResponseRouterTransmit'] = _RESPONSEROUTERTRANSMIT
DESCRIPTOR.message_types_by_name['ResponseRouterPathCallback'] = _RESPONSEROUTERPATHCALLBACK
DESCRIPTOR.message_types_by_name['ResponseSwitchCommunity'] = _RESPONSESWITCHCOMMUNITY
DESCRIPTOR.message_types_by_name['ResponseCommunityInfo'] = _RESPONSECOMMUNITYINFO
DESCRIPTOR.message_types_by_name['ResponseCommunityConfig'] = _RESPONSECOMMUNITYCONFIG
DESCRIPTOR.enum_types_by_name['CheckTxType'] = _CHECKTXTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestDeliverTx = _reflection.GeneratedProtocolMessageType('RequestDeliverTx', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTDELIVERTX,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.RequestDeliverTx)
  })
_sym_db.RegisterMessage(RequestDeliverTx)

RequestRouterInfo = _reflection.GeneratedProtocolMessageType('RequestRouterInfo', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTROUTERINFO,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.RequestRouterInfo)
  })
_sym_db.RegisterMessage(RequestRouterInfo)

RequestRouterTransmit = _reflection.GeneratedProtocolMessageType('RequestRouterTransmit', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTROUTERTRANSMIT,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.RequestRouterTransmit)
  })
_sym_db.RegisterMessage(RequestRouterTransmit)

RequestRouterPathCallback = _reflection.GeneratedProtocolMessageType('RequestRouterPathCallback', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTROUTERPATHCALLBACK,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.RequestRouterPathCallback)
  })
_sym_db.RegisterMessage(RequestRouterPathCallback)

RequestSwitchCommunity = _reflection.GeneratedProtocolMessageType('RequestSwitchCommunity', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSWITCHCOMMUNITY,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.RequestSwitchCommunity)
  })
_sym_db.RegisterMessage(RequestSwitchCommunity)

RequestCommunityInfo = _reflection.GeneratedProtocolMessageType('RequestCommunityInfo', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCOMMUNITYINFO,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.RequestCommunityInfo)
  })
_sym_db.RegisterMessage(RequestCommunityInfo)

RequestCommunityConfig = _reflection.GeneratedProtocolMessageType('RequestCommunityConfig', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCOMMUNITYCONFIG,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.RequestCommunityConfig)
  })
_sym_db.RegisterMessage(RequestCommunityConfig)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.Event)
  })
_sym_db.RegisterMessage(Event)

EventAttribute = _reflection.GeneratedProtocolMessageType('EventAttribute', (_message.Message,), {
  'DESCRIPTOR' : _EVENTATTRIBUTE,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.EventAttribute)
  })
_sym_db.RegisterMessage(EventAttribute)

ResponseDeliverTx = _reflection.GeneratedProtocolMessageType('ResponseDeliverTx', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEDELIVERTX,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.ResponseDeliverTx)
  })
_sym_db.RegisterMessage(ResponseDeliverTx)

ResponseRouterInfo = _reflection.GeneratedProtocolMessageType('ResponseRouterInfo', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEROUTERINFO,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.ResponseRouterInfo)
  })
_sym_db.RegisterMessage(ResponseRouterInfo)

ResponseRouterTransmit = _reflection.GeneratedProtocolMessageType('ResponseRouterTransmit', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEROUTERTRANSMIT,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.ResponseRouterTransmit)
  })
_sym_db.RegisterMessage(ResponseRouterTransmit)

ResponseRouterPathCallback = _reflection.GeneratedProtocolMessageType('ResponseRouterPathCallback', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEROUTERPATHCALLBACK,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.ResponseRouterPathCallback)
  })
_sym_db.RegisterMessage(ResponseRouterPathCallback)

ResponseSwitchCommunity = _reflection.GeneratedProtocolMessageType('ResponseSwitchCommunity', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSESWITCHCOMMUNITY,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.ResponseSwitchCommunity)
  })
_sym_db.RegisterMessage(ResponseSwitchCommunity)

ResponseCommunityInfo = _reflection.GeneratedProtocolMessageType('ResponseCommunityInfo', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSECOMMUNITYINFO,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.ResponseCommunityInfo)
  })
_sym_db.RegisterMessage(ResponseCommunityInfo)

ResponseCommunityConfig = _reflection.GeneratedProtocolMessageType('ResponseCommunityConfig', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSECOMMUNITYCONFIG,
  '__module__' : 'dci.dci_pb2'
  # @@protoc_insertion_point(class_scope:dci.ResponseCommunityConfig)
  })
_sym_db.RegisterMessage(ResponseCommunityConfig)


DESCRIPTOR._options = None
_CHECKTXTYPE.values_by_name["NEW"]._options = None
_CHECKTXTYPE.values_by_name["RECHECK"]._options = None
_EVENT.fields_by_name['attributes']._options = None

_DOCK = _descriptor.ServiceDescriptor(
  name='Dock',
  full_name='dci.Dock',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1241,
  serialized_end=1768,
  methods=[
  _descriptor.MethodDescriptor(
    name='DeliverTx',
    full_name='dci.Dock.DeliverTx',
    index=0,
    containing_service=None,
    input_type=_REQUESTDELIVERTX,
    output_type=_RESPONSEDELIVERTX,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RouterInfo',
    full_name='dci.Dock.RouterInfo',
    index=1,
    containing_service=None,
    input_type=_REQUESTROUTERINFO,
    output_type=_RESPONSEROUTERINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RouterTransmit',
    full_name='dci.Dock.RouterTransmit',
    index=2,
    containing_service=None,
    input_type=_REQUESTROUTERTRANSMIT,
    output_type=_RESPONSEROUTERTRANSMIT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RouterPathCallback',
    full_name='dci.Dock.RouterPathCallback',
    index=3,
    containing_service=None,
    input_type=_REQUESTROUTERPATHCALLBACK,
    output_type=_RESPONSEROUTERPATHCALLBACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SwitchCommunity',
    full_name='dci.Dock.SwitchCommunity',
    index=4,
    containing_service=None,
    input_type=_REQUESTSWITCHCOMMUNITY,
    output_type=_RESPONSESWITCHCOMMUNITY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CommunityInfo',
    full_name='dci.Dock.CommunityInfo',
    index=5,
    containing_service=None,
    input_type=_REQUESTCOMMUNITYINFO,
    output_type=_RESPONSECOMMUNITYINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CommunityConfig',
    full_name='dci.Dock.CommunityConfig',
    index=6,
    containing_service=None,
    input_type=_REQUESTCOMMUNITYCONFIG,
    output_type=_RESPONSECOMMUNITYCONFIG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DOCK)

DESCRIPTOR.services_by_name['Dock'] = _DOCK

# @@protoc_insertion_point(module_scope)
