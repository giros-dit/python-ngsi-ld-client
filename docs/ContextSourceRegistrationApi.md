# ngsi_ld_client.ContextSourceRegistrationApi

All URIs are relative to *https://localhost:443/ngsi-ld/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_csr**](ContextSourceRegistrationApi.md#create_csr) | **POST** /csourceRegistrations | Csource registration creation 
[**delete_csr**](ContextSourceRegistrationApi.md#delete_csr) | **DELETE** /csourceRegistrations/{registrationId} | Csource registration deletion by id 
[**delete_csr_subscription**](ContextSourceRegistrationApi.md#delete_csr_subscription) | **DELETE** /csourceSubscriptions/{subscriptionId} | Csource registration subscription deletion by id 
[**update_csr**](ContextSourceRegistrationApi.md#update_csr) | **PATCH** /csourceRegistrations/{registrationId} | Csource registration update by id 


# **create_csr**
> create_csr(local=local, link=link, ngsild_tenant=ngsild_tenant, create_csr_request=create_csr_request)

Csource registration creation 

5.9.2 Register Context Source.  This operation allows registering a context source within an NGSI-LD system. 

### Example

```python
import time
import os
import ngsi_ld_client
from ngsi_ld_client.models.create_csr_request import CreateCSRRequest
from ngsi_ld_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client.ContextSourceRegistrationApi(api_client)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    create_csr_request = ngsi_ld_client.CreateCSRRequest() # CreateCSRRequest | Payload body in the request contains a JSON-LD object which represents the context source registration that is to be created.  (optional)

    try:
        # Csource registration creation 
        api_instance.create_csr(local=local, link=link, ngsild_tenant=ngsild_tenant, create_csr_request=create_csr_request)
    except Exception as e:
        print("Exception when calling ContextSourceRegistrationApi->create_csr: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **create_csr_request** | [**CreateCSRRequest**](CreateCSRRequest.md)| Payload body in the request contains a JSON-LD object which represents the context source registration that is to be created.  | [optional] 

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
**201** | The HTTP response shall include a \&quot;Location\&quot; HTTP header that contains the resource URI of the created context source registration resource.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**409** | It is used to indicate that the entity or an exclusive or redirect registration defining the entity already exists, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**422** | It is used to indicate that the operation is not available, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_csr**
> delete_csr(registration_id, local=local, link=link, ngsild_tenant=ngsild_tenant)

Csource registration deletion by id 

5.9.4 Delete Context Source Registration.  This operation allows deleting a Context Source Registration from an NGSI-LD system. 

### Example

```python
import time
import os
import ngsi_ld_client
from ngsi_ld_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client.ContextSourceRegistrationApi(api_client)
    registration_id = 'registration_id_example' # str | Id (URI) of the context source registration.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Csource registration deletion by id 
        api_instance.delete_csr(registration_id, local=local, link=link, ngsild_tenant=ngsild_tenant)
    except Exception as e:
        print("Exception when calling ContextSourceRegistrationApi->delete_csr: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| Id (URI) of the context source registration. | 
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

# **delete_csr_subscription**
> delete_csr_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant)

Csource registration subscription deletion by id 

5.11.6 Delete Context Source Registration Subscription.  This operation allows deleting an existing Context Source Registration Subscription. 

### Example

```python
import time
import os
import ngsi_ld_client
from ngsi_ld_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client.ContextSourceRegistrationApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id (URI) of the concerned subscription.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Csource registration subscription deletion by id 
        api_instance.delete_csr_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant)
    except Exception as e:
        print("Exception when calling ContextSourceRegistrationApi->delete_csr_subscription: %s\n" % e)
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

# **update_csr**
> update_csr(registration_id, local=local, link=link, ngsild_tenant=ngsild_tenant, request_body=request_body)

Csource registration update by id 

5.9.3 Update Context Source Registration.  This operation allows updating a Context Source Registration in an NGSI-LD system. 

### Example

```python
import time
import os
import ngsi_ld_client
from ngsi_ld_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client.ContextSourceRegistrationApi(api_client)
    registration_id = 'registration_id_example' # str | Id (URI) of the context source registration.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    request_body = None # Dict[str, object] | Payload body in the request contains a JSON-LD object which represents the context source registration that is to be updated.  (optional)

    try:
        # Csource registration update by id 
        api_instance.update_csr(registration_id, local=local, link=link, ngsild_tenant=ngsild_tenant, request_body=request_body)
    except Exception as e:
        print("Exception when calling ContextSourceRegistrationApi->update_csr: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| Id (URI) of the context source registration. | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **request_body** | [**Dict[str, object]**](object.md)| Payload body in the request contains a JSON-LD object which represents the context source registration that is to be updated.  | [optional] 

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
**204** | The context source registration was successfully updated.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

