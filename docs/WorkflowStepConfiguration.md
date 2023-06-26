# WorkflowStepConfiguration

## Properties

| Name                | Type                                                      | Description               | Notes      |
| ------------------- | --------------------------------------------------------- | ------------------------- | ---------- |
| **id**              | **str**                                                   |                           | [optional] |
| **assignments**     | [**List[ProvidersPerLanguage]**](ProvidersPerLanguage.md) |                           |
| **due**             | **datetime**                                              | Use ISO 8601 date format. | [optional] |
| **notify_provider** | [**NotifyProviderDto**](NotifyProviderDto.md)             |                           | [optional] |

## Example

```python
from phrasetms_client.models.workflow_step_configuration import WorkflowStepConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepConfiguration from a JSON string
workflow_step_configuration_instance = WorkflowStepConfiguration.from_json(json)
# print the JSON string representation of the object
print WorkflowStepConfiguration.to_json()

# convert the object into a dict
workflow_step_configuration_dict = workflow_step_configuration_instance.to_dict()
# create an instance of WorkflowStepConfiguration from a dict
workflow_step_configuration_from_dict = WorkflowStepConfiguration.from_dict(workflow_step_configuration_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
