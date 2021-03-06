# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mercury.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mercury.proto',
  package='spotify.mercury.proto',
  serialized_pb='\n\rmercury.proto\x12\x15spotify.mercury.proto\"P\n\x16MercuryMultiGetRequest\x12\x36\n\x07request\x18\x01 \x03(\x0b\x32%.spotify.mercury.proto.MercuryRequest\"J\n\x14MercuryMultiGetReply\x12\x32\n\x05reply\x18\x01 \x03(\x0b\x32#.spotify.mercury.proto.MercuryReply\"\x9f\x01\n\x0eMercuryRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x02 \x01(\t\x12\x0e\n\x06method\x18\x03 \x01(\t\x12\x13\n\x0bstatus_code\x18\x04 \x01(\x11\x12\x0e\n\x06source\x18\x05 \x01(\t\x12\x35\n\x0buser_fields\x18\x06 \x03(\x0b\x32 .spotify.mercury.proto.UserField\"\x83\x02\n\x0cMercuryReply\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x11\x12\x16\n\x0estatus_message\x18\x02 \x01(\t\x12\x45\n\x0c\x63\x61\x63he_policy\x18\x03 \x01(\x0e\x32/.spotify.mercury.proto.MercuryReply.CachePolicy\x12\x0b\n\x03ttl\x18\x04 \x01(\x11\x12\x0c\n\x04\x65tag\x18\x05 \x01(\x0c\x12\x14\n\x0c\x63ontent_type\x18\x06 \x01(\x0c\x12\x0c\n\x04\x62ody\x18\x07 \x01(\x0c\"@\n\x0b\x43\x61\x63hePolicy\x12\x0c\n\x08\x43\x41\x43HE_NO\x10\x01\x12\x11\n\rCACHE_PRIVATE\x10\x02\x12\x10\n\x0c\x43\x41\x43HE_PUBLIC\x10\x03\"(\n\tUserField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c')



_MERCURYREPLY_CACHEPOLICY = _descriptor.EnumDescriptor(
  name='CachePolicy',
  full_name='spotify.mercury.proto.MercuryReply.CachePolicy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CACHE_NO', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CACHE_PRIVATE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CACHE_PUBLIC', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=556,
  serialized_end=620,
)


_MERCURYMULTIGETREQUEST = _descriptor.Descriptor(
  name='MercuryMultiGetRequest',
  full_name='spotify.mercury.proto.MercuryMultiGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='spotify.mercury.proto.MercuryMultiGetRequest.request', index=0,
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
  extension_ranges=[],
  serialized_start=40,
  serialized_end=120,
)


_MERCURYMULTIGETREPLY = _descriptor.Descriptor(
  name='MercuryMultiGetReply',
  full_name='spotify.mercury.proto.MercuryMultiGetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='spotify.mercury.proto.MercuryMultiGetReply.reply', index=0,
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
  extension_ranges=[],
  serialized_start=122,
  serialized_end=196,
)


_MERCURYREQUEST = _descriptor.Descriptor(
  name='MercuryRequest',
  full_name='spotify.mercury.proto.MercuryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='spotify.mercury.proto.MercuryRequest.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='spotify.mercury.proto.MercuryRequest.content_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='spotify.mercury.proto.MercuryRequest.method', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_code', full_name='spotify.mercury.proto.MercuryRequest.status_code', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='spotify.mercury.proto.MercuryRequest.source', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_fields', full_name='spotify.mercury.proto.MercuryRequest.user_fields', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  serialized_start=199,
  serialized_end=358,
)


_MERCURYREPLY = _descriptor.Descriptor(
  name='MercuryReply',
  full_name='spotify.mercury.proto.MercuryReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='spotify.mercury.proto.MercuryReply.status_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_message', full_name='spotify.mercury.proto.MercuryReply.status_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cache_policy', full_name='spotify.mercury.proto.MercuryReply.cache_policy', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='spotify.mercury.proto.MercuryReply.ttl', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='etag', full_name='spotify.mercury.proto.MercuryReply.etag', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='spotify.mercury.proto.MercuryReply.content_type', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='spotify.mercury.proto.MercuryReply.body', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MERCURYREPLY_CACHEPOLICY,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=361,
  serialized_end=620,
)


_USERFIELD = _descriptor.Descriptor(
  name='UserField',
  full_name='spotify.mercury.proto.UserField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='spotify.mercury.proto.UserField.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='spotify.mercury.proto.UserField.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=622,
  serialized_end=662,
)

_MERCURYMULTIGETREQUEST.fields_by_name['request'].message_type = _MERCURYREQUEST
_MERCURYMULTIGETREPLY.fields_by_name['reply'].message_type = _MERCURYREPLY
_MERCURYREQUEST.fields_by_name['user_fields'].message_type = _USERFIELD
_MERCURYREPLY.fields_by_name['cache_policy'].enum_type = _MERCURYREPLY_CACHEPOLICY
_MERCURYREPLY_CACHEPOLICY.containing_type = _MERCURYREPLY;
DESCRIPTOR.message_types_by_name['MercuryMultiGetRequest'] = _MERCURYMULTIGETREQUEST
DESCRIPTOR.message_types_by_name['MercuryMultiGetReply'] = _MERCURYMULTIGETREPLY
DESCRIPTOR.message_types_by_name['MercuryRequest'] = _MERCURYREQUEST
DESCRIPTOR.message_types_by_name['MercuryReply'] = _MERCURYREPLY
DESCRIPTOR.message_types_by_name['UserField'] = _USERFIELD

class MercuryMultiGetRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MERCURYMULTIGETREQUEST

  # @@protoc_insertion_point(class_scope:spotify.mercury.proto.MercuryMultiGetRequest)

class MercuryMultiGetReply(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MERCURYMULTIGETREPLY

  # @@protoc_insertion_point(class_scope:spotify.mercury.proto.MercuryMultiGetReply)

class MercuryRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MERCURYREQUEST

  # @@protoc_insertion_point(class_scope:spotify.mercury.proto.MercuryRequest)

class MercuryReply(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MERCURYREPLY

  # @@protoc_insertion_point(class_scope:spotify.mercury.proto.MercuryReply)

class UserField(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERFIELD

  # @@protoc_insertion_point(class_scope:spotify.mercury.proto.UserField)


# @@protoc_insertion_point(module_scope)
