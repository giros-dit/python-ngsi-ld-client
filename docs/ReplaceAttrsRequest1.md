# ReplaceAttrsRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**LdContext**](LdContext.md) |  | 
**type** | **str** | Node type.  | [optional] [default to 'LanguageProperty']
**value** | [**Geometry**](Geometry.md) | Geolocation encoded as GeoJSON. As mandated by clause 4.7.  | [optional] 
**observed_at** | **datetime** | Timestamp. See clause 4.8.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 
**previous_value** | [**GeoPropertyPreviousValue**](GeoPropertyPreviousValue.md) |  | [optional] 
**object** | **str** | Relationship&#39;s target object.  | [optional] 
**previous_object** | **str** | Previous Relationship&#39;s target object. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 
**language_map** | **object** | String Property Values defined in multiple natural languages.  | [optional] 
**previous_language_map** | **object** | Previous Language Property languageMap. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_client.models.replace_attrs_request1 import ReplaceAttrsRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceAttrsRequest1 from a JSON string
replace_attrs_request1_instance = ReplaceAttrsRequest1.from_json(json)
# print the JSON string representation of the object
print(ReplaceAttrsRequest1.to_json())

# convert the object into a dict
replace_attrs_request1_dict = replace_attrs_request1_instance.to_dict()
# create an instance of ReplaceAttrsRequest1 from a dict
replace_attrs_request1_from_dict = ReplaceAttrsRequest1.from_dict(replace_attrs_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


