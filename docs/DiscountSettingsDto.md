# DiscountSettingsDto

## Properties

| Name           | Type      | Description | Notes      |
| -------------- | --------- | ----------- | ---------- |
| **repetition** | **float** |             | [optional] |
| **tm101**      | **float** |             | [optional] |
| **tm100**      | **float** |             | [optional] |
| **tm95**       | **float** |             | [optional] |
| **tm85**       | **float** |             | [optional] |
| **tm75**       | **float** |             | [optional] |
| **tm50**       | **float** |             | [optional] |
| **tm0**        | **float** |             | [optional] |
| **mt100**      | **float** |             | [optional] |
| **mt95**       | **float** |             | [optional] |
| **mt85**       | **float** |             | [optional] |
| **mt75**       | **float** |             | [optional] |
| **mt50**       | **float** |             | [optional] |
| **mt0**        | **float** |             | [optional] |
| **nt100**      | **float** |             | [optional] |
| **nt99**       | **float** |             | [optional] |
| **nt85**       | **float** |             | [optional] |
| **nt75**       | **float** |             | [optional] |
| **nt50**       | **float** |             | [optional] |
| **nt0**        | **float** |             | [optional] |
| **if100**      | **float** |             | [optional] |
| **if95**       | **float** |             | [optional] |
| **if85**       | **float** |             | [optional] |
| **if75**       | **float** |             | [optional] |
| **if50**       | **float** |             | [optional] |
| **if0**        | **float** |             | [optional] |

## Example

```python
from phrasetms_client.models.discount_settings_dto import DiscountSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountSettingsDto from a JSON string
discount_settings_dto_instance = DiscountSettingsDto.from_json(json)
# print the JSON string representation of the object
print DiscountSettingsDto.to_json()

# convert the object into a dict
discount_settings_dto_dict = discount_settings_dto_instance.to_dict()
# create an instance of DiscountSettingsDto from a dict
discount_settings_dto_from_dict = DiscountSettingsDto.from_dict(discount_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
