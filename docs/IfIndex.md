# IfIndex

NGSI-LD Property Type. The ifIndex value for the ifEntry represented by this interface.

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
from ngsi_ld_client.models.if_index import IfIndex

# TODO update the JSON string below
json = "{}"
# create an instance of IfIndex from a JSON string
if_index_instance = IfIndex.from_json(json)
# print the JSON string representation of the object
print IfIndex.to_json()

# convert the object into a dict
if_index_dict = if_index_instance.to_dict()
# create an instance of IfIndex from a dict
if_index_form_dict = if_index.from_dict(if_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


