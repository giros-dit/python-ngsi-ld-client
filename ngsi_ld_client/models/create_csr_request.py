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
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from ngsi_ld_client.models.csource_registration_scope import CsourceRegistrationScope
from ngsi_ld_client.models.geometry import Geometry
from ngsi_ld_client.models.key_value_pair import KeyValuePair
from ngsi_ld_client.models.registration_info import RegistrationInfo
from ngsi_ld_client.models.registration_management_info import RegistrationManagementInfo
from ngsi_ld_client.models.time_interval import TimeInterval
from typing import Optional, Set
from typing_extensions import Self

class CreateCSRRequest(BaseModel):
    """
    CreateCSRRequest
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique registration identifier. (JSON-LD @id). There may be multiple registrations per Context Source, i.e. the id is unique per registration. ")
    type: StrictStr = Field(description="JSON-LD @type Use reserved type for identifying Context Source Registration. ")
    registration_name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="A name given to this Context Source Registration. ", alias="registrationName")
    description: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="A description of this Context Source Registration. ")
    information: Annotated[List[RegistrationInfo], Field(min_length=1)] = Field(description="Describes the Entities, Properties and Relationships for which the Context Source may be able to provide information. ")
    tenant: Optional[StrictStr] = Field(default=None, description="Identifies the tenant that has to be specified in all requests to the Context Source that are related to the information registered in this Context Source Registration. If not present, the default tenant is assumed. Should only be present in systems supporting multi-tenancy. ")
    observation_interval: Optional[TimeInterval] = Field(default=None, alias="observationInterval")
    management_interval: Optional[TimeInterval] = Field(default=None, alias="managementInterval")
    location: Optional[Geometry] = None
    observation_space: Optional[Geometry] = Field(default=None, alias="observationSpace")
    operation_space: Optional[Geometry] = Field(default=None, alias="operationSpace")
    expires_at: Optional[datetime] = Field(default=None, description="Provides an expiration date. When passed the Context Source Registration will become invalid and the Context Source might no longer be available. ", alias="expiresAt")
    endpoint: Optional[StrictStr] = Field(default=None, description="Endpoint expressed as dereferenceable URI through which the Context Source exposes its NGSI-LD interface. ")
    context_source_info: Optional[List[KeyValuePair]] = Field(default=None, description="Generic {key, value} array to convey optional information to provide when contacting the registered Context Source. ", alias="contextSourceInfo")
    scope: Optional[CsourceRegistrationScope] = None
    mode: Optional[StrictStr] = Field(default=None, description="The definition of the mode of distributed operation (see clause 4.3.6) supported by the registered Context Source. ")
    operations: Optional[List[StrictStr]] = Field(default=None, description="The definition limited subset of API operations supported by the registered Context Source.  If undefined, the default set of operations is \"federationOps\" (see clause 4.20). ")
    refresh_rate: Optional[StrictStr] = Field(default=None, description="An indication of the likely period of time to elapse between updates at this registered endpoint. Brokers may optionally use this information to help implement caching. ", alias="refreshRate")
    management: Optional[RegistrationManagementInfo] = None
    created_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    status: Optional[StrictStr] = Field(default=None, description="Read-only. Status of the Registration. It shall be \"ok\" if the last attempt to perform a distributed operation succeeded. It shall be \"failed\" if the last attempt to perform a distributed operation failed. ")
    times_sent: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Number of times that the registration triggered a distributed operation, including failed attempts. ", alias="timesSent")
    times_failed: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Number of times that the registration triggered a distributed operation request that failed.", alias="timesFailed")
    last_success: Optional[datetime] = Field(default=None, description="Timestamp corresponding to the instant when the last successfully distributed operation was sent. Created on first successful operation. ", alias="lastSuccess")
    last_failure: Optional[datetime] = Field(default=None, description="Timestamp corresponding to the instant when the last distributed operation resulting in a failure (for instance, in the HTTP binding, an HTTP response code other than 2xx) was returned. ", alias="lastFailure")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "registrationName", "description", "information", "tenant", "observationInterval", "managementInterval", "location", "observationSpace", "operationSpace", "expiresAt", "endpoint", "contextSourceInfo", "scope", "mode", "operations", "refreshRate", "management", "createdAt", "modifiedAt", "deletedAt", "status", "timesSent", "timesFailed", "lastSuccess", "lastFailure"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ContextSourceRegistration'):
            raise ValueError("must be one of enum values ('ContextSourceRegistration')")
        return value

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('inclusive', 'exclusive', 'redirect', 'auxiliary'):
            raise ValueError("must be one of enum values ('inclusive', 'exclusive', 'redirect', 'auxiliary')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ok', 'failed'):
            raise ValueError("must be one of enum values ('ok', 'failed')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateCSRRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "modified_at",
            "deleted_at",
            "status",
            "times_sent",
            "times_failed",
            "last_success",
            "last_failure",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateCSRRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "registrationName": obj.get("registrationName"),
            "description": obj.get("description"),
            "information": [RegistrationInfo.from_dict(_item) for _item in obj["information"]] if obj.get("information") is not None else None,
            "tenant": obj.get("tenant"),
            "observationInterval": TimeInterval.from_dict(obj["observationInterval"]) if obj.get("observationInterval") is not None else None,
            "managementInterval": TimeInterval.from_dict(obj["managementInterval"]) if obj.get("managementInterval") is not None else None,
            "location": Geometry.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "observationSpace": Geometry.from_dict(obj["observationSpace"]) if obj.get("observationSpace") is not None else None,
            "operationSpace": Geometry.from_dict(obj["operationSpace"]) if obj.get("operationSpace") is not None else None,
            "expiresAt": obj.get("expiresAt"),
            "endpoint": obj.get("endpoint"),
            "contextSourceInfo": [KeyValuePair.from_dict(_item) for _item in obj["contextSourceInfo"]] if obj.get("contextSourceInfo") is not None else None,
            "scope": CsourceRegistrationScope.from_dict(obj["scope"]) if obj.get("scope") is not None else None,
            "mode": obj.get("mode"),
            "operations": obj.get("operations"),
            "refreshRate": obj.get("refreshRate"),
            "management": RegistrationManagementInfo.from_dict(obj["management"]) if obj.get("management") is not None else None,
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "status": obj.get("status"),
            "timesSent": obj.get("timesSent"),
            "timesFailed": obj.get("timesFailed"),
            "lastSuccess": obj.get("lastSuccess"),
            "lastFailure": obj.get("lastFailure")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


