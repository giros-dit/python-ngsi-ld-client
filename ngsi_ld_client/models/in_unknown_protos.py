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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class InUnknownProtos(BaseModel):
    """
    NGSI-LD Property Type. For packet-oriented interfaces, the number of packets received via the interface that were discarded because of an unknown or unsupported protocol.  For character-oriented or fixed-length interfaces that support protocol multiplexing, the number of transmission units received via the interface that were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter is not present. 
    """
    type: StrictStr = Field(..., description="Node type. ")
    value: StrictInt = Field(...)
    observed_at: Optional[datetime] = Field(None, alias="observedAt", description="Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time. ")
    unit_code: Optional[StrictStr] = Field(None, alias="unitCode", description="Property Value's unit code. ")
    dataset_id: Optional[StrictStr] = Field(None, alias="datasetId", description="It allows identifying a set or group of property values. ")
    __properties = ["type", "value", "observedAt", "unitCode", "datasetId"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Property'):
            raise ValueError("must be one of enum values ('Property')")
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
    def from_json(cls, json_str: str) -> InUnknownProtos:
        """Create an instance of InUnknownProtos from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InUnknownProtos:
        """Create an instance of InUnknownProtos from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InUnknownProtos.parse_obj(obj)

        _obj = InUnknownProtos.parse_obj({
            "type": obj.get("type"),
            "value": obj.get("value"),
            "observed_at": obj.get("observedAt"),
            "unit_code": obj.get("unitCode"),
            "dataset_id": obj.get("datasetId")
        })
        return _obj

