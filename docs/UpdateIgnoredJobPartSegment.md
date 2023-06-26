# UpdateIgnoredJobPartSegment

## Properties

| Name             | Type                                                      | Description | Notes |
| ---------------- | --------------------------------------------------------- | ----------- | ----- |
| **job_part_uid** | **str**                                                   |             |
| **segments**     | [**List[UpdateIgnoredSegment]**](UpdateIgnoredSegment.md) |             |

## Example

```python
from phrasetms_client.models.update_ignored_job_part_segment import UpdateIgnoredJobPartSegment

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIgnoredJobPartSegment from a JSON string
update_ignored_job_part_segment_instance = UpdateIgnoredJobPartSegment.from_json(json)
# print the JSON string representation of the object
print UpdateIgnoredJobPartSegment.to_json()

# convert the object into a dict
update_ignored_job_part_segment_dict = update_ignored_job_part_segment_instance.to_dict()
# create an instance of UpdateIgnoredJobPartSegment from a dict
update_ignored_job_part_segment_from_dict = UpdateIgnoredJobPartSegment.from_dict(update_ignored_job_part_segment_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
