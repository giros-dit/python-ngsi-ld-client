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
from pydantic import BaseModel, Field, StrictStr
from ngsi_ld_client.models.entity_common_scope import EntityCommonScope
from ngsi_ld_client.models.entity_common_type import EntityCommonType
from ngsi_ld_client.models.geo_property_input import GeoPropertyInput

class EntityFragmentInput(BaseModel):
    """
    EntityFragmentInput
    """
    id: Optional[StrictStr] = Field(None, description="Entity id. ")
    type: Optional[EntityCommonType] = None
    scope: Optional[EntityCommonScope] = None
    location: Optional[GeoPropertyInput] = None
    observation_space: Optional[GeoPropertyInput] = Field(None, alias="observationSpace")
    operation_space: Optional[GeoPropertyInput] = Field(None, alias="operationSpace")
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "type", "scope", "location", "observationSpace", "operationSpace"]

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
    def from_json(cls, json_str: str) -> EntityFragmentInput:
        """Create an instance of EntityFragmentInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scope
        if self.scope:
            _dict['scope'] = self.scope.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of observation_space
        if self.observation_space:
            _dict['observationSpace'] = self.observation_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation_space
        if self.operation_space:
            _dict['operationSpace'] = self.operation_space.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EntityFragmentInput:
        """Create an instance of EntityFragmentInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EntityFragmentInput.parse_obj(obj)

        _obj = EntityFragmentInput.parse_obj({
            "id": obj.get("id"),
            "type": EntityCommonType.from_dict(obj.get("type")) if obj.get("type") is not None else None,
            "scope": EntityCommonScope.from_dict(obj.get("scope")) if obj.get("scope") is not None else None,
            "location": GeoPropertyInput.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "observation_space": GeoPropertyInput.from_dict(obj.get("observationSpace")) if obj.get("observationSpace") is not None else None,
            "operation_space": GeoPropertyInput.from_dict(obj.get("operationSpace")) if obj.get("operationSpace") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

