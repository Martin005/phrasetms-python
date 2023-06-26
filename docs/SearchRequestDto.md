# SearchRequestDto

## Properties

| Name                 | Type                                          | Description                                                      | Notes      |
| -------------------- | --------------------------------------------- | ---------------------------------------------------------------- | ---------- |
| **query**            | **str**                                       |                                                                  |
| **source_lang**      | **str**                                       |                                                                  |
| **target_langs**     | **List[str]**                                 |                                                                  | [optional] |
| **previous_segment** | **str**                                       |                                                                  | [optional] |
| **next_segment**     | **str**                                       |                                                                  | [optional] |
| **tag_metadata**     | [**List[TagMetadataDto]**](TagMetadataDto.md) |                                                                  | [optional] |
| **trim_query**       | **bool**                                      | Remove leading and trailing whitespace from query. Default: true | [optional] |
| **phrase_query**     | **bool**                                      | Return both wildcard and exact search results. Default: true     | [optional] |

## Example

```python
from phrasetms_client.models.search_request_dto import SearchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestDto from a JSON string
search_request_dto_instance = SearchRequestDto.from_json(json)
# print the JSON string representation of the object
print SearchRequestDto.to_json()

# convert the object into a dict
search_request_dto_dict = search_request_dto_instance.to_dict()
# create an instance of SearchRequestDto from a dict
search_request_dto_from_dict = SearchRequestDto.from_dict(search_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
