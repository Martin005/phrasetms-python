# SetProjectTransMemoryV3Dto

## Properties

| Name                         | Type                                | Description                                                                                                                                   | Notes      |
| ---------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **trans_memory**             | [**UidReference**](UidReference.md) |                                                                                                                                               |
| **read_mode**                | **bool**                            | Default: false                                                                                                                                | [optional] |
| **write_mode**               | **bool**                            | Can be set only for Translation Memory with read &#x3D;&#x3D; true.&lt;br/&gt; Max 2 write TMs allowed per project.&lt;br/&gt; Default: false | [optional] |
| **penalty**                  | **float**                           |                                                                                                                                               | [optional] |
| **apply_penalty_to101_only** | **bool**                            | Can be set only for penalty &#x3D;&#x3D; 1&lt;br/&gt;Default: false                                                                           | [optional] |
| **order**                    | **int**                             |                                                                                                                                               | [optional] |

## Example

```python
from phrasetms_client.models.set_project_trans_memory_v3_dto import SetProjectTransMemoryV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of SetProjectTransMemoryV3Dto from a JSON string
set_project_trans_memory_v3_dto_instance = SetProjectTransMemoryV3Dto.from_json(json)
# print the JSON string representation of the object
print SetProjectTransMemoryV3Dto.to_json()

# convert the object into a dict
set_project_trans_memory_v3_dto_dict = set_project_trans_memory_v3_dto_instance.to_dict()
# create an instance of SetProjectTransMemoryV3Dto from a dict
set_project_trans_memory_v3_dto_from_dict = SetProjectTransMemoryV3Dto.from_dict(set_project_trans_memory_v3_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
