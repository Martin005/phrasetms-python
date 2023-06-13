# phrasetms_client.model.lqa_error_category_dto.LqaErrorCategoryDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                     | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                     |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------- |
| **errorCategoryId**                     | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 32 bit integer |
| **name**                                | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **enabled**                             | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                |
| **[errorCategories](#errorCategories)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                |
| **any_string_name**                     | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                |

# errorCategories

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                        | Input Type                                        | Accessed Type                                     | Description | Notes |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ----------- | ----- |
| [**LqaErrorCategoryDto**](LqaErrorCategoryDto.md) | [**LqaErrorCategoryDto**](LqaErrorCategoryDto.md) | [**LqaErrorCategoryDto**](LqaErrorCategoryDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
