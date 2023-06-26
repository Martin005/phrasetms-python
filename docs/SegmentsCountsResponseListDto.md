# SegmentsCountsResponseListDto

## Properties

| Name                        | Type                                                                | Description | Notes      |
| --------------------------- | ------------------------------------------------------------------- | ----------- | ---------- |
| **segments_counts_results** | [**List[SegmentsCountsResponseDto]**](SegmentsCountsResponseDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.segments_counts_response_list_dto import SegmentsCountsResponseListDto

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentsCountsResponseListDto from a JSON string
segments_counts_response_list_dto_instance = SegmentsCountsResponseListDto.from_json(json)
# print the JSON string representation of the object
print SegmentsCountsResponseListDto.to_json()

# convert the object into a dict
segments_counts_response_list_dto_dict = segments_counts_response_list_dto_instance.to_dict()
# create an instance of SegmentsCountsResponseListDto from a dict
segments_counts_response_list_dto_from_dict = SegmentsCountsResponseListDto.from_dict(segments_counts_response_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
