# ProgressDto

## Properties

| Name               | Type    | Description | Notes      |
| ------------------ | ------- | ----------- | ---------- |
| **total_count**    | **int** |             | [optional] |
| **finished_count** | **int** |             | [optional] |
| **overdue_count**  | **int** |             | [optional] |

## Example

```python
from phrasetms_client.models.progress_dto import ProgressDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressDto from a JSON string
progress_dto_instance = ProgressDto.from_json(json)
# print the JSON string representation of the object
print ProgressDto.to_json()

# convert the object into a dict
progress_dto_dict = progress_dto_instance.to_dict()
# create an instance of ProgressDto from a dict
progress_dto_from_dict = ProgressDto.from_dict(progress_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
