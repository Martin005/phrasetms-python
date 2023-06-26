# JobNonTranslatableSettingsDto

Non-translatables related settings

## Properties

| Name                                | Type     | Description                                                                        | Notes      |
| ----------------------------------- | -------- | ---------------------------------------------------------------------------------- | ---------- |
| **pre_translate_non_translatables** | **bool** | Pre-translate non-translatables. Default: true                                     | [optional] |
| **confirm100_percent_matches**      | **bool** | Set segment status to confirmed for: 100% non-translatable matches. Default: false | [optional] |
| **lock100_percent_matches**         | **bool** | Lock section: 100% non-translatable matches. Default: false                        | [optional] |

## Example

```python
from phrasetms_client.models.job_non_translatable_settings_dto import JobNonTranslatableSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobNonTranslatableSettingsDto from a JSON string
job_non_translatable_settings_dto_instance = JobNonTranslatableSettingsDto.from_json(json)
# print the JSON string representation of the object
print JobNonTranslatableSettingsDto.to_json()

# convert the object into a dict
job_non_translatable_settings_dto_dict = job_non_translatable_settings_dto_instance.to_dict()
# create an instance of JobNonTranslatableSettingsDto from a dict
job_non_translatable_settings_dto_from_dict = JobNonTranslatableSettingsDto.from_dict(job_non_translatable_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
