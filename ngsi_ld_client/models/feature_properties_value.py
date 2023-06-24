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
from pydantic import BaseModel, Field, StrictStr, ValidationError, conlist, validator
from ngsi_ld_client.models.geo_property import GeoProperty
from ngsi_ld_client.models.language_property import LanguageProperty
from ngsi_ld_client.models.model_property import ModelProperty
from ngsi_ld_client.models.relationship import Relationship
from typing import Any, List
from pydantic import StrictStr, Field

FEATUREPROPERTIESVALUE_ONE_OF_SCHEMAS = ["GeoProperty", "LanguageProperty", "List[GeoProperty]", "List[LanguageProperty]", "List[ModelProperty]", "List[Relationship]", "ModelProperty", "Relationship"]

class FeaturePropertiesValue(BaseModel):
    """
    FeaturePropertiesValue
    """
    # data type: ModelProperty
    oneof_schema_1_validator: Optional[ModelProperty] = None
    # data type: List[ModelProperty]
    oneof_schema_2_validator: Optional[conlist(ModelProperty)] = None
    # data type: Relationship
    oneof_schema_3_validator: Optional[Relationship] = None
    # data type: List[Relationship]
    oneof_schema_4_validator: Optional[conlist(Relationship)] = None
    # data type: GeoProperty
    oneof_schema_5_validator: Optional[GeoProperty] = None
    # data type: List[GeoProperty]
    oneof_schema_6_validator: Optional[conlist(GeoProperty)] = None
    # data type: LanguageProperty
    oneof_schema_7_validator: Optional[LanguageProperty] = None
    # data type: List[LanguageProperty]
    oneof_schema_8_validator: Optional[conlist(LanguageProperty)] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(FEATUREPROPERTIESVALUE_ONE_OF_SCHEMAS, const=True)

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
        instance = FeaturePropertiesValue.construct()
        error_messages = []
        match = 0
        # validate data type: ModelProperty
        if not isinstance(v, ModelProperty):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ModelProperty`")
        else:
            match += 1
        # validate data type: List[ModelProperty]
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: Relationship
        if not isinstance(v, Relationship):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Relationship`")
        else:
            match += 1
        # validate data type: List[Relationship]
        try:
            instance.oneof_schema_4_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: GeoProperty
        if not isinstance(v, GeoProperty):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GeoProperty`")
        else:
            match += 1
        # validate data type: List[GeoProperty]
        try:
            instance.oneof_schema_6_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: LanguageProperty
        if not isinstance(v, LanguageProperty):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LanguageProperty`")
        else:
            match += 1
        # validate data type: List[LanguageProperty]
        try:
            instance.oneof_schema_8_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in FeaturePropertiesValue with oneOf schemas: GeoProperty, LanguageProperty, List[GeoProperty], List[LanguageProperty], List[ModelProperty], List[Relationship], ModelProperty, Relationship. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in FeaturePropertiesValue with oneOf schemas: GeoProperty, LanguageProperty, List[GeoProperty], List[LanguageProperty], List[ModelProperty], List[Relationship], ModelProperty, Relationship. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> FeaturePropertiesValue:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> FeaturePropertiesValue:
        """Returns the object represented by the json string"""
        instance = FeaturePropertiesValue.construct()
        error_messages = []
        match = 0

        # deserialize data into ModelProperty
        try:
            instance.actual_instance = ModelProperty.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[ModelProperty]
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Relationship
        try:
            instance.actual_instance = Relationship.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[Relationship]
        try:
            # validation
            instance.oneof_schema_4_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_4_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GeoProperty
        try:
            instance.actual_instance = GeoProperty.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[GeoProperty]
        try:
            # validation
            instance.oneof_schema_6_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_6_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LanguageProperty
        try:
            instance.actual_instance = LanguageProperty.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[LanguageProperty]
        try:
            # validation
            instance.oneof_schema_8_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_8_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into FeaturePropertiesValue with oneOf schemas: GeoProperty, LanguageProperty, List[GeoProperty], List[LanguageProperty], List[ModelProperty], List[Relationship], ModelProperty, Relationship. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FeaturePropertiesValue with oneOf schemas: GeoProperty, LanguageProperty, List[GeoProperty], List[LanguageProperty], List[ModelProperty], List[Relationship], ModelProperty, Relationship. Details: " + ", ".join(error_messages))
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

