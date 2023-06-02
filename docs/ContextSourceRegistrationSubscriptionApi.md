# ngsi_ld_client.ContextSourceRegistrationSubscriptionApi

All URIs are relative to *https://localhost/ngsi-ld/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_csr_subscription**](ContextSourceRegistrationSubscriptionApi.md#create_csr_subscription) | **POST** /csourceSubscriptions | Create subscription to Csource registration 
[**query_csr_subscription**](ContextSourceRegistrationSubscriptionApi.md#query_csr_subscription) | **GET** /csourceSubscriptions | Retrieval of list of subscription to Csource registration 
[**retrieve_csr_subscription**](ContextSourceRegistrationSubscriptionApi.md#retrieve_csr_subscription) | **GET** /csourceSubscriptions/{subscriptionId} | Retrieval of list of subscription to Csource registration 
[**update_csr_subscription**](ContextSourceRegistrationSubscriptionApi.md#update_csr_subscription) | **PATCH** /csourceSubscriptions/{subscriptionId} | Csource registration subscription update by id 


# **create_csr_subscription**
> create_csr_subscription(subscription_input, local=local, link=link, ngsild_tenant=ngsild_tenant)

Create subscription to Csource registration 

5.11.2 Create Context Source Registration Subscription.  This operation allows creating a new Context Source Registration Subscription. 

### Example

```python
import time
import os
import ngsi_ld_client
from ngsi_ld_client.models.subscription_input import SubscriptionInput
from ngsi_ld_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "https://localhost/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client.ContextSourceRegistrationSubscriptionApi(api_client)
    subscription_input = ngsi_ld_client.SubscriptionInput() # SubscriptionInput | 
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Create subscription to Csource registration 
        api_instance.create_csr_subscription(subscription_input, local=local, link=link, ngsild_tenant=ngsild_tenant)
    except Exception as e:
        print("Exception when calling ContextSourceRegistrationSubscriptionApi->create_csr_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_input** | [**SubscriptionInput**](SubscriptionInput.md)|  | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json+ld
 - **Accept**: application/json, application/json+ld, application/geo

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The HTTP response shall include a \&quot;Location\&quot; HTTP header that contains the resource URI of the created context source registration subscription resource.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**409** | It is used to indicate that the entity or an exclusive or redirect registration defining the entity already exists, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**422** | It is used to indicate that the operation is not available, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_csr_subscription**
> List[SubscriptionOutput] query_csr_subscription(options=options, limit=limit, count=count, local=local, link=link, ngsild_tenant=ngsild_tenant)

Retrieval of list of subscription to Csource registration 

5.11.5 Query Context Source Registration Subscriptions.  This operation allows querying existing Context Source Registration Subscriptions. 

### Example

```python
import time
import os
import ngsi_ld_client
from ngsi_ld_client.models.options_sys_attrs import OptionsSysAttrs
from ngsi_ld_client.models.subscription_output import SubscriptionOutput
from ngsi_ld_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "https://localhost/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client.ContextSourceRegistrationSubscriptionApi(api_client)
    options = [ngsi_ld_client.OptionsSysAttrs()] # List[OptionsSysAttrs] |  (optional)
    limit = 56 # int | 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  (optional)
    count = True # bool | 6.3.13 Counting number of results. If true, then a special HTTP header (NGSILD-Results-Count) is set in the response. Regardless of how many entities are actually returned (maybe due to the \"limit\" URI parameter), the total number of matching results (e.g. number of Entities) is returned.  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Retrieval of list of subscription to Csource registration 
        api_response = api_instance.query_csr_subscription(options=options, limit=limit, count=count, local=local, link=link, ngsild_tenant=ngsild_tenant)
        print("The response of ContextSourceRegistrationSubscriptionApi->query_csr_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextSourceRegistrationSubscriptionApi->query_csr_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**List[OptionsSysAttrs]**](OptionsSysAttrs.md)|  | [optional] 
 **limit** | **int**| 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  | [optional] 
 **count** | **bool**| 6.3.13 Counting number of results. If true, then a special HTTP header (NGSILD-Results-Count) is set in the response. Regardless of how many entities are actually returned (maybe due to the \&quot;limit\&quot; URI parameter), the total number of matching results (e.g. number of Entities) is returned.  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

[**List[SubscriptionOutput]**](SubscriptionOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld, application/geo

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing a list of context source registration subscriptions.  |  * NGSILD-Tenant -  <br>  * NGSILD-Results-Count -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_csr_subscription**
> SubscriptionOutput retrieve_csr_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant)

Retrieval of list of subscription to Csource registration 

5.11.4 Retrieve Context Source Registration Subscription.  This operation allows retrieving an existing Context Source Registration Subscription. 

### Example

```python
import time
import os
import ngsi_ld_client
from ngsi_ld_client.models.subscription_output import SubscriptionOutput
from ngsi_ld_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "https://localhost/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client.ContextSourceRegistrationSubscriptionApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id (URI) of the concerned subscription.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Retrieval of list of subscription to Csource registration 
        api_response = api_instance.retrieve_csr_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant)
        print("The response of ContextSourceRegistrationSubscriptionApi->retrieve_csr_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextSourceRegistrationSubscriptionApi->retrieve_csr_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id (URI) of the concerned subscription. | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

[**SubscriptionOutput**](SubscriptionOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld, application/geo

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the JSON-LD representation of the target context source registration subscription.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_csr_subscription**
> update_csr_subscription(subscription_id, subscription_fragment, local=local, link=link, ngsild_tenant=ngsild_tenant)

Csource registration subscription update by id 

5.11.3 Update Context Source Registration Subscription.  This operation allows updating an existing Context Source Registration Subscription. 

### Example

```python
import time
import os
import ngsi_ld_client
from ngsi_ld_client.models.subscription_fragment import SubscriptionFragment
from ngsi_ld_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "https://localhost/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client.ContextSourceRegistrationSubscriptionApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id (URI) of the concerned subscription.
    subscription_fragment = ngsi_ld_client.SubscriptionFragment() # SubscriptionFragment | 
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Csource registration subscription update by id 
        api_instance.update_csr_subscription(subscription_id, subscription_fragment, local=local, link=link, ngsild_tenant=ngsild_tenant)
    except Exception as e:
        print("Exception when calling ContextSourceRegistrationSubscriptionApi->update_csr_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id (URI) of the concerned subscription. | 
 **subscription_fragment** | [**SubscriptionFragment**](SubscriptionFragment.md)|  | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json+ld
 - **Accept**: application/json, application/json+ld, application/geo

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The context source registration subscription was successfully updated.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
