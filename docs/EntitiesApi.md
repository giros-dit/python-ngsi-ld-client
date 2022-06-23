# ngsi_ld_client.EntitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_entity_attrs**](EntitiesApi.md#append_entity_attrs) | **POST** /entities/{entityId}/attrs/ | 
[**batch_entity_creation**](EntitiesApi.md#batch_entity_creation) | **POST** /entityOperations/create | 
[**batch_entity_delete**](EntitiesApi.md#batch_entity_delete) | **POST** /entityOperations/delete | 
[**batch_entity_update**](EntitiesApi.md#batch_entity_update) | **POST** /entityOperations/update | 
[**batch_entity_upsert**](EntitiesApi.md#batch_entity_upsert) | **POST** /entityOperations/upsert | 
[**create_entity**](EntitiesApi.md#create_entity) | **POST** /entities/ | 
[**partial_attr_update**](EntitiesApi.md#partial_attr_update) | **PATCH** /entities/{entityId}/attrs/{attrId} | 
[**query_entities**](EntitiesApi.md#query_entities) | **GET** /entities/ | 
[**remove_entity_attr**](EntitiesApi.md#remove_entity_attr) | **DELETE** /entities/{entityId}/attrs/{attrId} | 
[**remove_entity_by_id**](EntitiesApi.md#remove_entity_by_id) | **DELETE** /entities/{entityId} | 
[**retrieve_entity_by_id**](EntitiesApi.md#retrieve_entity_by_id) | **GET** /entities/{entityId} | 
[**update_entity_attrs**](EntitiesApi.md#update_entity_attrs) | **PATCH** /entities/{entityId}/attrs/ | 

# **append_entity_attrs**
> append_entity_attrs(entity_identity_fragment)



Append new Entity attributes to an existing Entity within an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.entity_fragment import EntityFragment
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.update_result import UpdateResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
    }
    query_params = {
    }
    body = EntityFragment(
        context=LdContext(None),
        location=GeoProperty(
            type="GeoProperty",
            value=GeoJSON(None),
            observed_at="1970-01-01T00:00:00.00Z",
            created_at="1970-01-01T00:00:00.00Z",
            modified_at="1970-01-01T00:00:00.00Z",
            dataset_id="dataset_id_example",
            instance_id="instance_id_example",
        ),
        observation_space=GeoProperty(),
        operation_space=GeoProperty(),
        id="id_example",
        type=Name("_"),
        created_at="1970-01-01T00:00:00.00Z",
        modified_at="1970-01-01T00:00:00.00Z",
    )
    try:
        api_response = api_instance.append_entity_attrs(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->append_entity_attrs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'entityId': "entityId_example",
    }
    query_params = {
        'options': "noOverwrite",
    }
    body = EntityFragment(
        context=LdContext(None),
        location=GeoProperty(
            type="GeoProperty",
            value=GeoJSON(None),
            observed_at="1970-01-01T00:00:00.00Z",
            created_at="1970-01-01T00:00:00.00Z",
            modified_at="1970-01-01T00:00:00.00Z",
            dataset_id="dataset_id_example",
            instance_id="instance_id_example",
        ),
        observation_space=GeoProperty(),
        operation_space=GeoProperty(),
        id="id_example",
        type=Name("_"),
        created_at="1970-01-01T00:00:00.00Z",
        modified_at="1970-01-01T00:00:00.00Z",
    )
    try:
        api_response = api_instance.append_entity_attrs(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->append_entity_attrs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityFragment**](EntityFragment.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityFragment**](EntityFragment.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
options | OptionsSchema | | optional


#### OptionsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  |  must be one of ["noOverwrite", ]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content
207 | ApiResponseFor207 | Partial Success. Only the attributes included in the response payload were successfully appended
400 | ApiResponseFor400 | Bad request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor207
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor207ResponseBodyApplicationJson, SchemaFor207ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor207ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateResult**](UpdateResult.md) |  | 


#### SchemaFor207ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateResult**](UpdateResult.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_entity_creation**
> BatchOperationResult batch_entity_creation(entity_list)



Batch Entity creation

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.entity_list import EntityList
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.batch_operation_result import BatchOperationResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    body = EntityList([
        Entity(None)
    ])
    try:
        api_response = api_instance.batch_entity_creation(
            body=body,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->batch_entity_creation: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityList**](EntityList.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityList**](EntityList.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Success
400 | ApiResponseFor400 | Bad request

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchOperationResult**](BatchOperationResult.md) |  | 


#### SchemaFor200ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchOperationResult**](BatchOperationResult.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



[**BatchOperationResult**](BatchOperationResult.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_entity_delete**
> BatchOperationResult batch_entity_delete(request_body)



Batch Entity delete

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.batch_operation_result import BatchOperationResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    body = [
        "request_body_example"
    ]
    try:
        api_response = api_instance.batch_entity_delete(
            body=body,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->batch_entity_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**[str]** |  | 

#### SchemaForRequestBodyApplicationLdjson

Type | Description | Notes
------------- | ------------- | -------------
**[str]** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Success
400 | ApiResponseFor400 | Bad request

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchOperationResult**](BatchOperationResult.md) |  | 


#### SchemaFor200ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchOperationResult**](BatchOperationResult.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



[**BatchOperationResult**](BatchOperationResult.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_entity_update**
> BatchOperationResult batch_entity_update(entity_list)



Batch Entity update

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.entity_list import EntityList
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.batch_operation_result import BatchOperationResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = EntityList([
        Entity(None)
    ])
    try:
        api_response = api_instance.batch_entity_update(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->batch_entity_update: %s\n" % e)

    # example passing only optional values
    query_params = {
        'options': "noOverwrite",
    }
    body = EntityList([
        Entity(None)
    ])
    try:
        api_response = api_instance.batch_entity_update(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->batch_entity_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityList**](EntityList.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityList**](EntityList.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
options | OptionsSchema | | optional


#### OptionsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  |  must be one of ["noOverwrite", ]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Success
400 | ApiResponseFor400 | Bad request

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchOperationResult**](BatchOperationResult.md) |  | 


#### SchemaFor200ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchOperationResult**](BatchOperationResult.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



[**BatchOperationResult**](BatchOperationResult.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_entity_upsert**
> BatchOperationResult batch_entity_upsert(entity_list)



Batch Entity upsert

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.entity_list import EntityList
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.batch_operation_result import BatchOperationResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = EntityList([
        Entity(None)
    ])
    try:
        api_response = api_instance.batch_entity_upsert(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->batch_entity_upsert: %s\n" % e)

    # example passing only optional values
    query_params = {
        'options': "replace",
    }
    body = EntityList([
        Entity(None)
    ])
    try:
        api_response = api_instance.batch_entity_upsert(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->batch_entity_upsert: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityList**](EntityList.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityList**](EntityList.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
options | OptionsSchema | | optional


#### OptionsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  |  must be one of ["replace", "update", ]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Success
400 | ApiResponseFor400 | Bad request

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchOperationResult**](BatchOperationResult.md) |  | 


#### SchemaFor200ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchOperationResult**](BatchOperationResult.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



[**BatchOperationResult**](BatchOperationResult.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity**
> create_entity(entity)



Create a new Entity within an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.entity import Entity
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    body = Entity(None)
    try:
        api_response = api_instance.create_entity(
            body=body,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->create_entity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Entity**](Entity.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Entity**](Entity.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | ApiResponseFor201 | Created. Contains the resource URI of the created Entity
400 | ApiResponseFor400 | Bad request
409 | ApiResponseFor409 | Already exists
422 | ApiResponseFor422 | Unprocessable Entity

#### ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, SchemaFor409ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor409ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, SchemaFor422ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor422ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_attr_update**
> partial_attr_update(entity_idattr_identity_fragment)



Update existing Entity attributes within an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.name import Name
from ngsi_ld_client.model.entity_fragment import EntityFragment
from ngsi_ld_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
        'attrId': Name("_"),
    }
    body = EntityFragment(
        context=LdContext(None),
        location=GeoProperty(
            type="GeoProperty",
            value=GeoJSON(None),
            observed_at="1970-01-01T00:00:00.00Z",
            created_at="1970-01-01T00:00:00.00Z",
            modified_at="1970-01-01T00:00:00.00Z",
            dataset_id="dataset_id_example",
            instance_id="instance_id_example",
        ),
        observation_space=GeoProperty(),
        operation_space=GeoProperty(),
        id="id_example",
        type=Name("_"),
        created_at="1970-01-01T00:00:00.00Z",
        modified_at="1970-01-01T00:00:00.00Z",
    )
    try:
        api_response = api_instance.partial_attr_update(
            path_params=path_params,
            body=body,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->partial_attr_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityFragment**](EntityFragment.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityFragment**](EntityFragment.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 
attrId | AttrIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AttrIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Name**](Name.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content.
400 | ApiResponseFor400 | Bad Request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_entities**
> EntityList query_entities()



Retrieve a set of entities which matches a specific query from an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.entity_list import EntityList
from ngsi_ld_client.model.coordinates import Coordinates
from ngsi_ld_client.model.geometry import Geometry
from ngsi_ld_client.model.georel import Georel
from ngsi_ld_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only optional values
    query_params = {
        'id': "id_example",
        'idPattern': "idPattern_example",
        'type': "type_example",
        'attrs': "attrs_example",
        'q': "q_example",
        'georel': Georel(None),
        'geometry': Geometry("Point"),
        'coordinates': Coordinates(None),
        'geoproperty': "geoproperty_example",
        'csf': "csf_example",
        'limit': 1,
        'options': "keyValues",
    }
    try:
        api_response = api_instance.query_entities(
            query_params=query_params,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->query_entities: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | optional
idPattern | IdPatternSchema | | optional
type | TypeSchema | | optional
attrs | AttrsSchema | | optional
q | QSchema | | optional
georel | GeorelSchema | | optional
geometry | GeometrySchema | | optional
coordinates | CoordinatesSchema | | optional
geoproperty | GeopropertySchema | | optional
csf | CsfSchema | | optional
limit | LimitSchema | | optional
options | OptionsSchema | | optional


#### IdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### IdPatternSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TypeSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AttrsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### QSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### GeorelSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Georel**](Georel.md) |  | 


#### GeometrySchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Geometry**](Geometry.md) |  | 


#### CoordinatesSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Coordinates**](Coordinates.md) |  | 


#### GeopropertySchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### CsfSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | 

#### OptionsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  |  must be one of ["keyValues", "sysAttrs", ]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | OK
400 | ApiResponseFor400 | Bad request

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityList**](EntityList.md) |  | 


#### SchemaFor200ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityList**](EntityList.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



[**EntityList**](EntityList.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_entity_attr**
> remove_entity_attr(entity_idattr_id)



Removes an existing Entity attribute within an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.name import Name
from ngsi_ld_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
        'attrId': Name("_"),
    }
    try:
        api_response = api_instance.remove_entity_attr(
            path_params=path_params,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->remove_entity_attr: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 
attrId | AttrIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AttrIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Name**](Name.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content.
400 | ApiResponseFor400 | Bad Request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_entity_by_id**
> remove_entity_by_id(entity_id)



Removes an specific Entity from an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.name import Name
from ngsi_ld_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.remove_entity_by_id(
            path_params=path_params,
            query_params=query_params,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->remove_entity_by_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'entityId': "entityId_example",
    }
    query_params = {
        'type': Name("_"),
    }
    try:
        api_response = api_instance.remove_entity_by_id(
            path_params=path_params,
            query_params=query_params,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->remove_entity_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


#### TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Name**](Name.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content. The entity was removed successfully
400 | ApiResponseFor400 | Bad Request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_entity_by_id**
> Entity retrieve_entity_by_id(entity_id)



Retrieve an specific Entity from an NGSI-LD system. It's possible to specify the Entity attributes to be retrieved by using query parameters

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.name import Name
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.entity import Entity
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.retrieve_entity_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->retrieve_entity_by_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'entityId': "entityId_example",
    }
    query_params = {
        'attrs': "attrs_example",
        'type': Name("_"),
        'options': "keyValues",
    }
    try:
        api_response = api_instance.retrieve_entity_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->retrieve_entity_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
attrs | AttrsSchema | | optional
type | TypeSchema | | optional
options | OptionsSchema | | optional


#### AttrsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Name**](Name.md) |  | 


#### OptionsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  |  must be one of ["keyValues", "sysAttrs", ]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | OK
400 | ApiResponseFor400 | Bad request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Entity**](Entity.md) |  | 


#### SchemaFor200ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Entity**](Entity.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



[**Entity**](Entity.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_attrs**
> update_entity_attrs(entity_identity_fragment)



Update existing Entity attributes within an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import entities_api
from ngsi_ld_client.model.entity_fragment import EntityFragment
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.update_result import UpdateResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
    }
    body = EntityFragment(
        context=LdContext(None),
        location=GeoProperty(
            type="GeoProperty",
            value=GeoJSON(None),
            observed_at="1970-01-01T00:00:00.00Z",
            created_at="1970-01-01T00:00:00.00Z",
            modified_at="1970-01-01T00:00:00.00Z",
            dataset_id="dataset_id_example",
            instance_id="instance_id_example",
        ),
        observation_space=GeoProperty(),
        operation_space=GeoProperty(),
        id="id_example",
        type=Name("_"),
        created_at="1970-01-01T00:00:00.00Z",
        modified_at="1970-01-01T00:00:00.00Z",
    )
    try:
        api_response = api_instance.update_entity_attrs(
            path_params=path_params,
            body=body,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling EntitiesApi->update_entity_attrs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityFragment**](EntityFragment.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityFragment**](EntityFragment.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content.
207 | ApiResponseFor207 | Partial Success. Only the attributes included in the response payload were successfully updated
400 | ApiResponseFor400 | Bad Request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor207
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor207ResponseBodyApplicationJson, SchemaFor207ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor207ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateResult**](UpdateResult.md) |  | 


#### SchemaFor207ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateResult**](UpdateResult.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

