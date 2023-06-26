# JobPartUpdateSourceDto

## Properties

| Name               | Type                                                  | Description | Notes      |
| ------------------ | ----------------------------------------------------- | ----------- | ---------- |
| **uid**            | **str**                                               |             | [optional] |
| **status**         | **str**                                               |             | [optional] |
| **target_lang**    | **str**                                               |             | [optional] |
| **filename**       | **str**                                               |             | [optional] |
| **workflow_level** | **int**                                               |             | [optional] |
| **workflow_step**  | [**WorkflowStepReference**](WorkflowStepReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_part_update_source_dto import JobPartUpdateSourceDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartUpdateSourceDto from a JSON string
job_part_update_source_dto_instance = JobPartUpdateSourceDto.from_json(json)
# print the JSON string representation of the object
print JobPartUpdateSourceDto.to_json()

# convert the object into a dict
job_part_update_source_dto_dict = job_part_update_source_dto_instance.to_dict()
# create an instance of JobPartUpdateSourceDto from a dict
job_part_update_source_dto_from_dict = JobPartUpdateSourceDto.from_dict(job_part_update_source_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
