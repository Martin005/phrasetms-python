# JobMachineTranslationSettingsDto

Machine translation related settings

## Properties

| Name                           | Type     | Description                                                                                            | Notes      |
| ------------------------------ | -------- | ------------------------------------------------------------------------------------------------------ | ---------- |
| **use_machine_translation**    | **bool** | Pre-translate from machine translation. Default: true                                                  | [optional] |
| **lock100_percent_matches**    | **bool** | Lock section: 100% machine translation matches. Default: false                                         | [optional] |
| **confirm100_percent_matches** | **bool** | Set segment status to confirmed for: 100% translation machine matches. Default: false                  | [optional] |
| **use_alt_trans_only**         | **bool** | Do not put machine translations to target and use alt-trans fields (alt-trans in mxlf). Default: false | [optional] |

## Example

```python
from phrasetms_client.models.job_machine_translation_settings_dto import JobMachineTranslationSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobMachineTranslationSettingsDto from a JSON string
job_machine_translation_settings_dto_instance = JobMachineTranslationSettingsDto.from_json(json)
# print the JSON string representation of the object
print JobMachineTranslationSettingsDto.to_json()

# convert the object into a dict
job_machine_translation_settings_dto_dict = job_machine_translation_settings_dto_instance.to_dict()
# create an instance of JobMachineTranslationSettingsDto from a dict
job_machine_translation_settings_dto_from_dict = JobMachineTranslationSettingsDto.from_dict(job_machine_translation_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
