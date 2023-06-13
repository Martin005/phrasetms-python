# phrasetms_client.model.term_base_edit_dto.TermBaseEditDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **name**            | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **[langs](#langs)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    |
| **client**          | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional] |
| **domain**          | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional] |
| **subDomain**       | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional] |
| **businessUnit**    | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional] |
| **owner**           | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional] |
| **note**            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# langs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
