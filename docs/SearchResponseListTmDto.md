# SearchResponseListTmDto

## Properties

| Name               | Type                                                    | Description | Notes      |
| ------------------ | ------------------------------------------------------- | ----------- | ---------- |
| **search_results** | [**List[SearchTMResponseDto]**](SearchTMResponseDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.search_response_list_tm_dto import SearchResponseListTmDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseListTmDto from a JSON string
search_response_list_tm_dto_instance = SearchResponseListTmDto.from_json(json)
# print the JSON string representation of the object
print SearchResponseListTmDto.to_json()

# convert the object into a dict
search_response_list_tm_dto_dict = search_response_list_tm_dto_instance.to_dict()
# create an instance of SearchResponseListTmDto from a dict
search_response_list_tm_dto_from_dict = SearchResponseListTmDto.from_dict(search_response_list_tm_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
