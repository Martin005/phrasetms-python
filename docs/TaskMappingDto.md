# TaskMappingDto

## Properties

| Name               | Type       | Description | Notes      |
| ------------------ | ---------- | ----------- | ---------- |
| **task_id**        | **str**    |             | [optional] |
| **workflow_level** | **str**    |             | [optional] |
| **resource_path**  | **str**    |             | [optional] |
| **project**        | **object** |             | [optional] |
| **job**            | **object** |             | [optional] |

## Example

```python
from phrasetms_client.models.task_mapping_dto import TaskMappingDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaskMappingDto from a JSON string
task_mapping_dto_instance = TaskMappingDto.from_json(json)
# print the JSON string representation of the object
print TaskMappingDto.to_json()

# convert the object into a dict
task_mapping_dto_dict = task_mapping_dto_instance.to_dict()
# create an instance of TaskMappingDto from a dict
task_mapping_dto_from_dict = TaskMappingDto.from_dict(task_mapping_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
