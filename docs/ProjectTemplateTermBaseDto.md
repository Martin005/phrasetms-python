# ProjectTemplateTermBaseDto

## Properties

| Name                  | Type                                                  | Description | Notes      |
| --------------------- | ----------------------------------------------------- | ----------- | ---------- |
| **target_locale**     | **str**                                               |             | [optional] |
| **workflow_step**     | [**WorkflowStepReference**](WorkflowStepReference.md) |             | [optional] |
| **read_mode**         | **bool**                                              |             | [optional] |
| **write_mode**        | **bool**                                              |             | [optional] |
| **term_base**         | [**TermBaseDto**](TermBaseDto.md)                     |             | [optional] |
| **quality_assurance** | **bool**                                              |             | [optional] |

## Example

```python
from phrasetms_client.models.project_template_term_base_dto import ProjectTemplateTermBaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateTermBaseDto from a JSON string
project_template_term_base_dto_instance = ProjectTemplateTermBaseDto.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateTermBaseDto.to_json()

# convert the object into a dict
project_template_term_base_dto_dict = project_template_term_base_dto_instance.to_dict()
# create an instance of ProjectTemplateTermBaseDto from a dict
project_template_term_base_dto_from_dict = ProjectTemplateTermBaseDto.from_dict(project_template_term_base_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
