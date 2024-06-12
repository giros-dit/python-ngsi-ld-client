# Relationship

5.2.6 NGSI-LD Relationship. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Relationship']
**object** | **str** | Relationship&#39;s target object.  | [optional] 
**observed_at** | **datetime** | Timestamp. See clause 4.8.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Relationship instance (see clause 4.5.8). System generated.  | [optional] [readonly] 
**previous_object** | **str** | Previous Relationship&#39;s target object. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_client.models.relationship import Relationship

# TODO update the JSON string below
json = "{}"
# create an instance of Relationship from a JSON string
relationship_instance = Relationship.from_json(json)
# print the JSON string representation of the object
print(Relationship.to_json())

# convert the object into a dict
relationship_dict = relationship_instance.to_dict()
# create an instance of Relationship from a dict
relationship_from_dict = Relationship.from_dict(relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


