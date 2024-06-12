# GeoPropertyValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**observed_at** | **datetime** | Timestamp. See clause 4.8.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Relationship instance (see clause 4.5.8). System generated.  | [optional] [readonly] 
**previous_value** | [**PropertyPreviousValue**](PropertyPreviousValue.md) |  | [optional] 
**object** | **str** | Relationship&#39;s target object.  | [optional] 
**previous_object** | **str** | Previous Relationship&#39;s target object. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_client.models.geo_property_value import GeoPropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of GeoPropertyValue from a JSON string
geo_property_value_instance = GeoPropertyValue.from_json(json)
# print the JSON string representation of the object
print(GeoPropertyValue.to_json())

# convert the object into a dict
geo_property_value_dict = geo_property_value_instance.to_dict()
# create an instance of GeoPropertyValue from a dict
geo_property_value_from_dict = GeoPropertyValue.from_dict(geo_property_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


