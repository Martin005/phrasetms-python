# JobPartReadyReferences

## Properties

| Name          | Type                                      | Description | Notes      |
| ------------- | ----------------------------------------- | ----------- | ---------- |
| **jobs**      | [**List[UidReference]**](UidReference.md) |             | [optional] |
| **get_parts** | **object**                                |             | [optional] |

## Example

```python
from phrasetms_client.models.job_part_ready_references import JobPartReadyReferences

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartReadyReferences from a JSON string
job_part_ready_references_instance = JobPartReadyReferences.from_json(json)
# print the JSON string representation of the object
print JobPartReadyReferences.to_json()

# convert the object into a dict
job_part_ready_references_dict = job_part_ready_references_instance.to_dict()
# create an instance of JobPartReadyReferences from a dict
job_part_ready_references_from_dict = JobPartReadyReferences.from_dict(job_part_ready_references_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
