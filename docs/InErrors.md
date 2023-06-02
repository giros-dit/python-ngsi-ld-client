# InErrors

NGSI-LD Property Type. For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character- oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | 
**value** | **int** |  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 

## Example

```python
from ngsi_ld_client.models.in_errors import InErrors

# TODO update the JSON string below
json = "{}"
# create an instance of InErrors from a JSON string
in_errors_instance = InErrors.from_json(json)
# print the JSON string representation of the object
print InErrors.to_json()

# convert the object into a dict
in_errors_dict = in_errors_instance.to_dict()
# create an instance of InErrors from a dict
in_errors_form_dict = in_errors.from_dict(in_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


