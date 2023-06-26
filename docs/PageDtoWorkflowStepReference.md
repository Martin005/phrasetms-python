# PageDtoWorkflowStepReference

## Properties

| Name                   | Type                                                        | Description | Notes      |
| ---------------------- | ----------------------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                                     |             | [optional] |
| **total_pages**        | **int**                                                     |             | [optional] |
| **page_size**          | **int**                                                     |             | [optional] |
| **page_number**        | **int**                                                     |             | [optional] |
| **number_of_elements** | **int**                                                     |             | [optional] |
| **content**            | [**List[WorkflowStepReference]**](WorkflowStepReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_workflow_step_reference import PageDtoWorkflowStepReference

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoWorkflowStepReference from a JSON string
page_dto_workflow_step_reference_instance = PageDtoWorkflowStepReference.from_json(json)
# print the JSON string representation of the object
print PageDtoWorkflowStepReference.to_json()

# convert the object into a dict
page_dto_workflow_step_reference_dict = page_dto_workflow_step_reference_instance.to_dict()
# create an instance of PageDtoWorkflowStepReference from a dict
page_dto_workflow_step_reference_from_dict = PageDtoWorkflowStepReference.from_dict(page_dto_workflow_step_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
