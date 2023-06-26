# DesignWeightsDto

## Properties

| Name                 | Type                                              | Description | Notes      |
| -------------------- | ------------------------------------------------- | ----------- | ---------- |
| **design**           | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **length**           | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **local_formatting** | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **markup**           | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **missing_text**     | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **truncation**       | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.design_weights_dto import DesignWeightsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DesignWeightsDto from a JSON string
design_weights_dto_instance = DesignWeightsDto.from_json(json)
# print the JSON string representation of the object
print DesignWeightsDto.to_json()

# convert the object into a dict
design_weights_dto_dict = design_weights_dto_instance.to_dict()
# create an instance of DesignWeightsDto from a dict
design_weights_dto_from_dict = DesignWeightsDto.from_dict(design_weights_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
