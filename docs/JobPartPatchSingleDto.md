# JobPartPatchSingleDto

## Properties

| Name          | Type                                                | Description | Notes      |
| ------------- | --------------------------------------------------- | ----------- | ---------- |
| **status**    | **str**                                             |             | [optional] |
| **date_due**  | **datetime**                                        |             | [optional] |
| **providers** | [**List[ProviderReference]**](ProviderReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_part_patch_single_dto import JobPartPatchSingleDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartPatchSingleDto from a JSON string
job_part_patch_single_dto_instance = JobPartPatchSingleDto.from_json(json)
# print the JSON string representation of the object
print JobPartPatchSingleDto.to_json()

# convert the object into a dict
job_part_patch_single_dto_dict = job_part_patch_single_dto_instance.to_dict()
# create an instance of JobPartPatchSingleDto from a dict
job_part_patch_single_dto_from_dict = JobPartPatchSingleDto.from_dict(job_part_patch_single_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
