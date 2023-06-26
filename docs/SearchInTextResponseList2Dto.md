# SearchInTextResponseList2Dto

## Properties

| Name               | Type                                                              | Description | Notes      |
| ------------------ | ----------------------------------------------------------------- | ----------- | ---------- |
| **search_results** | [**List[SearchInTextResponse2Dto]**](SearchInTextResponse2Dto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.search_in_text_response_list2_dto import SearchInTextResponseList2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchInTextResponseList2Dto from a JSON string
search_in_text_response_list2_dto_instance = SearchInTextResponseList2Dto.from_json(json)
# print the JSON string representation of the object
print SearchInTextResponseList2Dto.to_json()

# convert the object into a dict
search_in_text_response_list2_dto_dict = search_in_text_response_list2_dto_instance.to_dict()
# create an instance of SearchInTextResponseList2Dto from a dict
search_in_text_response_list2_dto_from_dict = SearchInTextResponseList2Dto.from_dict(search_in_text_response_list2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
