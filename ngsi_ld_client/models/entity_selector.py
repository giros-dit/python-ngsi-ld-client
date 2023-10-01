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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class EntitySelector(BaseModel):
    """
    5.2.33 This type selects which entity or group of entities are queried or subscribed to by Context Consumers. `id` takes precedence over `idPattern`. 
    """
    id: Optional[StrictStr] = Field(None, description="Entity identifier. ")
    id_pattern: Optional[StrictStr] = Field(None, alias="idPattern", description="A regular expression which denotes a pattern that shall be matched by the provided or subscribed Entities. ")
    type: StrictStr = Field(..., description="Selector of Entity Type(s). ")
    __properties = ["id", "idPattern", "type"]

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
    def from_json(cls, json_str: str) -> EntitySelector:
        """Create an instance of EntitySelector from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EntitySelector:
        """Create an instance of EntitySelector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EntitySelector.parse_obj(obj)

        _obj = EntitySelector.parse_obj({
            "id": obj.get("id"),
            "id_pattern": obj.get("idPattern"),
            "type": obj.get("type")
        })
        return _obj


