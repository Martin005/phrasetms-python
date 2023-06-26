# TerminologyWarningDtoAllOf

## Properties

| Name                | Type          | Description | Notes      |
| ------------------- | ------------- | ----------- | ---------- |
| **missing_terms**   | **List[str]** |             | [optional] |
| **forbidden_terms** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.terminology_warning_dto_all_of import TerminologyWarningDtoAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of TerminologyWarningDtoAllOf from a JSON string
terminology_warning_dto_all_of_instance = TerminologyWarningDtoAllOf.from_json(json)
# print the JSON string representation of the object
print TerminologyWarningDtoAllOf.to_json()

# convert the object into a dict
terminology_warning_dto_all_of_dict = terminology_warning_dto_all_of_instance.to_dict()
# create an instance of TerminologyWarningDtoAllOf from a dict
terminology_warning_dto_all_of_from_dict = TerminologyWarningDtoAllOf.from_dict(terminology_warning_dto_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
