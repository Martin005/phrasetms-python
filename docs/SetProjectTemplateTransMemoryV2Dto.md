# SetProjectTemplateTransMemoryV2Dto

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
from phrasetms_client.models.set_project_template_trans_memory_v2_dto import SetProjectTemplateTransMemoryV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of SetProjectTemplateTransMemoryV2Dto from a JSON string
set_project_template_trans_memory_v2_dto_instance = SetProjectTemplateTransMemoryV2Dto.from_json(json)
# print the JSON string representation of the object
print SetProjectTemplateTransMemoryV2Dto.to_json()

# convert the object into a dict
set_project_template_trans_memory_v2_dto_dict = set_project_template_trans_memory_v2_dto_instance.to_dict()
# create an instance of SetProjectTemplateTransMemoryV2Dto from a dict
set_project_template_trans_memory_v2_dto_from_dict = SetProjectTemplateTransMemoryV2Dto.from_dict(set_project_template_trans_memory_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
