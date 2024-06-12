# QueryCSR200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique registration identifier. (JSON-LD @id). There may be multiple registrations per Context Source, i.e. the id is unique per registration.  | 
**type** | **str** | JSON-LD @type Use reserved type for identifying Context Source Registration.  | 
**registration_name** | **str** | A name given to this Context Source Registration.  | [optional] 
**description** | **str** | A description of this Context Source Registration.  | [optional] 
**information** | [**List[RegistrationInfo]**](RegistrationInfo.md) | Describes the Entities, Properties and Relationships for which the Context Source may be able to provide information.  | 
**tenant** | **str** | Identifies the tenant that has to be specified in all requests to the Context Source that are related to the information registered in this Context Source Registration. If not present, the default tenant is assumed. Should only be present in systems supporting multi-tenancy.  | [optional] 
**observation_interval** | [**TimeInterval**](TimeInterval.md) | If present, the Context Source can be queried for Temporal Entity Representations. (If latest Entity information is also provided, a separate Context Registration is needed for this purpose). The observationInterval specifies the time interval for which the Context Source can provide Entity information as specified by the observedAt Temporal Property. A temporal query based on the observedAt Temporal Property, which is the default, is matched against the observationInterval for overlap.  | [optional] 
**management_interval** | [**TimeInterval**](TimeInterval.md) | If present, the Context Source can be queried for Temporal Entity Representations. (If latest Entity information is also provided, a separate Context Registration is needed for this purpose). The managementInterval specifies the time interval for which the Context Source can provide Entity information as specified by the createdAt, modifiedAt and deletedAt Temporal Properties. A temporal query based on the createdAt, modifiedAt or deletedAt Temporal Property is matched against the managementInterval for overlap.  | [optional] 
**location** | [**Geometry**](Geometry.md) | Location for which the Context Source may be able to provide information.  | [optional] 
**observation_space** | [**Geometry**](Geometry.md) | Geographic location that includes the observation spaces of all entities as specified by their  respective observationSpace GeoProperty for which the Context Source may be able to provide  information.  | [optional] 
**operation_space** | [**Geometry**](Geometry.md) | Geographic location that includes the operation spaces of all entities as specified by their  respective operationSpace GeoProperty for which the Context Source may be able to provide  information.  | [optional] 
**expires_at** | **datetime** | Provides an expiration date. When passed the Context Source Registration will become invalid and the Context Source might no longer be available.  | [optional] 
**endpoint** | **str** | Endpoint expressed as dereferenceable URI through which the Context Source exposes its NGSI-LD interface.  | 
**context_source_info** | [**List[KeyValuePair]**](KeyValuePair.md) | Generic {key, value} array to convey optional information to provide when contacting the registered Context Source.  | [optional] 
**scope** | [**CsourceRegistrationScope**](CsourceRegistrationScope.md) |  | [optional] 
**mode** | **str** | The definition of the mode of distributed operation (see clause 4.3.6) supported by the registered Context Source.  | [optional] [default to 'inclusive']
**operations** | **List[str]** | The definition limited subset of API operations supported by the registered Context Source.  If undefined, the default set of operations is \&quot;federationOps\&quot; (see clause 4.20).  | [optional] 
**refresh_rate** | **str** | An indication of the likely period of time to elapse between updates at this registered endpoint. Brokers may optionally use this information to help implement caching.  | [optional] 
**management** | [**RegistrationManagementInfo**](RegistrationManagementInfo.md) | Holds additional optional registration management information that can be used to limit unnecessary distributed operation requests.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**status** | **str** | Read-only. Status of the Registration. It shall be \&quot;ok\&quot; if the last attempt to perform a distributed operation succeeded. It shall be \&quot;failed\&quot; if the last attempt to perform a distributed operation failed.  | [optional] [readonly] 
**times_sent** | **float** | Number of times that the registration triggered a distributed operation, including failed attempts.  | [optional] [readonly] 
**times_failed** | **float** | Number of times that the registration triggered a distributed operation request that failed. | [optional] [readonly] 
**last_success** | **datetime** | Timestamp corresponding to the instant when the last successfully distributed operation was sent. Created on first successful operation.  | [optional] [readonly] 
**last_failure** | **datetime** | Timestamp corresponding to the instant when the last distributed operation resulting in a failure (for instance, in the HTTP binding, an HTTP response code other than 2xx) was returned.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_client.models.query_csr200_response_inner import QueryCSR200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryCSR200ResponseInner from a JSON string
query_csr200_response_inner_instance = QueryCSR200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(QueryCSR200ResponseInner.to_json())

# convert the object into a dict
query_csr200_response_inner_dict = query_csr200_response_inner_instance.to_dict()
# create an instance of QueryCSR200ResponseInner from a dict
query_csr200_response_inner_from_dict = QueryCSR200ResponseInner.from_dict(query_csr200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


