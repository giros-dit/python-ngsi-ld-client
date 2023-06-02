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


from typing import Optional
from pydantic import BaseModel, Field
from ngsi_ld_client.models.geo_property_input import GeoPropertyInput

class EntityFragmentInputAllOf(BaseModel):
    """
    EntityFragmentInputAllOf
    """
    location: Optional[GeoPropertyInput] = None
    observation_space: Optional[GeoPropertyInput] = Field(None, alias="observationSpace")
    operation_space: Optional[GeoPropertyInput] = Field(None, alias="operationSpace")
    __properties = ["location", "observationSpace", "operationSpace"]

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
    def from_json(cls, json_str: str) -> EntityFragmentInputAllOf:
        """Create an instance of EntityFragmentInputAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of observation_space
        if self.observation_space:
            _dict['observationSpace'] = self.observation_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation_space
        if self.operation_space:
            _dict['operationSpace'] = self.operation_space.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EntityFragmentInputAllOf:
        """Create an instance of EntityFragmentInputAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EntityFragmentInputAllOf.parse_obj(obj)

        _obj = EntityFragmentInputAllOf.parse_obj({
            "location": GeoPropertyInput.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "observation_space": GeoPropertyInput.from_dict(obj.get("observationSpace")) if obj.get("observationSpace") is not None else None,
            "operation_space": GeoPropertyInput.from_dict(obj.get("operationSpace")) if obj.get("operationSpace") is not None else None
        })
        return _obj

