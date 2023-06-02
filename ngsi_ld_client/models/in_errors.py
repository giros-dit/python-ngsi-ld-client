# coding: utf-8

"""
    ietf-intefaces@2018-02-20.yang

    OpenAPI schema for the ietf-intefaces@2018-02-20.yang YANG module  supported by a model-based network device.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
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

class InErrors(BaseModel):
    """
    NGSI-LD Property Type. For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character- oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. 
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
    def from_json(cls, json_str: str) -> InErrors:
        """Create an instance of InErrors from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InErrors:
        """Create an instance of InErrors from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InErrors.parse_obj(obj)

        _obj = InErrors.parse_obj({
            "type": obj.get("type"),
            "value": obj.get("value"),
            "observed_at": obj.get("observedAt"),
            "unit_code": obj.get("unitCode"),
            "dataset_id": obj.get("datasetId")
        })
        return _obj

