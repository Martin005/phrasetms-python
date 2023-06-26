# ProjectTermBaseDto

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
from phrasetms_client.models.project_term_base_dto import ProjectTermBaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTermBaseDto from a JSON string
project_term_base_dto_instance = ProjectTermBaseDto.from_json(json)
# print the JSON string representation of the object
print ProjectTermBaseDto.to_json()

# convert the object into a dict
project_term_base_dto_dict = project_term_base_dto_instance.to_dict()
# create an instance of ProjectTermBaseDto from a dict
project_term_base_dto_from_dict = ProjectTermBaseDto.from_dict(project_term_base_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
