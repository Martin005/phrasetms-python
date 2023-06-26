# CreateWorkflowStepDto

## Properties

| Name            | Type     | Description                   | Notes      |
| --------------- | -------- | ----------------------------- | ---------- |
| **name**        | **str**  | Name of the lqa workflow step |
| **order**       | **int**  | Order value                   | [optional] |
| **lqa_enabled** | **bool** | Default: false                | [optional] |
| **abbr**        | **str**  | Abbreviation                  |

## Example

```python
from phrasetms_client.models.create_workflow_step_dto import CreateWorkflowStepDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkflowStepDto from a JSON string
create_workflow_step_dto_instance = CreateWorkflowStepDto.from_json(json)
# print the JSON string representation of the object
print CreateWorkflowStepDto.to_json()

# convert the object into a dict
create_workflow_step_dto_dict = create_workflow_step_dto_instance.to_dict()
# create an instance of CreateWorkflowStepDto from a dict
create_workflow_step_dto_from_dict = CreateWorkflowStepDto.from_dict(create_workflow_step_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
