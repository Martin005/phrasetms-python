# OtherWeightsDto

## Properties

| Name      | Type                                              | Description | Notes      |
| --------- | ------------------------------------------------- | ----------- | ---------- |
| **other** | [**ToggleableWeightDto**](ToggleableWeightDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.other_weights_dto import OtherWeightsDto

# TODO update the JSON string below
json = "{}"
# create an instance of OtherWeightsDto from a JSON string
other_weights_dto_instance = OtherWeightsDto.from_json(json)
# print the JSON string representation of the object
print OtherWeightsDto.to_json()

# convert the object into a dict
other_weights_dto_dict = other_weights_dto_instance.to_dict()
# create an instance of OtherWeightsDto from a dict
other_weights_dto_from_dict = OtherWeightsDto.from_dict(other_weights_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
