# MissingNumbersV3WarningDto

## Properties

| Name          | Type                              | Description | Notes      |
| ------------- | --------------------------------- | ----------- | ---------- |
| **number**    | **str**                           |             | [optional] |
| **positions** | [**List[Position]**](Position.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.missing_numbers_v3_warning_dto import MissingNumbersV3WarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of MissingNumbersV3WarningDto from a JSON string
missing_numbers_v3_warning_dto_instance = MissingNumbersV3WarningDto.from_json(json)
# print the JSON string representation of the object
print MissingNumbersV3WarningDto.to_json()

# convert the object into a dict
missing_numbers_v3_warning_dto_dict = missing_numbers_v3_warning_dto_instance.to_dict()
# create an instance of MissingNumbersV3WarningDto from a dict
missing_numbers_v3_warning_dto_from_dict = MissingNumbersV3WarningDto.from_dict(missing_numbers_v3_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
