# ForbiddenStringWarningDto

## Properties

| Name                 | Type                              | Description | Notes      |
| -------------------- | --------------------------------- | ----------- | ---------- |
| **forbidden_string** | **str**                           |             | [optional] |
| **positions**        | [**List[Position]**](Position.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.forbidden_string_warning_dto import ForbiddenStringWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenStringWarningDto from a JSON string
forbidden_string_warning_dto_instance = ForbiddenStringWarningDto.from_json(json)
# print the JSON string representation of the object
print ForbiddenStringWarningDto.to_json()

# convert the object into a dict
forbidden_string_warning_dto_dict = forbidden_string_warning_dto_instance.to_dict()
# create an instance of ForbiddenStringWarningDto from a dict
forbidden_string_warning_dto_from_dict = ForbiddenStringWarningDto.from_dict(forbidden_string_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
