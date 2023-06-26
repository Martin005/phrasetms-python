# MoraviaWarningDto

## Properties

| Name         | Type    | Description | Notes      |
| ------------ | ------- | ----------- | ---------- |
| **message**  | **str** |             | [optional] |
| **sub_type** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.moravia_warning_dto import MoraviaWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of MoraviaWarningDto from a JSON string
moravia_warning_dto_instance = MoraviaWarningDto.from_json(json)
# print the JSON string representation of the object
print MoraviaWarningDto.to_json()

# convert the object into a dict
moravia_warning_dto_dict = moravia_warning_dto_instance.to_dict()
# create an instance of MoraviaWarningDto from a dict
moravia_warning_dto_from_dict = MoraviaWarningDto.from_dict(moravia_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
