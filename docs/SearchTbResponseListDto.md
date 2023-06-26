# SearchTbResponseListDto

## Properties

| Name               | Type                                                    | Description | Notes      |
| ------------------ | ------------------------------------------------------- | ----------- | ---------- |
| **search_results** | [**List[SearchTbResponseDto]**](SearchTbResponseDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tb_response_list_dto import SearchTbResponseListDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTbResponseListDto from a JSON string
search_tb_response_list_dto_instance = SearchTbResponseListDto.from_json(json)
# print the JSON string representation of the object
print SearchTbResponseListDto.to_json()

# convert the object into a dict
search_tb_response_list_dto_dict = search_tb_response_list_dto_instance.to_dict()
# create an instance of SearchTbResponseListDto from a dict
search_tb_response_list_dto_from_dict = SearchTbResponseListDto.from_dict(search_tb_response_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
