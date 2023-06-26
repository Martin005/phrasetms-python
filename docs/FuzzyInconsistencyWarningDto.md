# FuzzyInconsistencyWarningDto

## Properties

| Name            | Type          | Description | Notes      |
| --------------- | ------------- | ----------- | ---------- |
| **segment_ids** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.fuzzy_inconsistency_warning_dto import FuzzyInconsistencyWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of FuzzyInconsistencyWarningDto from a JSON string
fuzzy_inconsistency_warning_dto_instance = FuzzyInconsistencyWarningDto.from_json(json)
# print the JSON string representation of the object
print FuzzyInconsistencyWarningDto.to_json()

# convert the object into a dict
fuzzy_inconsistency_warning_dto_dict = fuzzy_inconsistency_warning_dto_instance.to_dict()
# create an instance of FuzzyInconsistencyWarningDto from a dict
fuzzy_inconsistency_warning_dto_from_dict = FuzzyInconsistencyWarningDto.from_dict(fuzzy_inconsistency_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
