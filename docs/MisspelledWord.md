# MisspelledWord

## Properties

| Name       | Type    | Description | Notes      |
| ---------- | ------- | ----------- | ---------- |
| **word**   | **str** |             | [optional] |
| **offset** | **int** |             | [optional] |

## Example

```python
from phrasetms_client.models.misspelled_word import MisspelledWord

# TODO update the JSON string below
json = "{}"
# create an instance of MisspelledWord from a JSON string
misspelled_word_instance = MisspelledWord.from_json(json)
# print the JSON string representation of the object
print MisspelledWord.to_json()

# convert the object into a dict
misspelled_word_dict = misspelled_word_instance.to_dict()
# create an instance of MisspelledWord from a dict
misspelled_word_from_dict = MisspelledWord.from_dict(misspelled_word_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
