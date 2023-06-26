# JobPartUpdateBatchDto

## Properties

| Name          | Type                                                | Description | Notes      |
| ------------- | --------------------------------------------------- | ----------- | ---------- |
| **jobs**      | [**List[UidReference]**](UidReference.md)           |             | [optional] |
| **status**    | **str**                                             |             |
| **date_due**  | **datetime**                                        |             | [optional] |
| **providers** | [**List[ProviderReference]**](ProviderReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_part_update_batch_dto import JobPartUpdateBatchDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartUpdateBatchDto from a JSON string
job_part_update_batch_dto_instance = JobPartUpdateBatchDto.from_json(json)
# print the JSON string representation of the object
print JobPartUpdateBatchDto.to_json()

# convert the object into a dict
job_part_update_batch_dto_dict = job_part_update_batch_dto_instance.to_dict()
# create an instance of JobPartUpdateBatchDto from a dict
job_part_update_batch_dto_from_dict = JobPartUpdateBatchDto.from_dict(job_part_update_batch_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
