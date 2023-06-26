# JobPartSegmentsDtoV3

## Properties

| Name         | Type                                | Description | Notes |
| ------------ | ----------------------------------- | ----------- | ----- |
| **job**      | [**UidReference**](UidReference.md) |             |
| **segments** | **List[str]**                       |             |

## Example

```python
from phrasetms_client.models.job_part_segments_dto_v3 import JobPartSegmentsDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartSegmentsDtoV3 from a JSON string
job_part_segments_dto_v3_instance = JobPartSegmentsDtoV3.from_json(json)
# print the JSON string representation of the object
print JobPartSegmentsDtoV3.to_json()

# convert the object into a dict
job_part_segments_dto_v3_dict = job_part_segments_dto_v3_instance.to_dict()
# create an instance of JobPartSegmentsDtoV3 from a dict
job_part_segments_dto_v3_from_dict = JobPartSegmentsDtoV3.from_dict(job_part_segments_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
