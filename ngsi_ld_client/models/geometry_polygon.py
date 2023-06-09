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
from ngsi_ld_client.models.geometry_linear_ring import GeometryLinearRing

class GeometryPolygon(BaseModel):
    """
    GeometryPolygon
    """
    type: Optional[StrictStr] = None
    coordinates: Optional[conlist(GeometryLinearRing)] = Field(None, description="An array of linear rings. ")
    additional_properties: Dict[str, Any] = {}
    __properties = ["type", "coordinates"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Polygon'):
            raise ValueError("must be one of enum values ('Polygon')")
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
    def from_json(cls, json_str: str) -> GeometryPolygon:
        """Create an instance of GeometryPolygon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in coordinates (list)
        _items = []
        if self.coordinates:
            for _item in self.coordinates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['coordinates'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GeometryPolygon:
        """Create an instance of GeometryPolygon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GeometryPolygon.parse_obj(obj)

        _obj = GeometryPolygon.parse_obj({
            "type": obj.get("type"),
            "coordinates": [GeometryLinearRing.from_dict(_item) for _item in obj.get("coordinates")] if obj.get("coordinates") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

