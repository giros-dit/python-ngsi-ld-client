# VocabularyPropertyVocab

String Values which shall be type coerced to URIs based on the supplied @context. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_client.models.vocabulary_property_vocab import VocabularyPropertyVocab

# TODO update the JSON string below
json = "{}"
# create an instance of VocabularyPropertyVocab from a JSON string
vocabulary_property_vocab_instance = VocabularyPropertyVocab.from_json(json)
# print the JSON string representation of the object
print(VocabularyPropertyVocab.to_json())

# convert the object into a dict
vocabulary_property_vocab_dict = vocabulary_property_vocab_instance.to_dict()
# create an instance of VocabularyPropertyVocab from a dict
vocabulary_property_vocab_from_dict = VocabularyPropertyVocab.from_dict(vocabulary_property_vocab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


