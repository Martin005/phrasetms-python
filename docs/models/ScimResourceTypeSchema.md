# phrasetms_client.model.scim_resource_type_schema.ScimResourceTypeSchema

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **[schemas](#schemas)**                   | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **id**                                    | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **name**                                  | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **endpoint**                              | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **description**                           | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **schema**                                | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **[schemaExtensions](#schemaExtensions)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **any_string_name**                       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# schemas

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# schemaExtensions

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                | Input Type                                | Accessed Type                             | Description | Notes |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------- | ----- |
| [**SchemaExtension**](SchemaExtension.md) | [**SchemaExtension**](SchemaExtension.md) | [**SchemaExtension**](SchemaExtension.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
