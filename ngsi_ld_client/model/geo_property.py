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


class GeoProperty(
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
                "GeoProperty": "GEOPROPERTY",
            }
        ),
        StrSchema
    ):
        
        @classmethod
        @property
        def GEOPROPERTY(cls):
            return cls("GeoProperty")

    @classmethod
    @property
    def value(cls) -> typing.Type['GeoJSON']:
        return GeoJSON
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
    ) -> 'GeoProperty':
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

from ngsi_ld_client.model.geo_json import GeoJSON
