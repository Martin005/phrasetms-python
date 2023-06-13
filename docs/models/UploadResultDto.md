# phrasetms_client.model.upload_result_dto.UploadResultDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------- |
| **id**              | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **name**            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **folder**          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **encodedName**     | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **size**            | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 64 bit integer |
| **error**           | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **asyncTaskId**     | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **errors**          | [**ConnectorErrorsDto**](ConnectorErrorsDto.md)                                                                                             | [**ConnectorErrorsDto**](ConnectorErrorsDto.md)                                         |                                                                    | [optional]                                |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
