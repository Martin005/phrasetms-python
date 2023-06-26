# AdditionalWorkflowStepDto

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **id**   | **str** |             | [optional] |
| **name** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.additional_workflow_step_dto import AdditionalWorkflowStepDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalWorkflowStepDto from a JSON string
additional_workflow_step_dto_instance = AdditionalWorkflowStepDto.from_json(json)
# print the JSON string representation of the object
print AdditionalWorkflowStepDto.to_json()

# convert the object into a dict
additional_workflow_step_dto_dict = additional_workflow_step_dto_instance.to_dict()
# create an instance of AdditionalWorkflowStepDto from a dict
additional_workflow_step_dto_from_dict = AdditionalWorkflowStepDto.from_dict(additional_workflow_step_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
