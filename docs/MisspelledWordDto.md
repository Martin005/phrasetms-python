# MisspelledWordDto

## Properties

| Name       | Type    | Description | Notes      |
| ---------- | ------- | ----------- | ---------- |
| **word**   | **str** |             | [optional] |
| **offset** | **int** |             | [optional] |

## Example

```python
from phrasetms_client.models.misspelled_word_dto import MisspelledWordDto

# TODO update the JSON string below
json = "{}"
# create an instance of MisspelledWordDto from a JSON string
misspelled_word_dto_instance = MisspelledWordDto.from_json(json)
# print the JSON string representation of the object
print MisspelledWordDto.to_json()

# convert the object into a dict
misspelled_word_dto_dict = misspelled_word_dto_instance.to_dict()
# create an instance of MisspelledWordDto from a dict
misspelled_word_dto_from_dict = MisspelledWordDto.from_dict(misspelled_word_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
