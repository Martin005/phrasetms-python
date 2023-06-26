# TerminologyWarningDto

## Properties

| Name                | Type          | Description | Notes      |
| ------------------- | ------------- | ----------- | ---------- |
| **missing_terms**   | **List[str]** |             | [optional] |
| **forbidden_terms** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.terminology_warning_dto import TerminologyWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of TerminologyWarningDto from a JSON string
terminology_warning_dto_instance = TerminologyWarningDto.from_json(json)
# print the JSON string representation of the object
print TerminologyWarningDto.to_json()

# convert the object into a dict
terminology_warning_dto_dict = terminology_warning_dto_instance.to_dict()
# create an instance of TerminologyWarningDto from a dict
terminology_warning_dto_from_dict = TerminologyWarningDto.from_dict(terminology_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
