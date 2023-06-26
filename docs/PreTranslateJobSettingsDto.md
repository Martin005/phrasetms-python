# PreTranslateJobSettingsDto

Pre-translate settings

## Properties

| Name                                        | Type                                                                        | Description                                                                                                                                                   | Notes      |
| ------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **auto_propagate_repetitions**              | **bool**                                                                    | Propagate repetitions. Default: false                                                                                                                         | [optional] |
| **confirm_repetitions**                     | **bool**                                                                    | Set segment status to confirmed for: Repetitions. Default: false                                                                                              | [optional] |
| **set_job_status_completed**                | **bool**                                                                    | Pre-translate &amp; set job to completed: Set job to completed once pre-translated. Default: false                                                            | [optional] |
| **set_job_status_completed_when_confirmed** | **bool**                                                                    | Pre-translate &amp; set job to completed when all segments confirmed: Set job to completed once pre-translated and all segments are confirmed. Default: false | [optional] |
| **set_project_status_completed**            | **bool**                                                                    | Pre-translate &amp; set job to completed: Set project to completed once all jobs pre-translated. Default: false                                               | [optional] |
| **overwrite_existing_translations**         | **bool**                                                                    | Overwrite existing translations in target segments. Default: false                                                                                            | [optional] |
| **translation_memory_settings**             | [**JobTranslationMemorySettingsDto**](JobTranslationMemorySettingsDto.md)   |                                                                                                                                                               | [optional] |
| **machine_translation_settings**            | [**JobMachineTranslationSettingsDto**](JobMachineTranslationSettingsDto.md) |                                                                                                                                                               | [optional] |
| **non_translatable_settings**               | [**JobNonTranslatableSettingsDto**](JobNonTranslatableSettingsDto.md)       |                                                                                                                                                               | [optional] |

## Example

```python
from phrasetms_client.models.pre_translate_job_settings_dto import PreTranslateJobSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PreTranslateJobSettingsDto from a JSON string
pre_translate_job_settings_dto_instance = PreTranslateJobSettingsDto.from_json(json)
# print the JSON string representation of the object
print PreTranslateJobSettingsDto.to_json()

# convert the object into a dict
pre_translate_job_settings_dto_dict = pre_translate_job_settings_dto_instance.to_dict()
# create an instance of PreTranslateJobSettingsDto from a dict
pre_translate_job_settings_dto_from_dict = PreTranslateJobSettingsDto.from_dict(pre_translate_job_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
