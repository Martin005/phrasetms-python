# VariableDto

## Properties

| Name      | Type    | Description | Notes      |
| --------- | ------- | ----------- | ---------- |
| **name**  | **str** |             | [optional] |
| **value** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.variable_dto import VariableDto

# TODO update the JSON string below
json = "{}"
# create an instance of VariableDto from a JSON string
variable_dto_instance = VariableDto.from_json(json)
# print the JSON string representation of the object
print VariableDto.to_json()

# convert the object into a dict
variable_dto_dict = variable_dto_instance.to_dict()
# create an instance of VariableDto from a dict
variable_dto_from_dict = VariableDto.from_dict(variable_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
