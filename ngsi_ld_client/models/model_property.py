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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from ngsi_ld_client.models.property_previous_value import PropertyPreviousValue
from ngsi_ld_client.models.property_value import PropertyValue
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ModelProperty(BaseModel):
    """
    5.2.5 NGSI-LD Property.   # noqa: E501
    """
    type: Optional[StrictStr] = Field(default='Property', description="Node type. ")
    value: Optional[PropertyValue] = None
    observed_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time. ", alias="observedAt")
    unit_code: Optional[StrictStr] = Field(default=None, description="Property Value's unit code. ", alias="unitCode")
    dataset_id: Optional[StrictStr] = Field(default=None, description="It allows identifying a set or group of property values. ", alias="datasetId")
    created_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    instance_id: Optional[StrictStr] = Field(default=None, description="A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated. ", alias="instanceId")
    previous_value: Optional[PropertyPreviousValue] = Field(default=None, alias="previousValue")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "value", "observedAt", "unitCode", "datasetId", "createdAt", "modifiedAt", "deletedAt", "instanceId", "previousValue"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Property', 'Relationship', 'GeoProperty', 'LanguageProperty'):
            raise ValueError("must be one of enum values ('Property', 'Relationship', 'GeoProperty', 'LanguageProperty')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ModelProperty from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                            "created_at",
                            "modified_at",
                            "deleted_at",
                            "instance_id",
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of previous_value
        if self.previous_value:
            _dict['previousValue'] = self.previous_value.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of ModelProperty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'Property',
            "value": PropertyValue.from_dict(obj.get("value")) if obj.get("value") is not None else None,
            "observedAt": obj.get("observedAt"),
            "unitCode": obj.get("unitCode"),
            "datasetId": obj.get("datasetId"),
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "instanceId": obj.get("instanceId"),
            "previousValue": PropertyPreviousValue.from_dict(obj.get("previousValue")) if obj.get("previousValue") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


