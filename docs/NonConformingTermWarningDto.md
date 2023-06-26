# NonConformingTermWarningDto

## Properties

| Name                       | Type                              | Description | Notes      |
| -------------------------- | --------------------------------- | ----------- | ---------- |
| **term**                   | **str**                           |             | [optional] |
| **positions**              | [**List[Position]**](Position.md) |             | [optional] |
| **suggested_target_terms** | [**List[Term]**](Term.md)         |             | [optional] |

## Example

```python
from phrasetms_client.models.non_conforming_term_warning_dto import NonConformingTermWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of NonConformingTermWarningDto from a JSON string
non_conforming_term_warning_dto_instance = NonConformingTermWarningDto.from_json(json)
# print the JSON string representation of the object
print NonConformingTermWarningDto.to_json()

# convert the object into a dict
non_conforming_term_warning_dto_dict = non_conforming_term_warning_dto_instance.to_dict()
# create an instance of NonConformingTermWarningDto from a dict
non_conforming_term_warning_dto_from_dict = NonConformingTermWarningDto.from_dict(non_conforming_term_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
