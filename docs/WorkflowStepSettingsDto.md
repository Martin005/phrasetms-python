# WorkflowStepSettingsDto

## Properties

| Name                | Type                                                                                                      | Description | Notes      |
| ------------------- | --------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| **workflow_step**   | [**WorkflowStepReference**](WorkflowStepReference.md)                                                     |             | [optional] |
| **assigned_to**     | [**List[ProjectTemplateWorkflowSettingsAssignedToDto]**](ProjectTemplateWorkflowSettingsAssignedToDto.md) |             | [optional] |
| **notify_provider** | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md)                               |             | [optional] |
| **lqa_profile**     | [**UidReference**](UidReference.md)                                                                       |             | [optional] |

## Example

```python
from phrasetms_client.models.workflow_step_settings_dto import WorkflowStepSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepSettingsDto from a JSON string
workflow_step_settings_dto_instance = WorkflowStepSettingsDto.from_json(json)
# print the JSON string representation of the object
print WorkflowStepSettingsDto.to_json()

# convert the object into a dict
workflow_step_settings_dto_dict = workflow_step_settings_dto_instance.to_dict()
# create an instance of WorkflowStepSettingsDto from a dict
workflow_step_settings_dto_from_dict = WorkflowStepSettingsDto.from_dict(workflow_step_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
