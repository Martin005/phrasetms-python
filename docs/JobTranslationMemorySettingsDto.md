# JobTranslationMemorySettingsDto

Translation memory related settings

## Properties

| Name                             | Type      | Description                                                                          | Notes      |
| -------------------------------- | --------- | ------------------------------------------------------------------------------------ | ---------- |
| **use_translation_memory**       | **bool**  | Pre-translate from translation memory. Default: true                                 | [optional] |
| **translation_memory_threshold** | **float** | Pre-translation threshold percent. Default: 0.7                                      | [optional] |
| **confirm100_percent_matches**   | **bool**  | Set segment status to confirmed for: 100% translation memory matches. Default: false | [optional] |
| **confirm101_percent_matches**   | **bool**  | Set segment status to confirmed for: 101% translation memory matches. Default: false | [optional] |
| **lock100_percent_matches**      | **bool**  | Lock section: 100% translation memory matches. Default: false                        | [optional] |
| **lock101_percent_matches**      | **bool**  | Lock section: 101% translation memory matches. Default: false                        | [optional] |

## Example

```python
from phrasetms_client.models.job_translation_memory_settings_dto import JobTranslationMemorySettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobTranslationMemorySettingsDto from a JSON string
job_translation_memory_settings_dto_instance = JobTranslationMemorySettingsDto.from_json(json)
# print the JSON string representation of the object
print JobTranslationMemorySettingsDto.to_json()

# convert the object into a dict
job_translation_memory_settings_dto_dict = job_translation_memory_settings_dto_instance.to_dict()
# create an instance of JobTranslationMemorySettingsDto from a dict
job_translation_memory_settings_dto_from_dict = JobTranslationMemorySettingsDto.from_dict(job_translation_memory_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
