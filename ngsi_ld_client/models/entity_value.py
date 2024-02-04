# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from ngsi_ld_client.models.model_property import ModelProperty
from ngsi_ld_client.models.relationship import Relationship
from pydantic import StrictStr, Field
from typing import Union, List, Optional, Dict
from typing_extensions import Literal, Self

ENTITYVALUE_ONE_OF_SCHEMAS = ["List[ModelProperty]", "List[Relationship]", "ModelProperty", "Relationship"]

class EntityValue(BaseModel):
    """
    EntityValue
    """
    # data type: ModelProperty
    oneof_schema_1_validator: Optional[ModelProperty] = None
    # data type: List[ModelProperty]
    oneof_schema_2_validator: Optional[List[ModelProperty]] = None
    # data type: Relationship
    oneof_schema_3_validator: Optional[Relationship] = None
    # data type: List[Relationship]
    oneof_schema_4_validator: Optional[List[Relationship]] = None
    actual_instance: Optional[Union[List[ModelProperty], List[Relationship], ModelProperty, Relationship]] = None
    one_of_schemas: List[str] = Field(default=Literal["List[ModelProperty]", "List[Relationship]", "ModelProperty", "Relationship"])

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = EntityValue.model_construct()
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
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in EntityValue with oneOf schemas: List[ModelProperty], List[Relationship], ModelProperty, Relationship. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in EntityValue with oneOf schemas: List[ModelProperty], List[Relationship], ModelProperty, Relationship. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
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

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into EntityValue with oneOf schemas: List[ModelProperty], List[Relationship], ModelProperty, Relationship. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into EntityValue with oneOf schemas: List[ModelProperty], List[Relationship], ModelProperty, Relationship. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], List[ModelProperty], List[Relationship], ModelProperty, Relationship]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


