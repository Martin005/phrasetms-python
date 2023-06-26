# BrowseRequestDto

## Properties

| Name            | Type    | Description | Notes      |
| --------------- | ------- | ----------- | ---------- |
| **query_lang**  | **str** |             | [optional] |
| **query**       | **str** |             | [optional] |
| **status**      | **str** |             | [optional] |
| **page_number** | **int** |             | [optional] |
| **page_size**   | **int** |             | [optional] |

## Example

```python
from phrasetms_client.models.browse_request_dto import BrowseRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseRequestDto from a JSON string
browse_request_dto_instance = BrowseRequestDto.from_json(json)
# print the JSON string representation of the object
print BrowseRequestDto.to_json()

# convert the object into a dict
browse_request_dto_dict = browse_request_dto_instance.to_dict()
# create an instance of BrowseRequestDto from a dict
browse_request_dto_from_dict = BrowseRequestDto.from_dict(browse_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
