# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bci/bci.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import interface.common.id_pb2 as common_dot_id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bci/bci.proto',
  package='bci',
  syntax='proto3',
  serialized_options=b'Z+github.com/tendermint/tendermint/abci/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rbci/bci.proto\x12\x03\x62\x63i\x1a\x0f\x63ommon/id.proto\":\n\x0fRequestSendData\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0b\n\x03log\x18\x02 \x01(\t\x12\x0c\n\x04info\x18\x03 \x01(\t\";\n\x10ResponseSendData\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0b\n\x03log\x18\x02 \x01(\t\x12\x0c\n\x04info\x18\x03 \x01(\t\"G\n\rRequestJoinRC\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0b\n\x03log\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\n\n\x02rc\x18\x04 \x01(\t\"<\n\x0eResponseJoinRC\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0b\n\x03log\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"\x88\x01\n\x16RequestGossipQueryPath\x12\x1d\n\x06target\x18\x01 \x01(\x0b\x32\r.common.Chain\x12\x1d\n\x06source\x18\x02 \x01(\x0b\x32\r.common.Chain\x12\x0b\n\x03ttl\x18\x03 \x01(\r\x12#\n\x0croute_chains\x18\x04 \x03(\x0b\x32\r.common.Chain\"5\n\x17ResponseGossipQueryPath\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0c\n\x04info\x18\x02 \x01(\t\"z\n\x15RequestGossipCallBack\x12\x1d\n\x06target\x18\x01 \x01(\x0b\x32\r.common.Chain\x12\x1d\n\x06source\x18\x02 \x01(\x0b\x32\r.common.Chain\x12#\n\x0croute_chains\x18\x03 \x03(\x0b\x32\r.common.Chain\"4\n\x16ResponseGossipCallBack\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0c\n\x04info\x18\x02 \x01(\t2\x8b\x02\n\x04Lane\x12\x37\n\x08SendData\x12\x14.bci.RequestSendData\x1a\x15.bci.ResponseSendData\x12\x31\n\x06JoinRC\x12\x12.bci.RequestJoinRC\x1a\x13.bci.ResponseJoinRC\x12L\n\x0fGossipQueryPath\x12\x1b.bci.RequestGossipQueryPath\x1a\x1c.bci.ResponseGossipQueryPath\x12I\n\x0eGossipCallBack\x12\x1a.bci.RequestGossipCallBack\x1a\x1b.bci.ResponseGossipCallBackB-Z+github.com/tendermint/tendermint/abci/typesb\x06proto3'
  ,
  dependencies=[common_dot_id__pb2.DESCRIPTOR,])




_REQUESTSENDDATA = _descriptor.Descriptor(
  name='RequestSendData',
  full_name='bci.RequestSendData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='bci.RequestSendData.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log', full_name='bci.RequestSendData.log', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='bci.RequestSendData.info', index=2,
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
  serialized_start=39,
  serialized_end=97,
)


_RESPONSESENDDATA = _descriptor.Descriptor(
  name='ResponseSendData',
  full_name='bci.ResponseSendData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='bci.ResponseSendData.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log', full_name='bci.ResponseSendData.log', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='bci.ResponseSendData.info', index=2,
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
  serialized_start=99,
  serialized_end=158,
)


_REQUESTJOINRC = _descriptor.Descriptor(
  name='RequestJoinRC',
  full_name='bci.RequestJoinRC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='bci.RequestJoinRC.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log', full_name='bci.RequestJoinRC.log', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='bci.RequestJoinRC.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rc', full_name='bci.RequestJoinRC.rc', index=3,
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
  serialized_start=160,
  serialized_end=231,
)


_RESPONSEJOINRC = _descriptor.Descriptor(
  name='ResponseJoinRC',
  full_name='bci.ResponseJoinRC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='bci.ResponseJoinRC.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log', full_name='bci.ResponseJoinRC.log', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='bci.ResponseJoinRC.message', index=2,
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
  serialized_start=233,
  serialized_end=293,
)


_REQUESTGOSSIPQUERYPATH = _descriptor.Descriptor(
  name='RequestGossipQueryPath',
  full_name='bci.RequestGossipQueryPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='bci.RequestGossipQueryPath.target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='bci.RequestGossipQueryPath.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='bci.RequestGossipQueryPath.ttl', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='route_chains', full_name='bci.RequestGossipQueryPath.route_chains', index=3,
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
  serialized_start=296,
  serialized_end=432,
)


_RESPONSEGOSSIPQUERYPATH = _descriptor.Descriptor(
  name='ResponseGossipQueryPath',
  full_name='bci.ResponseGossipQueryPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='bci.ResponseGossipQueryPath.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='bci.ResponseGossipQueryPath.info', index=1,
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
  serialized_start=434,
  serialized_end=487,
)


_REQUESTGOSSIPCALLBACK = _descriptor.Descriptor(
  name='RequestGossipCallBack',
  full_name='bci.RequestGossipCallBack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='bci.RequestGossipCallBack.target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='bci.RequestGossipCallBack.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='route_chains', full_name='bci.RequestGossipCallBack.route_chains', index=2,
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
  serialized_start=489,
  serialized_end=611,
)


_RESPONSEGOSSIPCALLBACK = _descriptor.Descriptor(
  name='ResponseGossipCallBack',
  full_name='bci.ResponseGossipCallBack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='bci.ResponseGossipCallBack.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='bci.ResponseGossipCallBack.info', index=1,
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
  serialized_start=613,
  serialized_end=665,
)

