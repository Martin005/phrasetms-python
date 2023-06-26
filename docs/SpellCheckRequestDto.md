# SpellCheckRequestDto

## Properties

| Name                      | Type          | Description | Notes      |
| ------------------------- | ------------- | ----------- | ---------- |
| **lang**                  | **str**       |             |
| **texts**                 | **List[str]** |             |
| **reference_texts**       | **List[str]** |             | [optional] |
| **zero_length_separator** | **str**       |             | [optional] |

## Example

```python
from phrasetms_client.models.spell_check_request_dto import SpellCheckRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SpellCheckRequestDto from a JSON string
spell_check_request_dto_instance = SpellCheckRequestDto.from_json(json)
# print the JSON string representation of the object
print SpellCheckRequestDto.to_json()

# convert the object into a dict
spell_check_request_dto_dict = spell_check_request_dto_instance.to_dict()
# create an instance of SpellCheckRequestDto from a dict
spell_check_request_dto_from_dict = SpellCheckRequestDto.from_dict(spell_check_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
