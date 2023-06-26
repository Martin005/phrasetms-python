# SpellCheckResponseDto

## Properties

| Name                    | Type                                        | Description | Notes      |
| ----------------------- | ------------------------------------------- | ----------- | ---------- |
| **spell_check_results** | [**List[CheckResponse]**](CheckResponse.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.spell_check_response_dto import SpellCheckResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SpellCheckResponseDto from a JSON string
spell_check_response_dto_instance = SpellCheckResponseDto.from_json(json)
# print the JSON string representation of the object
print SpellCheckResponseDto.to_json()

# convert the object into a dict
spell_check_response_dto_dict = spell_check_response_dto_instance.to_dict()
# create an instance of SpellCheckResponseDto from a dict
spell_check_response_dto_from_dict = SpellCheckResponseDto.from_dict(spell_check_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
