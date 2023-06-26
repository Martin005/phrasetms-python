# NameDto

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **id**   | **str** |             | [optional] |
| **name** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.name_dto import NameDto

# TODO update the JSON string below
json = "{}"
# create an instance of NameDto from a JSON string
name_dto_instance = NameDto.from_json(json)
# print the JSON string representation of the object
print NameDto.to_json()

# convert the object into a dict
name_dto_dict = name_dto_instance.to_dict()
# create an instance of NameDto from a dict
name_dto_from_dict = NameDto.from_dict(name_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
