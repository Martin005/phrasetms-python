# ProjectTemplateTransMemoryDtoV3

## Properties

| Name                         | Type                                                      | Description | Notes      |
| ---------------------------- | --------------------------------------------------------- | ----------- | ---------- |
| **target_locale**            | **str**                                                   |             | [optional] |
| **workflow_step**            | [**WorkflowStepReferenceV3**](WorkflowStepReferenceV3.md) |             | [optional] |
| **read_mode**                | **bool**                                                  |             | [optional] |
| **write_mode**               | **bool**                                                  |             | [optional] |
| **trans_memory**             | [**TransMemoryDtoV3**](TransMemoryDtoV3.md)               |             | [optional] |
| **penalty**                  | **float**                                                 |             | [optional] |
| **apply_penalty_to101_only** | **bool**                                                  |             | [optional] |

## Example

```python
from phrasetms_client.models.project_template_trans_memory_dto_v3 import ProjectTemplateTransMemoryDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateTransMemoryDtoV3 from a JSON string
project_template_trans_memory_dto_v3_instance = ProjectTemplateTransMemoryDtoV3.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateTransMemoryDtoV3.to_json()

# convert the object into a dict
project_template_trans_memory_dto_v3_dict = project_template_trans_memory_dto_v3_instance.to_dict()
# create an instance of ProjectTemplateTransMemoryDtoV3 from a dict
project_template_trans_memory_dto_v3_from_dict = ProjectTemplateTransMemoryDtoV3.from_dict(project_template_trans_memory_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
