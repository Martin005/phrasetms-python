# VerityWeightsDto

## Properties

| Name                           | Type                                              | Description | Notes      |
| ------------------------------ | ------------------------------------------------- | ----------- | ---------- |
| **verity**                     | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **culture_specific_reference** | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.verity_weights_dto import VerityWeightsDto

# TODO update the JSON string below
json = "{}"
# create an instance of VerityWeightsDto from a JSON string
verity_weights_dto_instance = VerityWeightsDto.from_json(json)
# print the JSON string representation of the object
print VerityWeightsDto.to_json()

# convert the object into a dict
verity_weights_dto_dict = verity_weights_dto_instance.to_dict()
# create an instance of VerityWeightsDto from a dict
verity_weights_dto_from_dict = VerityWeightsDto.from_dict(verity_weights_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
