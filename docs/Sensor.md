# Sensor

NGSI-LD Entity Type that represents an IoT sensor. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | 
**type** | **str** | Entity Type(s). Both short hand string(s) (type name) or URI(s) are allowed.  | 
**scope** | [**EntityCommonScope**](EntityCommonScope.md) |  | [optional] 
**location** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**observation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**operation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**name** | [**SensorAllOfName**](SensorAllOfName.md) |  | 
**description** | [**SensorAllOfDescription**](SensorAllOfDescription.md) |  | 
**temperature** | [**SensorAllOfTemperature**](SensorAllOfTemperature.md) |  | 
**humidity** | [**SensorAllOfHumidity**](SensorAllOfHumidity.md) |  | 

## Example

```python
from ngsi_ld_client.models.sensor import Sensor

# TODO update the JSON string below
json = "{}"
# create an instance of Sensor from a JSON string
sensor_instance = Sensor.from_json(json)
# print the JSON string representation of the object
print Sensor.to_json()

# convert the object into a dict
sensor_dict = sensor_instance.to_dict()
# create an instance of Sensor from a dict
sensor_form_dict = sensor.from_dict(sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


