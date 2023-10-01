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
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class Relationship(BaseModel):
    """
    5.2.6 NGSI-LD Relationship. 
    """
    type: Optional[StrictStr] = Field('Relationship', description="Node type. ")
    object: Optional[StrictStr] = Field(None, description="Relationship's target object. ")
    observed_at: Optional[datetime] = Field(None, alias="observedAt", description="Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time. ")
    dataset_id: Optional[StrictStr] = Field(None, alias="datasetId", description="It allows identifying a set or group of target relationship objects. ")
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ")
    modified_at: Optional[datetime] = Field(None, alias="modifiedAt", description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ")
    deleted_at: Optional[datetime] = Field(None, alias="deletedAt", description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ")
    instance_id: Optional[StrictStr] = Field(None, alias="instanceId", description="A URI uniquely identifying a Relationship instance (see clause 4.5.8). System generated. ")
    previous_object: Optional[StrictStr] = Field(None, alias="previousObject", description="Previous Relationship's target object. Only used in notifications. ")
    additional_properties: Optional[EntityAdditionalProperties] = Field(None, alias="additionalProperties")
    __properties = ["type", "object", "observedAt", "datasetId", "createdAt", "modifiedAt", "deletedAt", "instanceId", "previousObject", "additionalProperties"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Relationship'):
            raise ValueError("must be one of enum values ('Relationship')")
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
    def from_json(cls, json_str: str) -> Relationship:
        """Create an instance of Relationship from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_at",
                            "modified_at",
                            "deleted_at",
                            "instance_id",
                            "previous_object",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of additional_properties
        if self.additional_properties:
            _dict['additionalProperties'] = self.additional_properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Relationship:
        """Create an instance of Relationship from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Relationship.parse_obj(obj)

        _obj = Relationship.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'Relationship',
            "object": obj.get("object"),
            "observed_at": obj.get("observedAt"),
            "dataset_id": obj.get("datasetId"),
            "created_at": obj.get("createdAt"),
            "modified_at": obj.get("modifiedAt"),
            "deleted_at": obj.get("deletedAt"),
            "instance_id": obj.get("instanceId"),
            "previous_object": obj.get("previousObject"),
            "additional_properties": EntityAdditionalProperties.from_dict(obj.get("additionalProperties")) if obj.get("additionalProperties") is not None else None
        })
        return _obj

from ngsi_ld_client.models.entity_additional_properties import EntityAdditionalProperties
Relationship.update_forward_refs()

