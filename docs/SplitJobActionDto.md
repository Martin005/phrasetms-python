# SplitJobActionDto

## Properties

| Name                 | Type          | Description                           | Notes      |
| -------------------- | ------------- | ------------------------------------- | ---------- |
| **segment_ordinals** | **List[int]** |                                       | [optional] |
| **part_count**       | **int**       |                                       | [optional] |
| **part_size**        | **int**       |                                       | [optional] |
| **word_count**       | **int**       |                                       | [optional] |
| **by_document_part** | **bool**      | Can be used only for PowerPoint files | [optional] |

## Example

```python
from phrasetms_client.models.split_job_action_dto import SplitJobActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of SplitJobActionDto from a JSON string
split_job_action_dto_instance = SplitJobActionDto.from_json(json)
# print the JSON string representation of the object
print SplitJobActionDto.to_json()

# convert the object into a dict
split_job_action_dto_dict = split_job_action_dto_instance.to_dict()
# create an instance of SplitJobActionDto from a dict
split_job_action_dto_from_dict = SplitJobActionDto.from_dict(split_job_action_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
