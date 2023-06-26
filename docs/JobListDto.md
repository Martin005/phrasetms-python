# JobListDto

## Properties

| Name                  | Type                                                  | Description | Notes      |
| --------------------- | ----------------------------------------------------- | ----------- | ---------- |
| **unsupported_files** | **List[str]**                                         |             | [optional] |
| **jobs**              | [**List[JobPartReference]**](JobPartReference.md)     |             | [optional] |
| **async_request**     | [**AsyncRequestReference**](AsyncRequestReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_list_dto import JobListDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobListDto from a JSON string
job_list_dto_instance = JobListDto.from_json(json)
# print the JSON string representation of the object
print JobListDto.to_json()

# convert the object into a dict
job_list_dto_dict = job_list_dto_instance.to_dict()
# create an instance of JobListDto from a dict
job_list_dto_from_dict = JobListDto.from_dict(job_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
