# CreateEntityRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | 
**type** | [**EntityType**](EntityType.md) |  | 
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**additional_properties** | [**EntityAdditionalProperties**](EntityAdditionalProperties.md) |  | [optional] 

## Example

```python
from ngsi_ld_client.models.create_entity_request import CreateEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntityRequest from a JSON string
create_entity_request_instance = CreateEntityRequest.from_json(json)
# print the JSON string representation of the object
print CreateEntityRequest.to_json()

# convert the object into a dict
create_entity_request_dict = create_entity_request_instance.to_dict()
# create an instance of CreateEntityRequest from a dict
create_entity_request_form_dict = create_entity_request.from_dict(create_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


