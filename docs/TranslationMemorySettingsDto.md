# TranslationMemorySettingsDto

Translation memory related settings

## Properties

| Name                             | Type      | Description                                                                          | Notes      |
| -------------------------------- | --------- | ------------------------------------------------------------------------------------ | ---------- |
| **use_translation_memory**       | **bool**  | Pre-translate from translation memory. Default: false                                | [optional] |
| **translation_memory_threshold** | **float** | Pre-translation threshold percent                                                    | [optional] |
| **confirm100_percent_matches**   | **bool**  | Set segment status to confirmed for: 100% translation memory matches. Default: false | [optional] |
| **confirm101_percent_matches**   | **bool**  | Set segment status to confirmed for: 101% translation memory matches. Default: false | [optional] |
| **lock100_percent_matches**      | **bool**  | Lock section: 100% translation memory matches. Default: false                        | [optional] |
| **lock101_percent_matches**      | **bool**  | Lock section: 101% translation memory matches. Default: false                        | [optional] |

## Example

```python
from phrasetms_client.models.translation_memory_settings_dto import TranslationMemorySettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationMemorySettingsDto from a JSON string
translation_memory_settings_dto_instance = TranslationMemorySettingsDto.from_json(json)
# print the JSON string representation of the object
print TranslationMemorySettingsDto.to_json()

# convert the object into a dict
translation_memory_settings_dto_dict = translation_memory_settings_dto_instance.to_dict()
# create an instance of TranslationMemorySettingsDto from a dict
translation_memory_settings_dto_from_dict = TranslationMemorySettingsDto.from_dict(translation_memory_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
