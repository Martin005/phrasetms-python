# ProgressReference

## Properties

| Name               | Type      | Description | Notes      |
| ------------------ | --------- | ----------- | ---------- |
| **total_count**    | **int**   |             | [optional] |
| **finished_count** | **int**   |             | [optional] |
| **overdue_count**  | **int**   |             | [optional] |
| **finished_ratio** | **float** |             | [optional] |
| **overdue_ratio**  | **float** |             | [optional] |

## Example

```python
from phrasetms_client.models.progress_reference import ProgressReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressReference from a JSON string
progress_reference_instance = ProgressReference.from_json(json)
# print the JSON string representation of the object
print ProgressReference.to_json()

# convert the object into a dict
progress_reference_dict = progress_reference_instance.to_dict()
# create an instance of ProgressReference from a dict
progress_reference_from_dict = ProgressReference.from_dict(progress_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
