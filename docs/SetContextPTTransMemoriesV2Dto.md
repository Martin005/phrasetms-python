# SetContextPTTransMemoriesV2Dto

## Properties

| Name               | Type                                                                                  | Description                                                          | Notes      |
| ------------------ | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------- |
| **trans_memories** | [**List[SetProjectTemplateTransMemoryV2Dto]**](SetProjectTemplateTransMemoryV2Dto.md) |                                                                      |
| **target_lang**    | **str**                                                                               | Set translation memory only for the specific project target language | [optional] |
| **workflow_step**  | [**UidReference**](UidReference.md)                                                   |                                                                      | [optional] |
| **order_enabled**  | **bool**                                                                              | Default: false                                                       | [optional] |

## Example

```python
from phrasetms_client.models.set_context_pt_trans_memories_v2_dto import SetContextPTTransMemoriesV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of SetContextPTTransMemoriesV2Dto from a JSON string
set_context_pt_trans_memories_v2_dto_instance = SetContextPTTransMemoriesV2Dto.from_json(json)
# print the JSON string representation of the object
print SetContextPTTransMemoriesV2Dto.to_json()

# convert the object into a dict
set_context_pt_trans_memories_v2_dto_dict = set_context_pt_trans_memories_v2_dto_instance.to_dict()
# create an instance of SetContextPTTransMemoriesV2Dto from a dict
set_context_pt_trans_memories_v2_dto_from_dict = SetContextPTTransMemoriesV2Dto.from_dict(set_context_pt_trans_memories_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
