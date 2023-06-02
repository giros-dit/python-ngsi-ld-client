# Statistics

NGSI-LD Entity Type that represents a collection of interface-related statistics  of a model-based network device 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | 
**type** | **str** | NGSI-LD Entity identifier. It has to be Statistics. | [default to 'Statistics']
**scope** | [**EntityCommonScope**](EntityCommonScope.md) |  | [optional] 
**location** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**observation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**operation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 
**discontinuity_time** | [**DiscontinuityTime**](DiscontinuityTime.md) |  | 
**in_octets** | [**InOctets**](InOctets.md) |  | [optional] 
**in_unicast_pkts** | [**InUnicastPkts**](InUnicastPkts.md) |  | [optional] 
**in_broadcast_pkts** | [**InBroadcastPkts**](InBroadcastPkts.md) |  | [optional] 
**in_multicast_pkts** | [**InMulticastPkts**](InMulticastPkts.md) |  | [optional] 
**in_discards** | [**InDiscards**](InDiscards.md) |  | [optional] 
**in_errors** | [**InErrors**](InErrors.md) |  | [optional] 
**in_unknown_protos** | [**InUnknownProtos**](InUnknownProtos.md) |  | [optional] 
**out_octets** | [**OutOctets**](OutOctets.md) |  | [optional] 
**out_unicast_pkts** | [**OutUnicastPkts**](OutUnicastPkts.md) |  | [optional] 
**out_broadcast_pkts** | [**OutBroadcastPkts**](OutBroadcastPkts.md) |  | [optional] 
**out_multicast_pkts** | [**OutMulticastPkts**](OutMulticastPkts.md) |  | [optional] 
**out_discards** | [**OutDiscards**](OutDiscards.md) |  | [optional] 
**out_errors** | [**OutErrors**](OutErrors.md) |  | [optional] 

## Example

```python
from ngsi_ld_client.models.statistics import Statistics

# TODO update the JSON string below
json = "{}"
# create an instance of Statistics from a JSON string
statistics_instance = Statistics.from_json(json)
# print the JSON string representation of the object
print Statistics.to_json()

# convert the object into a dict
statistics_dict = statistics_instance.to_dict()
# create an instance of Statistics from a dict
statistics_form_dict = statistics.from_dict(statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


