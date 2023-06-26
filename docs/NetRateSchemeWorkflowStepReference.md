# NetRateSchemeWorkflowStepReference

## Properties

| Name              | Type                                                  | Description | Notes      |
| ----------------- | ----------------------------------------------------- | ----------- | ---------- |
| **id**            | **str**                                               |             | [optional] |
| **workflow_step** | [**WorkflowStepReference**](WorkflowStepReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.net_rate_scheme_workflow_step_reference import NetRateSchemeWorkflowStepReference

# TODO update the JSON string below
json = "{}"
# create an instance of NetRateSchemeWorkflowStepReference from a JSON string
net_rate_scheme_workflow_step_reference_instance = NetRateSchemeWorkflowStepReference.from_json(json)
# print the JSON string representation of the object
print NetRateSchemeWorkflowStepReference.to_json()

# convert the object into a dict
net_rate_scheme_workflow_step_reference_dict = net_rate_scheme_workflow_step_reference_instance.to_dict()
# create an instance of NetRateSchemeWorkflowStepReference from a dict
net_rate_scheme_workflow_step_reference_from_dict = NetRateSchemeWorkflowStepReference.from_dict(net_rate_scheme_workflow_step_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
