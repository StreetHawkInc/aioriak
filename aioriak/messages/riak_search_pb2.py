# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: riak_search.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import riak_pb2 as riak__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='riak_search.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x11riak_search.proto\x1a\nriak.proto\"(\n\x0cRpbSearchDoc\x12\x18\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x08.RpbPair\"\x9d\x01\n\x11RpbSearchQueryReq\x12\t\n\x01q\x18\x01 \x02(\x0c\x12\r\n\x05index\x18\x02 \x02(\x0c\x12\x0c\n\x04rows\x18\x03 \x01(\r\x12\r\n\x05start\x18\x04 \x01(\r\x12\x0c\n\x04sort\x18\x05 \x01(\x0c\x12\x0e\n\x06\x66ilter\x18\x06 \x01(\x0c\x12\n\n\x02\x64\x66\x18\x07 \x01(\x0c\x12\n\n\x02op\x18\x08 \x01(\x0c\x12\n\n\x02\x66l\x18\t \x03(\x0c\x12\x0f\n\x07presort\x18\n \x01(\x0c\"W\n\x12RpbSearchQueryResp\x12\x1b\n\x04\x64ocs\x18\x01 \x03(\x0b\x32\r.RpbSearchDoc\x12\x11\n\tmax_score\x18\x02 \x01(\x02\x12\x11\n\tnum_found\x18\x03 \x01(\rB\'\n\x17\x63om.basho.riak.protobufB\x0cRiakSearchPB')
  ,
  dependencies=[riak__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RPBSEARCHDOC = _descriptor.Descriptor(
  name='RpbSearchDoc',
  full_name='RpbSearchDoc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='RpbSearchDoc.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=73,
)


_RPBSEARCHQUERYREQ = _descriptor.Descriptor(
  name='RpbSearchQueryReq',
  full_name='RpbSearchQueryReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='q', full_name='RpbSearchQueryReq.q', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='RpbSearchQueryReq.index', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rows', full_name='RpbSearchQueryReq.rows', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='RpbSearchQueryReq.start', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort', full_name='RpbSearchQueryReq.sort', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter', full_name='RpbSearchQueryReq.filter', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='df', full_name='RpbSearchQueryReq.df', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op', full_name='RpbSearchQueryReq.op', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fl', full_name='RpbSearchQueryReq.fl', index=8,
      number=9, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='presort', full_name='RpbSearchQueryReq.presort', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=233,
)


_RPBSEARCHQUERYRESP = _descriptor.Descriptor(
  name='RpbSearchQueryResp',
  full_name='RpbSearchQueryResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docs', full_name='RpbSearchQueryResp.docs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_score', full_name='RpbSearchQueryResp.max_score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_found', full_name='RpbSearchQueryResp.num_found', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=322,
)

_RPBSEARCHDOC.fields_by_name['fields'].message_type = riak__pb2._RPBPAIR
_RPBSEARCHQUERYRESP.fields_by_name['docs'].message_type = _RPBSEARCHDOC
DESCRIPTOR.message_types_by_name['RpbSearchDoc'] = _RPBSEARCHDOC
DESCRIPTOR.message_types_by_name['RpbSearchQueryReq'] = _RPBSEARCHQUERYREQ
DESCRIPTOR.message_types_by_name['RpbSearchQueryResp'] = _RPBSEARCHQUERYRESP

RpbSearchDoc = _reflection.GeneratedProtocolMessageType('RpbSearchDoc', (_message.Message,), dict(
  DESCRIPTOR = _RPBSEARCHDOC,
  __module__ = 'riak_search_pb2'
  # @@protoc_insertion_point(class_scope:RpbSearchDoc)
  ))
_sym_db.RegisterMessage(RpbSearchDoc)

RpbSearchQueryReq = _reflection.GeneratedProtocolMessageType('RpbSearchQueryReq', (_message.Message,), dict(
  DESCRIPTOR = _RPBSEARCHQUERYREQ,
  __module__ = 'riak_search_pb2'
  # @@protoc_insertion_point(class_scope:RpbSearchQueryReq)
  ))
_sym_db.RegisterMessage(RpbSearchQueryReq)

RpbSearchQueryResp = _reflection.GeneratedProtocolMessageType('RpbSearchQueryResp', (_message.Message,), dict(
  DESCRIPTOR = _RPBSEARCHQUERYRESP,
  __module__ = 'riak_search_pb2'
  # @@protoc_insertion_point(class_scope:RpbSearchQueryResp)
  ))
_sym_db.RegisterMessage(RpbSearchQueryResp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027com.basho.riak.protobufB\014RiakSearchPB'))
# @@protoc_insertion_point(module_scope)
