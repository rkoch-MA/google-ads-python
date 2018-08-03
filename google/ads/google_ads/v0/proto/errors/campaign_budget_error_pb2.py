# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/campaign_budget_error.proto

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
  name='google/ads/googleads_v0/proto/errors/campaign_budget_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\n@google/ads/googleads_v0/proto/errors/campaign_budget_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xba\x05\n\x17\x43\x61mpaignBudgetErrorEnum\"\x9e\x05\n\x13\x43\x61mpaignBudgetError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1b\n\x17\x43\x41MPAIGN_BUDGET_REMOVED\x10\x02\x12\x1a\n\x16\x43\x41MPAIGN_BUDGET_IN_USE\x10\x03\x12(\n$CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE\x10\x04\x12<\n8CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET\x10\x06\x12\x36\n2CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED\x10\x07\x12\x43\n?CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME\x10\x08\x12\x36\n2CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED\x10\t\x12H\nDCANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS\x10\n\x12\x12\n\x0e\x44UPLICATE_NAME\x10\x0b\x12\"\n\x1eMONEY_AMOUNT_IN_WRONG_CURRENCY\x10\x0c\x12/\n+MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC\x10\r\x12\x1a\n\x16MONEY_AMOUNT_TOO_LARGE\x10\x0e\x12\x19\n\x15NEGATIVE_MONEY_AMOUNT\x10\x0f\x12)\n%NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT\x10\x10\x42\xce\x01\n\"com.google.ads.googleads.v0.errorsB\x18\x43\x61mpaignBudgetErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_CAMPAIGNBUDGETERRORENUM_CAMPAIGNBUDGETERROR = _descriptor.EnumDescriptor(
  name='CampaignBudgetError',
  full_name='google.ads.googleads.v0.errors.CampaignBudgetErrorEnum.CampaignBudgetError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_BUDGET_REMOVED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_BUDGET_IN_USE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_NAME', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONEY_AMOUNT_IN_WRONG_CURRENCY', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONEY_AMOUNT_TOO_LARGE', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEGATIVE_MONEY_AMOUNT', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT', index=15, number=16,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=129,
  serialized_end=799,
)
_sym_db.RegisterEnumDescriptor(_CAMPAIGNBUDGETERRORENUM_CAMPAIGNBUDGETERROR)


_CAMPAIGNBUDGETERRORENUM = _descriptor.Descriptor(
  name='CampaignBudgetErrorEnum',
  full_name='google.ads.googleads.v0.errors.CampaignBudgetErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CAMPAIGNBUDGETERRORENUM_CAMPAIGNBUDGETERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=799,
)

_CAMPAIGNBUDGETERRORENUM_CAMPAIGNBUDGETERROR.containing_type = _CAMPAIGNBUDGETERRORENUM
DESCRIPTOR.message_types_by_name['CampaignBudgetErrorEnum'] = _CAMPAIGNBUDGETERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignBudgetErrorEnum = _reflection.GeneratedProtocolMessageType('CampaignBudgetErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNBUDGETERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.campaign_budget_error_pb2'
  ,
  __doc__ = """Container for enum describing possible campaign budget errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.CampaignBudgetErrorEnum)
  ))
_sym_db.RegisterMessage(CampaignBudgetErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\030CampaignBudgetErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)