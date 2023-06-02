# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictStr

from typing import Optional

from ngsi_ld_client.models.subscription_fragment import SubscriptionFragment
from ngsi_ld_client.models.subscription_input import SubscriptionInput

from ngsi_ld_client.api_client import ApiClient
from ngsi_ld_client.api_response import ApiResponse
from ngsi_ld_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ContextInformationSubscriptionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_subscription(self, subscription_input : SubscriptionInput, local : Annotated[Optional[StrictBool], Field(description="6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). ")] = None, link : Annotated[Optional[StrictStr], Field(description="6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. ")] = None, ngsild_tenant : Annotated[Optional[StrictStr], Field(description="6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. ")] = None, **kwargs) -> None:  # noqa: E501
        """Create Subscription  # noqa: E501

        5.8.1 Create subscription.  This operation allows creating a new subscription.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_subscription(subscription_input, local, link, ngsild_tenant, async_req=True)
        >>> result = thread.get()

        :param subscription_input: (required)
        :type subscription_input: SubscriptionInput
        :param local: 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). 
        :type local: bool
        :param link: 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. 
        :type link: str
        :param ngsild_tenant: 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. 
        :type ngsild_tenant: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_subscription_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_subscription_with_http_info(subscription_input, local, link, ngsild_tenant, **kwargs)  # noqa: E501

    @validate_arguments
    def create_subscription_with_http_info(self, subscription_input : SubscriptionInput, local : Annotated[Optional[StrictBool], Field(description="6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). ")] = None, link : Annotated[Optional[StrictStr], Field(description="6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. ")] = None, ngsild_tenant : Annotated[Optional[StrictStr], Field(description="6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. ")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create Subscription  # noqa: E501

        5.8.1 Create subscription.  This operation allows creating a new subscription.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_subscription_with_http_info(subscription_input, local, link, ngsild_tenant, async_req=True)
        >>> result = thread.get()

        :param subscription_input: (required)
        :type subscription_input: SubscriptionInput
        :param local: 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). 
        :type local: bool
        :param link: 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. 
        :type link: str
        :param ngsild_tenant: 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. 
        :type ngsild_tenant: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'subscription_input',
            'local',
            'link',
            'ngsild_tenant'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_subscription" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('local') is not None:  # noqa: E501
            _query_params.append(('local', _params['local']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['link']:
            _header_params['Link'] = _params['link']

        if _params['ngsild_tenant']:
            _header_params['NGSILD-Tenant'] = _params['ngsild_tenant']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['subscription_input'] is not None:
            _body_params = _params['subscription_input']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/json+ld', 'application/geo'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'application/json+ld']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/subscriptions', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_subscription(self, subscription_id : Annotated[StrictStr, Field(..., description="Id (URI) of the concerned subscription.")], local : Annotated[Optional[StrictBool], Field(description="6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). ")] = None, link : Annotated[Optional[StrictStr], Field(description="6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. ")] = None, ngsild_tenant : Annotated[Optional[StrictStr], Field(description="6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. ")] = None, **kwargs) -> None:  # noqa: E501
        """Subscription deletion by id  # noqa: E501

        5.8.5 Delete Subscription.  This operation allows deleting an existing subscription.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_subscription(subscription_id, local, link, ngsild_tenant, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Id (URI) of the concerned subscription. (required)
        :type subscription_id: str
        :param local: 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). 
        :type local: bool
        :param link: 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. 
        :type link: str
        :param ngsild_tenant: 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. 
        :type ngsild_tenant: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_subscription_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_subscription_with_http_info(subscription_id, local, link, ngsild_tenant, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_subscription_with_http_info(self, subscription_id : Annotated[StrictStr, Field(..., description="Id (URI) of the concerned subscription.")], local : Annotated[Optional[StrictBool], Field(description="6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). ")] = None, link : Annotated[Optional[StrictStr], Field(description="6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. ")] = None, ngsild_tenant : Annotated[Optional[StrictStr], Field(description="6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. ")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Subscription deletion by id  # noqa: E501

        5.8.5 Delete Subscription.  This operation allows deleting an existing subscription.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_subscription_with_http_info(subscription_id, local, link, ngsild_tenant, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Id (URI) of the concerned subscription. (required)
        :type subscription_id: str
        :param local: 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). 
        :type local: bool
        :param link: 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. 
        :type link: str
        :param ngsild_tenant: 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. 
        :type ngsild_tenant: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'subscription_id',
            'local',
            'link',
            'ngsild_tenant'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_subscription" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['subscription_id']:
            _path_params['subscriptionId'] = _params['subscription_id']


        # process the query parameters
        _query_params = []
        if _params.get('local') is not None:  # noqa: E501
            _query_params.append(('local', _params['local']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['link']:
            _header_params['Link'] = _params['link']

        if _params['ngsild_tenant']:
            _header_params['NGSILD-Tenant'] = _params['ngsild_tenant']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/json+ld', 'application/geo'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/subscriptions/{subscriptionId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_subscription(self, subscription_id : Annotated[StrictStr, Field(..., description="Id (URI) of the concerned subscription.")], subscription_fragment : SubscriptionFragment, local : Annotated[Optional[StrictBool], Field(description="6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). ")] = None, link : Annotated[Optional[StrictStr], Field(description="6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. ")] = None, ngsild_tenant : Annotated[Optional[StrictStr], Field(description="6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. ")] = None, **kwargs) -> None:  # noqa: E501
        """Subscription update by id  # noqa: E501

        5.8.2 Update Subscription.  This operation allows updating an existing subscription.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_subscription(subscription_id, subscription_fragment, local, link, ngsild_tenant, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Id (URI) of the concerned subscription. (required)
        :type subscription_id: str
        :param subscription_fragment: (required)
        :type subscription_fragment: SubscriptionFragment
        :param local: 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). 
        :type local: bool
        :param link: 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. 
        :type link: str
        :param ngsild_tenant: 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. 
        :type ngsild_tenant: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_subscription_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_subscription_with_http_info(subscription_id, subscription_fragment, local, link, ngsild_tenant, **kwargs)  # noqa: E501

    @validate_arguments
    def update_subscription_with_http_info(self, subscription_id : Annotated[StrictStr, Field(..., description="Id (URI) of the concerned subscription.")], subscription_fragment : SubscriptionFragment, local : Annotated[Optional[StrictBool], Field(description="6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). ")] = None, link : Annotated[Optional[StrictStr], Field(description="6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. ")] = None, ngsild_tenant : Annotated[Optional[StrictStr], Field(description="6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. ")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Subscription update by id  # noqa: E501

        5.8.2 Update Subscription.  This operation allows updating an existing subscription.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_subscription_with_http_info(subscription_id, subscription_fragment, local, link, ngsild_tenant, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Id (URI) of the concerned subscription. (required)
        :type subscription_id: str
        :param subscription_fragment: (required)
        :type subscription_fragment: SubscriptionFragment
        :param local: 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4). 
        :type local: bool
        :param link: 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header. 
        :type link: str
        :param ngsild_tenant: 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted. 
        :type ngsild_tenant: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'subscription_id',
            'subscription_fragment',
            'local',
            'link',
            'ngsild_tenant'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_subscription" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['subscription_id']:
            _path_params['subscriptionId'] = _params['subscription_id']


        # process the query parameters
        _query_params = []
        if _params.get('local') is not None:  # noqa: E501
            _query_params.append(('local', _params['local']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['link']:
            _header_params['Link'] = _params['link']

        if _params['ngsild_tenant']:
            _header_params['NGSILD-Tenant'] = _params['ngsild_tenant']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['subscription_fragment'] is not None:
            _body_params = _params['subscription_fragment']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/json+ld', 'application/geo'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'application/json+ld']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/subscriptions/{subscriptionId}', 'PATCH',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
