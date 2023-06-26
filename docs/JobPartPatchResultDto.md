# JobPartPatchResultDto

## Properties

| Name        | Type                                              | Description                                           | Notes      |
| ----------- | ------------------------------------------------- | ----------------------------------------------------- | ---------- |
| **updated** | **int**                                           | Number of successfully updated job parts              | [optional] |
| **errors**  | [**List[ErrorDetailDtoV3]**](ErrorDetailDtoV3.md) | Errors and their counts encountered during the update | [optional] |

## Example

```python
from phrasetms_client.models.job_part_patch_result_dto import JobPartPatchResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartPatchResultDto from a JSON string
job_part_patch_result_dto_instance = JobPartPatchResultDto.from_json(json)
# print the JSON string representation of the object
print JobPartPatchResultDto.to_json()

# convert the object into a dict
job_part_patch_result_dto_dict = job_part_patch_result_dto_instance.to_dict()
# create an instance of JobPartPatchResultDto from a dict
job_part_patch_result_dto_from_dict = JobPartPatchResultDto.from_dict(job_part_patch_result_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
