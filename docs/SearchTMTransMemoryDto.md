# SearchTMTransMemoryDto

## Properties

| Name        | Type     | Description | Notes      |
| ----------- | -------- | ----------- | ---------- |
| **uid**     | **str**  |             | [optional] |
| **id**      | **str**  |             | [optional] |
| **name**    | **str**  |             | [optional] |
| **reverse** | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tm_trans_memory_dto import SearchTMTransMemoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMTransMemoryDto from a JSON string
search_tm_trans_memory_dto_instance = SearchTMTransMemoryDto.from_json(json)
# print the JSON string representation of the object
print SearchTMTransMemoryDto.to_json()

# convert the object into a dict
search_tm_trans_memory_dto_dict = search_tm_trans_memory_dto_instance.to_dict()
# create an instance of SearchTMTransMemoryDto from a dict
search_tm_trans_memory_dto_from_dict = SearchTMTransMemoryDto.from_dict(search_tm_trans_memory_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
