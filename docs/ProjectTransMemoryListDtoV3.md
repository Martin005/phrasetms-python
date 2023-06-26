# ProjectTransMemoryListDtoV3

## Properties

| Name               | Type                                                            | Description | Notes      |
| ------------------ | --------------------------------------------------------------- | ----------- | ---------- |
| **trans_memories** | [**List[ProjectTransMemoryDtoV3]**](ProjectTransMemoryDtoV3.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.project_trans_memory_list_dto_v3 import ProjectTransMemoryListDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTransMemoryListDtoV3 from a JSON string
project_trans_memory_list_dto_v3_instance = ProjectTransMemoryListDtoV3.from_json(json)
# print the JSON string representation of the object
print ProjectTransMemoryListDtoV3.to_json()

# convert the object into a dict
project_trans_memory_list_dto_v3_dict = project_trans_memory_list_dto_v3_instance.to_dict()
# create an instance of ProjectTransMemoryListDtoV3 from a dict
project_trans_memory_list_dto_v3_from_dict = ProjectTransMemoryListDtoV3.from_dict(project_trans_memory_list_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
