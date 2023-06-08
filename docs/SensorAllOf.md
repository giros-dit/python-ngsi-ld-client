# SensorAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**SensorAllOfName**](SensorAllOfName.md) |  | [optional] 
**description** | [**SensorAllOfDescription**](SensorAllOfDescription.md) |  | [optional] 
**temperature** | [**SensorAllOfTemperature**](SensorAllOfTemperature.md) |  | [optional] 
**humidity** | [**SensorAllOfHumidity**](SensorAllOfHumidity.md) |  | [optional] 

## Example

```python
from ngsi_ld_client.models.sensor_all_of import SensorAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SensorAllOf from a JSON string
sensor_all_of_instance = SensorAllOf.from_json(json)
# print the JSON string representation of the object
print SensorAllOf.to_json()

# convert the object into a dict
sensor_all_of_dict = sensor_all_of_instance.to_dict()
# create an instance of SensorAllOf from a dict
sensor_all_of_form_dict = sensor_all_of.from_dict(sensor_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


