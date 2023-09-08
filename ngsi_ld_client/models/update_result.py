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


from typing import Any, Dict, List
from pydantic import BaseModel, Field, StrictStr, conlist
from ngsi_ld_client.models.not_updated_details import NotUpdatedDetails

class UpdateResult(BaseModel):
    """
    5.2.18 represents the result of Attribute update (append or update) operations in the NGSI-LD API regardless of whether local or distributed. 
    """
    updated: conlist(StrictStr) = Field(..., description="List of Attributes (represented by their Name) that were appended or updated. ")
    not_updated: conlist(NotUpdatedDetails) = Field(..., alias="notUpdated", description="List which contains the Attributes (represented by their Name) that were not updated, together with the reason for not being updated. ")
    additional_properties: Dict[str, Any] = {}
    __properties = ["updated", "notUpdated"]

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
    def from_json(cls, json_str: str) -> UpdateResult:
        """Create an instance of UpdateResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in not_updated (list)
        _items = []
        if self.not_updated:
            for _item in self.not_updated:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notUpdated'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateResult:
        """Create an instance of UpdateResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateResult.parse_obj(obj)

        _obj = UpdateResult.parse_obj({
            "updated": obj.get("updated"),
            "not_updated": [NotUpdatedDetails.from_dict(_item) for _item in obj.get("notUpdated")] if obj.get("notUpdated") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


