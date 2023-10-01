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
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from ngsi_ld_client.models.notification_data import NotificationData
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Notification(BaseModel):
    """
    5.3.1 This datatype represents the parameters that allow building a notification to be sent to a subscriber.   # noqa: E501
    """
    id: StrictStr = Field(description="Notification identifier (JSON-LD @id). It shall be automatically generated by the implementation. ")
    type: StrictStr = Field(description="JSON-LD @type. ")
    subscription_id: StrictStr = Field(description="Identifier of the subscription that originated the notification. ", alias="subscriptionId")
    notified_at: datetime = Field(description="Timestamp corresponding to the instant when the notification was generated by the system. ", alias="notifiedAt")
    data: NotificationData
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "subscriptionId", "notifiedAt", "data"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Notification'):
            raise ValueError("must be one of enum values ('Notification')")
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
        """Create an instance of Notification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of Notification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "subscriptionId": obj.get("subscriptionId"),
            "notifiedAt": obj.get("notifiedAt"),
            "data": NotificationData.from_dict(obj.get("data")) if obj.get("data") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


