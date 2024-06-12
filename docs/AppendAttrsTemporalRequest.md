# AppendAttrsTemporalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | [**EntityType**](EntityType.md) |  | [optional] 
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) | Default geospatial Property of an entity. See clause 4.7.  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_client.models.append_attrs_temporal_request import AppendAttrsTemporalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppendAttrsTemporalRequest from a JSON string
append_attrs_temporal_request_instance = AppendAttrsTemporalRequest.from_json(json)
# print the JSON string representation of the object
print(AppendAttrsTemporalRequest.to_json())

# convert the object into a dict
append_attrs_temporal_request_dict = append_attrs_temporal_request_instance.to_dict()
# create an instance of AppendAttrsTemporalRequest from a dict
append_attrs_temporal_request_from_dict = AppendAttrsTemporalRequest.from_dict(append_attrs_temporal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


