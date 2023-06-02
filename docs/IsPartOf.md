# IsPartOf

NGSI-LD Relationship Type. A hierarchical relationship to denote the statistics of an interface. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | 
**object** | **str** |  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 

## Example

```python
from ngsi_ld_client.models.is_part_of import IsPartOf

# TODO update the JSON string below
json = "{}"
# create an instance of IsPartOf from a JSON string
is_part_of_instance = IsPartOf.from_json(json)
# print the JSON string representation of the object
print IsPartOf.to_json()

# convert the object into a dict
is_part_of_dict = is_part_of_instance.to_dict()
# create an instance of IsPartOf from a dict
is_part_of_form_dict = is_part_of.from_dict(is_part_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


