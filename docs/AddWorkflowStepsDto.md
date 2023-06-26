# AddWorkflowStepsDto

## Properties

| Name               | Type                                    | Description | Notes      |
| ------------------ | --------------------------------------- | ----------- | ---------- |
| **workflow_steps** | [**List[IdReference]**](IdReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.add_workflow_steps_dto import AddWorkflowStepsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddWorkflowStepsDto from a JSON string
add_workflow_steps_dto_instance = AddWorkflowStepsDto.from_json(json)
# print the JSON string representation of the object
print AddWorkflowStepsDto.to_json()

# convert the object into a dict
add_workflow_steps_dto_dict = add_workflow_steps_dto_instance.to_dict()
# create an instance of AddWorkflowStepsDto from a dict
add_workflow_steps_dto_from_dict = AddWorkflowStepsDto.from_dict(add_workflow_steps_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
