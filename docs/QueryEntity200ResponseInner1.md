# QueryEntity200ResponseInner1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | 
**type** | [**EntityType**](EntityType.md) |  | 
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) | Default geospatial Property of an entity. See clause 4.7.  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_client.models.query_entity200_response_inner1 import QueryEntity200ResponseInner1

# TODO update the JSON string below
json = "{}"
# create an instance of QueryEntity200ResponseInner1 from a JSON string
query_entity200_response_inner1_instance = QueryEntity200ResponseInner1.from_json(json)
# print the JSON string representation of the object
print(QueryEntity200ResponseInner1.to_json())

# convert the object into a dict
query_entity200_response_inner1_dict = query_entity200_response_inner1_instance.to_dict()
# create an instance of QueryEntity200ResponseInner1 from a dict
query_entity200_response_inner1_from_dict = QueryEntity200ResponseInner1.from_dict(query_entity200_response_inner1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


