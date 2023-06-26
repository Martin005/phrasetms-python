# AnalyseV2Dto

## Properties

| Name                       | Type                                                              | Description | Notes      |
| -------------------------- | ----------------------------------------------------------------- | ----------- | ---------- |
| **id**                     | **str**                                                           |             | [optional] |
| **uid**                    | **str**                                                           |             | [optional] |
| **type**                   | **str**                                                           |             | [optional] |
| **name**                   | **str**                                                           |             | [optional] |
| **provider**               | [**ProviderReference**](ProviderReference.md)                     |             | [optional] |
| **created_by**             | [**UserReference**](UserReference.md)                             |             | [optional] |
| **date_created**           | **datetime**                                                      |             | [optional] |
| **net_rate_scheme**        | [**NetRateSchemeReference**](NetRateSchemeReference.md)           |             | [optional] |
| **analyse_language_parts** | [**List[AnalyseLanguagePartV2Dto]**](AnalyseLanguagePartV2Dto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.analyse_v2_dto import AnalyseV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyseV2Dto from a JSON string
analyse_v2_dto_instance = AnalyseV2Dto.from_json(json)
# print the JSON string representation of the object
print AnalyseV2Dto.to_json()

# convert the object into a dict
analyse_v2_dto_dict = analyse_v2_dto_instance.to_dict()
# create an instance of AnalyseV2Dto from a dict
analyse_v2_dto_from_dict = AnalyseV2Dto.from_dict(analyse_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
