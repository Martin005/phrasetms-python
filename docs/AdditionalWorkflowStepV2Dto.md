# AdditionalWorkflowStepV2Dto

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **id**   | **str** |             | [optional] |
| **name** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.additional_workflow_step_v2_dto import AdditionalWorkflowStepV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalWorkflowStepV2Dto from a JSON string
additional_workflow_step_v2_dto_instance = AdditionalWorkflowStepV2Dto.from_json(json)
# print the JSON string representation of the object
print AdditionalWorkflowStepV2Dto.to_json()

# convert the object into a dict
additional_workflow_step_v2_dto_dict = additional_workflow_step_v2_dto_instance.to_dict()
# create an instance of AdditionalWorkflowStepV2Dto from a dict
additional_workflow_step_v2_dto_from_dict = AdditionalWorkflowStepV2Dto.from_dict(additional_workflow_step_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
