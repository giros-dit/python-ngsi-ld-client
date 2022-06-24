# coding: utf-8

"""
    ETSI ISG CIM / NGSI-LD API

    This OAS file describes the NGSI-LD API defined by the ETSI ISG CIM group. This Cross-domain Context Information Management API allows to provide, consume and subscribe to context information in multiple scenarios and involving multiple stakeholders  # noqa: E501

    The version of the OpenAPI document: latest
    Contact: NGSI-LD@etsi.org
    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
from datetime import date, datetime  # noqa: F401

from frozendict import frozendict  # noqa: F401
from ngsi_ld_client.schemas import (AnyTypeSchema, BinaryBase,  # noqa: F401
                                    BinarySchema, BoolBase, BoolSchema,
                                    ComposedBase, ComposedSchema,
                                    Configuration, DateBase, DateSchema,
                                    DateTimeBase, DateTimeSchema,
                                    DecimalSchema, DictBase, DictSchema,
                                    Float32Base, Float32Schema, Float64Base,
                                    Float64Schema, Int32Base, Int32Schema,
                                    Int64Base, Int64Schema, IntBase, IntSchema,
                                    ListBase, ListSchema, NoneBase, NoneSchema,
                                    NumberBase, NumberSchema, Schema, StrBase,
                                    StrSchema, Unset, UUIDBase, UUIDSchema,
                                    _SchemaEnumMaker, _SchemaTypeChecker,
                                    _SchemaValidator, none_type, unset)


class ContextSourceRegistrationFragment(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @classmethod
    @property
    def context(cls) -> typing.Type['LdContext']:
        return LdContext


    class information(
        _SchemaValidator(
            min_items=1,
        ),
        ListSchema
    ):

        @classmethod
        @property
        def _items(cls) -> typing.Type['RegistrationInfo']:
            return RegistrationInfo

    @classmethod
    @property
    def observationInterval(cls) -> typing.Type['TimeInterval']:
        return TimeInterval

    @classmethod
    @property
    def managementInterval(cls) -> typing.Type['TimeInterval']:
        return TimeInterval

    @classmethod
    @property
    def location(cls) -> typing.Type['GeoJSON']:
        return GeoJSON

    @classmethod
    @property
    def observationSpace(cls) -> typing.Type['GeoJSON']:
        return GeoJSON

    @classmethod
    @property
    def operationSpace(cls) -> typing.Type['GeoJSON']:
        return GeoJSON
    expires = DateTimeSchema


    class name(
        _SchemaValidator(
            min_length=1,
        ),
        StrSchema
    ):
        pass


    class description(
        _SchemaValidator(
            min_length=1,
        ),
        StrSchema
    ):
        pass
    endpoint = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        information: typing.Union[information, Unset] = unset,
        observationInterval: typing.Union['TimeInterval', Unset] = unset,
        managementInterval: typing.Union['TimeInterval', Unset] = unset,
        location: typing.Union['GeoJSON', Unset] = unset,
        observationSpace: typing.Union['GeoJSON', Unset] = unset,
        operationSpace: typing.Union['GeoJSON', Unset] = unset,
        expires: typing.Union[expires, Unset] = unset,
        name: typing.Union[name, Unset] = unset,
        description: typing.Union[description, Unset] = unset,
        endpoint: typing.Union[endpoint, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'ContextSourceRegistrationFragment':
        return super().__new__(
            cls,
            *args,
            information=information,
            observationInterval=observationInterval,
            managementInterval=managementInterval,
            location=location,
            observationSpace=observationSpace,
            operationSpace=operationSpace,
            expires=expires,
            name=name,
            description=description,
            endpoint=endpoint,
            _configuration=_configuration,
            **kwargs,
        )

from ngsi_ld_client.model.geo_json import GeoJSON
from ngsi_ld_client.model.ld_context import LdContext
from ngsi_ld_client.model.registration_info import RegistrationInfo
from ngsi_ld_client.model.time_interval import TimeInterval
