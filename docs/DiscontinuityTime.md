# DiscontinuityTime

NGSI-LD Property Type. The time on the most recent occasion at which any one or more of this interface's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re-initialization of the local management subsystem, then this node contains the time the local management subsystem re-initialized itself. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | 
**value** | **datetime** |  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 

## Example

```python
from ngsi_ld_client.models.discontinuity_time import DiscontinuityTime

# TODO update the JSON string below
json = "{}"
# create an instance of DiscontinuityTime from a JSON string
discontinuity_time_instance = DiscontinuityTime.from_json(json)
# print the JSON string representation of the object
print DiscontinuityTime.to_json()

# convert the object into a dict
discontinuity_time_dict = discontinuity_time_instance.to_dict()
# create an instance of DiscontinuityTime from a dict
discontinuity_time_form_dict = discontinuity_time.from_dict(discontinuity_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


