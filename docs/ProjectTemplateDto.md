# ProjectTemplateDto

## Properties

| Name                   | Type                                                                        | Description                                     | Notes      |
| ---------------------- | --------------------------------------------------------------------------- | ----------------------------------------------- | ---------- |
| **id**                 | **str**                                                                     |                                                 | [optional] |
| **uid**                | **str**                                                                     |                                                 | [optional] |
| **template_name**      | **str**                                                                     |                                                 | [optional] |
| **name**               | **str**                                                                     |                                                 | [optional] |
| **source_lang**        | **str**                                                                     |                                                 | [optional] |
| **target_langs**       | **List[str]**                                                               |                                                 | [optional] |
| **note**               | **str**                                                                     |                                                 | [optional] |
| **use_dynamic_title**  | **bool**                                                                    |                                                 | [optional] |
| **dynamic_title**      | **str**                                                                     |                                                 | [optional] |
| **owner**              | [**UserReference**](UserReference.md)                                       |                                                 | [optional] |
| **client**             | [**ClientReference**](ClientReference.md)                                   |                                                 | [optional] |
| **domain**             | [**DomainReference**](DomainReference.md)                                   |                                                 | [optional] |
| **sub_domain**         | [**SubDomainReference**](SubDomainReference.md)                             |                                                 | [optional] |
| **vendor**             | [**VendorReference**](VendorReference.md)                                   |                                                 | [optional] |
| **created_by**         | [**UserReference**](UserReference.md)                                       |                                                 | [optional] |
| **date_created**       | **datetime**                                                                |                                                 | [optional] |
| **modified_by**        | [**UserReference**](UserReference.md)                                       |                                                 | [optional] |
| **date_modified**      | **datetime**                                                                | Deprecated - use dateTimeModified field instead | [optional] |
| **date_time_modified** | **datetime**                                                                |                                                 | [optional] |
| **workflow_steps**     | [**List[WorkflowStepDto]**](WorkflowStepDto.md)                             |                                                 | [optional] |
| **workflow_settings**  | [**List[WorkflowStepSettingsDto]**](WorkflowStepSettingsDto.md)             |                                                 | [optional] |
| **business_unit**      | [**BusinessUnitReference**](BusinessUnitReference.md)                       |                                                 | [optional] |
| **notify_providers**   | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md) |                                                 | [optional] |
| **assigned_to**        | [**List[AssignmentPerTargetLangDto]**](AssignmentPerTargetLangDto.md)       |                                                 | [optional] |
| **import_settings**    | [**UidReference**](UidReference.md)                                         |                                                 | [optional] |

## Example

```python
from phrasetms_client.models.project_template_dto import ProjectTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateDto from a JSON string
project_template_dto_instance = ProjectTemplateDto.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateDto.to_json()

# convert the object into a dict
project_template_dto_dict = project_template_dto_instance.to_dict()
# create an instance of ProjectTemplateDto from a dict
project_template_dto_from_dict = ProjectTemplateDto.from_dict(project_template_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
