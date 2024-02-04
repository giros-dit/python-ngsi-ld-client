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
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from ngsi_ld_client.models.entity_selector import EntitySelector
from ngsi_ld_client.models.geo_query import GeoQuery
from ngsi_ld_client.models.ld_context import LdContext
from ngsi_ld_client.models.notification_params import NotificationParams
from ngsi_ld_client.models.temporal_query import TemporalQuery
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateSubscriptionRequest1(BaseModel):
    """
    CreateSubscriptionRequest1
    """
    id: Optional[StrictStr] = Field(default=None, description="Subscription identifier (JSON-LD @id). ")
    type: StrictStr = Field(description="JSON-LD @type. ")
    subscription_name: Optional[StrictStr] = Field(default=None, description="A (short) name given to this Subscription. ", alias="subscriptionName")
    description: Optional[StrictStr] = Field(default=None, description="Subscription description. ")
    entities: Annotated[List[EntitySelector], Field(min_length=1)] = Field(description="Entities subscribed. ")
    notification_trigger: Optional[List[StrictStr]] = Field(default=None, description="The notification triggers listed indicate what kind of changes shall trigger a notification. If not present, the default is the combination attributeCreated and attributeUpdated. entityUpdated is equivalent to the combination attributeCreated, attributeUpdated and attributeDeleted. ", alias="notificationTrigger")
    q: Optional[StrictStr] = Field(default=None, description="Query that shall be met by subscribed entities in order to trigger the notification. ")
    geo_q: Optional[GeoQuery] = Field(default=None, alias="geoQ")
    csf: Optional[StrictStr] = Field(default=None, description="Context source filter that shall be met by Context Source Registrations describing Context Sources to be used for Entity Subscriptions. ")
    is_active: Optional[StrictBool] = Field(default=None, description="Allows clients to temporarily pause the subscription by making it inactive. true indicates that the Subscription is under operation. false indicates that the subscription is paused and notifications shall not be delivered. ", alias="isActive")
    notification: Optional[NotificationParams] = None
    expires_at: Optional[datetime] = Field(default=None, description="Expiration date for the subscription. ", alias="expiresAt")
    temporal_q: Optional[TemporalQuery] = Field(default=None, alias="temporalQ")
    scope_q: Optional[StrictStr] = Field(default=None, description="Scope query. ", alias="scopeQ")
    lang: Optional[StrictStr] = Field(default=None, description="Language filter to be applied to the query (clause 4.15). ")
    created_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    status: Optional[StrictStr] = Field(default=None, description="Read-only. Provided by the system when querying the details of a subscription. ")
    watched_attributes: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Watched Attributes (Properties or Relationships). If not defined it means any Attribute. ", alias="watchedAttributes")
    throttling: Optional[Union[Annotated[float, Field(strict=True, ge=1)], Annotated[int, Field(strict=True, ge=1)]]] = Field(default=None, description="Minimal period of time in seconds which shall elapse between two consecutive notifications. ")
    time_interval: Optional[Union[Annotated[float, Field(strict=True, ge=1)], Annotated[int, Field(strict=True, ge=1)]]] = Field(default=None, description="Indicates that a notification shall be delivered periodically regardless of attribute changes. Actually, when the time interval (in seconds) specified in this value field is reached. ", alias="timeInterval")
    context: LdContext = Field(alias="@context")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "subscriptionName", "description", "entities", "notificationTrigger", "q", "geoQ", "csf", "isActive", "notification", "expiresAt", "temporalQ", "scopeQ", "lang", "createdAt", "modifiedAt", "deletedAt", "status", "watchedAttributes", "throttling", "timeInterval", "@context"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Subscription'):
            raise ValueError("must be one of enum values ('Subscription')")
        return value

    @field_validator('notification_trigger')
    def notification_trigger_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('entityCreated', 'entityUpdated', 'entityDeleted', 'attributeCreated', 'attributeUpdated', 'attributeDeleted'):
                raise ValueError("each list item must be one of ('entityCreated', 'entityUpdated', 'entityDeleted', 'attributeCreated', 'attributeUpdated', 'attributeDeleted')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('active', 'paused', 'expired'):
            raise ValueError("must be one of enum values ('active', 'paused', 'expired')")
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
        """Create an instance of CreateSubscriptionRequest1 from a JSON string"""
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
        * Fields in `self.additional_properties` are added to the output dict.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "created_at",
                "modified_at",
                "deleted_at",
                "status",
                "additional_properties",
            },
            exclude_none=True,
        )
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
        # override the default output from pydantic by calling `to_dict()` of notification
        if self.notification:
            _dict['notification'] = self.notification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of temporal_q
        if self.temporal_q:
            _dict['temporalQ'] = self.temporal_q.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of CreateSubscriptionRequest1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "subscriptionName": obj.get("subscriptionName"),
            "description": obj.get("description"),
            "entities": [EntitySelector.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None,
            "notificationTrigger": obj.get("notificationTrigger"),
            "q": obj.get("q"),
            "geoQ": GeoQuery.from_dict(obj.get("geoQ")) if obj.get("geoQ") is not None else None,
            "csf": obj.get("csf"),
            "isActive": obj.get("isActive"),
            "notification": NotificationParams.from_dict(obj.get("notification")) if obj.get("notification") is not None else None,
            "expiresAt": obj.get("expiresAt"),
            "temporalQ": TemporalQuery.from_dict(obj.get("temporalQ")) if obj.get("temporalQ") is not None else None,
            "scopeQ": obj.get("scopeQ"),
            "lang": obj.get("lang"),
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "status": obj.get("status"),
            "watchedAttributes": obj.get("watchedAttributes"),
            "throttling": obj.get("throttling"),
            "timeInterval": obj.get("timeInterval"),
            "@context": LdContext.from_dict(obj.get("@context")) if obj.get("@context") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


