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
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictStr, confloat, conint, conlist, constr, validator
from ngsi_ld_client.models.csource_registration_scope import CsourceRegistrationScope
from ngsi_ld_client.models.geometry import Geometry
from ngsi_ld_client.models.key_value_pair import KeyValuePair
from ngsi_ld_client.models.registration_info import RegistrationInfo
from ngsi_ld_client.models.registration_management_info import RegistrationManagementInfo
from ngsi_ld_client.models.time_interval import TimeInterval

class CsourceRegistration(BaseModel):
    """
    5.2.9 represents the data needed to register a new Context Source. 
    """
    id: Optional[StrictStr] = Field(None, description="Unique registration identifier. (JSON-LD @id). There may be multiple registrations per Context Source, i.e. the id is unique per registration. ")
    type: Optional[StrictStr] = Field(None, description="JSON-LD @type Use reserved type for identifying Context Source Registration. ")
    registration_name: Optional[constr(strict=True, min_length=1)] = Field(None, alias="registrationName", description="A name given to this Context Source Registration. ")
    description: Optional[constr(strict=True, min_length=1)] = Field(None, description="A description of this Context Source Registration. ")
    information: Optional[conlist(RegistrationInfo, min_items=1)] = Field(None, description="Describes the Entities, Properties and Relationships for which the Context Source may be able to provide information. ")
    tenant: Optional[StrictStr] = Field(None, description="Identifies the tenant that has to be specified in all requests to the Context Source that are related to the information registered in this Context Source Registration. If not present, the default tenant is assumed. Should only be present in systems supporting multi-tenancy. ")
    observation_interval: Optional[TimeInterval] = Field(None, alias="observationInterval")
    management_interval: Optional[TimeInterval] = Field(None, alias="managementInterval")
    location: Optional[Geometry] = None
    observation_space: Optional[Geometry] = Field(None, alias="observationSpace")
    operation_space: Optional[Geometry] = Field(None, alias="operationSpace")
    expires_at: Optional[datetime] = Field(None, alias="expiresAt", description="Provides an expiration date. When passed the Context Source Registration will become invalid and the Context Source might no longer be available. ")
    endpoint: Optional[StrictStr] = Field(None, description="Endpoint expressed as dereferenceable URI through which the Context Source exposes its NGSI-LD interface. ")
    context_source_info: Optional[conlist(KeyValuePair)] = Field(None, alias="contextSourceInfo", description="Generic {key, value} array to convey optional information to provide when contacting the registered Context Source. ")
    scope: Optional[CsourceRegistrationScope] = None
    mode: Optional[StrictStr] = Field(None, description="The definition of the mode of distributed operation (see clause 4.3.6) supported by the registered Context Source. ")
    operations: Optional[conlist(StrictStr)] = Field(None, description="The definition limited subset of API operations supported by the registered Context Source.  If undefined, the default set of operations is \"federationOps\" (see clause 4.20). ")
    refresh_rate: Optional[StrictStr] = Field(None, alias="refreshRate", description="An indication of the likely period of time to elapse between updates at this registered endpoint. Brokers may optionally use this information to help implement caching. ")
    management: Optional[RegistrationManagementInfo] = None
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ")
    modified_at: Optional[datetime] = Field(None, alias="modifiedAt", description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ")
    deleted_at: Optional[datetime] = Field(None, alias="deletedAt", description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ")
    status: Optional[StrictStr] = Field(None, description="Read-only. Status of the Registration. It shall be \"ok\" if the last attempt to perform a distributed operation succeeded. It shall be \"failed\" if the last attempt to perform a distributed operation failed. ")
    times_sent: Optional[Union[confloat(ge=0, strict=True), conint(ge=0, strict=True)]] = Field(None, alias="timesSent", description="Number of times that the registration triggered a distributed operation, including failed attempts. ")
    times_failed: Optional[Union[confloat(ge=0, strict=True), conint(ge=0, strict=True)]] = Field(None, alias="timesFailed", description="Number of times that the registration triggered a distributed operation request that failed.")
    last_success: Optional[datetime] = Field(None, alias="lastSuccess", description="Timestamp corresponding to the instant when the last successfully distributed operation was sent. Created on first successful operation. ")
    last_failure: Optional[datetime] = Field(None, alias="lastFailure", description="Timestamp corresponding to the instant when the last distributed operation resulting in a failure (for instance, in the HTTP binding, an HTTP response code other than 2xx) was returned. ")
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "type", "registrationName", "description", "information", "tenant", "observationInterval", "managementInterval", "location", "observationSpace", "operationSpace", "expiresAt", "endpoint", "contextSourceInfo", "scope", "mode", "operations", "refreshRate", "management", "createdAt", "modifiedAt", "deletedAt", "status", "timesSent", "timesFailed", "lastSuccess", "lastFailure"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ContextSourceRegistration'):
            raise ValueError("must be one of enum values ('ContextSourceRegistration')")
        return value

    @validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('inclusive', 'exclusive', 'redirect', 'auxiliary'):
            raise ValueError("must be one of enum values ('inclusive', 'exclusive', 'redirect', 'auxiliary')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ok', 'failed'):
            raise ValueError("must be one of enum values ('ok', 'failed')")
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
    def from_json(cls, json_str: str) -> CsourceRegistration:
        """Create an instance of CsourceRegistration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_at",
                            "modified_at",
                            "deleted_at",
                            "status",
                            "times_sent",
                            "times_failed",
                            "last_success",
                            "last_failure",
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in information (list)
        _items = []
        if self.information:
            for _item in self.information:
                if _item:
                    _items.append(_item.to_dict())
            _dict['information'] = _items
        # override the default output from pydantic by calling `to_dict()` of observation_interval
        if self.observation_interval:
            _dict['observationInterval'] = self.observation_interval.to_dict()
        # override the default output from pydantic by calling `to_dict()` of management_interval
        if self.management_interval:
            _dict['managementInterval'] = self.management_interval.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of observation_space
        if self.observation_space:
            _dict['observationSpace'] = self.observation_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation_space
        if self.operation_space:
            _dict['operationSpace'] = self.operation_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in context_source_info (list)
        _items = []
        if self.context_source_info:
            for _item in self.context_source_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['contextSourceInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of scope
        if self.scope:
            _dict['scope'] = self.scope.to_dict()
        # override the default output from pydantic by calling `to_dict()` of management
        if self.management:
            _dict['management'] = self.management.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CsourceRegistration:
        """Create an instance of CsourceRegistration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CsourceRegistration.parse_obj(obj)

        _obj = CsourceRegistration.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "registration_name": obj.get("registrationName"),
            "description": obj.get("description"),
            "information": [RegistrationInfo.from_dict(_item) for _item in obj.get("information")] if obj.get("information") is not None else None,
            "tenant": obj.get("tenant"),
            "observation_interval": TimeInterval.from_dict(obj.get("observationInterval")) if obj.get("observationInterval") is not None else None,
            "management_interval": TimeInterval.from_dict(obj.get("managementInterval")) if obj.get("managementInterval") is not None else None,
            "location": Geometry.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "observation_space": Geometry.from_dict(obj.get("observationSpace")) if obj.get("observationSpace") is not None else None,
            "operation_space": Geometry.from_dict(obj.get("operationSpace")) if obj.get("operationSpace") is not None else None,
            "expires_at": obj.get("expiresAt"),
            "endpoint": obj.get("endpoint"),
            "context_source_info": [KeyValuePair.from_dict(_item) for _item in obj.get("contextSourceInfo")] if obj.get("contextSourceInfo") is not None else None,
            "scope": CsourceRegistrationScope.from_dict(obj.get("scope")) if obj.get("scope") is not None else None,
            "mode": obj.get("mode"),
            "operations": obj.get("operations"),
            "refresh_rate": obj.get("refreshRate"),
            "management": RegistrationManagementInfo.from_dict(obj.get("management")) if obj.get("management") is not None else None,
            "created_at": obj.get("createdAt"),
            "modified_at": obj.get("modifiedAt"),
            "deleted_at": obj.get("deletedAt"),
            "status": obj.get("status"),
            "times_sent": obj.get("timesSent"),
            "times_failed": obj.get("timesFailed"),
            "last_success": obj.get("lastSuccess"),
            "last_failure": obj.get("lastFailure")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


