# JobExportResponseDto

## Properties

| Name     | Type                                      | Description | Notes      |
| -------- | ----------------------------------------- | ----------- | ---------- |
| **jobs** | [**List[UidReference]**](UidReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_export_response_dto import JobExportResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobExportResponseDto from a JSON string
job_export_response_dto_instance = JobExportResponseDto.from_json(json)
# print the JSON string representation of the object
print JobExportResponseDto.to_json()

# convert the object into a dict
job_export_response_dto_dict = job_export_response_dto_instance.to_dict()
# create an instance of JobExportResponseDto from a dict
job_export_response_dto_from_dict = JobExportResponseDto.from_dict(job_export_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
