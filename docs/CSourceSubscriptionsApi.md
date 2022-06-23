# ngsi_ld_client.CSourceSubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_c_source_subscription**](CSourceSubscriptionsApi.md#create_c_source_subscription) | **POST** /csourceSubscriptions/ | 
[**remove_c_source_subscription**](CSourceSubscriptionsApi.md#remove_c_source_subscription) | **DELETE** /csourceSubscriptions/{subscriptionId} | 
[**retrieve_c_source_subscriptions**](CSourceSubscriptionsApi.md#retrieve_c_source_subscriptions) | **GET** /csourceSubscriptions/ | 
[**retrieve_c_source_subscriptions_by_id**](CSourceSubscriptionsApi.md#retrieve_c_source_subscriptions_by_id) | **GET** /csourceSubscriptions/{subscriptionId} | 
[**update_c_source_subscription**](CSourceSubscriptionsApi.md#update_c_source_subscription) | **PATCH** /csourceSubscriptions/{subscriptionId} | 

# **create_c_source_subscription**
> create_c_source_subscription(subscription)



Creates a context source discovery Subscription within an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import c_source_subscriptions_api
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.subscription import Subscription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = c_source_subscriptions_api.CSourceSubscriptionsApi(api_client)

    # example passing only required values which don't have defaults set
    body = Subscription(None)
    try:
        api_response = api_instance.create_c_source_subscription(
            body=body,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling CSourceSubscriptionsApi->create_c_source_subscription: %s\n" % e)
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
[**Subscription**](Subscription.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Subscription**](Subscription.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | ApiResponseFor201 | Created. Contains the resource URI of the created Subscription
400 | ApiResponseFor400 | Bad request
409 | ApiResponseFor409 | Already exists

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



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_c_source_subscription**
> remove_c_source_subscription(subscription_id)



Removes a specific Context Source Subscription from an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import c_source_subscriptions_api
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
    api_instance = c_source_subscriptions_api.CSourceSubscriptionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'subscriptionId': "subscriptionId_example",
    }
    try:
        api_response = api_instance.remove_c_source_subscription(
            path_params=path_params,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling CSourceSubscriptionsApi->remove_c_source_subscription: %s\n" % e)
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
subscriptionId | SubscriptionIdSchema | | 

#### SubscriptionIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content. The Subscription was removed successfully
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

# **retrieve_c_source_subscriptions**
> SubscriptionList retrieve_c_source_subscriptions()



Retrieves the context source discovery subscriptions available in an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import c_source_subscriptions_api
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.subscription_list import SubscriptionList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = c_source_subscriptions_api.CSourceSubscriptionsApi(api_client)

    # example passing only optional values
    query_params = {
        'limit': 1,
    }
    try:
        api_response = api_instance.retrieve_c_source_subscriptions(
            query_params=query_params,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling CSourceSubscriptionsApi->retrieve_c_source_subscriptions: %s\n" % e)
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
limit | LimitSchema | | optional


#### LimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | 

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
[**SubscriptionList**](SubscriptionList.md) |  | 


#### SchemaFor200ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**SubscriptionList**](SubscriptionList.md) |  | 


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



[**SubscriptionList**](SubscriptionList.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_c_source_subscriptions_by_id**
> Subscription retrieve_c_source_subscriptions_by_id(subscription_id)



Retrieves a specific Subscription from an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import c_source_subscriptions_api
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.subscription import Subscription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = c_source_subscriptions_api.CSourceSubscriptionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'subscriptionId': "subscriptionId_example",
    }
    try:
        api_response = api_instance.retrieve_c_source_subscriptions_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling CSourceSubscriptionsApi->retrieve_c_source_subscriptions_by_id: %s\n" % e)
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
subscriptionId | SubscriptionIdSchema | | 

#### SubscriptionIdSchema

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
[**Subscription**](Subscription.md) |  | 


#### SchemaFor200ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Subscription**](Subscription.md) |  | 


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



[**Subscription**](Subscription.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_c_source_subscription**
> update_c_source_subscription(subscription_idsubscription_fragment)



Updates a specific context source discovery Subscription within an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import c_source_subscriptions_api
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.subscription_fragment import SubscriptionFragment
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = c_source_subscriptions_api.CSourceSubscriptionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'subscriptionId': "subscriptionId_example",
    }
    body = SubscriptionFragment(
        context=LdContext(None),
        entities=[
            EntityInfo(
                id="id_example",
                type=Name("_"),
                id_pattern="id_pattern_example",
            )
        ],
        name="name_example",
        description="description_example",
        watched_attributes=[
            Name("watched_attributes_example")
        ],
        time_interval=0,
        expires="1970-01-01T00:00:00.00Z",
        is_active=True,
        throttling=1,
        q="q_example",
        geo_q=GeoQuery(
            georel=Georel(None),
            coordinates=Coordinates(None),
            geometry=Geometry("Point"),
        ),
        csf="csf_example",
    )
    try:
        api_response = api_instance.update_c_source_subscription(
            path_params=path_params,
            body=body,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling CSourceSubscriptionsApi->update_c_source_subscription: %s\n" % e)
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
[**SubscriptionFragment**](SubscriptionFragment.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**SubscriptionFragment**](SubscriptionFragment.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
subscriptionId | SubscriptionIdSchema | | 

#### SubscriptionIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content. The Subscription was updated successfully
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

