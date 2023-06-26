# SetProjectTemplateTransMemoriesV2Dto

## Properties

| Name                 | Type                                                                          | Description | Notes |
| -------------------- | ----------------------------------------------------------------------------- | ----------- | ----- |
| **data_per_context** | [**List[SetContextPTTransMemoriesV2Dto]**](SetContextPTTransMemoriesV2Dto.md) |             |

## Example

```python
from phrasetms_client.models.set_project_template_trans_memories_v2_dto import SetProjectTemplateTransMemoriesV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of SetProjectTemplateTransMemoriesV2Dto from a JSON string
set_project_template_trans_memories_v2_dto_instance = SetProjectTemplateTransMemoriesV2Dto.from_json(json)
# print the JSON string representation of the object
print SetProjectTemplateTransMemoriesV2Dto.to_json()

# convert the object into a dict
set_project_template_trans_memories_v2_dto_dict = set_project_template_trans_memories_v2_dto_instance.to_dict()
# create an instance of SetProjectTemplateTransMemoriesV2Dto from a dict
set_project_template_trans_memories_v2_dto_from_dict = SetProjectTemplateTransMemoriesV2Dto.from_dict(set_project_template_trans_memories_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
