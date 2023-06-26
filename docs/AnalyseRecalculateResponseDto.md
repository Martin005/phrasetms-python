# AnalyseRecalculateResponseDto

## Properties

| Name         | Type                                                            | Description | Notes      |
| ------------ | --------------------------------------------------------------- | ----------- | ---------- |
| **analyses** | [**List[AsyncAnalyseResponseDto]**](AsyncAnalyseResponseDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.analyse_recalculate_response_dto import AnalyseRecalculateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyseRecalculateResponseDto from a JSON string
analyse_recalculate_response_dto_instance = AnalyseRecalculateResponseDto.from_json(json)
# print the JSON string representation of the object
print AnalyseRecalculateResponseDto.to_json()

# convert the object into a dict
analyse_recalculate_response_dto_dict = analyse_recalculate_response_dto_instance.to_dict()
# create an instance of AnalyseRecalculateResponseDto from a dict
analyse_recalculate_response_dto_from_dict = AnalyseRecalculateResponseDto.from_dict(analyse_recalculate_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
