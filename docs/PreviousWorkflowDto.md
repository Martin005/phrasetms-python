# PreviousWorkflowDto

## Properties

| Name          | Type                                          | Description | Notes      |
| ------------- | --------------------------------------------- | ----------- | ---------- |
| **completed** | **bool**                                      |             | [optional] |
| **counts**    | [**SegmentsCountsDto**](SegmentsCountsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.previous_workflow_dto import PreviousWorkflowDto

# TODO update the JSON string below
json = "{}"
# create an instance of PreviousWorkflowDto from a JSON string
previous_workflow_dto_instance = PreviousWorkflowDto.from_json(json)
# print the JSON string representation of the object
print PreviousWorkflowDto.to_json()

# convert the object into a dict
previous_workflow_dto_dict = previous_workflow_dto_instance.to_dict()
# create an instance of PreviousWorkflowDto from a dict
previous_workflow_dto_from_dict = PreviousWorkflowDto.from_dict(previous_workflow_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
