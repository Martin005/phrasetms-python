# SearchTMResponseDto

## Properties

| Name             | Type                                                    | Description | Notes      |
| ---------------- | ------------------------------------------------------- | ----------- | ---------- |
| **segment_id**   | **str**                                                 |             | [optional] |
| **source**       | [**SearchTMSegmentDto**](SearchTMSegmentDto.md)         |             | [optional] |
| **translations** | [**List[SearchTMSegmentDto]**](SearchTMSegmentDto.md)   |             | [optional] |
| **trans_memory** | [**SearchTMTransMemoryDto**](SearchTMTransMemoryDto.md) |             | [optional] |
| **gross_score**  | **float**                                               |             | [optional] |
| **score**        | **float**                                               |             | [optional] |
| **sub_segment**  | **bool**                                                |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tm_response_dto import SearchTMResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMResponseDto from a JSON string
search_tm_response_dto_instance = SearchTMResponseDto.from_json(json)
# print the JSON string representation of the object
print SearchTMResponseDto.to_json()

# convert the object into a dict
search_tm_response_dto_dict = search_tm_response_dto_instance.to_dict()
# create an instance of SearchTMResponseDto from a dict
search_tm_response_dto_from_dict = SearchTMResponseDto.from_dict(search_tm_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
