# TrailingPunctuationWarningDtoAllOf

## Properties

| Name                    | Type                        | Description | Notes      |
| ----------------------- | --------------------------- | ----------- | ---------- |
| **src_position**        | [**Position**](Position.md) |             | [optional] |
| **src_end_punctuation** | **str**                     |             | [optional] |
| **tgt_position**        | [**Position**](Position.md) |             | [optional] |
| **tgt_end_punctuation** | **str**                     |             | [optional] |

## Example

```python
from phrasetms_client.models.trailing_punctuation_warning_dto_all_of import TrailingPunctuationWarningDtoAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of TrailingPunctuationWarningDtoAllOf from a JSON string
trailing_punctuation_warning_dto_all_of_instance = TrailingPunctuationWarningDtoAllOf.from_json(json)
# print the JSON string representation of the object
print TrailingPunctuationWarningDtoAllOf.to_json()

# convert the object into a dict
trailing_punctuation_warning_dto_all_of_dict = trailing_punctuation_warning_dto_all_of_instance.to_dict()
# create an instance of TrailingPunctuationWarningDtoAllOf from a dict
trailing_punctuation_warning_dto_all_of_from_dict = TrailingPunctuationWarningDtoAllOf.from_dict(trailing_punctuation_warning_dto_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
