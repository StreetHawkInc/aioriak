# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: riak_yokozuna.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='riak_yokozuna.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x13riak_yokozuna.proto\"?\n\x10RpbYokozunaIndex\x12\x0c\n\x04name\x18\x01 \x02(\x0c\x12\x0e\n\x06schema\x18\x02 \x01(\x0c\x12\r\n\x05n_val\x18\x03 \x01(\r\"&\n\x16RpbYokozunaIndexGetReq\x12\x0c\n\x04name\x18\x01 \x01(\x0c\";\n\x17RpbYokozunaIndexGetResp\x12 \n\x05index\x18\x01 \x03(\x0b\x32\x11.RpbYokozunaIndex\"K\n\x16RpbYokozunaIndexPutReq\x12 \n\x05index\x18\x01 \x02(\x0b\x32\x11.RpbYokozunaIndex\x12\x0f\n\x07timeout\x18\x02 \x01(\r\")\n\x19RpbYokozunaIndexDeleteReq\x12\x0c\n\x04name\x18\x01 \x02(\x0c\"2\n\x11RpbYokozunaSchema\x12\x0c\n\x04name\x18\x01 \x02(\x0c\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"=\n\x17RpbYokozunaSchemaPutReq\x12\"\n\x06schema\x18\x01 \x02(\x0b\x32\x12.RpbYokozunaSchema\"\'\n\x17RpbYokozunaSchemaGetReq\x12\x0c\n\x04name\x18\x01 \x02(\x0c\">\n\x18RpbYokozunaSchemaGetResp\x12\"\n\x06schema\x18\x01 \x02(\x0b\x32\x12.RpbYokozunaSchemaB)\n\x17\x63om.basho.riak.protobufB\x0eRiakYokozunaPB')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RPBYOKOZUNAINDEX = _descriptor.Descriptor(
  name='RpbYokozunaIndex',
  full_name='RpbYokozunaIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RpbYokozunaIndex.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schema', full_name='RpbYokozunaIndex.schema', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='n_val', full_name='RpbYokozunaIndex.n_val', index=2,
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
  serialized_start=23,
  serialized_end=86,
)


_RPBYOKOZUNAINDEXGETREQ = _descriptor.Descriptor(
  name='RpbYokozunaIndexGetReq',
  full_name='RpbYokozunaIndexGetReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RpbYokozunaIndexGetReq.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=88,
  serialized_end=126,
)


_RPBYOKOZUNAINDEXGETRESP = _descriptor.Descriptor(
  name='RpbYokozunaIndexGetResp',
  full_name='RpbYokozunaIndexGetResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='RpbYokozunaIndexGetResp.index', index=0,
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
  serialized_start=128,
  serialized_end=187,
)


_RPBYOKOZUNAINDEXPUTREQ = _descriptor.Descriptor(
  name='RpbYokozunaIndexPutReq',
  full_name='RpbYokozunaIndexPutReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='RpbYokozunaIndexPutReq.index', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='RpbYokozunaIndexPutReq.timeout', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=189,
  serialized_end=264,
)


_RPBYOKOZUNAINDEXDELETEREQ = _descriptor.Descriptor(
  name='RpbYokozunaIndexDeleteReq',
  full_name='RpbYokozunaIndexDeleteReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RpbYokozunaIndexDeleteReq.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
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
  serialized_start=266,
  serialized_end=307,
)


_RPBYOKOZUNASCHEMA = _descriptor.Descriptor(
  name='RpbYokozunaSchema',
  full_name='RpbYokozunaSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RpbYokozunaSchema.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='RpbYokozunaSchema.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_start=309,
  serialized_end=359,
)


_RPBYOKOZUNASCHEMAPUTREQ = _descriptor.Descriptor(
  name='RpbYokozunaSchemaPutReq',
  full_name='RpbYokozunaSchemaPutReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='RpbYokozunaSchemaPutReq.schema', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=361,
  serialized_end=422,
)


_RPBYOKOZUNASCHEMAGETREQ = _descriptor.Descriptor(
  name='RpbYokozunaSchemaGetReq',
  full_name='RpbYokozunaSchemaGetReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RpbYokozunaSchemaGetReq.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
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
  serialized_start=424,
  serialized_end=463,
)


_RPBYOKOZUNASCHEMAGETRESP = _descriptor.Descriptor(
  name='RpbYokozunaSchemaGetResp',
  full_name='RpbYokozunaSchemaGetResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='RpbYokozunaSchemaGetResp.schema', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=465,
  serialized_end=527,
)

