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

class RelationshipInput(BaseModel):
    """
    RelationshipInput
    """
    type: StrictStr = Field(..., description="Node type. ")
    object: StrictStr = Field(..., description="Relationship's target object. ")
    observed_at: Optional[datetime] = Field(None, alias="observedAt", description="Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time. ")
    dataset_id: Optional[StrictStr] = Field(None, alias="datasetId", description="It allows identifying a set or group of target relationship objects. ")
    __properties = ["type", "object", "observedAt", "datasetId"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Relationship'):
            raise ValueError("must be one of enum values ('Relationship')")
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
    def from_json(cls, json_str: str) -> RelationshipInput:
        """Create an instance of RelationshipInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RelationshipInput:
        """Create an instance of RelationshipInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RelationshipInput.parse_obj(obj)

        _obj = RelationshipInput.parse_obj({
            "type": obj.get("type"),
            "object": obj.get("object"),
            "observed_at": obj.get("observedAt"),
            "dataset_id": obj.get("datasetId")
        })
        return _obj

