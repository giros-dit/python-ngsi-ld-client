# InUnicastPkts

NGSI-LD Property Type. The number of packets, delivered by this sub-layer to a higher (sub-)layer, that were not addressed to a multicast or broadcast address at this sub-layer. 

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
from ngsi_ld_client.models.in_unicast_pkts import InUnicastPkts

# TODO update the JSON string below
json = "{}"
# create an instance of InUnicastPkts from a JSON string
in_unicast_pkts_instance = InUnicastPkts.from_json(json)
# print the JSON string representation of the object
print InUnicastPkts.to_json()

# convert the object into a dict
in_unicast_pkts_dict = in_unicast_pkts_instance.to_dict()
# create an instance of InUnicastPkts from a dict
in_unicast_pkts_form_dict = in_unicast_pkts.from_dict(in_unicast_pkts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


