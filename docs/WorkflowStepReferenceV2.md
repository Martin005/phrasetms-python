# WorkflowStepReferenceV2

## Properties

| Name            | Type     | Description | Notes      |
| --------------- | -------- | ----------- | ---------- |
| **name**        | **str**  |             | [optional] |
| **uid**         | **str**  |             | [optional] |
| **id**          | **str**  |             | [optional] |
| **order**       | **int**  |             | [optional] |
| **lqa_enabled** | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.workflow_step_reference_v2 import WorkflowStepReferenceV2

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepReferenceV2 from a JSON string
workflow_step_reference_v2_instance = WorkflowStepReferenceV2.from_json(json)
# print the JSON string representation of the object
print WorkflowStepReferenceV2.to_json()

# convert the object into a dict
workflow_step_reference_v2_dict = workflow_step_reference_v2_instance.to_dict()
# create an instance of WorkflowStepReferenceV2 from a dict
workflow_step_reference_v2_from_dict = WorkflowStepReferenceV2.from_dict(workflow_step_reference_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
