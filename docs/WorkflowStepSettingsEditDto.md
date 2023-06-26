# WorkflowStepSettingsEditDto

## Properties

| Name                | Type                                                                                                      | Description | Notes      |
| ------------------- | --------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| **workflow_step**   | [**IdReference**](IdReference.md)                                                                         |             | [optional] |
| **assigned_to**     | [**List[ProjectTemplateWorkflowSettingsAssignedToDto]**](ProjectTemplateWorkflowSettingsAssignedToDto.md) |             | [optional] |
| **notify_provider** | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md)                               |             | [optional] |
| **lqa_profile**     | [**UidReference**](UidReference.md)                                                                       |             | [optional] |

## Example

```python
from phrasetms_client.models.workflow_step_settings_edit_dto import WorkflowStepSettingsEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepSettingsEditDto from a JSON string
workflow_step_settings_edit_dto_instance = WorkflowStepSettingsEditDto.from_json(json)
# print the JSON string representation of the object
print WorkflowStepSettingsEditDto.to_json()

# convert the object into a dict
workflow_step_settings_edit_dto_dict = workflow_step_settings_edit_dto_instance.to_dict()
# create an instance of WorkflowStepSettingsEditDto from a dict
workflow_step_settings_edit_dto_from_dict = WorkflowStepSettingsEditDto.from_dict(workflow_step_settings_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
