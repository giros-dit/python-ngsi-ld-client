# LinkUpDownTrapEnable

NGSI-LD Property Type. Controls whether linkUp/linkDown SNMP notifications should be generated for this interface.

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
from ngsi_ld_client.models.link_up_down_trap_enable import LinkUpDownTrapEnable

# TODO update the JSON string below
json = "{}"
# create an instance of LinkUpDownTrapEnable from a JSON string
link_up_down_trap_enable_instance = LinkUpDownTrapEnable.from_json(json)
# print the JSON string representation of the object
print LinkUpDownTrapEnable.to_json()

# convert the object into a dict
link_up_down_trap_enable_dict = link_up_down_trap_enable_instance.to_dict()
# create an instance of LinkUpDownTrapEnable from a dict
link_up_down_trap_enable_form_dict = link_up_down_trap_enable.from_dict(link_up_down_trap_enable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


