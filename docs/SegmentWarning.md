# SegmentWarning

## Properties

| Name                    | Type     | Description | Notes      |
| ----------------------- | -------- | ----------- | ---------- |
| **id**                  | **str**  |             | [optional] |
| **ignored**             | **bool** |             | [optional] |
| **type**                | **str**  |             | [optional] |
| **repetition_group_id** | **str**  |             | [optional] |

## Example

```python
from phrasetms_client.models.segment_warning import SegmentWarning

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentWarning from a JSON string
segment_warning_instance = SegmentWarning.from_json(json)
# print the JSON string representation of the object
print SegmentWarning.to_json()

# convert the object into a dict
segment_warning_dict = segment_warning_instance.to_dict()
# create an instance of SegmentWarning from a dict
segment_warning_from_dict = SegmentWarning.from_dict(segment_warning_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
