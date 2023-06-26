# ProjectTemplateTransMemoryListV2Dto

## Properties

| Name               | Type                                                                            | Description | Notes      |
| ------------------ | ------------------------------------------------------------------------------- | ----------- | ---------- |
| **trans_memories** | [**List[ProjectTemplateTransMemoryV2Dto]**](ProjectTemplateTransMemoryV2Dto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.project_template_trans_memory_list_v2_dto import ProjectTemplateTransMemoryListV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateTransMemoryListV2Dto from a JSON string
project_template_trans_memory_list_v2_dto_instance = ProjectTemplateTransMemoryListV2Dto.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateTransMemoryListV2Dto.to_json()

# convert the object into a dict
project_template_trans_memory_list_v2_dto_dict = project_template_trans_memory_list_v2_dto_instance.to_dict()
# create an instance of ProjectTemplateTransMemoryListV2Dto from a dict
project_template_trans_memory_list_v2_dto_from_dict = ProjectTemplateTransMemoryListV2Dto.from_dict(project_template_trans_memory_list_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
