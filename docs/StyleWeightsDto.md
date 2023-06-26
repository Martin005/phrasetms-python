# StyleWeightsDto

## Properties

| Name                   | Type                                              | Description | Notes      |
| ---------------------- | ------------------------------------------------- | ----------- | ---------- |
| **style**              | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **awkward**            | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **company_style**      | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **inconsistent_style** | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **third_party_style**  | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **unidiomatic**        | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.style_weights_dto import StyleWeightsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StyleWeightsDto from a JSON string
style_weights_dto_instance = StyleWeightsDto.from_json(json)
# print the JSON string representation of the object
print StyleWeightsDto.to_json()

# convert the object into a dict
style_weights_dto_dict = style_weights_dto_instance.to_dict()
# create an instance of StyleWeightsDto from a dict
style_weights_dto_from_dict = StyleWeightsDto.from_dict(style_weights_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
