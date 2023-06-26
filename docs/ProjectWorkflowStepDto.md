# ProjectWorkflowStepDto

## Properties

| Name                | Type       | Description | Notes      |
| ------------------- | ---------- | ----------- | ---------- |
| **id**              | **int**    |             | [optional] |
| **abbreviation**    | **str**    |             | [optional] |
| **name**            | **str**    |             | [optional] |
| **workflow_level**  | **int**    |             | [optional] |
| **workflow_step**   | **object** |             | [optional] |
| **lqa_profile_uid** | **str**    |             | [optional] |

## Example

```python
from phrasetms_client.models.project_workflow_step_dto import ProjectWorkflowStepDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectWorkflowStepDto from a JSON string
project_workflow_step_dto_instance = ProjectWorkflowStepDto.from_json(json)
# print the JSON string representation of the object
print ProjectWorkflowStepDto.to_json()

# convert the object into a dict
project_workflow_step_dto_dict = project_workflow_step_dto_instance.to_dict()
# create an instance of ProjectWorkflowStepDto from a dict
project_workflow_step_dto_from_dict = ProjectWorkflowStepDto.from_dict(project_workflow_step_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
