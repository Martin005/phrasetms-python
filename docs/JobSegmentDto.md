# JobSegmentDto

## Properties

| Name               | Type                                      | Description | Notes      |
| ------------------ | ----------------------------------------- | ----------- | ---------- |
| **id**             | **str**                                   |             | [optional] |
| **source**         | **str**                                   |             | [optional] |
| **translation**    | **str**                                   |             | [optional] |
| **created_at**     | **int**                                   |             | [optional] |
| **modified_at**    | **int**                                   |             | [optional] |
| **created_by**     | [**UserReference**](UserReference.md)     |             | [optional] |
| **modified_by**    | [**UserReference**](UserReference.md)     |             | [optional] |
| **workflow_level** | **int**                                   |             | [optional] |
| **workflow_step**  | [**WorkflowStepDto**](WorkflowStepDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_segment_dto import JobSegmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobSegmentDto from a JSON string
job_segment_dto_instance = JobSegmentDto.from_json(json)
# print the JSON string representation of the object
print JobSegmentDto.to_json()

# convert the object into a dict
job_segment_dto_dict = job_segment_dto_instance.to_dict()
# create an instance of JobSegmentDto from a dict
job_segment_dto_from_dict = JobSegmentDto.from_dict(job_segment_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
