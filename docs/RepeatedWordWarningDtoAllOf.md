# RepeatedWordWarningDtoAllOf

## Properties

| Name          | Type                              | Description | Notes      |
| ------------- | --------------------------------- | ----------- | ---------- |
| **word**      | **str**                           |             | [optional] |
| **positions** | [**List[Position]**](Position.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.repeated_word_warning_dto_all_of import RepeatedWordWarningDtoAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of RepeatedWordWarningDtoAllOf from a JSON string
repeated_word_warning_dto_all_of_instance = RepeatedWordWarningDtoAllOf.from_json(json)
# print the JSON string representation of the object
print RepeatedWordWarningDtoAllOf.to_json()

# convert the object into a dict
repeated_word_warning_dto_all_of_dict = repeated_word_warning_dto_all_of_instance.to_dict()
# create an instance of RepeatedWordWarningDtoAllOf from a dict
repeated_word_warning_dto_all_of_from_dict = RepeatedWordWarningDtoAllOf.from_dict(repeated_word_warning_dto_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
