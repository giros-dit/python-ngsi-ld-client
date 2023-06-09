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
from pydantic import BaseModel, Field, StrictStr, validator

class DiscontinuityTime(BaseModel):
    """
    NGSI-LD Property Type. The time on the most recent occasion at which any one or more of this interface's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re-initialization of the local management subsystem, then this node contains the time the local management subsystem re-initialized itself. 
    """
    type: StrictStr = Field(..., description="Node type. ")
    value: datetime = Field(...)
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
    def from_json(cls, json_str: str) -> DiscontinuityTime:
        """Create an instance of DiscontinuityTime from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiscontinuityTime:
        """Create an instance of DiscontinuityTime from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DiscontinuityTime.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in DiscontinuityTime) in the input: " + obj)

        _obj = DiscontinuityTime.parse_obj({
            "type": obj.get("type"),
            "value": obj.get("value"),
            "observed_at": obj.get("observedAt"),
            "unit_code": obj.get("unitCode"),
            "dataset_id": obj.get("datasetId")
        })
        return _obj

