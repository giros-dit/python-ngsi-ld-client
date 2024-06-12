# Feature

5.2.29 This data type represents a spatially bounded Entity in GeoJSON format, as mandated by IETF RFC 7946. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | 
**type** | **str** | GeoJSON Type.  | 
**geometry** | [**Geometry**](Geometry.md) | Null if no matching GeoProperty.  | 
**properties** | [**FeatureProperties**](FeatureProperties.md) | List of attributes as mandated by clause 5.2.31.  | 
**context** | [**LdContext**](LdContext.md) | JSON-LD @context. This field is only present if requested in the payload by the HTTP Prefer Header (IETF RFC 7240).  | [optional] 

## Example

```python
from ngsi_ld_client.models.feature import Feature

# TODO update the JSON string below
json = "{}"
# create an instance of Feature from a JSON string
feature_instance = Feature.from_json(json)
# print the JSON string representation of the object
print(Feature.to_json())

# convert the object into a dict
feature_dict = feature_instance.to_dict()
# create an instance of Feature from a dict
feature_from_dict = Feature.from_dict(feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


