# SearchTMTransMemoryDtoV3

## Properties

| Name        | Type     | Description | Notes      |
| ----------- | -------- | ----------- | ---------- |
| **uid**     | **str**  |             | [optional] |
| **id**      | **str**  |             | [optional] |
| **name**    | **str**  |             | [optional] |
| **reverse** | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tm_trans_memory_dto_v3 import SearchTMTransMemoryDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMTransMemoryDtoV3 from a JSON string
search_tm_trans_memory_dto_v3_instance = SearchTMTransMemoryDtoV3.from_json(json)
# print the JSON string representation of the object
print SearchTMTransMemoryDtoV3.to_json()

# convert the object into a dict
search_tm_trans_memory_dto_v3_dict = search_tm_trans_memory_dto_v3_instance.to_dict()
# create an instance of SearchTMTransMemoryDtoV3 from a dict
search_tm_trans_memory_dto_v3_from_dict = SearchTMTransMemoryDtoV3.from_dict(search_tm_trans_memory_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
