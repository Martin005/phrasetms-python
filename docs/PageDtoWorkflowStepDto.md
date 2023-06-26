# PageDtoWorkflowStepDto

## Properties

| Name                   | Type                                            | Description | Notes      |
| ---------------------- | ----------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                         |             | [optional] |
| **total_pages**        | **int**                                         |             | [optional] |
| **page_size**          | **int**                                         |             | [optional] |
| **page_number**        | **int**                                         |             | [optional] |
| **number_of_elements** | **int**                                         |             | [optional] |
| **content**            | [**List[WorkflowStepDto]**](WorkflowStepDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_workflow_step_dto import PageDtoWorkflowStepDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoWorkflowStepDto from a JSON string
page_dto_workflow_step_dto_instance = PageDtoWorkflowStepDto.from_json(json)
# print the JSON string representation of the object
print PageDtoWorkflowStepDto.to_json()

# convert the object into a dict
page_dto_workflow_step_dto_dict = page_dto_workflow_step_dto_instance.to_dict()
# create an instance of PageDtoWorkflowStepDto from a dict
page_dto_workflow_step_dto_from_dict = PageDtoWorkflowStepDto.from_dict(page_dto_workflow_step_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
