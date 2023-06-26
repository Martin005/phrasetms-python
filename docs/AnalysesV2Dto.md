# AnalysesV2Dto

## Properties

| Name         | Type                                      | Description | Notes      |
| ------------ | ----------------------------------------- | ----------- | ---------- |
| **analyses** | [**List[AnalyseV2Dto]**](AnalyseV2Dto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.analyses_v2_dto import AnalysesV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysesV2Dto from a JSON string
analyses_v2_dto_instance = AnalysesV2Dto.from_json(json)
# print the JSON string representation of the object
print AnalysesV2Dto.to_json()

# convert the object into a dict
analyses_v2_dto_dict = analyses_v2_dto_instance.to_dict()
# create an instance of AnalysesV2Dto from a dict
analyses_v2_dto_from_dict = AnalysesV2Dto.from_dict(analyses_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
