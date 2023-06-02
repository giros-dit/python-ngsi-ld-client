# OutMulticastPkts

NGSI-LD Property Type. The total number of packets that higher-level protocols requested be transmitted and that were addressed to a multicast address at this sub-layer, including those that were discarded or not sent.  For a MAC-layer protocol, this includes both Group and Functional addresses. 

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
from ngsi_ld_client.models.out_multicast_pkts import OutMulticastPkts

# TODO update the JSON string below
json = "{}"
# create an instance of OutMulticastPkts from a JSON string
out_multicast_pkts_instance = OutMulticastPkts.from_json(json)
# print the JSON string representation of the object
print OutMulticastPkts.to_json()

# convert the object into a dict
out_multicast_pkts_dict = out_multicast_pkts_instance.to_dict()
# create an instance of OutMulticastPkts from a dict
out_multicast_pkts_form_dict = out_multicast_pkts.from_dict(out_multicast_pkts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


