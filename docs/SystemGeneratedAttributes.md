# SystemGeneratedAttributes

5.2.2 Common members.   For grouping the subschemas of system-generated temporal attributes: createdAt, modifiedAt, and deletedAt. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] [readonly] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] [readonly] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 

## Example

```python
from ngsi_ld_client.models.system_generated_attributes import SystemGeneratedAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SystemGeneratedAttributes from a JSON string
system_generated_attributes_instance = SystemGeneratedAttributes.from_json(json)
# print the JSON string representation of the object
print(SystemGeneratedAttributes.to_json())

# convert the object into a dict
system_generated_attributes_dict = system_generated_attributes_instance.to_dict()
# create an instance of SystemGeneratedAttributes from a dict
system_generated_attributes_from_dict = SystemGeneratedAttributes.from_dict(system_generated_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


