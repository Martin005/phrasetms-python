# ExtraNumbersWarningDto

## Properties

| Name              | Type          | Description | Notes      |
| ----------------- | ------------- | ----------- | ---------- |
| **extra_numbers** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.extra_numbers_warning_dto import ExtraNumbersWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraNumbersWarningDto from a JSON string
extra_numbers_warning_dto_instance = ExtraNumbersWarningDto.from_json(json)
# print the JSON string representation of the object
print ExtraNumbersWarningDto.to_json()

# convert the object into a dict
extra_numbers_warning_dto_dict = extra_numbers_warning_dto_instance.to_dict()
# create an instance of ExtraNumbersWarningDto from a dict
extra_numbers_warning_dto_from_dict = ExtraNumbersWarningDto.from_dict(extra_numbers_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
