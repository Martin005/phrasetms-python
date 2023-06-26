# UpdateIgnoredSegment

## Properties

| Name         | Type                                                      | Description | Notes |
| ------------ | --------------------------------------------------------- | ----------- | ----- |
| **uid**      | **str**                                                   |             |
| **warnings** | [**List[UpdateIgnoredWarning]**](UpdateIgnoredWarning.md) |             |

## Example

```python
from phrasetms_client.models.update_ignored_segment import UpdateIgnoredSegment

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIgnoredSegment from a JSON string
update_ignored_segment_instance = UpdateIgnoredSegment.from_json(json)
# print the JSON string representation of the object
print UpdateIgnoredSegment.to_json()

# convert the object into a dict
update_ignored_segment_dict = update_ignored_segment_instance.to_dict()
# create an instance of UpdateIgnoredSegment from a dict
update_ignored_segment_from_dict = UpdateIgnoredSegment.from_dict(update_ignored_segment_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
