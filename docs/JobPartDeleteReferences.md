# JobPartDeleteReferences

## Properties

| Name          | Type                                      | Description | Notes      |
| ------------- | ----------------------------------------- | ----------- | ---------- |
| **jobs**      | [**List[UidReference]**](UidReference.md) |             |
| **get_parts** | **object**                                |             | [optional] |

## Example

```python
from phrasetms_client.models.job_part_delete_references import JobPartDeleteReferences

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartDeleteReferences from a JSON string
job_part_delete_references_instance = JobPartDeleteReferences.from_json(json)
# print the JSON string representation of the object
print JobPartDeleteReferences.to_json()

# convert the object into a dict
job_part_delete_references_dict = job_part_delete_references_instance.to_dict()
# create an instance of JobPartDeleteReferences from a dict
job_part_delete_references_from_dict = JobPartDeleteReferences.from_dict(job_part_delete_references_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
