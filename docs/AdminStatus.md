# AdminStatus

NGSI-LD Property Type. The desired state of the interface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | 
**value** | [**AdminStatusOptions**](AdminStatusOptions.md) |  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 

## Example

```python
from ngsi_ld_client.models.admin_status import AdminStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AdminStatus from a JSON string
admin_status_instance = AdminStatus.from_json(json)
# print the JSON string representation of the object
print AdminStatus.to_json()

# convert the object into a dict
admin_status_dict = admin_status_instance.to_dict()
# create an instance of AdminStatus from a dict
admin_status_form_dict = admin_status.from_dict(admin_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


