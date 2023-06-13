# phrasetms_client.model.custom_field_instance_api_dto.CustomFieldInstanceApiDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                     | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **customField**                         | [**UidReference**](UidReference.md)                                                                                                         | [**UidReference**](UidReference.md)                                                     |                                                                    | [optional] |
| **[selectedOptions](#selectedOptions)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **value**                               | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **any_string_name**                     | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# selectedOptions

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
