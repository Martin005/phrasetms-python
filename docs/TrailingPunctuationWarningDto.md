# TrailingPunctuationWarningDto

## Properties

| Name                    | Type                        | Description | Notes      |
| ----------------------- | --------------------------- | ----------- | ---------- |
| **src_position**        | [**Position**](Position.md) |             | [optional] |
| **src_end_punctuation** | **str**                     |             | [optional] |
| **tgt_position**        | [**Position**](Position.md) |             | [optional] |
| **tgt_end_punctuation** | **str**                     |             | [optional] |

## Example

```python
from phrasetms_client.models.trailing_punctuation_warning_dto import TrailingPunctuationWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of TrailingPunctuationWarningDto from a JSON string
trailing_punctuation_warning_dto_instance = TrailingPunctuationWarningDto.from_json(json)
# print the JSON string representation of the object
print TrailingPunctuationWarningDto.to_json()

# convert the object into a dict
trailing_punctuation_warning_dto_dict = trailing_punctuation_warning_dto_instance.to_dict()
# create an instance of TrailingPunctuationWarningDto from a dict
trailing_punctuation_warning_dto_from_dict = TrailingPunctuationWarningDto.from_dict(trailing_punctuation_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
