# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/ad_group_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import ad_group_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/ad_group_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\n=google/ads/googleads_v0/proto/services/ad_group_service.proto\x12 google.ads.googleads.v0.services\x1a\x36google/ads/googleads_v0/proto/resources/ad_group.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"*\n\x11GetAdGroupRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"t\n\x15MutateAdGroupsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\x46\n\noperations\x18\x02 \x03(\x0b\x32\x32.google.ads.googleads.v0.services.AdGroupOperation\"\xde\x01\n\x10\x41\x64GroupOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12<\n\x06\x63reate\x18\x01 \x01(\x0b\x32*.google.ads.googleads.v0.resources.AdGroupH\x00\x12<\n\x06update\x18\x02 \x01(\x0b\x32*.google.ads.googleads.v0.resources.AdGroupH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"`\n\x16MutateAdGroupsResponse\x12\x46\n\x07results\x18\x02 \x03(\x0b\x32\x35.google.ads.googleads.v0.services.MutateAdGroupResult\",\n\x13MutateAdGroupResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xf4\x02\n\x0e\x41\x64GroupService\x12\xa1\x01\n\nGetAdGroup\x12\x33.google.ads.googleads.v0.services.GetAdGroupRequest\x1a*.google.ads.googleads.v0.resources.AdGroup\"2\x82\xd3\xe4\x93\x02,\x12*/v0/{resource_name=customers/*/adGroups/*}\x12\xbd\x01\n\x0eMutateAdGroups\x12\x37.google.ads.googleads.v0.services.MutateAdGroupsRequest\x1a\x38.google.ads.googleads.v0.services.MutateAdGroupsResponse\"8\x82\xd3\xe4\x93\x02\x32\"-/v0/customers/{customer_id=*}/adGroups:mutate:\x01*B\xd3\x01\n$com.google.ads.googleads.v0.servicesB\x13\x41\x64GroupServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_GETADGROUPREQUEST = _descriptor.Descriptor(
  name='GetAdGroupRequest',
  full_name='google.ads.googleads.v0.services.GetAdGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetAdGroupRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=261,
)


_MUTATEADGROUPSREQUEST = _descriptor.Descriptor(
  name='MutateAdGroupsRequest',
  full_name='google.ads.googleads.v0.services.MutateAdGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.MutateAdGroupsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v0.services.MutateAdGroupsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=263,
  serialized_end=379,
)


_ADGROUPOPERATION = _descriptor.Descriptor(
  name='AdGroupOperation',
  full_name='google.ads.googleads.v0.services.AdGroupOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v0.services.AdGroupOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v0.services.AdGroupOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v0.services.AdGroupOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v0.services.AdGroupOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v0.services.AdGroupOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=382,
  serialized_end=604,
)


_MUTATEADGROUPSRESPONSE = _descriptor.Descriptor(
  name='MutateAdGroupsResponse',
  full_name='google.ads.googleads.v0.services.MutateAdGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v0.services.MutateAdGroupsResponse.results', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=702,
)


_MUTATEADGROUPRESULT = _descriptor.Descriptor(
  name='MutateAdGroupResult',
  full_name='google.ads.googleads.v0.services.MutateAdGroupResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.MutateAdGroupResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=704,
  serialized_end=748,
)

_MUTATEADGROUPSREQUEST.fields_by_name['operations'].message_type = _ADGROUPOPERATION
_ADGROUPOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_ADGROUPOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__pb2._ADGROUP
_ADGROUPOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__pb2._ADGROUP
_ADGROUPOPERATION.oneofs_by_name['operation'].fields.append(
  _ADGROUPOPERATION.fields_by_name['create'])
_ADGROUPOPERATION.fields_by_name['create'].containing_oneof = _ADGROUPOPERATION.oneofs_by_name['operation']
_ADGROUPOPERATION.oneofs_by_name['operation'].fields.append(
  _ADGROUPOPERATION.fields_by_name['update'])
_ADGROUPOPERATION.fields_by_name['update'].containing_oneof = _ADGROUPOPERATION.oneofs_by_name['operation']
_ADGROUPOPERATION.oneofs_by_name['operation'].fields.append(
  _ADGROUPOPERATION.fields_by_name['remove'])
