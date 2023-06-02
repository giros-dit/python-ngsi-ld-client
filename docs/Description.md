# Description

NGSI-LD Property Type. Description of the interface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | 
**value** | **str** |  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 

## Example

```python
from ngsi_ld_client.models.description import Description

# TODO update the JSON string below
json = "{}"
# create an instance of Description from a JSON string
description_instance = Description.from_json(json)
# print the JSON string representation of the object
print Description.to_json()

# convert the object into a dict
description_dict = description_instance.to_dict()
# create an instance of Description from a dict
description_form_dict = description.from_dict(description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


