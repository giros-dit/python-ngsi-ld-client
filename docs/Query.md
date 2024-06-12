# Query

5.2.23 This datatype represents the information that is required in order to convey a query when a \"Query Entities\" operation is to be performed (as per clause 5.7.2). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | JSON-LD @type.  | 
**entities** | [**List[EntitySelector]**](EntitySelector.md) | Entity ids, id pattern and Entity types that shall be matched by Entities in order to be retrieved.  | [optional] 
**attrs** | **List[str]** | List of Attributes that shall be matched by Entities in order to be retrieved. If not present all Attributes will be retrieved.  | [optional] 
**q** | **str** | Query that shall be matched by Entities in order to be retrieved.  | [optional] 
**geo_q** | [**GeoQuery**](GeoQuery.md) | Geoquery that shall be matched by Entities in order be retrieved.  | [optional] 
**csf** | **str** | Context source filter that shall be matched by Context Source Registrations describing Context Sources to be used for retrieving Entities.  | [optional] 
**scope_q** | **str** | Scope query. | [optional] 
**lang** | **str** | Language filter to be applied to the query (clause 4.15). | [optional] 

## Example

```python
from ngsi_ld_client.models.query import Query

# TODO update the JSON string below
json = "{}"
# create an instance of Query from a JSON string
query_instance = Query.from_json(json)
# print the JSON string representation of the object
print(Query.to_json())

# convert the object into a dict
query_dict = query_instance.to_dict()
# create an instance of Query from a dict
query_from_dict = Query.from_dict(query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