_ADGROUPOPERATION.fields_by_name['remove'].containing_oneof = _ADGROUPOPERATION.oneofs_by_name['operation']
_MUTATEADGROUPSRESPONSE.fields_by_name['results'].message_type = _MUTATEADGROUPRESULT
DESCRIPTOR.message_types_by_name['GetAdGroupRequest'] = _GETADGROUPREQUEST
DESCRIPTOR.message_types_by_name['MutateAdGroupsRequest'] = _MUTATEADGROUPSREQUEST
DESCRIPTOR.message_types_by_name['AdGroupOperation'] = _ADGROUPOPERATION
DESCRIPTOR.message_types_by_name['MutateAdGroupsResponse'] = _MUTATEADGROUPSRESPONSE
DESCRIPTOR.message_types_by_name['MutateAdGroupResult'] = _MUTATEADGROUPRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdGroupRequest = _reflection.GeneratedProtocolMessageType('GetAdGroupRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETADGROUPREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.ad_group_service_pb2'
  ,
  __doc__ = """Request message for
  [AdGroupService.GetAdGroup][google.ads.googleads.v0.services.AdGroupService.GetAdGroup].
  
  
  Attributes:
      resource_name:
          The resource name of the ad group to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetAdGroupRequest)
  ))
_sym_db.RegisterMessage(GetAdGroupRequest)

MutateAdGroupsRequest = _reflection.GeneratedProtocolMessageType('MutateAdGroupsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADGROUPSREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.ad_group_service_pb2'
  ,
  __doc__ = """Request message for
  [AdGroupService.MutateAdGroups][google.ads.googleads.v0.services.AdGroupService.MutateAdGroups].
  
  
  Attributes:
      customer_id:
          The ID of the customer whose ad groups are being modified.
      operations:
          The list of operations to perform on individual ad groups.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateAdGroupsRequest)
  ))
_sym_db.RegisterMessage(MutateAdGroupsRequest)

AdGroupOperation = _reflection.GeneratedProtocolMessageType('AdGroupOperation', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPOPERATION,
  __module__ = 'google.ads.googleads_v0.proto.services.ad_group_service_pb2'
  ,
  __doc__ = """A single operation (create, update, remove) on an ad group.
  
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new ad
          group.
      update:
          Update operation: The ad group is expected to have a valid
          resource name.
      remove:
          Remove operation: A resource name for the removed ad group is
          expected, in this format:
          ``customers/{customer_id}/adGroups/{ad_group_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.AdGroupOperation)
  ))
_sym_db.RegisterMessage(AdGroupOperation)

MutateAdGroupsResponse = _reflection.GeneratedProtocolMessageType('MutateAdGroupsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADGROUPSRESPONSE,
  __module__ = 'google.ads.googleads_v0.proto.services.ad_group_service_pb2'
  ,
  __doc__ = """Response message for an ad group mutate.
  
  
  Attributes:
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateAdGroupsResponse)
  ))
_sym_db.RegisterMessage(MutateAdGroupsResponse)

MutateAdGroupResult = _reflection.GeneratedProtocolMessageType('MutateAdGroupResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADGROUPRESULT,
  __module__ = 'google.ads.googleads_v0.proto.services.ad_group_service_pb2'
  ,
  __doc__ = """The result for the ad group mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateAdGroupResult)
  ))
_sym_db.RegisterMessage(MutateAdGroupResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\023AdGroupServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_ADGROUPSERVICE = _descriptor.ServiceDescriptor(
  name='AdGroupService',
  full_name='google.ads.googleads.v0.services.AdGroupService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=751,
  serialized_end=1123,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAdGroup',
    full_name='google.ads.googleads.v0.services.AdGroupService.GetAdGroup',
    index=0,
    containing_service=None,
    input_type=_GETADGROUPREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__pb2._ADGROUP,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002,\022*/v0/{resource_name=customers/*/adGroups/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='MutateAdGroups',
    full_name='google.ads.googleads.v0.services.AdGroupService.MutateAdGroups',
    index=1,
    containing_service=None,
    input_type=_MUTATEADGROUPSREQUEST,
    output_type=_MUTATEADGROUPSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0022\"-/v0/customers/{customer_id=*}/adGroups:mutate:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_ADGROUPSERVICE)

DESCRIPTOR.services_by_name['AdGroupService'] = _ADGROUPSERVICE

# @@protoc_insertion_point(module_scope)