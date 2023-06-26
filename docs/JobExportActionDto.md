# JobExportActionDto

## Properties

| Name     | Type                                      | Description | Notes |
| -------- | ----------------------------------------- | ----------- | ----- |
| **jobs** | [**List[UidReference]**](UidReference.md) |             |

## Example

```python
from phrasetms_client.models.job_export_action_dto import JobExportActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobExportActionDto from a JSON string
job_export_action_dto_instance = JobExportActionDto.from_json(json)
# print the JSON string representation of the object
print JobExportActionDto.to_json()

# convert the object into a dict
job_export_action_dto_dict = job_export_action_dto_instance.to_dict()
# create an instance of JobExportActionDto from a dict
job_export_action_dto_from_dict = JobExportActionDto.from_dict(job_export_action_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
