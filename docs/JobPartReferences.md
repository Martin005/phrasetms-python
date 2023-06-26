# JobPartReferences

## Properties

| Name     | Type                                      | Description | Notes |
| -------- | ----------------------------------------- | ----------- | ----- |
| **jobs** | [**List[UidReference]**](UidReference.md) |             |

## Example

```python
from phrasetms_client.models.job_part_references import JobPartReferences

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartReferences from a JSON string
job_part_references_instance = JobPartReferences.from_json(json)
# print the JSON string representation of the object
print JobPartReferences.to_json()

# convert the object into a dict
job_part_references_dict = job_part_references_instance.to_dict()
# create an instance of JobPartReferences from a dict
job_part_references_from_dict = JobPartReferences.from_dict(job_part_references_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
