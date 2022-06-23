# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from ngsi_ld_client import api_client, exceptions
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

from ngsi_ld_client.model.coordinates import Coordinates
from ngsi_ld_client.model.geometry import Geometry
from ngsi_ld_client.model.georel import Georel
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.context_source_registration_list import ContextSourceRegistrationList

# query params
IdSchema = StrSchema
IdPatternSchema = StrSchema


class TypeSchema(
    _SchemaValidator(
        min_length=1,
    ),
    StrSchema
):
    pass


class AttrsSchema(
    _SchemaValidator(
        min_length=1,
    ),
    StrSchema
):
    pass


class QSchema(
    _SchemaValidator(
        min_length=1,
    ),
    StrSchema
):
    pass
GeorelSchema = Georel
GeometrySchema = Geometry
CoordinatesSchema = Coordinates


class GeopropertySchema(
    _SchemaValidator(
        min_length=1,
    ),
    StrSchema
):
    pass


class LimitSchema(
    _SchemaValidator(
        inclusive_minimum=1,
    ),
    IntSchema
):
    pass
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
        'id': IdSchema,
        'idPattern': IdPatternSchema,
        'type': TypeSchema,
        'attrs': AttrsSchema,
        'q': QSchema,
        'georel': GeorelSchema,
        'geometry': GeometrySchema,
        'coordinates': CoordinatesSchema,
        'geoproperty': GeopropertySchema,
        'limit': LimitSchema,
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_id = api_client.QueryParameter(
    name="id",
    style=api_client.ParameterStyle.FORM,
    schema=IdSchema,
    explode=True,
)
request_query_id_pattern = api_client.QueryParameter(
    name="idPattern",
    style=api_client.ParameterStyle.FORM,
    schema=IdPatternSchema,
    explode=True,
)
request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
request_query_attrs = api_client.QueryParameter(
    name="attrs",
    style=api_client.ParameterStyle.FORM,
    schema=AttrsSchema,
    explode=True,
)
request_query_q = api_client.QueryParameter(
    name="q",
    style=api_client.ParameterStyle.FORM,
    schema=QSchema,
    explode=True,
)
request_query_georel = api_client.QueryParameter(
    name="georel",
    style=api_client.ParameterStyle.FORM,
    schema=GeorelSchema,
    explode=True,
)
request_query_geometry = api_client.QueryParameter(
    name="geometry",
    style=api_client.ParameterStyle.FORM,
    schema=GeometrySchema,
    explode=True,
)
request_query_coordinates = api_client.QueryParameter(
    name="coordinates",
    style=api_client.ParameterStyle.FORM,
    schema=CoordinatesSchema,
    explode=True,
)
request_query_geoproperty = api_client.QueryParameter(
    name="geoproperty",
    style=api_client.ParameterStyle.FORM,
    schema=GeopropertySchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
_path = '/csourceRegistrations/'
_method = 'GET'
SchemaFor200ResponseBodyApplicationJson = ContextSourceRegistrationList
SchemaFor200ResponseBodyApplicationLdjson = ContextSourceRegistrationList


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
        SchemaFor200ResponseBodyApplicationLdjson,
    ]
    headers: Unset = unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/ld+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationLdjson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ProblemDetails
SchemaFor400ResponseBodyApplicationLdjson = ProblemDetails


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationJson,
        SchemaFor400ResponseBodyApplicationLdjson,
    ]
    headers: Unset = unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
        'application/ld+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationLdjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
    'application/ld+json',
)


class QueryCsources(api_client.Api):

    def query_csources(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)

        _query_params = []
        for parameter in (
            request_query_id,
            request_query_id_pattern,
            request_query_type,
            request_query_attrs,
            request_query_q,
            request_query_georel,
            request_query_geometry,
            request_query_coordinates,
            request_query_geoproperty,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _query_params.extend(serialized_data)

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=_path,
            method=_method,
            query_params=tuple(_query_params),
            headers=_headers,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response
