# ProjectTemplateWorkflowSettingsAssignedToDto

## Properties

| Name            | Type                                                | Description | Notes      |
| --------------- | --------------------------------------------------- | ----------- | ---------- |
| **target_lang** | **str**                                             |             | [optional] |
| **providers**   | [**List[ProviderReference]**](ProviderReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.project_template_workflow_settings_assigned_to_dto import ProjectTemplateWorkflowSettingsAssignedToDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateWorkflowSettingsAssignedToDto from a JSON string
project_template_workflow_settings_assigned_to_dto_instance = ProjectTemplateWorkflowSettingsAssignedToDto.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateWorkflowSettingsAssignedToDto.to_json()

# convert the object into a dict
project_template_workflow_settings_assigned_to_dto_dict = project_template_workflow_settings_assigned_to_dto_instance.to_dict()
# create an instance of ProjectTemplateWorkflowSettingsAssignedToDto from a dict
project_template_workflow_settings_assigned_to_dto_from_dict = ProjectTemplateWorkflowSettingsAssignedToDto.from_dict(project_template_workflow_settings_assigned_to_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
