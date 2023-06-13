# phrasetms_client.model.pseudo_translate_action_dto_v2.PseudoTranslateActionDtoV2

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                               | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------- |
| **replacement**                   | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **prefix**                        | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **suffix**                        | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **length**                        | decimal.Decimal, int, float,                                                                                                                | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 64 bit float   |
| **keyHashPrefixLen**              | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 32 bit integer |
| **[substitution](#substitution)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                |
| **any_string_name**               | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                |

# substitution

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                | Input Type                                | Accessed Type                             | Description | Notes |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------- | ----- |
| [**SubstituteDtoV2**](SubstituteDtoV2.md) | [**SubstituteDtoV2**](SubstituteDtoV2.md) | [**SubstituteDtoV2**](SubstituteDtoV2.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
