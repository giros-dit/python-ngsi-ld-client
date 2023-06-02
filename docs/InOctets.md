# InOctets

NGSI-LD Property Type. The total number of octets received on the interface, including framing characters. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | 
**value** | **int** |  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 

## Example

```python
from ngsi_ld_client.models.in_octets import InOctets

# TODO update the JSON string below
json = "{}"
# create an instance of InOctets from a JSON string
in_octets_instance = InOctets.from_json(json)
# print the JSON string representation of the object
print InOctets.to_json()

# convert the object into a dict
in_octets_dict = in_octets_instance.to_dict()
# create an instance of InOctets from a dict
in_octets_form_dict = in_octets.from_dict(in_octets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


