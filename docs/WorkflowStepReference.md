# WorkflowStepReference

## Properties

| Name            | Type     | Description | Notes      |
| --------------- | -------- | ----------- | ---------- |
| **name**        | **str**  |             | [optional] |
| **id**          | **str**  |             | [optional] |
| **uid**         | **str**  |             | [optional] |
| **order**       | **int**  |             | [optional] |
| **lqa_enabled** | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.workflow_step_reference import WorkflowStepReference

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepReference from a JSON string
workflow_step_reference_instance = WorkflowStepReference.from_json(json)
# print the JSON string representation of the object
print WorkflowStepReference.to_json()

# convert the object into a dict
workflow_step_reference_dict = workflow_step_reference_instance.to_dict()
# create an instance of WorkflowStepReference from a dict
workflow_step_reference_from_dict = WorkflowStepReference.from_dict(workflow_step_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
