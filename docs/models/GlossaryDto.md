# phrasetms_client.model.glossary_dto.GlossaryDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- |
| **name**                  | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **id**                    | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **uid**                   | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **internalId**            | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 64 bit integer           |
| **[langs](#langs)**       | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **createdBy**             | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                          |
| **owner**                 | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                          |
| **dateCreated**           | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **profileCount**          | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 32 bit integer           |
| **active**                | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                          |
| **[profiles](#profiles)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **any_string_name**       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                          |

# langs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# profiles

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                                      | Input Type                                                                      | Accessed Type                                                                   | Description | Notes |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------- | ----- |
| [**MemsourceTranslateProfileSimpleDto**](MemsourceTranslateProfileSimpleDto.md) | [**MemsourceTranslateProfileSimpleDto**](MemsourceTranslateProfileSimpleDto.md) | [**MemsourceTranslateProfileSimpleDto**](MemsourceTranslateProfileSimpleDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
