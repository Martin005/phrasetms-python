# SpellCheckWarningDtoAllOf

## Properties

| Name                 | Type                                                | Description | Notes      |
| -------------------- | --------------------------------------------------- | ----------- | ---------- |
| **misspelled_words** | [**List[MisspelledWordDto]**](MisspelledWordDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.spell_check_warning_dto_all_of import SpellCheckWarningDtoAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SpellCheckWarningDtoAllOf from a JSON string
spell_check_warning_dto_all_of_instance = SpellCheckWarningDtoAllOf.from_json(json)
# print the JSON string representation of the object
print SpellCheckWarningDtoAllOf.to_json()

# convert the object into a dict
spell_check_warning_dto_all_of_dict = spell_check_warning_dto_all_of_instance.to_dict()
# create an instance of SpellCheckWarningDtoAllOf from a dict
spell_check_warning_dto_all_of_from_dict = SpellCheckWarningDtoAllOf.from_dict(spell_check_warning_dto_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
