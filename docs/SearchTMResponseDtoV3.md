# SearchTMResponseDtoV3

## Properties

| Name             | Type                                                        | Description | Notes      |
| ---------------- | ----------------------------------------------------------- | ----------- | ---------- |
| **segment_id**   | **str**                                                     |             | [optional] |
| **source**       | [**SearchTMSegmentDtoV3**](SearchTMSegmentDtoV3.md)         |             | [optional] |
| **translations** | [**List[SearchTMSegmentDtoV3]**](SearchTMSegmentDtoV3.md)   |             | [optional] |
| **trans_memory** | [**SearchTMTransMemoryDtoV3**](SearchTMTransMemoryDtoV3.md) |             | [optional] |
| **gross_score**  | **float**                                                   |             | [optional] |
| **score**        | **float**                                                   |             | [optional] |
| **sub_segment**  | **bool**                                                    |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tm_response_dto_v3 import SearchTMResponseDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMResponseDtoV3 from a JSON string
search_tm_response_dto_v3_instance = SearchTMResponseDtoV3.from_json(json)
# print the JSON string representation of the object
print SearchTMResponseDtoV3.to_json()

# convert the object into a dict
search_tm_response_dto_v3_dict = search_tm_response_dto_v3_instance.to_dict()
# create an instance of SearchTMResponseDtoV3 from a dict
search_tm_response_dto_v3_from_dict = SearchTMResponseDtoV3.from_dict(search_tm_response_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
