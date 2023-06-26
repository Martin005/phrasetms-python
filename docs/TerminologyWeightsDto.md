# TerminologyWeightsDto

## Properties

| Name                                | Type                                              | Description | Notes      |
| ----------------------------------- | ------------------------------------------------- | ----------- | ---------- |
| **terminology**                     | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **inconsistent_with_tb**            | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |
| **inconsistent_use_of_terminology** | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.terminology_weights_dto import TerminologyWeightsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TerminologyWeightsDto from a JSON string
terminology_weights_dto_instance = TerminologyWeightsDto.from_json(json)
# print the JSON string representation of the object
print TerminologyWeightsDto.to_json()

# convert the object into a dict
terminology_weights_dto_dict = terminology_weights_dto_instance.to_dict()
# create an instance of TerminologyWeightsDto from a dict
terminology_weights_dto_from_dict = TerminologyWeightsDto.from_dict(terminology_weights_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
