# NetRateSchemeWorkflowStep

## Properties

| Name              | Type                                                  | Description | Notes      |
| ----------------- | ----------------------------------------------------- | ----------- | ---------- |
| **id**            | **str**                                               |             | [optional] |
| **workflow_step** | [**WorkflowStepReference**](WorkflowStepReference.md) |             | [optional] |
| **rates**         | [**DiscountSettingsDto**](DiscountSettingsDto.md)     |             | [optional] |

## Example

```python
from phrasetms_client.models.net_rate_scheme_workflow_step import NetRateSchemeWorkflowStep

# TODO update the JSON string below
json = "{}"
# create an instance of NetRateSchemeWorkflowStep from a JSON string
net_rate_scheme_workflow_step_instance = NetRateSchemeWorkflowStep.from_json(json)
# print the JSON string representation of the object
print NetRateSchemeWorkflowStep.to_json()

# convert the object into a dict
net_rate_scheme_workflow_step_dict = net_rate_scheme_workflow_step_instance.to_dict()
# create an instance of NetRateSchemeWorkflowStep from a dict
net_rate_scheme_workflow_step_from_dict = NetRateSchemeWorkflowStep.from_dict(net_rate_scheme_workflow_step_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
