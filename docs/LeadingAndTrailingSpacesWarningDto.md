# LeadingAndTrailingSpacesWarningDto

## Properties

| Name                | Type                            | Description | Notes      |
| ------------------- | ------------------------------- | ----------- | ---------- |
| **src_position**    | [**Position**](Position.md)     |             | [optional] |
| **src_whitespaces** | **str**                         |             | [optional] |
| **tgt_position**    | [**Position**](Position.md)     |             | [optional] |
| **tgt_whitespaces** | **str**                         |             | [optional] |
| **suggestion**      | [**Suggestion**](Suggestion.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.leading_and_trailing_spaces_warning_dto import LeadingAndTrailingSpacesWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of LeadingAndTrailingSpacesWarningDto from a JSON string
leading_and_trailing_spaces_warning_dto_instance = LeadingAndTrailingSpacesWarningDto.from_json(json)
# print the JSON string representation of the object
print LeadingAndTrailingSpacesWarningDto.to_json()

# convert the object into a dict
leading_and_trailing_spaces_warning_dto_dict = leading_and_trailing_spaces_warning_dto_instance.to_dict()
# create an instance of LeadingAndTrailingSpacesWarningDto from a dict
leading_and_trailing_spaces_warning_dto_from_dict = LeadingAndTrailingSpacesWarningDto.from_dict(leading_and_trailing_spaces_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
