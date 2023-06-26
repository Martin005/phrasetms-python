# HumanTranslateJobsDto

## Properties

| Name                          | Type                                      | Description | Notes      |
| ----------------------------- | ----------------------------------------- | ----------- | ---------- |
| **jobs**                      | [**List[UidReference]**](UidReference.md) |             |
| **human_translate_settings**  | [**IdReference**](IdReference.md)         |             |
| **comment**                   | **str**                                   |             | [optional] |
| **glossary_id**               | **str**                                   |             | [optional] |
| **use_preferred_translators** | **bool**                                  |             | [optional] |
| **level**                     | **str**                                   |             | [optional] |
| **callback_url**              | **str**                                   |             | [optional] |

## Example

```python
from phrasetms_client.models.human_translate_jobs_dto import HumanTranslateJobsDto

# TODO update the JSON string below
json = "{}"
# create an instance of HumanTranslateJobsDto from a JSON string
human_translate_jobs_dto_instance = HumanTranslateJobsDto.from_json(json)
# print the JSON string representation of the object
print HumanTranslateJobsDto.to_json()

# convert the object into a dict
human_translate_jobs_dto_dict = human_translate_jobs_dto_instance.to_dict()
# create an instance of HumanTranslateJobsDto from a dict
human_translate_jobs_dto_from_dict = HumanTranslateJobsDto.from_dict(human_translate_jobs_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
