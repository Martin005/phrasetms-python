# BrowseResponseListDto

## Properties

| Name               | Type                                  | Description | Notes      |
| ------------------ | ------------------------------------- | ----------- | ---------- |
| **search_results** | [**List[ConceptDto]**](ConceptDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.browse_response_list_dto import BrowseResponseListDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseResponseListDto from a JSON string
browse_response_list_dto_instance = BrowseResponseListDto.from_json(json)
# print the JSON string representation of the object
print BrowseResponseListDto.to_json()

# convert the object into a dict
browse_response_list_dto_dict = browse_response_list_dto_instance.to_dict()
# create an instance of BrowseResponseListDto from a dict
browse_response_list_dto_from_dict = BrowseResponseListDto.from_dict(browse_response_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
