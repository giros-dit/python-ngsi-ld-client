# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, validator
from ngsi_ld_client.models.ld_context import LdContext

class RetrieveAttrInfo200Response(BaseModel):
    """
    RetrieveAttrInfo200Response
    """
    id: StrictStr = Field(..., description="Full URI of attribute name. ")
    type: StrictStr = Field(..., description="JSON-LD @type. ")
    attribute_name: StrictStr = Field(..., alias="attributeName", description="Name of the attribute, short name if contained in @context. ")
    attribute_count: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="attributeCount", description="Number of attribute instances with this attribute name. ")
    attribute_types: Optional[conlist(StrictStr)] = Field(None, alias="attributeTypes", description="List of attribute types (e.g. Property, Relationship, GeoProperty) for which entity instances exist, which contain an attribute with this name. ")
    type_names: Optional[conlist(StrictStr)] = Field(None, alias="typeNames", description="List of entity type names for which entity instances exist containing attributes that have the respective name. ")
    context: LdContext = Field(..., alias="@context")
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "type", "attributeName", "attributeCount", "attributeTypes", "typeNames", "@context"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Attribute'):
            raise ValueError("must be one of enum values ('Attribute')")
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
    def from_json(cls, json_str: str) -> RetrieveAttrInfo200Response:
        """Create an instance of RetrieveAttrInfo200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RetrieveAttrInfo200Response:
        """Create an instance of RetrieveAttrInfo200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RetrieveAttrInfo200Response.parse_obj(obj)

        _obj = RetrieveAttrInfo200Response.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "attribute_name": obj.get("attributeName"),
            "attribute_count": obj.get("attributeCount"),
            "attribute_types": obj.get("attributeTypes"),
            "type_names": obj.get("typeNames"),
            "context": LdContext.from_dict(obj.get("@context")) if obj.get("@context") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


