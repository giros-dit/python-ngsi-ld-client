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
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictStr, confloat, conint, conlist, validator
from ngsi_ld_client.models.endpoint import Endpoint

class NotificationParams(BaseModel):
    """
    5.2.14 represents the parameters that allow to convey the details of a notification. 
    """
    attributes: Optional[conlist(StrictStr, min_items=1)] = Field(None, description="Entity Attribute Names (Properties or Relationships) to be included in the notification payload body. If undefined it will mean all Attributes. ")
    sys_attrs: Optional[StrictBool] = Field(False, alias="sysAttrs", description="If true, the system generated attributes createdAt and modifiedAt are included in the response payload body, in the case of a deletion also deletedAt. ")
    format: Optional[StrictStr] = Field(None, description="Conveys the representation format of the entities delivered at notification time. By default, it will be in the normalized format. ")
    show_changes: Optional[StrictBool] = Field(False, alias="showChanges", description="If true the previous value (previousValue) of Properties or languageMap (previousLanguageMap) of Language Properties or object (previousObject) of Relationships is provided in addition to the current one. This requires that it exists, i.e. in case of modifications and deletions,  but not in the case of creations. showChanges cannot be true in case format is \"keyValues\". ")
    endpoint: Endpoint = Field(...)
    status: Optional[StrictStr] = Field(None, description="Status of the Notification. It shall be \"ok\" if the last attempt to notify the subscriber succeeded. It shall be \"failed\" if the last attempt to notify the subscriber failed. ")
    times_sent: Optional[Union[confloat(ge=0, strict=True), conint(ge=0, strict=True)]] = Field(None, alias="timesSent", description="Number of times that the notification has been sent. Provided by the system when querying the details of a subscription. ")
    times_failed: Optional[Union[confloat(ge=0, strict=True), conint(ge=0, strict=True)]] = Field(None, alias="timesFailed", description="Number of times an unsuccessful response (or timeout) has been received when deliverying the notification. Provided by the system when querying the details of a subscription. ")
    last_notification: Optional[datetime] = Field(None, alias="lastNotification", description="Timestamp corresponding to the instant when the last notification has been sent. Provided by the system when querying the details of a subscription. ")
    last_failure: Optional[datetime] = Field(None, alias="lastFailure", description="Timestamp corresponding to the instant when the last notification resulting in failure (for instance, in the HTTP binding, an HTTP response code different than 200) has been sent. Provided by the system when querying the details of a subscription. ")
    last_success: Optional[datetime] = Field(None, alias="lastSuccess", description="Timestamp corresponding to the instant when the last successful (200 OK response) notification has been sent. Provided by the system when querying the details of a subscription. ")
    __properties = ["attributes", "sysAttrs", "format", "showChanges", "endpoint", "status", "timesSent", "timesFailed", "lastNotification", "lastFailure", "lastSuccess"]

    @validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('normalized', 'concise', 'keyValues'):
            raise ValueError("must be one of enum values ('normalized', 'concise', 'keyValues')")
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
    def from_json(cls, json_str: str) -> NotificationParams:
        """Create an instance of NotificationParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of endpoint
        if self.endpoint:
            _dict['endpoint'] = self.endpoint.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NotificationParams:
        """Create an instance of NotificationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NotificationParams.parse_obj(obj)

        _obj = NotificationParams.parse_obj({
            "attributes": obj.get("attributes"),
            "sys_attrs": obj.get("sysAttrs") if obj.get("sysAttrs") is not None else False,
            "format": obj.get("format"),
            "show_changes": obj.get("showChanges") if obj.get("showChanges") is not None else False,
            "endpoint": Endpoint.from_dict(obj.get("endpoint")) if obj.get("endpoint") is not None else None,
            "status": obj.get("status"),
            "times_sent": obj.get("timesSent"),
            "times_failed": obj.get("timesFailed"),
            "last_notification": obj.get("lastNotification"),
            "last_failure": obj.get("lastFailure"),
            "last_success": obj.get("lastSuccess")
        })
        return _obj

