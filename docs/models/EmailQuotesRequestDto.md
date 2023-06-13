# phrasetms_client.model.email_quotes_request_dto.EmailQuotesRequestDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                   | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **subject**           | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **body**              | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **[quotes](#quotes)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    |
| **cc**                | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **bcc**               | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **any_string_name**   | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# quotes

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
