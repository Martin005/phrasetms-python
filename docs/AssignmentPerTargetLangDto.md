# AssignmentPerTargetLangDto

## Properties

| Name            | Type                                                | Description | Notes      |
| --------------- | --------------------------------------------------- | ----------- | ---------- |
| **target_lang** | **str**                                             |             | [optional] |
| **providers**   | [**List[ProviderReference]**](ProviderReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.assignment_per_target_lang_dto import AssignmentPerTargetLangDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentPerTargetLangDto from a JSON string
assignment_per_target_lang_dto_instance = AssignmentPerTargetLangDto.from_json(json)
# print the JSON string representation of the object
print AssignmentPerTargetLangDto.to_json()

# convert the object into a dict
assignment_per_target_lang_dto_dict = assignment_per_target_lang_dto_instance.to_dict()
# create an instance of AssignmentPerTargetLangDto from a dict
assignment_per_target_lang_dto_from_dict = AssignmentPerTargetLangDto.from_dict(assignment_per_target_lang_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
