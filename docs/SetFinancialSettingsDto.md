# SetFinancialSettingsDto

## Properties

| Name                | Type                              | Description | Notes      |
| ------------------- | --------------------------------- | ----------- | ---------- |
| **net_rate_scheme** | [**IdReference**](IdReference.md) |             | [optional] |
| **price_list**      | [**IdReference**](IdReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.set_financial_settings_dto import SetFinancialSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetFinancialSettingsDto from a JSON string
set_financial_settings_dto_instance = SetFinancialSettingsDto.from_json(json)
# print the JSON string representation of the object
print SetFinancialSettingsDto.to_json()

# convert the object into a dict
set_financial_settings_dto_dict = set_financial_settings_dto_instance.to_dict()
# create an instance of SetFinancialSettingsDto from a dict
set_financial_settings_dto_from_dict = SetFinancialSettingsDto.from_dict(set_financial_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
