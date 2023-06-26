# JobPartStatusChangeDto

## Properties

| Name             | Type                                  | Description | Notes      |
| ---------------- | ------------------------------------- | ----------- | ---------- |
| **status**       | **str**                               |             | [optional] |
| **changed_date** | **datetime**                          |             | [optional] |
| **changed_by**   | [**UserReference**](UserReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_part_status_change_dto import JobPartStatusChangeDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartStatusChangeDto from a JSON string
job_part_status_change_dto_instance = JobPartStatusChangeDto.from_json(json)
# print the JSON string representation of the object
print JobPartStatusChangeDto.to_json()

# convert the object into a dict
job_part_status_change_dto_dict = job_part_status_change_dto_instance.to_dict()
# create an instance of JobPartStatusChangeDto from a dict
job_part_status_change_dto_from_dict = JobPartStatusChangeDto.from_dict(job_part_status_change_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
