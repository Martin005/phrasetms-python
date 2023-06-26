# NonConformingTermWarningDtoAllOf

## Properties

| Name                       | Type                              | Description | Notes      |
| -------------------------- | --------------------------------- | ----------- | ---------- |
| **term**                   | **str**                           |             | [optional] |
| **positions**              | [**List[Position]**](Position.md) |             | [optional] |
| **suggested_target_terms** | [**List[Term]**](Term.md)         |             | [optional] |

## Example

```python
from phrasetms_client.models.non_conforming_term_warning_dto_all_of import NonConformingTermWarningDtoAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of NonConformingTermWarningDtoAllOf from a JSON string
non_conforming_term_warning_dto_all_of_instance = NonConformingTermWarningDtoAllOf.from_json(json)
# print the JSON string representation of the object
print NonConformingTermWarningDtoAllOf.to_json()

# convert the object into a dict
non_conforming_term_warning_dto_all_of_dict = non_conforming_term_warning_dto_all_of_instance.to_dict()
# create an instance of NonConformingTermWarningDtoAllOf from a dict
non_conforming_term_warning_dto_all_of_from_dict = NonConformingTermWarningDtoAllOf.from_dict(non_conforming_term_warning_dto_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
