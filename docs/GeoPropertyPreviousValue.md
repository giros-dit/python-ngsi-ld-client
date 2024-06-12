# GeoPropertyPreviousValue

Previous GeoProperty value. Only used in notifications, if the showChanges  option is explicitly requested. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | [**List[GeometryLineString]**](GeometryLineString.md) |  | [optional] 

## Example

```python
from ngsi_ld_client.models.geo_property_previous_value import GeoPropertyPreviousValue

# TODO update the JSON string below
json = "{}"
# create an instance of GeoPropertyPreviousValue from a JSON string
geo_property_previous_value_instance = GeoPropertyPreviousValue.from_json(json)
# print the JSON string representation of the object
print(GeoPropertyPreviousValue.to_json())

# convert the object into a dict
geo_property_previous_value_dict = geo_property_previous_value_instance.to_dict()
# create an instance of GeoPropertyPreviousValue from a dict
geo_property_previous_value_from_dict = GeoPropertyPreviousValue.from_dict(geo_property_previous_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


