# NetRateSchemeWorkflowStepCreate

## Properties

| Name              | Type                                              | Description | Notes      |
| ----------------- | ------------------------------------------------- | ----------- | ---------- |
| **workflow_step** | [**IdReference**](IdReference.md)                 |             |
| **rates**         | [**DiscountSettingsDto**](DiscountSettingsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.net_rate_scheme_workflow_step_create import NetRateSchemeWorkflowStepCreate

# TODO update the JSON string below
json = "{}"
# create an instance of NetRateSchemeWorkflowStepCreate from a JSON string
net_rate_scheme_workflow_step_create_instance = NetRateSchemeWorkflowStepCreate.from_json(json)
# print the JSON string representation of the object
print NetRateSchemeWorkflowStepCreate.to_json()

# convert the object into a dict
net_rate_scheme_workflow_step_create_dict = net_rate_scheme_workflow_step_create_instance.to_dict()
# create an instance of NetRateSchemeWorkflowStepCreate from a dict
net_rate_scheme_workflow_step_create_from_dict = NetRateSchemeWorkflowStepCreate.from_dict(net_rate_scheme_workflow_step_create_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
