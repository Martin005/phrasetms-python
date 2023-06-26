# SegmentWarningsDto

## Properties

| Name               | Type                                          | Description | Notes      |
| ------------------ | --------------------------------------------- | ----------- | ---------- |
| **segment_id**     | **str**                                       |             | [optional] |
| **warnings**       | [**List[SegmentWarning]**](SegmentWarning.md) |             | [optional] |
| **ignored_checks** | **List[str]**                                 |             | [optional] |

## Example

```python
from phrasetms_client.models.segment_warnings_dto import SegmentWarningsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentWarningsDto from a JSON string
segment_warnings_dto_instance = SegmentWarningsDto.from_json(json)
# print the JSON string representation of the object
print SegmentWarningsDto.to_json()

# convert the object into a dict
segment_warnings_dto_dict = segment_warnings_dto_instance.to_dict()
# create an instance of SegmentWarningsDto from a dict
segment_warnings_dto_from_dict = SegmentWarningsDto.from_dict(segment_warnings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
