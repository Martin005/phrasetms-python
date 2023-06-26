# SubstituteDto

## Properties

| Name       | Type    | Description | Notes |
| ---------- | ------- | ----------- | ----- |
| **source** | **str** |             |
| **target** | **str** |             |

## Example

```python
from phrasetms_client.models.substitute_dto import SubstituteDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubstituteDto from a JSON string
substitute_dto_instance = SubstituteDto.from_json(json)
# print the JSON string representation of the object
print SubstituteDto.to_json()

# convert the object into a dict
substitute_dto_dict = substitute_dto_instance.to_dict()
# create an instance of SubstituteDto from a dict
substitute_dto_from_dict = SubstituteDto.from_dict(substitute_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
