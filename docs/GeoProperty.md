# GeoProperty

5.2.7 NGSI-LD GeoProperty. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'GeoProperty']
**value** | [**Geometry**](Geometry.md) | Geolocation encoded as GeoJSON. As mandated by clause 4.7.  | [optional] 
**observed_at** | **datetime** | Timestamp. See clause 4.8.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 
**previous_value** | [**GeoPropertyPreviousValue**](GeoPropertyPreviousValue.md) |  | [optional] 

## Example

```python
from ngsi_ld_client.models.geo_property import GeoProperty

# TODO update the JSON string below
json = "{}"
# create an instance of GeoProperty from a JSON string
geo_property_instance = GeoProperty.from_json(json)
# print the JSON string representation of the object
print(GeoProperty.to_json())

# convert the object into a dict
geo_property_dict = geo_property_instance.to_dict()
# create an instance of GeoProperty from a dict
geo_property_from_dict = GeoProperty.from_dict(geo_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


