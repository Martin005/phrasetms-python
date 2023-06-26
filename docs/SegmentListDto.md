# SegmentListDto

## Properties

| Name         | Type                                        | Description | Notes      |
| ------------ | ------------------------------------------- | ----------- | ---------- |
| **segments** | [**List[JobSegmentDto]**](JobSegmentDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.segment_list_dto import SegmentListDto

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentListDto from a JSON string
segment_list_dto_instance = SegmentListDto.from_json(json)
# print the JSON string representation of the object
print SegmentListDto.to_json()

# convert the object into a dict
segment_list_dto_dict = segment_list_dto_instance.to_dict()
# create an instance of SegmentListDto from a dict
segment_list_dto_from_dict = SegmentListDto.from_dict(segment_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
