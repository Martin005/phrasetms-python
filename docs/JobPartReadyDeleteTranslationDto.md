# JobPartReadyDeleteTranslationDto

## Properties

| Name                | Type                                                                                    | Description                                                                                                       | Notes      |
| ------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------- |
| **jobs**            | [**List[UidReference]**](UidReference.md)                                               |                                                                                                                   | [optional] |
| **delete_settings** | [**TranslationSegmentsReferenceV2**](TranslationSegmentsReferenceV2.md)                 |                                                                                                                   | [optional] |
| **for_all_jobs**    | **bool**                                                                                | Set true if you want to delete translations for all jobs from project from specific workflow step. Default: false | [optional] |
| **workflow_level**  | **int**                                                                                 | Specifies workflow level for all jobs                                                                             | [optional] |
| **filter**          | [**JobPartReadyDeleteTranslationFilterDto**](JobPartReadyDeleteTranslationFilterDto.md) |                                                                                                                   | [optional] |
| **get_parts**       | **object**                                                                              |                                                                                                                   | [optional] |

## Example

```python
from phrasetms_client.models.job_part_ready_delete_translation_dto import JobPartReadyDeleteTranslationDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartReadyDeleteTranslationDto from a JSON string
job_part_ready_delete_translation_dto_instance = JobPartReadyDeleteTranslationDto.from_json(json)
# print the JSON string representation of the object
print JobPartReadyDeleteTranslationDto.to_json()

# convert the object into a dict
job_part_ready_delete_translation_dto_dict = job_part_ready_delete_translation_dto_instance.to_dict()
# create an instance of JobPartReadyDeleteTranslationDto from a dict
job_part_ready_delete_translation_dto_from_dict = JobPartReadyDeleteTranslationDto.from_dict(job_part_ready_delete_translation_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
