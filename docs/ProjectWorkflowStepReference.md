# ProjectWorkflowStepReference

## Properties

| Name               | Type    | Description | Notes      |
| ------------------ | ------- | ----------- | ---------- |
| **name**           | **str** |             | [optional] |
| **id**             | **str** |             | [optional] |
| **order**          | **int** |             | [optional] |
| **workflow_level** | **int** |             | [optional] |

## Example

```python
from phrasetms_client.models.project_workflow_step_reference import ProjectWorkflowStepReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectWorkflowStepReference from a JSON string
project_workflow_step_reference_instance = ProjectWorkflowStepReference.from_json(json)
# print the JSON string representation of the object
print ProjectWorkflowStepReference.to_json()

# convert the object into a dict
project_workflow_step_reference_dict = project_workflow_step_reference_instance.to_dict()
# create an instance of ProjectWorkflowStepReference from a dict
project_workflow_step_reference_from_dict = ProjectWorkflowStepReference.from_dict(project_workflow_step_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
