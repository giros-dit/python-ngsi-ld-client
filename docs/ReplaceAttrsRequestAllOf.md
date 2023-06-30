# ReplaceAttrsRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'LanguageProperty']
**value** | [**Geometry**](Geometry.md) |  | [optional] 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 
**previous_value** | [**PropertyPreviousValue**](PropertyPreviousValue.md) |  | [optional] 
**object** | **str** | Relationship&#39;s target object.  | [optional] 
**previous_object** | **str** | Previous Relationship&#39;s target object. Only used in notifications.  | [optional] [readonly] 
**additional_properties** | [**EntityAdditionalProperties**](EntityAdditionalProperties.md) |  | [optional] 
**language_map** | **object** | String Property Values defined in multiple natural languages.  | [optional] 
**previous_language_map** | **object** | Previous Language Property languageMap. Only used in notifications.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_client.models.replace_attrs_request_all_of import ReplaceAttrsRequestAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceAttrsRequestAllOf from a JSON string
replace_attrs_request_all_of_instance = ReplaceAttrsRequestAllOf.from_json(json)
# print the JSON string representation of the object
print ReplaceAttrsRequestAllOf.to_json()

# convert the object into a dict
replace_attrs_request_all_of_dict = replace_attrs_request_all_of_instance.to_dict()
# create an instance of ReplaceAttrsRequestAllOf from a dict
replace_attrs_request_all_of_form_dict = replace_attrs_request_all_of.from_dict(replace_attrs_request_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

