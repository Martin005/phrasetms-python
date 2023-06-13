# phrasetms_client.model.login_to_session_v3_dto.LoginToSessionV3Dto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------- |
| **password**        | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **userName**        | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **userUid**         | str,                                                                                                                                        | str,                                                                                    | When not filled, default user of identity will be logged in        | [optional]                                |
| **rememberMe**      | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                |
| **twoFactorCode**   | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 32 bit integer |
| **captchaCode**     | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
