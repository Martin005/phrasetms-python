# MTSettingsPerLanguageDto

## Properties

| Name                           | Type                                                              | Description                                                         | Notes      |
| ------------------------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- | ---------- |
| **target_lang**                | **str**                                                           | mtSettings is set for whole project if targetLang &#x3D;&#x3D; null |
| **machine_translate_settings** | [**MachineTranslateSettingsDto**](MachineTranslateSettingsDto.md) |                                                                     | [optional] |

## Example

```python
from phrasetms_client.models.mt_settings_per_language_dto import MTSettingsPerLanguageDto

# TODO update the JSON string below
json = "{}"
# create an instance of MTSettingsPerLanguageDto from a JSON string
mt_settings_per_language_dto_instance = MTSettingsPerLanguageDto.from_json(json)
# print the JSON string representation of the object
print MTSettingsPerLanguageDto.to_json()

# convert the object into a dict
mt_settings_per_language_dto_dict = mt_settings_per_language_dto_instance.to_dict()
# create an instance of MTSettingsPerLanguageDto from a dict
mt_settings_per_language_dto_from_dict = MTSettingsPerLanguageDto.from_dict(mt_settings_per_language_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
