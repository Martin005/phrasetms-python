# BackgroundTasksTmDto

## Properties

| Name                     | Type                                        | Description | Notes      |
| ------------------------ | ------------------------------------------- | ----------- | ---------- |
| **status**               | **str**                                     |             | [optional] |
| **finished_data_text**   | **str**                                     |             | [optional] |
| **async_request**        | [**AsyncRequestDto**](AsyncRequestDto.md)   |             | [optional] |
| **last_task_string**     | **str**                                     |             | [optional] |
| **metadata**             | [**MetadataResponse**](MetadataResponse.md) |             | [optional] |
| **last_task_ok**         | **str**                                     |             | [optional] |
| **last_task_error**      | **str**                                     |             | [optional] |
| **last_task_error_html** | **str**                                     |             | [optional] |

## Example

```python
from phrasetms_client.models.background_tasks_tm_dto import BackgroundTasksTmDto

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundTasksTmDto from a JSON string
background_tasks_tm_dto_instance = BackgroundTasksTmDto.from_json(json)
# print the JSON string representation of the object
print BackgroundTasksTmDto.to_json()

# convert the object into a dict
background_tasks_tm_dto_dict = background_tasks_tm_dto_instance.to_dict()
# create an instance of BackgroundTasksTmDto from a dict
background_tasks_tm_dto_from_dict = BackgroundTasksTmDto.from_dict(background_tasks_tm_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