_REQUESTGOSSIPQUERYPATH.fields_by_name['target'].message_type = common_dot_id__pb2._CHAIN
_REQUESTGOSSIPQUERYPATH.fields_by_name['source'].message_type = common_dot_id__pb2._CHAIN
_REQUESTGOSSIPQUERYPATH.fields_by_name['route_chains'].message_type = common_dot_id__pb2._CHAIN
_REQUESTGOSSIPCALLBACK.fields_by_name['target'].message_type = common_dot_id__pb2._CHAIN
_REQUESTGOSSIPCALLBACK.fields_by_name['source'].message_type = common_dot_id__pb2._CHAIN
_REQUESTGOSSIPCALLBACK.fields_by_name['route_chains'].message_type = common_dot_id__pb2._CHAIN
DESCRIPTOR.message_types_by_name['RequestSendData'] = _REQUESTSENDDATA
DESCRIPTOR.message_types_by_name['ResponseSendData'] = _RESPONSESENDDATA
DESCRIPTOR.message_types_by_name['RequestJoinRC'] = _REQUESTJOINRC
DESCRIPTOR.message_types_by_name['ResponseJoinRC'] = _RESPONSEJOINRC
DESCRIPTOR.message_types_by_name['RequestGossipQueryPath'] = _REQUESTGOSSIPQUERYPATH
DESCRIPTOR.message_types_by_name['ResponseGossipQueryPath'] = _RESPONSEGOSSIPQUERYPATH
DESCRIPTOR.message_types_by_name['RequestGossipCallBack'] = _REQUESTGOSSIPCALLBACK
DESCRIPTOR.message_types_by_name['ResponseGossipCallBack'] = _RESPONSEGOSSIPCALLBACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestSendData = _reflection.GeneratedProtocolMessageType('RequestSendData', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSENDDATA,
  '__module__' : 'bci.bci_pb2'
  # @@protoc_insertion_point(class_scope:bci.RequestSendData)
  })
_sym_db.RegisterMessage(RequestSendData)

ResponseSendData = _reflection.GeneratedProtocolMessageType('ResponseSendData', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSESENDDATA,
  '__module__' : 'bci.bci_pb2'
  # @@protoc_insertion_point(class_scope:bci.ResponseSendData)
  })
_sym_db.RegisterMessage(ResponseSendData)

RequestJoinRC = _reflection.GeneratedProtocolMessageType('RequestJoinRC', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTJOINRC,
  '__module__' : 'bci.bci_pb2'
  # @@protoc_insertion_point(class_scope:bci.RequestJoinRC)
  })
_sym_db.RegisterMessage(RequestJoinRC)

ResponseJoinRC = _reflection.GeneratedProtocolMessageType('ResponseJoinRC', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEJOINRC,
  '__module__' : 'bci.bci_pb2'
  # @@protoc_insertion_point(class_scope:bci.ResponseJoinRC)
  })
_sym_db.RegisterMessage(ResponseJoinRC)

RequestGossipQueryPath = _reflection.GeneratedProtocolMessageType('RequestGossipQueryPath', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTGOSSIPQUERYPATH,
  '__module__' : 'bci.bci_pb2'
  # @@protoc_insertion_point(class_scope:bci.RequestGossipQueryPath)
  })
_sym_db.RegisterMessage(RequestGossipQueryPath)

ResponseGossipQueryPath = _reflection.GeneratedProtocolMessageType('ResponseGossipQueryPath', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEGOSSIPQUERYPATH,
  '__module__' : 'bci.bci_pb2'
  # @@protoc_insertion_point(class_scope:bci.ResponseGossipQueryPath)
  })
_sym_db.RegisterMessage(ResponseGossipQueryPath)

RequestGossipCallBack = _reflection.GeneratedProtocolMessageType('RequestGossipCallBack', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTGOSSIPCALLBACK,
  '__module__' : 'bci.bci_pb2'
  # @@protoc_insertion_point(class_scope:bci.RequestGossipCallBack)
  })
_sym_db.RegisterMessage(RequestGossipCallBack)

ResponseGossipCallBack = _reflection.GeneratedProtocolMessageType('ResponseGossipCallBack', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEGOSSIPCALLBACK,
  '__module__' : 'bci.bci_pb2'
  # @@protoc_insertion_point(class_scope:bci.ResponseGossipCallBack)
  })
_sym_db.RegisterMessage(ResponseGossipCallBack)


DESCRIPTOR._options = None

_LANE = _descriptor.ServiceDescriptor(
  name='Lane',
  full_name='bci.Lane',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=668,
  serialized_end=935,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendData',
    full_name='bci.Lane.SendData',
    index=0,
    containing_service=None,
    input_type=_REQUESTSENDDATA,
    output_type=_RESPONSESENDDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='JoinRC',
    full_name='bci.Lane.JoinRC',
    index=1,
    containing_service=None,
    input_type=_REQUESTJOINRC,
    output_type=_RESPONSEJOINRC,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GossipQueryPath',
    full_name='bci.Lane.GossipQueryPath',
    index=2,
    containing_service=None,
    input_type=_REQUESTGOSSIPQUERYPATH,
    output_type=_RESPONSEGOSSIPQUERYPATH,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GossipCallBack',
    full_name='bci.Lane.GossipCallBack',
    index=3,
    containing_service=None,
    input_type=_REQUESTGOSSIPCALLBACK,
    output_type=_RESPONSEGOSSIPCALLBACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LANE)

DESCRIPTOR.services_by_name['Lane'] = _LANE

# @@protoc_insertion_point(module_scope)
