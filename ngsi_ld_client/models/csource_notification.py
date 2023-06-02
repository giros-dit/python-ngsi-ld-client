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
from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from ngsi_ld_client.models.csource_registration_input import CsourceRegistrationInput

class CsourceNotification(BaseModel):
    """
    5.3.2 This datatype represents the parameters that allow building a Context Source Notification to be sent to a subscriber. 
    """
    id: StrictStr = Field(..., description="Csource notification identifier (JSON-LD @id). ")
    type: StrictStr = Field(..., description="JSON-LD @type. ")
    subscription_id: StrictStr = Field(..., alias="subscriptionId", description="Identifier of the subscription that originated the notification. ")
    notified_at: datetime = Field(..., alias="notifiedAt", description="Timestamp corresponding to the instant when the notification was generated by the system. ")
    data: conlist(CsourceRegistrationInput) = Field(..., description="The content of the notification as NGSI-LD entities. See clause 5.2.4. ")
    trigger_reason: StrictStr = Field(..., alias="triggerReason", description="Indicates whether the Csources in the CsourceRegistration.Input(s) in data are newly matching (initial notification or creation), have been updated (but still match) or do not match any longer.  • \"newlyMatching\" - describes the case that the notified Context Source Registration(s) newly match(es) the identified subscription. This value is used in the first notification and whenever a new Context Source Registration matching the Subscription has been registered, or an existing Context Source Registration that did not match before has been updated in such a way that it matches now.  • \"updated\" - describes the case that the notified Context Source Registration that was part of a previous notification has been updated, but still matches the Subscription.  • \"noLongerMatching\" - describes the case that the notified Context Source Registration that was part of a previous notification no longer matches the Subscription, i.e. as a result of  an update or because it was deleted. ")
    __properties = ["id", "type", "subscriptionId", "notifiedAt", "data", "triggerReason"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CsourceNotification'):
            raise ValueError("must be one of enum values ('CsourceNotification')")
        return value

    @validator('trigger_reason')
    def trigger_reason_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('newlyMatching', 'updated', 'noLongerMatching'):
            raise ValueError("must be one of enum values ('newlyMatching', 'updated', 'noLongerMatching')")
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
    def from_json(cls, json_str: str) -> CsourceNotification:
        """Create an instance of CsourceNotification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CsourceNotification:
        """Create an instance of CsourceNotification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CsourceNotification.parse_obj(obj)

        _obj = CsourceNotification.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "subscription_id": obj.get("subscriptionId"),
            "notified_at": obj.get("notifiedAt"),
            "data": [CsourceRegistrationInput.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "trigger_reason": obj.get("triggerReason")
        })
        return _obj

