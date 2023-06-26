# AnalyseReference

## Properties

| Name                       | Type                                                                      | Description | Notes      |
| -------------------------- | ------------------------------------------------------------------------- | ----------- | ---------- |
| **id**                     | **str**                                                                   |             | [optional] |
| **uid**                    | **str**                                                                   |             | [optional] |
| **inner_id**               | **str**                                                                   |             | [optional] |
| **type**                   | **str**                                                                   |             | [optional] |
| **name**                   | **str**                                                                   |             | [optional] |
| **provider**               | [**ProviderReference**](ProviderReference.md)                             |             | [optional] |
| **created_by**             | [**UserReference**](UserReference.md)                                     |             | [optional] |
| **date_created**           | **datetime**                                                              |             | [optional] |
| **net_rate_scheme**        | [**NetRateSchemeReference**](NetRateSchemeReference.md)                   |             | [optional] |
| **analyse_language_parts** | [**List[AnalyseLanguagePartReference]**](AnalyseLanguagePartReference.md) |             | [optional] |
| **outdated**               | **bool**                                                                  |             | [optional] |
| **import_status**          | [**ImportStatusDto**](ImportStatusDto.md)                                 |             | [optional] |
| **pure_warnings**          | **List[str]**                                                             |             | [optional] |

## Example

```python
from phrasetms_client.models.analyse_reference import AnalyseReference

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyseReference from a JSON string
analyse_reference_instance = AnalyseReference.from_json(json)
# print the JSON string representation of the object
print AnalyseReference.to_json()

# convert the object into a dict
analyse_reference_dict = analyse_reference_instance.to_dict()
# create an instance of AnalyseReference from a dict
analyse_reference_from_dict = AnalyseReference.from_dict(analyse_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
