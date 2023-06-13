# phrasetms_client.model.export_by_query_dto.ExportByQueryDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                         | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                               |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- |
| **[queryLangs](#queryLangs)**               | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    |
| **[exportTargetLangs](#exportTargetLangs)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    |
| **[queries](#queries)**                     | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    |
| **createdAtMin**                            | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **createdAtMax**                            | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **modifiedAtMin**                           | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **modifiedAtMax**                           | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **createdBy**                               | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
| **modifiedBy**                              | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
| **filename**                                | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **project**                                 | [**UidReference**](UidReference.md)                                                                                                         | [**UidReference**](UidReference.md)                                                     |                                                                    | [optional]                                          |
| **callbackUrl**                             | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **any_string_name**                         | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                          |

# exportTargetLangs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# queries

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# queryLangs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
