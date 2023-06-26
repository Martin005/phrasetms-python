# WorkflowChangesDto

## Properties

| Name     | Type                                      | Description | Notes |
| -------- | ----------------------------------------- | ----------- | ----- |
| **jobs** | [**List[UidReference]**](UidReference.md) |             |

## Example

```python
from phrasetms_client.models.workflow_changes_dto import WorkflowChangesDto

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowChangesDto from a JSON string
workflow_changes_dto_instance = WorkflowChangesDto.from_json(json)
# print the JSON string representation of the object
print WorkflowChangesDto.to_json()

# convert the object into a dict
workflow_changes_dto_dict = workflow_changes_dto_instance.to_dict()
# create an instance of WorkflowChangesDto from a dict
workflow_changes_dto_from_dict = WorkflowChangesDto.from_dict(workflow_changes_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
