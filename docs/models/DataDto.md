# phrasetms_client.model.data_dto.DataDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                           | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **available**                 | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **estimate**                  | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **all**                       | [**CountsDto**](CountsDto.md)                                                                                                               | [**CountsDto**](CountsDto.md)                                                           |                                                                    | [optional] |
| **repetitions**               | [**CountsDto**](CountsDto.md)                                                                                                               | [**CountsDto**](CountsDto.md)                                                           |                                                                    | [optional] |
| **transMemoryMatches**        | [**MatchCounts101Dto**](MatchCounts101Dto.md)                                                                                               | [**MatchCounts101Dto**](MatchCounts101Dto.md)                                           |                                                                    | [optional] |
| **machineTranslationMatches** | [**MatchCountsDto**](MatchCountsDto.md)                                                                                                     | [**MatchCountsDto**](MatchCountsDto.md)                                                 |                                                                    | [optional] |
| **nonTranslatablesMatches**   | [**MatchCountsNTDto**](MatchCountsNTDto.md)                                                                                                 | [**MatchCountsNTDto**](MatchCountsNTDto.md)                                             |                                                                    | [optional] |
| **internalFuzzyMatches**      | [**MatchCountsDto**](MatchCountsDto.md)                                                                                                     | [**MatchCountsDto**](MatchCountsDto.md)                                                 |                                                                    | [optional] |
| **any_string_name**           | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
