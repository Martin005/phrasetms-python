# phrasetms_client.model.file_list_dto.FileListDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **[files](#files)**                       | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **currentFolder**                         | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **encodedCurrentFolder**                  | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **rootFolder**                            | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **[lastChangedFiles](#lastChangedFiles)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **any_string_name**                       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# files

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                | Input Type                | Accessed Type             | Description | Notes |
| ------------------------- | ------------------------- | ------------------------- | ----------- | ----- |
| [**FileDto**](FileDto.md) | [**FileDto**](FileDto.md) | [**FileDto**](FileDto.md) |             |

# lastChangedFiles

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                | Input Type                | Accessed Type             | Description | Notes |
| ------------------------- | ------------------------- | ------------------------- | ----------- | ----- |
| [**FileDto**](FileDto.md) | [**FileDto**](FileDto.md) | [**FileDto**](FileDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
