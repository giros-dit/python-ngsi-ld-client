# Interface

NGSI-LD Entity Type that represents an interface of a model-based network device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | 
**type** | **str** | NGSI-LD Entity identifier. It has to be Interface. | [default to 'Interface']
**scope** | [**EntityCommonScope**](EntityCommonScope.md) |  | [optional] 
**location** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**observation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**operation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**name** | [**Name**](Name.md) |  | 
**description** | [**Description**](Description.md) |  | [optional] 
**enabled** | [**Enabled**](Enabled.md) |  | [optional] 
**link_up_down_trap_enable** | [**LinkUpDownTrapEnable**](LinkUpDownTrapEnable.md) |  | [optional] 
**admin_status** | [**AdminStatus**](AdminStatus.md) |  | 
**oper_status** | [**OperStatus**](OperStatus.md) |  | 
**last_change** | [**LastChange**](LastChange.md) |  | [optional] 
**if_index** | [**IfIndex**](IfIndex.md) |  | 
**phys_address** | [**PhysAddress**](PhysAddress.md) |  | [optional] 
**speed** | [**Speed**](Speed.md) |  | [optional] 
**higher_layer_if** | [**HigherLayerIf**](HigherLayerIf.md) |  | [optional] 
**lower_layer_if** | [**LowerLayerIf**](LowerLayerIf.md) |  | [optional] 

## Example

```python
from ngsi_ld_client.models.interface import Interface

# TODO update the JSON string below
json = "{}"
# create an instance of Interface from a JSON string
interface_instance = Interface.from_json(json)
# print the JSON string representation of the object
print Interface.to_json()

# convert the object into a dict
interface_dict = interface_instance.to_dict()
# create an instance of Interface from a dict
interface_form_dict = interface.from_dict(interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


