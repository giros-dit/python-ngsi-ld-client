# ngsi_ld_client.BatchOperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_entity_creation**](BatchOperationsApi.md#batch_entity_creation) | **POST** /entityOperations/create | 
[**batch_entity_delete**](BatchOperationsApi.md#batch_entity_delete) | **POST** /entityOperations/delete | 
[**batch_entity_update**](BatchOperationsApi.md#batch_entity_update) | **POST** /entityOperations/update | 
[**batch_entity_upsert**](BatchOperationsApi.md#batch_entity_upsert) | **POST** /entityOperations/upsert | 

# **batch_entity_creation**
> BatchOperationResult batch_entity_creation(entity_list)



Batch Entity creation

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import batch_operations_api
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
    api_instance = batch_operations_api.BatchOperationsApi(api_client)

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
        print("Exception when calling BatchOperationsApi->batch_entity_creation: %s\n" % e)
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
from ngsi_ld_client.api import batch_operations_api
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
    api_instance = batch_operations_api.BatchOperationsApi(api_client)

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
        print("Exception when calling BatchOperationsApi->batch_entity_delete: %s\n" % e)
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
from ngsi_ld_client.api import batch_operations_api
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
    api_instance = batch_operations_api.BatchOperationsApi(api_client)

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
        print("Exception when calling BatchOperationsApi->batch_entity_update: %s\n" % e)

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
        print("Exception when calling BatchOperationsApi->batch_entity_update: %s\n" % e)
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
from ngsi_ld_client.api import batch_operations_api
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
    api_instance = batch_operations_api.BatchOperationsApi(api_client)

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
        print("Exception when calling BatchOperationsApi->batch_entity_upsert: %s\n" % e)

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
        print("Exception when calling BatchOperationsApi->batch_entity_upsert: %s\n" % e)
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

