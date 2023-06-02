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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from ngsi_ld_client.models.feature import Feature
from ngsi_ld_client.models.ld_context import LdContext

class FeatureCollection(BaseModel):
    """
    5.2.30 This data type represents a list of spatially bounded Entities in GeoJSON format, as mandated by IETF RFC 7946. 
    """
    type: StrictStr = Field(..., description="GeoJSON Type. ")
    features: Optional[conlist(Feature)] = Field(None, description="In the case that no matches are found, \"features\" will be an empty array. ")
    context: Optional[LdContext] = Field(None, alias="@context")
    __properties = ["type", "features", "@context"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('FeatureCollection'):
            raise ValueError("must be one of enum values ('FeatureCollection')")
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
    def from_json(cls, json_str: str) -> FeatureCollection:
        """Create an instance of FeatureCollection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item in self.features:
                if _item:
                    _items.append(_item.to_dict())
            _dict['features'] = _items
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FeatureCollection:
        """Create an instance of FeatureCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FeatureCollection.parse_obj(obj)

        _obj = FeatureCollection.parse_obj({
            "type": obj.get("type"),
            "features": [Feature.from_dict(_item) for _item in obj.get("features")] if obj.get("features") is not None else None,
            "context": LdContext.from_dict(obj.get("@context")) if obj.get("@context") is not None else None
        })
        return _obj

