# SetProjectStatusDto

## Properties

| Name       | Type    | Description | Notes |
| ---------- | ------- | ----------- | ----- |
| **status** | **str** |             |

## Example

```python
from phrasetms_client.models.set_project_status_dto import SetProjectStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetProjectStatusDto from a JSON string
set_project_status_dto_instance = SetProjectStatusDto.from_json(json)
# print the JSON string representation of the object
print SetProjectStatusDto.to_json()

# convert the object into a dict
set_project_status_dto_dict = set_project_status_dto_instance.to_dict()
# create an instance of SetProjectStatusDto from a dict
set_project_status_dto_from_dict = SetProjectStatusDto.from_dict(set_project_status_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
