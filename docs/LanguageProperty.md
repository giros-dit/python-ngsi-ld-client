# LanguageProperty

5.2.32 NGSI-LD LanguageProperty. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'LanguageProperty']
**language_map** | **object** | String Property Values defined in multiple natural languages.  | [optional] 
**observed_at** | **datetime** | Timestamp. See clause 4.8.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 
**previous_language_map** | **object** | Previous Language Property languageMap. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_client.models.language_property import LanguageProperty

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageProperty from a JSON string
language_property_instance = LanguageProperty.from_json(json)
# print the JSON string representation of the object
print(LanguageProperty.to_json())

# convert the object into a dict
language_property_dict = language_property_instance.to_dict()
# create an instance of LanguageProperty from a dict
language_property_from_dict = LanguageProperty.from_dict(language_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


