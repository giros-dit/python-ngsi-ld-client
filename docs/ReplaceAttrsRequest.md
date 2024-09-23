# ReplaceAttrsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | [**Geometry**](Geometry.md) |  | [optional] 
**observed_at** | **datetime** | It is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 
**previous_value** | [**Geometry**](Geometry.md) |  | [optional] 
**object** | **str** | Relationship&#39;s target object.  | [optional] 
**previous_object** | **str** | Previous Relationship&#39;s target object. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 
**language_map** | **object** | String Property Values defined in multiple natural languages.  | [optional] 
**previous_language_map** | **object** | Previous Language Property languageMap. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 
**vocab** | [**VocabularyPropertyVocab**](VocabularyPropertyVocab.md) |  | [optional] 
**previous_vocab** | [**VocabularyPropertyPreviousVocab**](VocabularyPropertyPreviousVocab.md) |  | [optional] 

## Example

```python
from ngsi_ld_client.models.replace_attrs_request import ReplaceAttrsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceAttrsRequest from a JSON string
replace_attrs_request_instance = ReplaceAttrsRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceAttrsRequest.to_json())

# convert the object into a dict
replace_attrs_request_dict = replace_attrs_request_instance.to_dict()
# create an instance of ReplaceAttrsRequest from a dict
replace_attrs_request_from_dict = ReplaceAttrsRequest.from_dict(replace_attrs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


