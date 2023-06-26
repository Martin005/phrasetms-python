# PreTranslateJobsV2Dto

## Properties

| Name                                   | Type                                                            | Description                                                                                                             | Notes      |
| -------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------- |
| **jobs**                               | [**List[UidReference]**](UidReference.md)                       | Jobs to be pre-translated                                                                                               |
| **segment_filters**                    | **List[str]**                                                   |                                                                                                                         | [optional] |
| **use_project_pre_translate_settings** | **bool**                                                        | If pre-translate settings from project should be used. If true, preTranslateSettings values are ignored. Default: false | [optional] |
| **callback_url**                       | **str**                                                         |                                                                                                                         | [optional] |
| **pre_translate_settings**             | [**PreTranslateJobSettingsDto**](PreTranslateJobSettingsDto.md) |                                                                                                                         | [optional] |

## Example

```python
from phrasetms_client.models.pre_translate_jobs_v2_dto import PreTranslateJobsV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of PreTranslateJobsV2Dto from a JSON string
pre_translate_jobs_v2_dto_instance = PreTranslateJobsV2Dto.from_json(json)
# print the JSON string representation of the object
print PreTranslateJobsV2Dto.to_json()

# convert the object into a dict
pre_translate_jobs_v2_dto_dict = pre_translate_jobs_v2_dto_instance.to_dict()
# create an instance of PreTranslateJobsV2Dto from a dict
pre_translate_jobs_v2_dto_from_dict = PreTranslateJobsV2Dto.from_dict(pre_translate_jobs_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
