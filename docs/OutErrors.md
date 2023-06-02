# OutErrors

NGSI-LD Property Type. For packet-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character-oriented or fixed-length interfaces, the number of outbound transmission units that could not be transmitted because of errors. 

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
from ngsi_ld_client.models.out_errors import OutErrors

# TODO update the JSON string below
json = "{}"
# create an instance of OutErrors from a JSON string
out_errors_instance = OutErrors.from_json(json)
# print the JSON string representation of the object
print OutErrors.to_json()

# convert the object into a dict
out_errors_dict = out_errors_instance.to_dict()
# create an instance of OutErrors from a dict
out_errors_form_dict = out_errors.from_dict(out_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


