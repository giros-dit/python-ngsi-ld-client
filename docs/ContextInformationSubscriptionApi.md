# ngsi_ld_client.ContextInformationSubscriptionApi

All URIs are relative to *https://localhost/ngsi-ld/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](ContextInformationSubscriptionApi.md#create_subscription) | **POST** /subscriptions | Create Subscription 
[**delete_subscription**](ContextInformationSubscriptionApi.md#delete_subscription) | **DELETE** /subscriptions/{subscriptionId} | Subscription deletion by id 
[**update_subscription**](ContextInformationSubscriptionApi.md#update_subscription) | **PATCH** /subscriptions/{subscriptionId} | Subscription update by id 


# **create_subscription**
> create_subscription(local=local, link=link, ngsild_tenant=ngsild_tenant, create_subscription_request=create_subscription_request)

Create Subscription 

5.8.1 Create subscription.  This operation allows creating a new subscription. 

### Example

```python
import time
import os
import ngsi_ld_client
from ngsi_ld_client.models.create_subscription_request import CreateSubscriptionRequest
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
    api_instance = ngsi_ld_client.ContextInformationSubscriptionApi(api_client)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    create_subscription_request = ngsi_ld_client.CreateSubscriptionRequest() # CreateSubscriptionRequest |  (optional)

    try:
        # Create Subscription 
        api_instance.create_subscription(local=local, link=link, ngsild_tenant=ngsild_tenant, create_subscription_request=create_subscription_request)
    except Exception as e:
        print("Exception when calling ContextInformationSubscriptionApi->create_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **create_subscription_request** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)|  | [optional] 

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
**201** | The HTTP response shall include a \&quot;Location\&quot; HTTP header that contains the resource URI of the created subscription resource.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**409** | It is used to indicate that the entity or an exclusive or redirect registration defining the entity already exists, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant)

Subscription deletion by id 

5.8.5 Delete Subscription.  This operation allows deleting an existing subscription. 

### Example

```python
import time
import os
import ngsi_ld_client
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
    api_instance = ngsi_ld_client.ContextInformationSubscriptionApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id (URI) of the concerned subscription.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Subscription deletion by id 
        api_instance.delete_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant)
    except Exception as e:
        print("Exception when calling ContextInformationSubscriptionApi->delete_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id (URI) of the concerned subscription. | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld, application/geo

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> update_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant, subscription=subscription)

Subscription update by id 

5.8.2 Update Subscription.  This operation allows updating an existing subscription. 

### Example

```python
import time
import os
import ngsi_ld_client
from ngsi_ld_client.models.subscription import Subscription
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
    api_instance = ngsi_ld_client.ContextInformationSubscriptionApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id (URI) of the concerned subscription.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    subscription = ngsi_ld_client.Subscription() # Subscription |  (optional)

    try:
        # Subscription update by id 
        api_instance.update_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant, subscription=subscription)
    except Exception as e:
        print("Exception when calling ContextInformationSubscriptionApi->update_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id (URI) of the concerned subscription. | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **subscription** | [**Subscription**](Subscription.md)|  | [optional] 

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
**204** | No Content.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

