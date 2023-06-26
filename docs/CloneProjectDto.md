# CloneProjectDto

## Properties

| Name     | Type    | Description | Notes |
| -------- | ------- | ----------- | ----- |
| **name** | **str** |             |

## Example

```python
from phrasetms_client.models.clone_project_dto import CloneProjectDto

# TODO update the JSON string below
json = "{}"
# create an instance of CloneProjectDto from a JSON string
clone_project_dto_instance = CloneProjectDto.from_json(json)
# print the JSON string representation of the object
print CloneProjectDto.to_json()

# convert the object into a dict
clone_project_dto_dict = clone_project_dto_instance.to_dict()
# create an instance of CloneProjectDto from a dict
clone_project_dto_from_dict = CloneProjectDto.from_dict(clone_project_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
