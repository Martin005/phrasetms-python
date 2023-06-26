# AnalyseV3Dto

## Properties

| Name                           | Type                                                              | Description | Notes      |
| ------------------------------ | ----------------------------------------------------------------- | ----------- | ---------- |
| **id**                         | **str**                                                           |             | [optional] |
| **uid**                        | **str**                                                           |             | [optional] |
| **inner_id**                   | **int**                                                           |             | [optional] |
| **type**                       | **str**                                                           |             | [optional] |
| **name**                       | **str**                                                           |             | [optional] |
| **provider**                   | [**ProviderReference**](ProviderReference.md)                     |             | [optional] |
| **created_by**                 | [**UserReference**](UserReference.md)                             |             | [optional] |
| **date_created**               | **datetime**                                                      |             | [optional] |
| **net_rate_scheme**            | [**NetRateSchemeReference**](NetRateSchemeReference.md)           |             | [optional] |
| **can_change_net_rate_scheme** | **bool**                                                          |             | [optional] |
| **analyse_language_parts**     | [**List[AnalyseLanguagePartV3Dto]**](AnalyseLanguagePartV3Dto.md) |             | [optional] |
| **settings**                   | [**AbstractAnalyseSettingsDto**](AbstractAnalyseSettingsDto.md)   |             | [optional] |
| **outdated**                   | **bool**                                                          |             | [optional] |
| **import_status**              | [**ImportStatusDto**](ImportStatusDto.md)                         |             | [optional] |
| **pure_warnings**              | **List[str]**                                                     |             | [optional] |
| **project**                    | [**ProjectReference**](ProjectReference.md)                       |             | [optional] |

## Example

```python
from phrasetms_client.models.analyse_v3_dto import AnalyseV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyseV3Dto from a JSON string
analyse_v3_dto_instance = AnalyseV3Dto.from_json(json)
# print the JSON string representation of the object
print AnalyseV3Dto.to_json()

# convert the object into a dict
analyse_v3_dto_dict = analyse_v3_dto_instance.to_dict()
# create an instance of AnalyseV3Dto from a dict
analyse_v3_dto_from_dict = AnalyseV3Dto.from_dict(analyse_v3_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
