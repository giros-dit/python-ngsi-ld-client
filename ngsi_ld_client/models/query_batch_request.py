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
from ngsi_ld_client.models.entity_selector import EntitySelector
from ngsi_ld_client.models.geo_query import GeoQuery
from ngsi_ld_client.models.ld_context import LdContext
from ngsi_ld_client.models.temporal_query import TemporalQuery

class QueryBatchRequest(BaseModel):
    """
    QueryBatchRequest
    """
    type: StrictStr = Field(..., description="JSON-LD @type. ")
    entities: Optional[conlist(EntitySelector, min_items=1)] = Field(None, description="Entity ids, id pattern and Entity types that shall be matched by Entities in order to be retrieved. ")
    attrs: Optional[conlist(StrictStr, min_items=1)] = Field(None, description="List of Attributes that shall be matched by Entities in order to be retrieved. If not present all Attributes will be retrieved. ")
    q: Optional[StrictStr] = Field(None, description="Query that shall be matched by Entities in order to be retrieved. ")
    geo_q: Optional[GeoQuery] = Field(None, alias="geoQ")
    csf: Optional[StrictStr] = Field(None, description="Context source filter that shall be matched by Context Source Registrations describing Context Sources to be used for retrieving Entities. ")
    temporal_q: Optional[TemporalQuery] = Field(None, alias="temporalQ")
    scope_q: Optional[StrictStr] = Field(None, alias="scopeQ", description="Scope query.")
    lang: Optional[StrictStr] = Field(None, description="Language filter to be applied to the query (clause 4.15).")
    context: LdContext = Field(..., alias="@context")
    __properties = ["type", "entities", "attrs", "q", "geoQ", "csf", "temporalQ", "scopeQ", "lang", "@context"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Query'):
            raise ValueError("must be one of enum values ('Query')")
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
    def from_json(cls, json_str: str) -> QueryBatchRequest:
        """Create an instance of QueryBatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item in self.entities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of geo_q
        if self.geo_q:
            _dict['geoQ'] = self.geo_q.to_dict()
        # override the default output from pydantic by calling `to_dict()` of temporal_q
        if self.temporal_q:
            _dict['temporalQ'] = self.temporal_q.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QueryBatchRequest:
        """Create an instance of QueryBatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QueryBatchRequest.parse_obj(obj)

        _obj = QueryBatchRequest.parse_obj({
            "type": obj.get("type"),
            "entities": [EntitySelector.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None,
            "attrs": obj.get("attrs"),
            "q": obj.get("q"),
            "geo_q": GeoQuery.from_dict(obj.get("geoQ")) if obj.get("geoQ") is not None else None,
            "csf": obj.get("csf"),
            "temporal_q": TemporalQuery.from_dict(obj.get("temporalQ")) if obj.get("temporalQ") is not None else None,
            "scope_q": obj.get("scopeQ"),
            "lang": obj.get("lang"),
            "context": LdContext.from_dict(obj.get("@context")) if obj.get("@context") is not None else None
        })
        return _obj
