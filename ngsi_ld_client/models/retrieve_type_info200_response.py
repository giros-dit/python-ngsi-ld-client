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


from typing import List, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, validator
from ngsi_ld_client.models.attribute import Attribute
from ngsi_ld_client.models.ld_context import LdContext

class RetrieveTypeInfo200Response(BaseModel):
    """
    RetrieveTypeInfo200Response
    """
    id: StrictStr = Field(..., description="Fully Qualified Name (FQN) of the entity type being described. ")
    type: StrictStr = Field(..., description="JSON-LD @type. ")
    type_name: StrictStr = Field(..., alias="typeName", description="Name of the entity type, short name if contained in @context. ")
    entity_count: Union[StrictFloat, StrictInt] = Field(..., alias="entityCount", description="Number of entity instances of this entity type. ")
    attribute_details: conlist(Attribute) = Field(..., alias="attributeDetails", description="List of attributes that entity instances with the specified entity type can have. ")
    context: LdContext = Field(..., alias="@context")
    __properties = ["id", "type", "typeName", "entityCount", "attributeDetails", "@context"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('EntityTypeInfo'):
            raise ValueError("must be one of enum values ('EntityTypeInfo')")
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
    def from_json(cls, json_str: str) -> RetrieveTypeInfo200Response:
        """Create an instance of RetrieveTypeInfo200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in attribute_details (list)
        _items = []
        if self.attribute_details:
            for _item in self.attribute_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributeDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RetrieveTypeInfo200Response:
        """Create an instance of RetrieveTypeInfo200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RetrieveTypeInfo200Response.parse_obj(obj)

        _obj = RetrieveTypeInfo200Response.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "type_name": obj.get("typeName"),
            "entity_count": obj.get("entityCount"),
            "attribute_details": [Attribute.from_dict(_item) for _item in obj.get("attributeDetails")] if obj.get("attributeDetails") is not None else None,
            "context": LdContext.from_dict(obj.get("@context")) if obj.get("@context") is not None else None
        })
        return _obj


