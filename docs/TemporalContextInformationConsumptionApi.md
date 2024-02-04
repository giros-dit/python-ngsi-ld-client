# ngsi_ld_client.TemporalContextInformationConsumptionApi

All URIs are relative to *https://localhost:443/ngsi-ld/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_temporal**](TemporalContextInformationConsumptionApi.md#query_temporal) | **GET** /temporal/entities | Query temporal evolution of Entities 
[**retrieve_temporal**](TemporalContextInformationConsumptionApi.md#retrieve_temporal) | **GET** /temporal/entities/{entityId} | Temporal Representation of Entity retrieval by id 
[**temporal_query_batch**](TemporalContextInformationConsumptionApi.md#temporal_query_batch) | **POST** /temporal/entityOperations/query | Temporal Representation of Entity Query based on POST 


# **query_temporal**
> List[QueryTemporal200ResponseInner] query_temporal(id=id, type=type, id_pattern=id_pattern, attrs=attrs, q=q, csf=csf, geometry=geometry, georel=georel, coordinates=coordinates, geoproperty=geoproperty, timeproperty=timeproperty, timerel=timerel, time_at=time_at, end_time_at=end_time_at, last_n=last_n, lang=lang, aggr_methods=aggr_methods, aggr_period_duration=aggr_period_duration, scope_q=scope_q, limit=limit, options=options, local=local, link=link, ngsild_tenant=ngsild_tenant)

Query temporal evolution of Entities 

5.7.4 Query Temporal Evolution of Entities.  This operation allows querying the temporal evolution of Entities present in an NGSI-LD system. It is similar to the operation defined by clause 5.7.2 (Query Entities) with the addition of a temporal query. 

### Example


```python
import ngsi_ld_client
from ngsi_ld_client.models.options_temporal import OptionsTemporal
from ngsi_ld_client.models.query_temporal200_response_inner import QueryTemporal200ResponseInner
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
    api_instance = ngsi_ld_client.TemporalContextInformationConsumptionApi(api_client)
    id = ['id_example'] # List[str] | List of entity ids to be retrieved. (optional)
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17.  (optional)
    id_pattern = 'id_pattern_example' # str | Regular expression that shall be matched by entity ids. (optional)
    attrs = ['attrs_example'] # List[str] | List of Attributes to be matched by the Entity and included in the response. If the Entity does not have any of the Attributes in attrs, then a 404 Not Found shall be retrieved. If attrs is not specified, no matching is performed and all Attributes related to the Entity shall be retrieved.  (optional)
    q = 'q_example' # str | Query as per clause 4.9.  (optional)
    csf = 'csf_example' # str | Context Source filter as per clause 4.9. (optional)
    geometry = 'geometry_example' # str | Geometry as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  (optional)
    georel = ngsi_ld_client.QueryEntityGeorelParameter() # QueryEntityGeorelParameter | Geo relationship as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  (optional)
    coordinates = ngsi_ld_client.QueryEntityCoordinatesParameter() # QueryEntityCoordinatesParameter | Coordinates serialized as a string as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  (optional)
    geoproperty = 'geoproperty_example' # str | The name of the Property that contains the geospatial data that will be used to resolve the geoquery. By default, will be location (see clause 4.7). It shall be ignored unless a geoquery is present.  (optional)
    timeproperty = 'timeproperty_example' # str | Allowed values: \"observedAt\", \"createdAt\", \"modifiedAt\" and \"deletedAt\". If not specified, the default is \"observedAt\". (See clause 4.8)  (optional)
    timerel = 'timerel_example' # str | Allowed values: \"before\", \"after\", \"between\"  (optional)
    time_at = '2013-10-20T19:20:30+01:00' # datetime | It shall be a DateTime. Cardinality shall be 1 if timerel is present. String representing the timeAt parameter as defined by clause 4.11.  (optional)
    end_time_at = '2013-10-20T19:20:30+01:00' # datetime | It shall be a DateTime. Cardinality shall be 1 if timerel is equal to \"between\". String representing the endTimeAt parameter as defined by clause 4.11.  (optional)
    last_n = 56 # int | Only the last n instances, per Attribute, per Entity (under the specified time interval) shall be retrieved.  (optional)
    lang = 'lang_example' # str | It is used to reduce languageMaps to a string or string array property in a single preferred language.  (optional)
    aggr_methods = 'aggr_methods_example' # str | 4.5.19.1 Aggregated Temporal Representation of an Entity.  Comma separated list of aggregation methods.  Only applicable if aggregatedValues is present in the options parameter.  (optional)
    aggr_period_duration = 'aggr_period_duration_example' # str | If not specified, it defaults to a duration of 0 seconds and is interpreted as a duration spanning the whole time range specified by the temporal query.  Only applicable if aggregatedValues is present in the options parameter.  (optional)
    scope_q = 'scope_q_example' # str | Scope query (see clause 4.19).  (optional)
    limit = 56 # int | 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  (optional)
    options = [ngsi_ld_client.OptionsTemporal()] # List[OptionsTemporal] |  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Query temporal evolution of Entities 
        api_response = api_instance.query_temporal(id=id, type=type, id_pattern=id_pattern, attrs=attrs, q=q, csf=csf, geometry=geometry, georel=georel, coordinates=coordinates, geoproperty=geoproperty, timeproperty=timeproperty, timerel=timerel, time_at=time_at, end_time_at=end_time_at, last_n=last_n, lang=lang, aggr_methods=aggr_methods, aggr_period_duration=aggr_period_duration, scope_q=scope_q, limit=limit, options=options, local=local, link=link, ngsild_tenant=ngsild_tenant)
        print("The response of TemporalContextInformationConsumptionApi->query_temporal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalContextInformationConsumptionApi->query_temporal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| List of entity ids to be retrieved. | [optional] 
 **type** | **str**| Selection of Entity Types as per clause 4.17.  | [optional] 
 **id_pattern** | **str**| Regular expression that shall be matched by entity ids. | [optional] 
 **attrs** | [**List[str]**](str.md)| List of Attributes to be matched by the Entity and included in the response. If the Entity does not have any of the Attributes in attrs, then a 404 Not Found shall be retrieved. If attrs is not specified, no matching is performed and all Attributes related to the Entity shall be retrieved.  | [optional] 
 **q** | **str**| Query as per clause 4.9.  | [optional] 
 **csf** | **str**| Context Source filter as per clause 4.9. | [optional] 
 **geometry** | **str**| Geometry as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  | [optional] 
 **georel** | [**QueryEntityGeorelParameter**](.md)| Geo relationship as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  | [optional] 
 **coordinates** | [**QueryEntityCoordinatesParameter**](.md)| Coordinates serialized as a string as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  | [optional] 
 **geoproperty** | **str**| The name of the Property that contains the geospatial data that will be used to resolve the geoquery. By default, will be location (see clause 4.7). It shall be ignored unless a geoquery is present.  | [optional] 
 **timeproperty** | **str**| Allowed values: \&quot;observedAt\&quot;, \&quot;createdAt\&quot;, \&quot;modifiedAt\&quot; and \&quot;deletedAt\&quot;. If not specified, the default is \&quot;observedAt\&quot;. (See clause 4.8)  | [optional] 
 **timerel** | **str**| Allowed values: \&quot;before\&quot;, \&quot;after\&quot;, \&quot;between\&quot;  | [optional] 
 **time_at** | **datetime**| It shall be a DateTime. Cardinality shall be 1 if timerel is present. String representing the timeAt parameter as defined by clause 4.11.  | [optional] 
 **end_time_at** | **datetime**| It shall be a DateTime. Cardinality shall be 1 if timerel is equal to \&quot;between\&quot;. String representing the endTimeAt parameter as defined by clause 4.11.  | [optional] 
 **last_n** | **int**| Only the last n instances, per Attribute, per Entity (under the specified time interval) shall be retrieved.  | [optional] 
 **lang** | **str**| It is used to reduce languageMaps to a string or string array property in a single preferred language.  | [optional] 
 **aggr_methods** | **str**| 4.5.19.1 Aggregated Temporal Representation of an Entity.  Comma separated list of aggregation methods.  Only applicable if aggregatedValues is present in the options parameter.  | [optional] 
 **aggr_period_duration** | **str**| If not specified, it defaults to a duration of 0 seconds and is interpreted as a duration spanning the whole time range specified by the temporal query.  Only applicable if aggregatedValues is present in the options parameter.  | [optional] 
 **scope_q** | **str**| Scope query (see clause 4.19).  | [optional] 
 **limit** | **int**| 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  | [optional] 
 **options** | [**List[OptionsTemporal]**](OptionsTemporal.md)|  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

[**List[QueryTemporal200ResponseInner]**](QueryTemporal200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld, application/geo

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the query result as a list of temporal representation of Entities.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_temporal**
> QueryTemporal200ResponseInner retrieve_temporal(entity_id, attrs=attrs, timeproperty=timeproperty, timerel=timerel, time_at=time_at, end_time_at=end_time_at, last_n=last_n, lang=lang, aggr_methods=aggr_methods, aggr_period_duration=aggr_period_duration, scope_q=scope_q, limit=limit, options=options, local=local, link=link, ngsild_tenant=ngsild_tenant)

Temporal Representation of Entity retrieval by id 

5.7.3 Retrieve Temporal Evolution of an Entity.  This operation allows retrieving the temporal evolution of an NGSI-LD Entity. 

### Example


```python
import ngsi_ld_client
from ngsi_ld_client.models.options_temporal import OptionsTemporal
from ngsi_ld_client.models.query_temporal200_response_inner import QueryTemporal200ResponseInner
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
    api_instance = ngsi_ld_client.TemporalContextInformationConsumptionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the entity to be retrieved.
    attrs = ['attrs_example'] # List[str] | List of Attributes to be matched by the Entity and included in the response. If the Entity does not have any of the Attributes in attrs, then a 404 Not Found shall be retrieved. If attrs is not specified, no matching is performed and all Attributes related to the Entity shall be retrieved.  (optional)
    timeproperty = 'timeproperty_example' # str | Allowed values: \"observedAt\", \"createdAt\", \"modifiedAt\" and \"deletedAt\". If not specified, the default is \"observedAt\". (See clause 4.8)  (optional)
    timerel = 'timerel_example' # str | Allowed values: \"before\", \"after\", \"between\"  (optional)
    time_at = '2013-10-20T19:20:30+01:00' # datetime | It shall be a DateTime. Cardinality shall be 1 if timerel is present. String representing the timeAt parameter as defined by clause 4.11.  (optional)
    end_time_at = '2013-10-20T19:20:30+01:00' # datetime | It shall be a DateTime. Cardinality shall be 1 if timerel is equal to \"between\". String representing the endTimeAt parameter as defined by clause 4.11.  (optional)
    last_n = 56 # int | Only the last n instances, per Attribute, per Entity (under the specified time interval) shall be retrieved.  (optional)
    lang = 'lang_example' # str | It is used to reduce languageMaps to a string or string array property in a single preferred language.  (optional)
    aggr_methods = 'aggr_methods_example' # str | 4.5.19.1 Aggregated Temporal Representation of an Entity.  Comma separated list of aggregation methods.  Only applicable if aggregatedValues is present in the options parameter.  (optional)
    aggr_period_duration = 'aggr_period_duration_example' # str | If not specified, it defaults to a duration of 0 seconds and is interpreted as a duration spanning the whole time range specified by the temporal query.  Only applicable if aggregatedValues is present in the options parameter.  (optional)
    scope_q = 'scope_q_example' # str | Scope query (see clause 4.19).  (optional)
    limit = 56 # int | 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  (optional)
    options = [ngsi_ld_client.OptionsTemporal()] # List[OptionsTemporal] |  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Temporal Representation of Entity retrieval by id 
        api_response = api_instance.retrieve_temporal(entity_id, attrs=attrs, timeproperty=timeproperty, timerel=timerel, time_at=time_at, end_time_at=end_time_at, last_n=last_n, lang=lang, aggr_methods=aggr_methods, aggr_period_duration=aggr_period_duration, scope_q=scope_q, limit=limit, options=options, local=local, link=link, ngsild_tenant=ngsild_tenant)
        print("The response of TemporalContextInformationConsumptionApi->retrieve_temporal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalContextInformationConsumptionApi->retrieve_temporal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the entity to be retrieved. | 
 **attrs** | [**List[str]**](str.md)| List of Attributes to be matched by the Entity and included in the response. If the Entity does not have any of the Attributes in attrs, then a 404 Not Found shall be retrieved. If attrs is not specified, no matching is performed and all Attributes related to the Entity shall be retrieved.  | [optional] 
 **timeproperty** | **str**| Allowed values: \&quot;observedAt\&quot;, \&quot;createdAt\&quot;, \&quot;modifiedAt\&quot; and \&quot;deletedAt\&quot;. If not specified, the default is \&quot;observedAt\&quot;. (See clause 4.8)  | [optional] 
 **timerel** | **str**| Allowed values: \&quot;before\&quot;, \&quot;after\&quot;, \&quot;between\&quot;  | [optional] 
 **time_at** | **datetime**| It shall be a DateTime. Cardinality shall be 1 if timerel is present. String representing the timeAt parameter as defined by clause 4.11.  | [optional] 
 **end_time_at** | **datetime**| It shall be a DateTime. Cardinality shall be 1 if timerel is equal to \&quot;between\&quot;. String representing the endTimeAt parameter as defined by clause 4.11.  | [optional] 
 **last_n** | **int**| Only the last n instances, per Attribute, per Entity (under the specified time interval) shall be retrieved.  | [optional] 
 **lang** | **str**| It is used to reduce languageMaps to a string or string array property in a single preferred language.  | [optional] 
 **aggr_methods** | **str**| 4.5.19.1 Aggregated Temporal Representation of an Entity.  Comma separated list of aggregation methods.  Only applicable if aggregatedValues is present in the options parameter.  | [optional] 
 **aggr_period_duration** | **str**| If not specified, it defaults to a duration of 0 seconds and is interpreted as a duration spanning the whole time range specified by the temporal query.  Only applicable if aggregatedValues is present in the options parameter.  | [optional] 
 **scope_q** | **str**| Scope query (see clause 4.19).  | [optional] 
 **limit** | **int**| 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  | [optional] 
 **options** | [**List[OptionsTemporal]**](OptionsTemporal.md)|  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

[**QueryTemporal200ResponseInner**](QueryTemporal200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld, application/geo

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the JSON-LD temporal representation of the target entity containing the selected Attributes.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **temporal_query_batch**
> List[QueryTemporal200ResponseInner] temporal_query_batch(local=local, link=link, ngsild_tenant=ngsild_tenant, query_temporal=query_temporal)

Temporal Representation of Entity Query based on POST 

5.7.4 Query Temporal Evolution of Entities.  This operation allows querying the temporal evolution of Entities present in an NGSI-LD system. It is similar to the operation defined by clause 5.7.2 (Query Entities) with the addition of a temporal query. 

### Example


```python
import ngsi_ld_client
from ngsi_ld_client.models.query_temporal import QueryTemporal
from ngsi_ld_client.models.query_temporal200_response_inner import QueryTemporal200ResponseInner
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
    api_instance = ngsi_ld_client.TemporalContextInformationConsumptionApi(api_client)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    query_temporal = ngsi_ld_client.QueryTemporal() # QueryTemporal |  (optional)

    try:
        # Temporal Representation of Entity Query based on POST 
        api_response = api_instance.temporal_query_batch(local=local, link=link, ngsild_tenant=ngsild_tenant, query_temporal=query_temporal)
        print("The response of TemporalContextInformationConsumptionApi->temporal_query_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalContextInformationConsumptionApi->temporal_query_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **query_temporal** | [**QueryTemporal**](QueryTemporal.md)|  | [optional] 

### Return type

[**List[QueryTemporal200ResponseInner]**](QueryTemporal200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json+ld
 - **Accept**: application/json, application/json+ld, application/geo

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the query result as a list of Entities.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

