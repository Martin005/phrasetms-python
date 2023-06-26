# JobPartPatchBatchDto

## Properties

| Name               | Type                                                | Description | Notes      |
| ------------------ | --------------------------------------------------- | ----------- | ---------- |
| **jobs**           | [**List[UidReference]**](UidReference.md)           |             |
| **status**         | **str**                                             |             | [optional] |
| **date_due**       | **datetime**                                        |             | [optional] |
| **clear_date_due** | **bool**                                            |             | [optional] |
| **providers**      | [**List[ProviderReference]**](ProviderReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_part_patch_batch_dto import JobPartPatchBatchDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartPatchBatchDto from a JSON string
job_part_patch_batch_dto_instance = JobPartPatchBatchDto.from_json(json)
# print the JSON string representation of the object
print JobPartPatchBatchDto.to_json()

# convert the object into a dict
job_part_patch_batch_dto_dict = job_part_patch_batch_dto_instance.to_dict()
# create an instance of JobPartPatchBatchDto from a dict
job_part_patch_batch_dto_from_dict = JobPartPatchBatchDto.from_dict(job_part_patch_batch_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
