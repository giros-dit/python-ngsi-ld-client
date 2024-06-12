# VocabularyProperty

5.2.35 NGSI-LD VocabularyProperty. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'VocabularyProperty']
**vocab** | [**VocabularyPropertyVocab**](VocabularyPropertyVocab.md) |  | [optional] 
**previous_vocab** | [**VocabularyPropertyPreviousVocab**](VocabularyPropertyPreviousVocab.md) |  | [optional] 
**observed_at** | **datetime** | Timestamp. See clause 4.8.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_client.models.vocabulary_property import VocabularyProperty

# TODO update the JSON string below
json = "{}"
# create an instance of VocabularyProperty from a JSON string
vocabulary_property_instance = VocabularyProperty.from_json(json)
# print the JSON string representation of the object
print(VocabularyProperty.to_json())

# convert the object into a dict
vocabulary_property_dict = vocabulary_property_instance.to_dict()
# create an instance of VocabularyProperty from a dict
vocabulary_property_from_dict = VocabularyProperty.from_dict(vocabulary_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


