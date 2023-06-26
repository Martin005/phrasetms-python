# ForbiddenTermWarningDto

## Properties

| Name             | Type                              | Description | Notes      |
| ---------------- | --------------------------------- | ----------- | ---------- |
| **term**         | **str**                           |             | [optional] |
| **positions**    | [**List[Position]**](Position.md) |             | [optional] |
| **source_terms** | [**List[Term]**](Term.md)         |             | [optional] |

## Example

```python
from phrasetms_client.models.forbidden_term_warning_dto import ForbiddenTermWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenTermWarningDto from a JSON string
forbidden_term_warning_dto_instance = ForbiddenTermWarningDto.from_json(json)
# print the JSON string representation of the object
print ForbiddenTermWarningDto.to_json()

# convert the object into a dict
forbidden_term_warning_dto_dict = forbidden_term_warning_dto_instance.to_dict()
# create an instance of ForbiddenTermWarningDto from a dict
forbidden_term_warning_dto_from_dict = ForbiddenTermWarningDto.from_dict(forbidden_term_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
