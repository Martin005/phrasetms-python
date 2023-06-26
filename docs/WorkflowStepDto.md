# WorkflowStepDto

## Properties

| Name            | Type     | Description | Notes      |
| --------------- | -------- | ----------- | ---------- |
| **id**          | **str**  |             | [optional] |
| **uid**         | **str**  |             | [optional] |
| **name**        | **str**  |             | [optional] |
| **abbr**        | **str**  |             | [optional] |
| **order**       | **int**  |             | [optional] |
| **lqa_enabled** | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.workflow_step_dto import WorkflowStepDto

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepDto from a JSON string
workflow_step_dto_instance = WorkflowStepDto.from_json(json)
# print the JSON string representation of the object
print WorkflowStepDto.to_json()

# convert the object into a dict
workflow_step_dto_dict = workflow_step_dto_instance.to_dict()
# create an instance of WorkflowStepDto from a dict
workflow_step_dto_from_dict = WorkflowStepDto.from_dict(workflow_step_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
