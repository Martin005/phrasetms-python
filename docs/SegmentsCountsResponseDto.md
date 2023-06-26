# SegmentsCountsResponseDto

## Properties

| Name                  | Type                                              | Description | Notes      |
| --------------------- | ------------------------------------------------- | ----------- | ---------- |
| **job_part_uid**      | **str**                                           |             | [optional] |
| **counts**            | [**SegmentsCountsDto**](SegmentsCountsDto.md)     |             | [optional] |
| **previous_workflow** | [**PreviousWorkflowDto**](PreviousWorkflowDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.segments_counts_response_dto import SegmentsCountsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentsCountsResponseDto from a JSON string
segments_counts_response_dto_instance = SegmentsCountsResponseDto.from_json(json)
# print the JSON string representation of the object
print SegmentsCountsResponseDto.to_json()

# convert the object into a dict
segments_counts_response_dto_dict = segments_counts_response_dto_instance.to_dict()
# create an instance of SegmentsCountsResponseDto from a dict
segments_counts_response_dto_from_dict = SegmentsCountsResponseDto.from_dict(segments_counts_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
