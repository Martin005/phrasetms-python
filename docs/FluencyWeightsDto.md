# FluencyWeightsDto

## Properties

| Name                     | Type                                              | Description | Notes      |
| ------------------------ | ------------------------------------------------- | ----------- | ---------- |
| **fluency**              | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **punctuation**          | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **spelling**             | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **grammar**              | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **grammatical_register** | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **inconsistency**        | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **cross_reference**      | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **character_encoding**   | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.fluency_weights_dto import FluencyWeightsDto

# TODO update the JSON string below
json = "{}"
# create an instance of FluencyWeightsDto from a JSON string
fluency_weights_dto_instance = FluencyWeightsDto.from_json(json)
# print the JSON string representation of the object
print FluencyWeightsDto.to_json()

# convert the object into a dict
fluency_weights_dto_dict = fluency_weights_dto_instance.to_dict()
# create an instance of FluencyWeightsDto from a dict
fluency_weights_dto_from_dict = FluencyWeightsDto.from_dict(fluency_weights_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
