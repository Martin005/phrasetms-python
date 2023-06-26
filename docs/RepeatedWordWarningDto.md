# RepeatedWordWarningDto

## Properties

| Name          | Type                              | Description | Notes      |
| ------------- | --------------------------------- | ----------- | ---------- |
| **word**      | **str**                           |             | [optional] |
| **positions** | [**List[Position]**](Position.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.repeated_word_warning_dto import RepeatedWordWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of RepeatedWordWarningDto from a JSON string
repeated_word_warning_dto_instance = RepeatedWordWarningDto.from_json(json)
# print the JSON string representation of the object
print RepeatedWordWarningDto.to_json()

# convert the object into a dict
repeated_word_warning_dto_dict = repeated_word_warning_dto_instance.to_dict()
# create an instance of RepeatedWordWarningDto from a dict
repeated_word_warning_dto_from_dict = RepeatedWordWarningDto.from_dict(repeated_word_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
