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


class ModelProperty(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'type',
        'value',
    ))
    
    
    class type(
        _SchemaEnumMaker(
            enum_value_to_name={
                "Property": "PROPERTY",
            }
        ),
        StrSchema
    ):
        
        @classmethod
        @property
        def PROPERTY(cls):
            return cls("Property")
    
    
    class value(
        ComposedSchema
    ):
    
        @classmethod
        @property
        @functools.cache
        def _composed_schemas(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            oneOf_0 = StrSchema
            oneOf_1 = NumberSchema
            oneOf_2 = BoolSchema
            
            
            class oneOf_3(
                ListSchema
            ):
                _items = DictSchema
            oneOf_4 = DictSchema
            return {
                'allOf': [
                ],
                'oneOf': [
                    oneOf_0,
                    oneOf_1,
                    oneOf_2,
                    oneOf_3,
                    oneOf_4,
                ],
                'anyOf': [
                ],
                'not':
                    None
            }
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, str, date, datetime, int, float, decimal.Decimal, None, list, tuple, bytes],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'value':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    observedAt = DateTimeSchema
    createdAt = DateTimeSchema
    modifiedAt = DateTimeSchema
    datasetId = StrSchema
    instanceId = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        type: type,
        value: value,
        observedAt: typing.Union[observedAt, Unset] = unset,
        createdAt: typing.Union[createdAt, Unset] = unset,
        modifiedAt: typing.Union[modifiedAt, Unset] = unset,
        datasetId: typing.Union[datasetId, Unset] = unset,
        instanceId: typing.Union[instanceId, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'ModelProperty':
        return super().__new__(
            cls,
            *args,
            type=type,
            value=value,
            observedAt=observedAt,
            createdAt=createdAt,
            modifiedAt=modifiedAt,
            datasetId=datasetId,
            instanceId=instanceId,
            _configuration=_configuration,
            **kwargs,
        )
