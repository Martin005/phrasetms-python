# SpellCheckWarningDto

## Properties

| Name                 | Type                                                | Description | Notes      |
| -------------------- | --------------------------------------------------- | ----------- | ---------- |
| **misspelled_words** | [**List[MisspelledWordDto]**](MisspelledWordDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.spell_check_warning_dto import SpellCheckWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of SpellCheckWarningDto from a JSON string
spell_check_warning_dto_instance = SpellCheckWarningDto.from_json(json)
# print the JSON string representation of the object
print SpellCheckWarningDto.to_json()

# convert the object into a dict
spell_check_warning_dto_dict = spell_check_warning_dto_instance.to_dict()
# create an instance of SpellCheckWarningDto from a dict
spell_check_warning_dto_from_dict = SpellCheckWarningDto.from_dict(spell_check_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
