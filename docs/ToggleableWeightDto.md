# ToggleableWeightDto

## Properties

| Name        | Type      | Description                                      | Notes      |
| ----------- | --------- | ------------------------------------------------ | ---------- |
| **enabled** | **bool**  | If this error category is enabled, default false | [optional] |
| **weight**  | **float** | Weight of this error category (0.1 - 99.9)       | [optional] |
| **code**    | **int**   | Code of the error category                       | [optional] |

## Example

```python
from phrasetms_client.models.toggleable_weight_dto import ToggleableWeightDto

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleableWeightDto from a JSON string
toggleable_weight_dto_instance = ToggleableWeightDto.from_json(json)
# print the JSON string representation of the object
print ToggleableWeightDto.to_json()

# convert the object into a dict
toggleable_weight_dto_dict = toggleable_weight_dto_instance.to_dict()
# create an instance of ToggleableWeightDto from a dict
toggleable_weight_dto_from_dict = ToggleableWeightDto.from_dict(toggleable_weight_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
