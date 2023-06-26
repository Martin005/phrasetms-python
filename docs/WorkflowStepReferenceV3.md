# WorkflowStepReferenceV3

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
from phrasetms_client.models.workflow_step_reference_v3 import WorkflowStepReferenceV3

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepReferenceV3 from a JSON string
workflow_step_reference_v3_instance = WorkflowStepReferenceV3.from_json(json)
# print the JSON string representation of the object
print WorkflowStepReferenceV3.to_json()

# convert the object into a dict
workflow_step_reference_v3_dict = workflow_step_reference_v3_instance.to_dict()
# create an instance of WorkflowStepReferenceV3 from a dict
workflow_step_reference_v3_from_dict = WorkflowStepReferenceV3.from_dict(workflow_step_reference_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
