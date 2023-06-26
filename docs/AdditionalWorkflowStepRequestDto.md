# AdditionalWorkflowStepRequestDto

## Properties

| Name     | Type    | Description                          | Notes |
| -------- | ------- | ------------------------------------ | ----- |
| **name** | **str** | Name of the additional workflow step |

## Example

```python
from phrasetms_client.models.additional_workflow_step_request_dto import AdditionalWorkflowStepRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalWorkflowStepRequestDto from a JSON string
additional_workflow_step_request_dto_instance = AdditionalWorkflowStepRequestDto.from_json(json)
# print the JSON string representation of the object
print AdditionalWorkflowStepRequestDto.to_json()

# convert the object into a dict
additional_workflow_step_request_dto_dict = additional_workflow_step_request_dto_instance.to_dict()
# create an instance of AdditionalWorkflowStepRequestDto from a dict
additional_workflow_step_request_dto_from_dict = AdditionalWorkflowStepRequestDto.from_dict(additional_workflow_step_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
