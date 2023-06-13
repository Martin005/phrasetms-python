# phrasetms_client.model.job_list_dto.JobListDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **[unsupportedFiles](#unsupportedFiles)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **[jobs](#jobs)**                         | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **asyncRequest**                          | [**AsyncRequestReference**](AsyncRequestReference.md)                                                                                       | [**AsyncRequestReference**](AsyncRequestReference.md)                                   |                                                                    | [optional] |
| **any_string_name**                       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# unsupportedFiles

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# jobs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                  | Input Type                                  | Accessed Type                               | Description | Notes |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ----------- | ----- |
| [**JobPartReference**](JobPartReference.md) | [**JobPartReference**](JobPartReference.md) | [**JobPartReference**](JobPartReference.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
