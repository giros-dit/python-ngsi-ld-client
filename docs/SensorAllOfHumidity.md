# SensorAllOfHumidity

NGSI-LD Property Type. The humidity measurement.

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
from ngsi_ld_client.models.sensor_all_of_humidity import SensorAllOfHumidity

# TODO update the JSON string below
json = "{}"
# create an instance of SensorAllOfHumidity from a JSON string
sensor_all_of_humidity_instance = SensorAllOfHumidity.from_json(json)
# print the JSON string representation of the object
print SensorAllOfHumidity.to_json()

# convert the object into a dict
sensor_all_of_humidity_dict = sensor_all_of_humidity_instance.to_dict()
# create an instance of SensorAllOfHumidity from a dict
sensor_all_of_humidity_form_dict = sensor_all_of_humidity.from_dict(sensor_all_of_humidity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

