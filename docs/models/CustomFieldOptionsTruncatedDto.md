# phrasetms_client.model.custom_field_options_truncated_dto.CustomFieldOptionsTruncatedDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                                                      | Notes                                     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **[truncatedOptions](#truncatedOptions)** | list, tuple,                                                                                                                                | tuple,                                                                                  | Truncated list of options with size 5. To get all options use endpoint for getting options of the specific field | [optional]                                |
| **remainingCount**                        | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                                                                  | [optional] value must be a 32 bit integer |
| **any_string_name**                       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                                               | [optional]                                |

# truncatedOptions

Truncated list of options with size 5. To get all options use endpoint for getting options of the specific field

## Model Type Info

| Input Type   | Accessed Type | Description                                                                                                      | Notes |
| ------------ | ------------- | ---------------------------------------------------------------------------------------------------------------- | ----- |
| list, tuple, | tuple,        | Truncated list of options with size 5. To get all options use endpoint for getting options of the specific field |

### Tuple Items

| Class Name                                          | Input Type                                          | Accessed Type                                       | Description | Notes |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | ----------- | ----- |
| [**CustomFieldOptionDto**](CustomFieldOptionDto.md) | [**CustomFieldOptionDto**](CustomFieldOptionDto.md) | [**CustomFieldOptionDto**](CustomFieldOptionDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
