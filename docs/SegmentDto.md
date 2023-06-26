# SegmentDto

## Properties

| Name                        | Type                                          | Description | Notes      |
| --------------------------- | --------------------------------------------- | ----------- | ---------- |
| **target_lang**             | **str**                                       |             |
| **source_segment**          | **str**                                       |             |
| **target_segment**          | **str**                                       |             |
| **previous_source_segment** | **str**                                       |             | [optional] |
| **next_source_segment**     | **str**                                       |             | [optional] |
| **source_tag_metadata**     | [**List[TagMetadataDto]**](TagMetadataDto.md) |             | [optional] |
| **target_tag_metadata**     | [**List[TagMetadataDto]**](TagMetadataDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.segment_dto import SegmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentDto from a JSON string
segment_dto_instance = SegmentDto.from_json(json)
# print the JSON string representation of the object
print SegmentDto.to_json()

# convert the object into a dict
segment_dto_dict = segment_dto_instance.to_dict()
# create an instance of SegmentDto from a dict
segment_dto_from_dict = SegmentDto.from_dict(segment_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
