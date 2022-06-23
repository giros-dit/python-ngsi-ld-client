# coding: utf-8

"""
    ETSI ISG CIM / NGSI-LD API

    This OAS file describes the NGSI-LD API defined by the ETSI ISG CIM group. This Cross-domain Context Information Management API allows to provide, consume and subscribe to context information in multiple scenarios and involving multiple stakeholders  # noqa: E501

    The version of the OpenAPI document: latest
    Contact: NGSI-LD@etsi.org
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from ngsi_ld_client.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class RegistrationInfo(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    
    class entities(
        _SchemaValidator(
            min_items=1,
        ),
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['EntityInfo']:
            return EntityInfo
    
    
    class properties(
        _SchemaValidator(
            unique_items=True,
            min_items=1,
        ),
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Name']:
            return Name
    
    
    class relationships(
        _SchemaValidator(
            unique_items=True,
            min_items=1,
        ),
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Name']:
            return Name


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        entities: typing.Union[entities, Unset] = unset,
        properties: typing.Union[properties, Unset] = unset,
        relationships: typing.Union[relationships, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'RegistrationInfo':
        return super().__new__(
            cls,
            *args,
            entities=entities,
            properties=properties,
            relationships=relationships,
            _configuration=_configuration,
            **kwargs,
        )

from ngsi_ld_client.model.entity_info import EntityInfo
from ngsi_ld_client.model.name import Name
