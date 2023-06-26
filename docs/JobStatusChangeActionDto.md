# JobStatusChangeActionDto

## Properties

| Name                 | Type     | Description                                                                                                                          | Notes      |
| -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **requested_status** | **str**  |                                                                                                                                      | [optional] |
| **notify_owner**     | **bool** | Default: false; Both project owner and job owner are notified; the parameter is subordinated to notification settings in the project | [optional] |
| **propagate_status** | **bool** | Default: false; Controls both job status and email notifications to previous/next provider                                           | [optional] |

## Example

```python
from phrasetms_client.models.job_status_change_action_dto import JobStatusChangeActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusChangeActionDto from a JSON string
job_status_change_action_dto_instance = JobStatusChangeActionDto.from_json(json)
# print the JSON string representation of the object
print JobStatusChangeActionDto.to_json()

# convert the object into a dict
job_status_change_action_dto_dict = job_status_change_action_dto_instance.to_dict()
# create an instance of JobStatusChangeActionDto from a dict
job_status_change_action_dto_from_dict = JobStatusChangeActionDto.from_dict(job_status_change_action_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
