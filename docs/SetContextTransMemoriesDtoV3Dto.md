# SetContextTransMemoriesDtoV3Dto

## Properties

| Name               | Type                                                                  | Description                                                          | Notes      |
| ------------------ | --------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------- |
| **trans_memories** | [**List[SetProjectTransMemoryV3Dto]**](SetProjectTransMemoryV3Dto.md) |                                                                      |
| **target_lang**    | **str**                                                               | Set translation memory only for the specific project target language | [optional] |
| **workflow_step**  | [**UidReference**](UidReference.md)                                   |                                                                      | [optional] |
| **order_enabled**  | **bool**                                                              | Default: false                                                       | [optional] |

## Example

```python
from phrasetms_client.models.set_context_trans_memories_dto_v3_dto import SetContextTransMemoriesDtoV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of SetContextTransMemoriesDtoV3Dto from a JSON string
set_context_trans_memories_dto_v3_dto_instance = SetContextTransMemoriesDtoV3Dto.from_json(json)
# print the JSON string representation of the object
print SetContextTransMemoriesDtoV3Dto.to_json()

# convert the object into a dict
set_context_trans_memories_dto_v3_dto_dict = set_context_trans_memories_dto_v3_dto_instance.to_dict()
# create an instance of SetContextTransMemoriesDtoV3Dto from a dict
set_context_trans_memories_dto_v3_dto_from_dict = SetContextTransMemoriesDtoV3Dto.from_dict(set_context_trans_memories_dto_v3_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
