# ProgressDtoV2

## Properties

| Name               | Type    | Description | Notes      |
| ------------------ | ------- | ----------- | ---------- |
| **total_count**    | **int** |             | [optional] |
| **finished_count** | **int** |             | [optional] |
| **overdue_count**  | **int** |             | [optional] |

## Example

```python
from phrasetms_client.models.progress_dto_v2 import ProgressDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressDtoV2 from a JSON string
progress_dto_v2_instance = ProgressDtoV2.from_json(json)
# print the JSON string representation of the object
print ProgressDtoV2.to_json()

# convert the object into a dict
progress_dto_v2_dict = progress_dto_v2_instance.to_dict()
# create an instance of ProgressDtoV2 from a dict
progress_dto_v2_from_dict = ProgressDtoV2.from_dict(progress_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
