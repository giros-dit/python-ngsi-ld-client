# InUnknownProtos

NGSI-LD Property Type. For packet-oriented interfaces, the number of packets received via the interface that were discarded because of an unknown or unsupported protocol.  For character-oriented or fixed-length interfaces that support protocol multiplexing, the number of transmission units received via the interface that were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter is not present. 

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
from ngsi_ld_client.models.in_unknown_protos import InUnknownProtos

# TODO update the JSON string below
json = "{}"
# create an instance of InUnknownProtos from a JSON string
in_unknown_protos_instance = InUnknownProtos.from_json(json)
# print the JSON string representation of the object
print InUnknownProtos.to_json()

# convert the object into a dict
in_unknown_protos_dict = in_unknown_protos_instance.to_dict()
# create an instance of InUnknownProtos from a dict
in_unknown_protos_form_dict = in_unknown_protos.from_dict(in_unknown_protos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


