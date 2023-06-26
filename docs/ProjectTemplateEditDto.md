# ProjectTemplateEditDto

## Properties

| Name                   | Type                                                                                                      | Description                                                                               | Notes      |
| ---------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ---------- |
| **name**               | **str**                                                                                                   |                                                                                           | [optional] |
| **template_name**      | **str**                                                                                                   |                                                                                           |
| **source_lang**        | **str**                                                                                                   |                                                                                           | [optional] |
| **target_langs**       | **List[str]**                                                                                             |                                                                                           | [optional] |
| **use_dynamic_title**  | **bool**                                                                                                  |                                                                                           | [optional] |
| **dynamic_title**      | **str**                                                                                                   |                                                                                           | [optional] |
| **notify_provider**    | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md)                               |                                                                                           | [optional] |
| **work_flow_settings** | [**List[WorkflowStepSettingsEditDto]**](WorkflowStepSettingsEditDto.md)                                   |                                                                                           | [optional] |
| **client**             | [**IdReference**](IdReference.md)                                                                         |                                                                                           | [optional] |
| **cost_center**        | [**IdReference**](IdReference.md)                                                                         |                                                                                           | [optional] |
| **business_unit**      | [**IdReference**](IdReference.md)                                                                         |                                                                                           | [optional] |
| **domain**             | [**IdReference**](IdReference.md)                                                                         |                                                                                           | [optional] |
| **sub_domain**         | [**IdReference**](IdReference.md)                                                                         |                                                                                           | [optional] |
| **vendor**             | [**IdReference**](IdReference.md)                                                                         |                                                                                           | [optional] |
| **import_settings**    | [**UidReference**](UidReference.md)                                                                       |                                                                                           | [optional] |
| **note**               | **str**                                                                                                   |                                                                                           | [optional] |
| **file_handover**      | **bool**                                                                                                  | Default: false                                                                            | [optional] |
| **assigned_to**        | [**List[ProjectTemplateWorkflowSettingsAssignedToDto]**](ProjectTemplateWorkflowSettingsAssignedToDto.md) | only use for projects without workflows; otherwise specify in the workflowSettings object | [optional] |

## Example

```python
from phrasetms_client.models.project_template_edit_dto import ProjectTemplateEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateEditDto from a JSON string
project_template_edit_dto_instance = ProjectTemplateEditDto.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateEditDto.to_json()

# convert the object into a dict
project_template_edit_dto_dict = project_template_edit_dto_instance.to_dict()
# create an instance of ProjectTemplateEditDto from a dict
project_template_edit_dto_from_dict = ProjectTemplateEditDto.from_dict(project_template_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
