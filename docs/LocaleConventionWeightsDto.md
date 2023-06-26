# LocaleConventionWeightsDto

## Properties

| Name                   | Type                                              | Description | Notes      |
| ---------------------- | ------------------------------------------------- | ----------- | ---------- |
| **locale_convention**  | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **address_format**     | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **date_format**        | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **currency_format**    | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **measurement_format** | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **shortcut_key**       | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **telephone_format**   | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.locale_convention_weights_dto import LocaleConventionWeightsDto

# TODO update the JSON string below
json = "{}"
# create an instance of LocaleConventionWeightsDto from a JSON string
locale_convention_weights_dto_instance = LocaleConventionWeightsDto.from_json(json)
# print the JSON string representation of the object
print LocaleConventionWeightsDto.to_json()

# convert the object into a dict
locale_convention_weights_dto_dict = locale_convention_weights_dto_instance.to_dict()
# create an instance of LocaleConventionWeightsDto from a dict
locale_convention_weights_dto_from_dict = LocaleConventionWeightsDto.from_dict(locale_convention_weights_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
