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


class SubscriptionFragment(
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


    class watchedAttributes(
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


    class timeInterval(
        _SchemaValidator(
            inclusive_minimum=0,
        ),
        NumberSchema
    ):
        pass
    expires = DateTimeSchema
    isActive = BoolSchema


    class throttling(
        _SchemaValidator(
            inclusive_minimum=1,
        ),
        NumberSchema
    ):
        pass
    q = StrSchema

    @classmethod
    @property
    def geoQ(cls) -> typing.Type['GeoQuery']:
        return GeoQuery
    csf = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        entities: typing.Union[entities, Unset] = unset,
        name: typing.Union[name, Unset] = unset,
        description: typing.Union[description, Unset] = unset,
        watchedAttributes: typing.Union[watchedAttributes, Unset] = unset,
        timeInterval: typing.Union[timeInterval, Unset] = unset,
        expires: typing.Union[expires, Unset] = unset,
        isActive: typing.Union[isActive, Unset] = unset,
        throttling: typing.Union[throttling, Unset] = unset,
        q: typing.Union[q, Unset] = unset,
        geoQ: typing.Union['GeoQuery', Unset] = unset,
        csf: typing.Union[csf, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'SubscriptionFragment':
        return super().__new__(
            cls,
            *args,
            entities=entities,
            name=name,
            description=description,
            watchedAttributes=watchedAttributes,
            timeInterval=timeInterval,
            expires=expires,
            isActive=isActive,
            throttling=throttling,
            q=q,
            geoQ=geoQ,
            csf=csf,
            _configuration=_configuration,
            **kwargs,
        )

from ngsi_ld_client.model.entity_info import EntityInfo
from ngsi_ld_client.model.geo_query import GeoQuery
from ngsi_ld_client.model.ld_context import LdContext
from ngsi_ld_client.model.name import Name
