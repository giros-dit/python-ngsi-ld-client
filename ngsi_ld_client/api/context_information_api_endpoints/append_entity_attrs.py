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

from ngsi_ld_client.model.entity_fragment import EntityFragment
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.update_result import UpdateResult

# query params


class OptionsSchema(
    _SchemaEnumMaker(
        enum_value_to_name={
            "noOverwrite": "NOOVERWRITE",
        }
    ),
    StrSchema
):
    
    @classmethod
    @property
    def NOOVERWRITE(cls):
        return cls("noOverwrite")
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
        'options': OptionsSchema,
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_options = api_client.QueryParameter(
    name="options",
    style=api_client.ParameterStyle.FORM,
    schema=OptionsSchema,
    explode=True,
)
# path params
EntityIdSchema = StrSchema
RequestRequiredPathParams = typing.TypedDict(
    'RequestRequiredPathParams',
    {
        'entityId': EntityIdSchema,
    }
)
RequestOptionalPathParams = typing.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_entity_id = api_client.PathParameter(
    name="entityId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EntityIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = EntityFragment
SchemaForRequestBodyApplicationLdjson = EntityFragment


request_body_entity_fragment = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/ld+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationLdjson),
    },
    required=True,
)
_path = '/entities/{entityId}/attrs/'
_method = 'POST'


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: Unset = unset
    headers: Unset = unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
)
SchemaFor207ResponseBodyApplicationJson = UpdateResult
SchemaFor207ResponseBodyApplicationLdjson = UpdateResult


@dataclass
class ApiResponseFor207(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor207ResponseBodyApplicationJson,
        SchemaFor207ResponseBodyApplicationLdjson,
    ]
    headers: Unset = unset


_response_for_207 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor207,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor207ResponseBodyApplicationJson),
        'application/ld+json': api_client.MediaType(
            schema=SchemaFor207ResponseBodyApplicationLdjson),
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
SchemaFor404ResponseBodyApplicationJson = ProblemDetails
SchemaFor404ResponseBodyApplicationLdjson = ProblemDetails


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor404ResponseBodyApplicationJson,
        SchemaFor404ResponseBodyApplicationLdjson,
    ]
    headers: Unset = unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
        'application/ld+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationLdjson),
    },
)
_status_code_to_response = {
    '204': _response_for_204,
    '207': _response_for_207,
    '400': _response_for_400,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
    'application/ld+json',
)


class AppendEntityAttrs(api_client.Api):

    def append_entity_attrs(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson],
        query_params: RequestQueryParams = frozendict(),
        path_params: RequestPathParams = frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        ApiResponseFor207,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs(RequestPathParams, path_params)
        used_path = _path

        _path_params = {}
        for parameter in (
            request_path_entity_id,
        ):
            parameter_data = path_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_options,
        ):
            parameter_data = query_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        if body is unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_entity_fragment.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method=_method,
            headers=_headers,
            fields=_fields,
            body=_body,
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