_RPBYOKOZUNAINDEXGETRESP.fields_by_name['index'].message_type = _RPBYOKOZUNAINDEX
_RPBYOKOZUNAINDEXPUTREQ.fields_by_name['index'].message_type = _RPBYOKOZUNAINDEX
_RPBYOKOZUNASCHEMAPUTREQ.fields_by_name['schema'].message_type = _RPBYOKOZUNASCHEMA
_RPBYOKOZUNASCHEMAGETRESP.fields_by_name['schema'].message_type = _RPBYOKOZUNASCHEMA
DESCRIPTOR.message_types_by_name['RpbYokozunaIndex'] = _RPBYOKOZUNAINDEX
DESCRIPTOR.message_types_by_name['RpbYokozunaIndexGetReq'] = _RPBYOKOZUNAINDEXGETREQ
DESCRIPTOR.message_types_by_name['RpbYokozunaIndexGetResp'] = _RPBYOKOZUNAINDEXGETRESP
DESCRIPTOR.message_types_by_name['RpbYokozunaIndexPutReq'] = _RPBYOKOZUNAINDEXPUTREQ
DESCRIPTOR.message_types_by_name['RpbYokozunaIndexDeleteReq'] = _RPBYOKOZUNAINDEXDELETEREQ
DESCRIPTOR.message_types_by_name['RpbYokozunaSchema'] = _RPBYOKOZUNASCHEMA
DESCRIPTOR.message_types_by_name['RpbYokozunaSchemaPutReq'] = _RPBYOKOZUNASCHEMAPUTREQ
DESCRIPTOR.message_types_by_name['RpbYokozunaSchemaGetReq'] = _RPBYOKOZUNASCHEMAGETREQ
DESCRIPTOR.message_types_by_name['RpbYokozunaSchemaGetResp'] = _RPBYOKOZUNASCHEMAGETRESP

RpbYokozunaIndex = _reflection.GeneratedProtocolMessageType('RpbYokozunaIndex', (_message.Message,), dict(
  DESCRIPTOR = _RPBYOKOZUNAINDEX,
  __module__ = 'riak_yokozuna_pb2'
  # @@protoc_insertion_point(class_scope:RpbYokozunaIndex)
  ))
_sym_db.RegisterMessage(RpbYokozunaIndex)

RpbYokozunaIndexGetReq = _reflection.GeneratedProtocolMessageType('RpbYokozunaIndexGetReq', (_message.Message,), dict(
  DESCRIPTOR = _RPBYOKOZUNAINDEXGETREQ,
  __module__ = 'riak_yokozuna_pb2'
  # @@protoc_insertion_point(class_scope:RpbYokozunaIndexGetReq)
  ))
_sym_db.RegisterMessage(RpbYokozunaIndexGetReq)

RpbYokozunaIndexGetResp = _reflection.GeneratedProtocolMessageType('RpbYokozunaIndexGetResp', (_message.Message,), dict(
  DESCRIPTOR = _RPBYOKOZUNAINDEXGETRESP,
  __module__ = 'riak_yokozuna_pb2'
  # @@protoc_insertion_point(class_scope:RpbYokozunaIndexGetResp)
  ))
_sym_db.RegisterMessage(RpbYokozunaIndexGetResp)

RpbYokozunaIndexPutReq = _reflection.GeneratedProtocolMessageType('RpbYokozunaIndexPutReq', (_message.Message,), dict(
  DESCRIPTOR = _RPBYOKOZUNAINDEXPUTREQ,
  __module__ = 'riak_yokozuna_pb2'
  # @@protoc_insertion_point(class_scope:RpbYokozunaIndexPutReq)
  ))
_sym_db.RegisterMessage(RpbYokozunaIndexPutReq)

RpbYokozunaIndexDeleteReq = _reflection.GeneratedProtocolMessageType('RpbYokozunaIndexDeleteReq', (_message.Message,), dict(
  DESCRIPTOR = _RPBYOKOZUNAINDEXDELETEREQ,
  __module__ = 'riak_yokozuna_pb2'
  # @@protoc_insertion_point(class_scope:RpbYokozunaIndexDeleteReq)
  ))
_sym_db.RegisterMessage(RpbYokozunaIndexDeleteReq)

RpbYokozunaSchema = _reflection.GeneratedProtocolMessageType('RpbYokozunaSchema', (_message.Message,), dict(
  DESCRIPTOR = _RPBYOKOZUNASCHEMA,
  __module__ = 'riak_yokozuna_pb2'
  # @@protoc_insertion_point(class_scope:RpbYokozunaSchema)
  ))
_sym_db.RegisterMessage(RpbYokozunaSchema)

RpbYokozunaSchemaPutReq = _reflection.GeneratedProtocolMessageType('RpbYokozunaSchemaPutReq', (_message.Message,), dict(
  DESCRIPTOR = _RPBYOKOZUNASCHEMAPUTREQ,
  __module__ = 'riak_yokozuna_pb2'
  # @@protoc_insertion_point(class_scope:RpbYokozunaSchemaPutReq)
  ))
_sym_db.RegisterMessage(RpbYokozunaSchemaPutReq)

RpbYokozunaSchemaGetReq = _reflection.GeneratedProtocolMessageType('RpbYokozunaSchemaGetReq', (_message.Message,), dict(
  DESCRIPTOR = _RPBYOKOZUNASCHEMAGETREQ,
  __module__ = 'riak_yokozuna_pb2'
  # @@protoc_insertion_point(class_scope:RpbYokozunaSchemaGetReq)
  ))
_sym_db.RegisterMessage(RpbYokozunaSchemaGetReq)

RpbYokozunaSchemaGetResp = _reflection.GeneratedProtocolMessageType('RpbYokozunaSchemaGetResp', (_message.Message,), dict(
  DESCRIPTOR = _RPBYOKOZUNASCHEMAGETRESP,
  __module__ = 'riak_yokozuna_pb2'
  # @@protoc_insertion_point(class_scope:RpbYokozunaSchemaGetResp)
  ))
_sym_db.RegisterMessage(RpbYokozunaSchemaGetResp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027com.basho.riak.protobufB\016RiakYokozunaPB'))
# @@protoc_insertion_point(module_scope)
