# EditWorkflowStepDto

## Properties

| Name            | Type     | Description                   | Notes      |
| --------------- | -------- | ----------------------------- | ---------- |
| **name**        | **str**  | Name of the lqa workflow step | [optional] |
| **order**       | **int**  | Order value                   | [optional] |
| **lqa_enabled** | **bool** | Default: false                | [optional] |
| **abbr**        | **str**  | Abbreviation                  | [optional] |

## Example

```python
from phrasetms_client.models.edit_workflow_step_dto import EditWorkflowStepDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditWorkflowStepDto from a JSON string
edit_workflow_step_dto_instance = EditWorkflowStepDto.from_json(json)
# print the JSON string representation of the object
print EditWorkflowStepDto.to_json()

# convert the object into a dict
edit_workflow_step_dto_dict = edit_workflow_step_dto_instance.to_dict()
# create an instance of EditWorkflowStepDto from a dict
edit_workflow_step_dto_from_dict = EditWorkflowStepDto.from_dict(edit_workflow_step_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
