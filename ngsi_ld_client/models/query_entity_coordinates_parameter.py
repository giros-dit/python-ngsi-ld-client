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

from typing import Any, List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, ValidationError, conlist, validator
from ngsi_ld_client.models.geometry_line_string import GeometryLineString
from ngsi_ld_client.models.geometry_linear_ring import GeometryLinearRing
from typing import Any, List
from pydantic import StrictStr, Field

QUERYENTITYCOORDINATESPARAMETER_ONE_OF_SCHEMAS = ["GeometryLineString", "List[GeometryLinearRing]", "List[List]", "List[float]"]

class QueryEntityCoordinatesParameter(BaseModel):
    """
    QueryEntityCoordinatesParameter
    """
    # data type: List[float]
    oneof_schema_1_validator: Optional[conlist(Union[StrictFloat, StrictInt], max_items=2, min_items=2)] = Field(None, description="A single position. ")
    # data type: List[List]
    oneof_schema_2_validator: Optional[conlist(conlist(Union[StrictFloat, StrictInt], max_items=2, min_items=2))] = Field(None, description="An array of positions. ")
    # data type: GeometryLineString
    oneof_schema_3_validator: Optional[GeometryLineString] = None
    # data type: List[GeometryLinearRing]
    oneof_schema_4_validator: Optional[conlist(GeometryLinearRing)] = Field(None, description="An array of linear rings. ")
    actual_instance: Any
    one_of_schemas: List[str] = Field(QUERYENTITYCOORDINATESPARAMETER_ONE_OF_SCHEMAS, const=True)

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
        instance = QueryEntityCoordinatesParameter.construct()
        error_messages = []
        match = 0
        # validate data type: List[float]
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[List]
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: GeometryLineString
        if not isinstance(v, GeometryLineString):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GeometryLineString`")
        else:
            match += 1
        # validate data type: List[GeometryLinearRing]
        try:
            instance.oneof_schema_4_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in QueryEntityCoordinatesParameter with oneOf schemas: GeometryLineString, List[GeometryLinearRing], List[List], List[float]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in QueryEntityCoordinatesParameter with oneOf schemas: GeometryLineString, List[GeometryLinearRing], List[List], List[float]. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> QueryEntityCoordinatesParameter:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> QueryEntityCoordinatesParameter:
        """Returns the object represented by the json string"""
        instance = QueryEntityCoordinatesParameter.construct()
        error_messages = []
        match = 0

        # deserialize data into List[float]
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[List]
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GeometryLineString
        try:
            instance.actual_instance = GeometryLineString.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[GeometryLinearRing]
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
            raise ValueError("Multiple matches found when deserializing the JSON string into QueryEntityCoordinatesParameter with oneOf schemas: GeometryLineString, List[GeometryLinearRing], List[List], List[float]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into QueryEntityCoordinatesParameter with oneOf schemas: GeometryLineString, List[GeometryLinearRing], List[List], List[float]. Details: " + ", ".join(error_messages))
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

