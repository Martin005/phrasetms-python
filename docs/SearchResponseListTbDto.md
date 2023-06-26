# SearchResponseListTbDto

## Properties

| Name               | Type                                                    | Description | Notes      |
| ------------------ | ------------------------------------------------------- | ----------- | ---------- |
| **search_results** | [**List[SearchResponseTbDto]**](SearchResponseTbDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.search_response_list_tb_dto import SearchResponseListTbDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseListTbDto from a JSON string
search_response_list_tb_dto_instance = SearchResponseListTbDto.from_json(json)
# print the JSON string representation of the object
print SearchResponseListTbDto.to_json()

# convert the object into a dict
search_response_list_tb_dto_dict = search_response_list_tb_dto_instance.to_dict()
# create an instance of SearchResponseListTbDto from a dict
search_response_list_tb_dto_from_dict = SearchResponseListTbDto.from_dict(search_response_list_tb_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
