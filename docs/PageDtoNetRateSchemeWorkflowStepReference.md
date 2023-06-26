# PageDtoNetRateSchemeWorkflowStepReference

## Properties

| Name                   | Type                                                                                  | Description | Notes      |
| ---------------------- | ------------------------------------------------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                                                               |             | [optional] |
| **total_pages**        | **int**                                                                               |             | [optional] |
| **page_size**          | **int**                                                                               |             | [optional] |
| **page_number**        | **int**                                                                               |             | [optional] |
| **number_of_elements** | **int**                                                                               |             | [optional] |
| **content**            | [**List[NetRateSchemeWorkflowStepReference]**](NetRateSchemeWorkflowStepReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_net_rate_scheme_workflow_step_reference import PageDtoNetRateSchemeWorkflowStepReference

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoNetRateSchemeWorkflowStepReference from a JSON string
page_dto_net_rate_scheme_workflow_step_reference_instance = PageDtoNetRateSchemeWorkflowStepReference.from_json(json)
# print the JSON string representation of the object
print PageDtoNetRateSchemeWorkflowStepReference.to_json()

# convert the object into a dict
page_dto_net_rate_scheme_workflow_step_reference_dict = page_dto_net_rate_scheme_workflow_step_reference_instance.to_dict()
# create an instance of PageDtoNetRateSchemeWorkflowStepReference from a dict
page_dto_net_rate_scheme_workflow_step_reference_from_dict = PageDtoNetRateSchemeWorkflowStepReference.from_dict(page_dto_net_rate_scheme_workflow_step_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
