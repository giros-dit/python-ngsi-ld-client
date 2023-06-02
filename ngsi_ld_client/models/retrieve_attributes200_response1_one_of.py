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



from pydantic import BaseModel, Field
from ngsi_ld_client.models.ld_context import LdContext

class RetrieveAttributes200Response1OneOf(BaseModel):
    """
    RetrieveAttributes200Response1OneOf
    """
    context: LdContext = Field(..., alias="@context")
    __properties = ["@context"]

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
    def from_json(cls, json_str: str) -> RetrieveAttributes200Response1OneOf:
        """Create an instance of RetrieveAttributes200Response1OneOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RetrieveAttributes200Response1OneOf:
        """Create an instance of RetrieveAttributes200Response1OneOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RetrieveAttributes200Response1OneOf.parse_obj(obj)

        _obj = RetrieveAttributes200Response1OneOf.parse_obj({
            "context": LdContext.from_dict(obj.get("@context")) if obj.get("@context") is not None else None
        })
        return _obj

