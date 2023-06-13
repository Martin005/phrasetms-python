# phrasetms_client.model.job_create_remote_file_dto.JobCreateRemoteFileDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                     | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **remoteFileName**      | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **connectorToken**      | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **remoteFolder**        | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **remoteFileNameRegex** | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **continuous**          | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **any_string_name**     | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
