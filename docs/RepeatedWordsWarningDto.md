# RepeatedWordsWarningDto

## Properties

| Name               | Type          | Description | Notes      |
| ------------------ | ------------- | ----------- | ---------- |
| **repeated_words** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.repeated_words_warning_dto import RepeatedWordsWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of RepeatedWordsWarningDto from a JSON string
repeated_words_warning_dto_instance = RepeatedWordsWarningDto.from_json(json)
# print the JSON string representation of the object
print RepeatedWordsWarningDto.to_json()

# convert the object into a dict
repeated_words_warning_dto_dict = repeated_words_warning_dto_instance.to_dict()
# create an instance of RepeatedWordsWarningDto from a dict
repeated_words_warning_dto_from_dict = RepeatedWordsWarningDto.from_dict(repeated_words_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
