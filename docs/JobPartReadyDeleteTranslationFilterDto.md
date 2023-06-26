# JobPartReadyDeleteTranslationFilterDto

## Properties

| Name             | Type                                          | Description | Notes      |
| ---------------- | --------------------------------------------- | ----------- | ---------- |
| **filename**     | **str**                                       |             | [optional] |
| **statuses**     | **List[str]**                                 |             | [optional] |
| **target_lang**  | **str**                                       |             | [optional] |
| **provider**     | [**ProviderReference**](ProviderReference.md) |             | [optional] |
| **owner**        | [**UidReference**](UidReference.md)           |             | [optional] |
| **date_due**     | **datetime**                                  |             | [optional] |
| **due_in_hours** | **int**                                       |             | [optional] |
| **overdue**      | **bool**                                      |             | [optional] |

## Example

```python
from phrasetms_client.models.job_part_ready_delete_translation_filter_dto import JobPartReadyDeleteTranslationFilterDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartReadyDeleteTranslationFilterDto from a JSON string
job_part_ready_delete_translation_filter_dto_instance = JobPartReadyDeleteTranslationFilterDto.from_json(json)
# print the JSON string representation of the object
print JobPartReadyDeleteTranslationFilterDto.to_json()

# convert the object into a dict
job_part_ready_delete_translation_filter_dto_dict = job_part_ready_delete_translation_filter_dto_instance.to_dict()
# create an instance of JobPartReadyDeleteTranslationFilterDto from a dict
job_part_ready_delete_translation_filter_dto_from_dict = JobPartReadyDeleteTranslationFilterDto.from_dict(job_part_ready_delete_translation_filter_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
