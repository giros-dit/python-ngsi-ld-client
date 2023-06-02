# InDiscards

NGSI-LD Property Type. The number of inbound packets that were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space. 

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
from ngsi_ld_client.models.in_discards import InDiscards

# TODO update the JSON string below
json = "{}"
# create an instance of InDiscards from a JSON string
in_discards_instance = InDiscards.from_json(json)
# print the JSON string representation of the object
print InDiscards.to_json()

# convert the object into a dict
in_discards_dict = in_discards_instance.to_dict()
# create an instance of InDiscards from a dict
in_discards_form_dict = in_discards.from_dict(in_discards_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


