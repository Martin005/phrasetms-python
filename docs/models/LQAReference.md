# phrasetms_client.model.lqa_reference.LQAReference

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------- |
| **errorCategoryId** | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | value must be a 32 bit integer                           |
| **severityId**      | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | value must be a 32 bit integer                           |
| **user**            | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                               |
| **repeated**        | str,                                                                                                                                        | str,                                                                                    | Default: &#x60;NOT_REPEATED&#x60;                                  | [optional] must be one of ["REPEATED", "NOT_REPEATED", ] |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                               |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
