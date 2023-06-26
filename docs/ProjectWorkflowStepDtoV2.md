# ProjectWorkflowStepDtoV2

## Properties

| Name               | Type                                                      | Description | Notes      |
| ------------------ | --------------------------------------------------------- | ----------- | ---------- |
| **id**             | **int**                                                   |             | [optional] |
| **abbreviation**   | **str**                                                   |             | [optional] |
| **name**           | **str**                                                   |             | [optional] |
| **workflow_level** | **int**                                                   |             | [optional] |
| **workflow_step**  | [**WorkflowStepReferenceV2**](WorkflowStepReferenceV2.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.project_workflow_step_dto_v2 import ProjectWorkflowStepDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectWorkflowStepDtoV2 from a JSON string
project_workflow_step_dto_v2_instance = ProjectWorkflowStepDtoV2.from_json(json)
# print the JSON string representation of the object
print ProjectWorkflowStepDtoV2.to_json()

# convert the object into a dict
project_workflow_step_dto_v2_dict = project_workflow_step_dto_v2_instance.to_dict()
# create an instance of ProjectWorkflowStepDtoV2 from a dict
project_workflow_step_dto_v2_from_dict = ProjectWorkflowStepDtoV2.from_dict(project_workflow_step_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
