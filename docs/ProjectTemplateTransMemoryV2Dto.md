# ProjectTemplateTransMemoryV2Dto

## Properties

| Name                         | Type                                                      | Description | Notes      |
| ---------------------------- | --------------------------------------------------------- | ----------- | ---------- |
| **target_locale**            | **str**                                                   |             | [optional] |
| **workflow_step**            | [**WorkflowStepReferenceV2**](WorkflowStepReferenceV2.md) |             | [optional] |
| **read_mode**                | **bool**                                                  |             | [optional] |
| **write_mode**               | **bool**                                                  |             | [optional] |
| **trans_memory**             | [**TransMemoryDtoV2**](TransMemoryDtoV2.md)               |             | [optional] |
| **penalty**                  | **float**                                                 |             | [optional] |
| **apply_penalty_to101_only** | **bool**                                                  |             | [optional] |
| **order**                    | **int**                                                   |             | [optional] |

## Example

```python
from phrasetms_client.models.project_template_trans_memory_v2_dto import ProjectTemplateTransMemoryV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateTransMemoryV2Dto from a JSON string
project_template_trans_memory_v2_dto_instance = ProjectTemplateTransMemoryV2Dto.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateTransMemoryV2Dto.to_json()

# convert the object into a dict
project_template_trans_memory_v2_dto_dict = project_template_trans_memory_v2_dto_instance.to_dict()
# create an instance of ProjectTemplateTransMemoryV2Dto from a dict
project_template_trans_memory_v2_dto_from_dict = ProjectTemplateTransMemoryV2Dto.from_dict(project_template_trans_memory_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
