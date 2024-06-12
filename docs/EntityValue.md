# EntityValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
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
**vocab** | [**VocabularyPropertyVocab**](VocabularyPropertyVocab.md) |  | [optional] 
**previous_vocab** | [**VocabularyPropertyPreviousVocab**](VocabularyPropertyPreviousVocab.md) |  | [optional] 

## Example

```python
from ngsi_ld_client.models.entity_value import EntityValue

# TODO update the JSON string below
json = "{}"
# create an instance of EntityValue from a JSON string
entity_value_instance = EntityValue.from_json(json)
# print the JSON string representation of the object
print(EntityValue.to_json())

# convert the object into a dict
entity_value_dict = entity_value_instance.to_dict()
# create an instance of EntityValue from a dict
entity_value_from_dict = EntityValue.from_dict(entity_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


