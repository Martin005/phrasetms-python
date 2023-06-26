# CleanedTransMemoriesDto

## Properties

| Name               | Type          | Description | Notes      |
| ------------------ | ------------- | ----------- | ---------- |
| **uids**           | **List[str]** |             |
| **output_format**  | **str**       |             | [optional] |
| **preserve_ratio** | **float**     |             | [optional] |
| **target_langs**   | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.cleaned_trans_memories_dto import CleanedTransMemoriesDto

# TODO update the JSON string below
json = "{}"
# create an instance of CleanedTransMemoriesDto from a JSON string
cleaned_trans_memories_dto_instance = CleanedTransMemoriesDto.from_json(json)
# print the JSON string representation of the object
print CleanedTransMemoriesDto.to_json()

# convert the object into a dict
cleaned_trans_memories_dto_dict = cleaned_trans_memories_dto_instance.to_dict()
# create an instance of CleanedTransMemoriesDto from a dict
cleaned_trans_memories_dto_from_dict = CleanedTransMemoriesDto.from_dict(cleaned_trans_memories_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
