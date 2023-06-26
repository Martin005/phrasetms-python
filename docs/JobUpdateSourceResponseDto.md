# JobUpdateSourceResponseDto

## Properties

| Name              | Type                                                          | Description | Notes      |
| ----------------- | ------------------------------------------------------------- | ----------- | ---------- |
| **async_request** | [**AsyncRequestReference**](AsyncRequestReference.md)         |             | [optional] |
| **jobs**          | [**List[JobPartUpdateSourceDto]**](JobPartUpdateSourceDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_update_source_response_dto import JobUpdateSourceResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobUpdateSourceResponseDto from a JSON string
job_update_source_response_dto_instance = JobUpdateSourceResponseDto.from_json(json)
# print the JSON string representation of the object
print JobUpdateSourceResponseDto.to_json()

# convert the object into a dict
job_update_source_response_dto_dict = job_update_source_response_dto_instance.to_dict()
# create an instance of JobUpdateSourceResponseDto from a dict
job_update_source_response_dto_from_dict = JobUpdateSourceResponseDto.from_dict(job_update_source_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
