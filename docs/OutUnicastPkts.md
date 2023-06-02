# OutUnicastPkts

NGSI-LD Property Type. The total number of packets that higher-level protocols requested be transmitted and that were not addressed to a multicast or broadcast address at this sub-layer, including those that were discarded or not sent. 

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
from ngsi_ld_client.models.out_unicast_pkts import OutUnicastPkts

# TODO update the JSON string below
json = "{}"
# create an instance of OutUnicastPkts from a JSON string
out_unicast_pkts_instance = OutUnicastPkts.from_json(json)
# print the JSON string representation of the object
print OutUnicastPkts.to_json()

# convert the object into a dict
out_unicast_pkts_dict = out_unicast_pkts_instance.to_dict()
# create an instance of OutUnicastPkts from a dict
out_unicast_pkts_form_dict = out_unicast_pkts.from_dict(out_unicast_pkts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


