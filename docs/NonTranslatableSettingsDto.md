# NonTranslatableSettingsDto

Non-translatables related settings

## Properties

| Name                                | Type     | Description                                                                        | Notes      |
| ----------------------------------- | -------- | ---------------------------------------------------------------------------------- | ---------- |
| **pre_translate_non_translatables** | **bool** | Pre-translate non-translatables. Default: false                                    | [optional] |
| **confirm100_percent_matches**      | **bool** | Set segment status to confirmed for: 100% non-translatable matches. Default: false | [optional] |
| **lock100_percent_matches**         | **bool** | Lock section: 100% non-translatable matches. Default: false                        | [optional] |
| **non_translatables_in_editors**    | **bool** | If non-translatables are enabled in Editors.                                       | [optional] |

## Example

```python
from phrasetms_client.models.non_translatable_settings_dto import NonTranslatableSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of NonTranslatableSettingsDto from a JSON string
non_translatable_settings_dto_instance = NonTranslatableSettingsDto.from_json(json)
# print the JSON string representation of the object
print NonTranslatableSettingsDto.to_json()

# convert the object into a dict
non_translatable_settings_dto_dict = non_translatable_settings_dto_instance.to_dict()
# create an instance of NonTranslatableSettingsDto from a dict
non_translatable_settings_dto_from_dict = NonTranslatableSettingsDto.from_dict(non_translatable_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
