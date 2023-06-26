# JobPartStatusChangesDto

## Properties

| Name               | Type                                                          | Description | Notes      |
| ------------------ | ------------------------------------------------------------- | ----------- | ---------- |
| **status_changes** | [**List[JobPartStatusChangeDto]**](JobPartStatusChangeDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_part_status_changes_dto import JobPartStatusChangesDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartStatusChangesDto from a JSON string
job_part_status_changes_dto_instance = JobPartStatusChangesDto.from_json(json)
# print the JSON string representation of the object
print JobPartStatusChangesDto.to_json()

# convert the object into a dict
job_part_status_changes_dto_dict = job_part_status_changes_dto_instance.to_dict()
# create an instance of JobPartStatusChangesDto from a dict
job_part_status_changes_dto_from_dict = JobPartStatusChangesDto.from_dict(job_part_status_changes_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
