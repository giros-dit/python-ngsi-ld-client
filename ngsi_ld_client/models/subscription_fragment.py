# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from ngsi_ld_client.models.subscription_fragment_on_change import SubscriptionFragmentOnChange
from ngsi_ld_client.models.subscription_fragment_periodic import SubscriptionFragmentPeriodic
from typing import Any, List
from pydantic import StrictStr, Field

SUBSCRIPTIONFRAGMENT_ONE_OF_SCHEMAS = ["SubscriptionFragmentOnChange", "SubscriptionFragmentPeriodic"]

class SubscriptionFragment(BaseModel):
    """
    SubscriptionFragment
    """
    # data type: SubscriptionFragmentPeriodic
    oneof_schema_1_validator: Optional[SubscriptionFragmentPeriodic] = None
    # data type: SubscriptionFragmentOnChange
    oneof_schema_2_validator: Optional[SubscriptionFragmentOnChange] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(SUBSCRIPTIONFRAGMENT_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = SubscriptionFragment.construct()
        error_messages = []
        match = 0
        # validate data type: SubscriptionFragmentPeriodic
        if not isinstance(v, SubscriptionFragmentPeriodic):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SubscriptionFragmentPeriodic`")
        else:
            match += 1
        # validate data type: SubscriptionFragmentOnChange
        if not isinstance(v, SubscriptionFragmentOnChange):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SubscriptionFragmentOnChange`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SubscriptionFragment with oneOf schemas: SubscriptionFragmentOnChange, SubscriptionFragmentPeriodic. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SubscriptionFragment with oneOf schemas: SubscriptionFragmentOnChange, SubscriptionFragmentPeriodic. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> SubscriptionFragment:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> SubscriptionFragment:
        """Returns the object represented by the json string"""
        instance = SubscriptionFragment.construct()
        error_messages = []
        match = 0

        # deserialize data into SubscriptionFragmentPeriodic
        try:
            instance.actual_instance = SubscriptionFragmentPeriodic.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SubscriptionFragmentOnChange
        try:
            instance.actual_instance = SubscriptionFragmentOnChange.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SubscriptionFragment with oneOf schemas: SubscriptionFragmentOnChange, SubscriptionFragmentPeriodic. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SubscriptionFragment with oneOf schemas: SubscriptionFragmentOnChange, SubscriptionFragmentPeriodic. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

