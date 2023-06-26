# SearchResponseListTmDtoV3

## Properties

| Name               | Type                                                        | Description | Notes      |
| ------------------ | ----------------------------------------------------------- | ----------- | ---------- |
| **search_results** | [**List[SearchTMResponseDtoV3]**](SearchTMResponseDtoV3.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.search_response_list_tm_dto_v3 import SearchResponseListTmDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseListTmDtoV3 from a JSON string
search_response_list_tm_dto_v3_instance = SearchResponseListTmDtoV3.from_json(json)
# print the JSON string representation of the object
print SearchResponseListTmDtoV3.to_json()

# convert the object into a dict
search_response_list_tm_dto_v3_dict = search_response_list_tm_dto_v3_instance.to_dict()
# create an instance of SearchResponseListTmDtoV3 from a dict
search_response_list_tm_dto_v3_from_dict = SearchResponseListTmDtoV3.from_dict(search_response_list_tm_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
