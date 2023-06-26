# MissingNumbersWarningDto

## Properties

| Name                | Type          | Description | Notes      |
| ------------------- | ------------- | ----------- | ---------- |
| **missing_numbers** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.missing_numbers_warning_dto import MissingNumbersWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of MissingNumbersWarningDto from a JSON string
missing_numbers_warning_dto_instance = MissingNumbersWarningDto.from_json(json)
# print the JSON string representation of the object
print MissingNumbersWarningDto.to_json()

# convert the object into a dict
missing_numbers_warning_dto_dict = missing_numbers_warning_dto_instance.to_dict()
# create an instance of MissingNumbersWarningDto from a dict
missing_numbers_warning_dto_from_dict = MissingNumbersWarningDto.from_dict(missing_numbers_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
