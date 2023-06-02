# PhysAddress

NGSI-LD Property Type. The interface's address at its protocol sub-layer.

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
from ngsi_ld_client.models.phys_address import PhysAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PhysAddress from a JSON string
phys_address_instance = PhysAddress.from_json(json)
# print the JSON string representation of the object
print PhysAddress.to_json()

# convert the object into a dict
phys_address_dict = phys_address_instance.to_dict()
# create an instance of PhysAddress from a dict
phys_address_form_dict = phys_address.from_dict(phys_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


