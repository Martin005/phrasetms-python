# AssignedJobDto

## Properties

| Name              | Type                                                                | Description | Notes      |
| ----------------- | ------------------------------------------------------------------- | ----------- | ---------- |
| **uid**           | **str**                                                             |             | [optional] |
| **inner_id**      | **str**                                                             |             | [optional] |
| **filename**      | **str**                                                             |             | [optional] |
| **date_due**      | **datetime**                                                        |             | [optional] |
| **date_created**  | **datetime**                                                        |             | [optional] |
| **status**        | **str**                                                             |             | [optional] |
| **target_lang**   | **str**                                                             |             | [optional] |
| **source_lang**   | **str**                                                             |             | [optional] |
| **project**       | [**ProjectReference**](ProjectReference.md)                         |             | [optional] |
| **workflow_step** | [**ProjectWorkflowStepReference**](ProjectWorkflowStepReference.md) |             | [optional] |
| **import_status** | [**ImportStatusDto**](ImportStatusDto.md)                           |             | [optional] |
| **imported**      | **bool**                                                            |             | [optional] |

## Example

```python
from phrasetms_client.models.assigned_job_dto import AssignedJobDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedJobDto from a JSON string
assigned_job_dto_instance = AssignedJobDto.from_json(json)
# print the JSON string representation of the object
print AssignedJobDto.to_json()

# convert the object into a dict
assigned_job_dto_dict = assigned_job_dto_instance.to_dict()
# create an instance of AssignedJobDto from a dict
assigned_job_dto_from_dict = AssignedJobDto.from_dict(assigned_job_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
