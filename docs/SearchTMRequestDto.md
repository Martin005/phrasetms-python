# SearchTMRequestDto

## Properties

| Name                 | Type                                          | Description | Notes      |
| -------------------- | --------------------------------------------- | ----------- | ---------- |
| **segment**          | **str**                                       |             |
| **workflow_level**   | **int**                                       |             | [optional] |
| **score_threshold**  | **float**                                     |             | [optional] |
| **previous_segment** | **str**                                       |             | [optional] |
| **next_segment**     | **str**                                       |             | [optional] |
| **context_key**      | **str**                                       |             | [optional] |
| **max_segments**     | **int**                                       | Default: 5  | [optional] |
| **max_sub_segments** | **int**                                       | Default: 5  | [optional] |
| **tag_metadata**     | [**List[TagMetadataDto]**](TagMetadataDto.md) |             | [optional] |
| **target_langs**     | **List[str]**                                 |             |

## Example

```python
from phrasetms_client.models.search_tm_request_dto import SearchTMRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMRequestDto from a JSON string
search_tm_request_dto_instance = SearchTMRequestDto.from_json(json)
# print the JSON string representation of the object
print SearchTMRequestDto.to_json()

# convert the object into a dict
search_tm_request_dto_dict = search_tm_request_dto_instance.to_dict()
# create an instance of SearchTMRequestDto from a dict
search_tm_request_dto_from_dict = SearchTMRequestDto.from_dict(search_tm_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
