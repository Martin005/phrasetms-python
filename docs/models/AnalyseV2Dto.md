# phrasetms_client.model.analyse_v2_dto.AnalyseV2Dto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                               | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                                                                                          |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **id**                                            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                     |
| **uid**                                           | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                     |
| **type**                                          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] must be one of ["PreAnalyse", "PostAnalyse", "PreAnalyseTarget", "Compare", "PreAnalyseProvider", ] |
| **name**                                          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                     |
| **provider**                                      | [**ProviderReference**](ProviderReference.md)                                                                                               | [**ProviderReference**](ProviderReference.md)                                           |                                                                    | [optional]                                                                                                     |
| **createdBy**                                     | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                                                                                     |
| **dateCreated**                                   | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time                                                            |
| **netRateScheme**                                 | [**NetRateSchemeReference**](NetRateSchemeReference.md)                                                                                     | [**NetRateSchemeReference**](NetRateSchemeReference.md)                                 |                                                                    | [optional]                                                                                                     |
| **[analyseLanguageParts](#analyseLanguageParts)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                                                                                     |
| **any_string_name**                               | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                                                                                     |

# analyseLanguageParts

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                  | Input Type                                                  | Accessed Type                                               | Description | Notes |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------- | ----- |
| [**AnalyseLanguagePartV2Dto**](AnalyseLanguagePartV2Dto.md) | [**AnalyseLanguagePartV2Dto**](AnalyseLanguagePartV2Dto.md) | [**AnalyseLanguagePartV2Dto**](AnalyseLanguagePartV2Dto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
