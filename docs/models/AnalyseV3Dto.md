# phrasetms_client.model.analyse_v3_dto.AnalyseV3Dto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                               | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                                                                                          |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **id**                                            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                     |
| **uid**                                           | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                     |
| **innerId**                                       | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 32 bit integer                                                                      |
| **type**                                          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] must be one of ["PreAnalyse", "PostAnalyse", "PreAnalyseTarget", "Compare", "PreAnalyseProvider", ] |
| **name**                                          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                     |
| **provider**                                      | [**ProviderReference**](ProviderReference.md)                                                                                               | [**ProviderReference**](ProviderReference.md)                                           |                                                                    | [optional]                                                                                                     |
| **createdBy**                                     | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                                                                                     |
| **dateCreated**                                   | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time                                                            |
| **netRateScheme**                                 | [**NetRateSchemeReference**](NetRateSchemeReference.md)                                                                                     | [**NetRateSchemeReference**](NetRateSchemeReference.md)                                 |                                                                    | [optional]                                                                                                     |
| **canChangeNetRateScheme**                        | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                                                                                     |
| **[analyseLanguageParts](#analyseLanguageParts)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                                                                                     |
| **settings**                                      | [**AbstractAnalyseSettingsDto**](AbstractAnalyseSettingsDto.md)                                                                             | [**AbstractAnalyseSettingsDto**](AbstractAnalyseSettingsDto.md)                         |                                                                    | [optional]                                                                                                     |
| **outdated**                                      | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                                                                                     |
| **importStatus**                                  | [**ImportStatusDto**](ImportStatusDto.md)                                                                                                   | [**ImportStatusDto**](ImportStatusDto.md)                                               |                                                                    | [optional]                                                                                                     |
| **[pureWarnings](#pureWarnings)**                 | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                                                                                     |
| **project**                                       | [**ProjectReference**](ProjectReference.md)                                                                                                 | [**ProjectReference**](ProjectReference.md)                                             |                                                                    | [optional]                                                                                                     |
| **any_string_name**                               | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                                                                                     |

# analyseLanguageParts

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                  | Input Type                                                  | Accessed Type                                               | Description | Notes |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------- | ----- |
| [**AnalyseLanguagePartV3Dto**](AnalyseLanguagePartV3Dto.md) | [**AnalyseLanguagePartV3Dto**](AnalyseLanguagePartV3Dto.md) | [**AnalyseLanguagePartV3Dto**](AnalyseLanguagePartV3Dto.md) |             |

# pureWarnings

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
