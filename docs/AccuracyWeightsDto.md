# AccuracyWeightsDto

## Properties

| Name                  | Type                                              | Description | Notes      |
| --------------------- | ------------------------------------------------- | ----------- | ---------- |
| **accuracy**          | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **addition**          | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **omission**          | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **mistranslation**    | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **under_translation** | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **untranslated**      | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **improper_tm_match** | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **over_translation**  | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.accuracy_weights_dto import AccuracyWeightsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccuracyWeightsDto from a JSON string
accuracy_weights_dto_instance = AccuracyWeightsDto.from_json(json)
# print the JSON string representation of the object
print AccuracyWeightsDto.to_json()

# convert the object into a dict
accuracy_weights_dto_dict = accuracy_weights_dto_instance.to_dict()
# create an instance of AccuracyWeightsDto from a dict
accuracy_weights_dto_from_dict = AccuracyWeightsDto.from_dict(accuracy_weights_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
