# TargetFileWarningsDto

## Properties

| Name         | Type          | Description | Notes      |
| ------------ | ------------- | ----------- | ---------- |
| **warnings** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.target_file_warnings_dto import TargetFileWarningsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TargetFileWarningsDto from a JSON string
target_file_warnings_dto_instance = TargetFileWarningsDto.from_json(json)
# print the JSON string representation of the object
print TargetFileWarningsDto.to_json()

# convert the object into a dict
target_file_warnings_dto_dict = target_file_warnings_dto_instance.to_dict()
# create an instance of TargetFileWarningsDto from a dict
target_file_warnings_dto_from_dict = TargetFileWarningsDto.from_dict(target_file_warnings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
