# JobReference

## Properties

| Name         | Type    | Description | Notes      |
| ------------ | ------- | ----------- | ---------- |
| **uid**      | **str** |             | [optional] |
| **filename** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.job_reference import JobReference

# TODO update the JSON string below
json = "{}"
# create an instance of JobReference from a JSON string
job_reference_instance = JobReference.from_json(json)
# print the JSON string representation of the object
print JobReference.to_json()

# convert the object into a dict
job_reference_dict = job_reference_instance.to_dict()
# create an instance of JobReference from a dict
job_reference_from_dict = JobReference.from_dict(job_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
