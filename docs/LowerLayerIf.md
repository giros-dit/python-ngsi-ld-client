# LowerLayerIf

NGSI-LD Relationship Type. A list of references to interfaces layered underneath of this interface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | 
**object** | **str** |  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 

## Example

```python
from ngsi_ld_client.models.lower_layer_if import LowerLayerIf

# TODO update the JSON string below
json = "{}"
# create an instance of LowerLayerIf from a JSON string
lower_layer_if_instance = LowerLayerIf.from_json(json)
# print the JSON string representation of the object
print LowerLayerIf.to_json()

# convert the object into a dict
lower_layer_if_dict = lower_layer_if_instance.to_dict()
# create an instance of LowerLayerIf from a dict
lower_layer_if_form_dict = lower_layer_if.from_dict(lower_layer_if_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


