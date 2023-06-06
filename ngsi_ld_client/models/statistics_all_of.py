# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from ngsi_ld_client.models.discontinuity_time import DiscontinuityTime
from ngsi_ld_client.models.in_broadcast_pkts import InBroadcastPkts
from ngsi_ld_client.models.in_discards import InDiscards
from ngsi_ld_client.models.in_errors import InErrors
from ngsi_ld_client.models.in_multicast_pkts import InMulticastPkts
from ngsi_ld_client.models.in_octets import InOctets
from ngsi_ld_client.models.in_unicast_pkts import InUnicastPkts
from ngsi_ld_client.models.in_unknown_protos import InUnknownProtos
from ngsi_ld_client.models.is_part_of import IsPartOf
from ngsi_ld_client.models.out_broadcast_pkts import OutBroadcastPkts
from ngsi_ld_client.models.out_discards import OutDiscards
from ngsi_ld_client.models.out_errors import OutErrors
from ngsi_ld_client.models.out_multicast_pkts import OutMulticastPkts
from ngsi_ld_client.models.out_octets import OutOctets
from ngsi_ld_client.models.out_unicast_pkts import OutUnicastPkts

class StatisticsAllOf(BaseModel):
    """
    StatisticsAllOf
    """
    type: Optional[StrictStr] = Field('Statistics', description="NGSI-LD Entity identifier. It has to be Statistics.")
    is_part_of: Optional[IsPartOf] = Field(None, alias="isPartOf")
    discontinuity_time: Optional[DiscontinuityTime] = Field(None, alias="discontinuityTime")
    in_octets: Optional[InOctets] = Field(None, alias="inOctets")
    in_unicast_pkts: Optional[InUnicastPkts] = Field(None, alias="inUnicastPkts")
    in_broadcast_pkts: Optional[InBroadcastPkts] = Field(None, alias="inBroadcastPkts")
    in_multicast_pkts: Optional[InMulticastPkts] = Field(None, alias="inMulticastPkts")
    in_discards: Optional[InDiscards] = Field(None, alias="inDiscards")
    in_errors: Optional[InErrors] = Field(None, alias="inErrors")
    in_unknown_protos: Optional[InUnknownProtos] = Field(None, alias="inUnknownProtos")
    out_octets: Optional[OutOctets] = Field(None, alias="outOctets")
    out_unicast_pkts: Optional[OutUnicastPkts] = Field(None, alias="outUnicastPkts")
    out_broadcast_pkts: Optional[OutBroadcastPkts] = Field(None, alias="outBroadcastPkts")
    out_multicast_pkts: Optional[OutMulticastPkts] = Field(None, alias="outMulticastPkts")
    out_discards: Optional[OutDiscards] = Field(None, alias="outDiscards")
    out_errors: Optional[OutErrors] = Field(None, alias="outErrors")
    __properties = ["type", "isPartOf", "discontinuityTime", "inOctets", "inUnicastPkts", "inBroadcastPkts", "inMulticastPkts", "inDiscards", "inErrors", "inUnknownProtos", "outOctets", "outUnicastPkts", "outBroadcastPkts", "outMulticastPkts", "outDiscards", "outErrors"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Statistics'):
            raise ValueError("must be one of enum values ('Statistics')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> StatisticsAllOf:
        """Create an instance of StatisticsAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of is_part_of
        if self.is_part_of:
            _dict['isPartOf'] = self.is_part_of.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discontinuity_time
        if self.discontinuity_time:
            _dict['discontinuityTime'] = self.discontinuity_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_octets
        if self.in_octets:
            _dict['inOctets'] = self.in_octets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_unicast_pkts
        if self.in_unicast_pkts:
            _dict['inUnicastPkts'] = self.in_unicast_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_broadcast_pkts
        if self.in_broadcast_pkts:
            _dict['inBroadcastPkts'] = self.in_broadcast_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_multicast_pkts
        if self.in_multicast_pkts:
            _dict['inMulticastPkts'] = self.in_multicast_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_discards
        if self.in_discards:
            _dict['inDiscards'] = self.in_discards.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_errors
        if self.in_errors:
            _dict['inErrors'] = self.in_errors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_unknown_protos
        if self.in_unknown_protos:
            _dict['inUnknownProtos'] = self.in_unknown_protos.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_octets
        if self.out_octets:
            _dict['outOctets'] = self.out_octets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_unicast_pkts
        if self.out_unicast_pkts:
            _dict['outUnicastPkts'] = self.out_unicast_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_broadcast_pkts
        if self.out_broadcast_pkts:
            _dict['outBroadcastPkts'] = self.out_broadcast_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_multicast_pkts
        if self.out_multicast_pkts:
            _dict['outMulticastPkts'] = self.out_multicast_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_discards
        if self.out_discards:
            _dict['outDiscards'] = self.out_discards.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_errors
        if self.out_errors:
            _dict['outErrors'] = self.out_errors.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StatisticsAllOf:
        """Create an instance of StatisticsAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StatisticsAllOf.parse_obj(obj)

        _obj = StatisticsAllOf.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'Statistics',
            "is_part_of": IsPartOf.from_dict(obj.get("isPartOf")) if obj.get("isPartOf") is not None else None,
            "discontinuity_time": DiscontinuityTime.from_dict(obj.get("discontinuityTime")) if obj.get("discontinuityTime") is not None else None,
            "in_octets": InOctets.from_dict(obj.get("inOctets")) if obj.get("inOctets") is not None else None,
            "in_unicast_pkts": InUnicastPkts.from_dict(obj.get("inUnicastPkts")) if obj.get("inUnicastPkts") is not None else None,
            "in_broadcast_pkts": InBroadcastPkts.from_dict(obj.get("inBroadcastPkts")) if obj.get("inBroadcastPkts") is not None else None,
            "in_multicast_pkts": InMulticastPkts.from_dict(obj.get("inMulticastPkts")) if obj.get("inMulticastPkts") is not None else None,
            "in_discards": InDiscards.from_dict(obj.get("inDiscards")) if obj.get("inDiscards") is not None else None,
            "in_errors": InErrors.from_dict(obj.get("inErrors")) if obj.get("inErrors") is not None else None,
            "in_unknown_protos": InUnknownProtos.from_dict(obj.get("inUnknownProtos")) if obj.get("inUnknownProtos") is not None else None,
            "out_octets": OutOctets.from_dict(obj.get("outOctets")) if obj.get("outOctets") is not None else None,
            "out_unicast_pkts": OutUnicastPkts.from_dict(obj.get("outUnicastPkts")) if obj.get("outUnicastPkts") is not None else None,
            "out_broadcast_pkts": OutBroadcastPkts.from_dict(obj.get("outBroadcastPkts")) if obj.get("outBroadcastPkts") is not None else None,
            "out_multicast_pkts": OutMulticastPkts.from_dict(obj.get("outMulticastPkts")) if obj.get("outMulticastPkts") is not None else None,
            "out_discards": OutDiscards.from_dict(obj.get("outDiscards")) if obj.get("outDiscards") is not None else None,
            "out_errors": OutErrors.from_dict(obj.get("outErrors")) if obj.get("outErrors") is not None else None
        })
        return _obj

