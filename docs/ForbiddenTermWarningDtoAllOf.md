# ForbiddenTermWarningDtoAllOf

## Properties

| Name             | Type                              | Description | Notes      |
| ---------------- | --------------------------------- | ----------- | ---------- |
| **term**         | **str**                           |             | [optional] |
| **positions**    | [**List[Position]**](Position.md) |             | [optional] |
| **source_terms** | [**List[Term]**](Term.md)         |             | [optional] |

## Example

```python
from phrasetms_client.models.forbidden_term_warning_dto_all_of import ForbiddenTermWarningDtoAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenTermWarningDtoAllOf from a JSON string
forbidden_term_warning_dto_all_of_instance = ForbiddenTermWarningDtoAllOf.from_json(json)
# print the JSON string representation of the object
print ForbiddenTermWarningDtoAllOf.to_json()

# convert the object into a dict
forbidden_term_warning_dto_all_of_dict = forbidden_term_warning_dto_all_of_instance.to_dict()
# create an instance of ForbiddenTermWarningDtoAllOf from a dict
forbidden_term_warning_dto_all_of_from_dict = ForbiddenTermWarningDtoAllOf.from_dict(forbidden_term_warning_dto_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
