# SegmentReference

## Properties

| Name    | Type    | Description | Notes      |
| ------- | ------- | ----------- | ---------- |
| **uid** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.segment_reference import SegmentReference

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentReference from a JSON string
segment_reference_instance = SegmentReference.from_json(json)
# print the JSON string representation of the object
print SegmentReference.to_json()

# convert the object into a dict
segment_reference_dict = segment_reference_instance.to_dict()
# create an instance of SegmentReference from a dict
segment_reference_from_dict = SegmentReference.from_dict(segment_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
