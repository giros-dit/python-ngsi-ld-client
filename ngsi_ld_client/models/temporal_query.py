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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class TemporalQuery(BaseModel):
    """
    5.2.21 This datatype represents a temporal query. 
    """
    timerel: StrictStr = Field(..., description="Allowed values: \"before\", \"after\" and \"between\". ")
    time_at: datetime = Field(..., alias="timeAt", description="It shall be a DateTime. ")
    end_time_at: Optional[datetime] = Field(None, alias="endTimeAt", description="It shall be a DateTime. Cardinality shall be 1 if timerel is equal to \"between\". ")
    timeproperty: Optional[StrictStr] = Field('observedAt', description="Allowed values: \"observedAt\", \"createdAt\", \"modifiedAt\" and \"deletedAt\". If not specified, the default is \"observedAt\". (See clause 4.8). ")
    __properties = ["timerel", "timeAt", "endTimeAt", "timeproperty"]

    @validator('timerel')
    def timerel_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('before', 'after', 'between'):
            raise ValueError("must be one of enum values ('before', 'after', 'between')")
        return value

    @validator('timeproperty')
    def timeproperty_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('observedAt', 'createdAt', 'modifiedAt', 'deletedAt'):
            raise ValueError("must be one of enum values ('observedAt', 'createdAt', 'modifiedAt', 'deletedAt')")
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
    def from_json(cls, json_str: str) -> TemporalQuery:
        """Create an instance of TemporalQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TemporalQuery:
        """Create an instance of TemporalQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TemporalQuery.parse_obj(obj)

        _obj = TemporalQuery.parse_obj({
            "timerel": obj.get("timerel"),
            "time_at": obj.get("timeAt"),
            "end_time_at": obj.get("endTimeAt"),
            "timeproperty": obj.get("timeproperty") if obj.get("timeproperty") is not None else 'observedAt'
        })
        return _obj
