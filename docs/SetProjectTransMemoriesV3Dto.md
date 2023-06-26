# SetProjectTransMemoriesV3Dto

## Properties

| Name                 | Type                                                                            | Description | Notes |
| -------------------- | ------------------------------------------------------------------------------- | ----------- | ----- |
| **data_per_context** | [**List[SetContextTransMemoriesDtoV3Dto]**](SetContextTransMemoriesDtoV3Dto.md) |             |

## Example

```python
from phrasetms_client.models.set_project_trans_memories_v3_dto import SetProjectTransMemoriesV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of SetProjectTransMemoriesV3Dto from a JSON string
set_project_trans_memories_v3_dto_instance = SetProjectTransMemoriesV3Dto.from_json(json)
# print the JSON string representation of the object
print SetProjectTransMemoriesV3Dto.to_json()

# convert the object into a dict
set_project_trans_memories_v3_dto_dict = set_project_trans_memories_v3_dto_instance.to_dict()
# create an instance of SetProjectTransMemoriesV3Dto from a dict
set_project_trans_memories_v3_dto_from_dict = SetProjectTransMemoriesV3Dto.from_dict(set_project_trans_memories_v3_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
