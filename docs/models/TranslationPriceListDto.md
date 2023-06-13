# phrasetms_client.model.translation_price_list_dto.TranslationPriceListDto

Price list with set of prices for language pairs

## Model Type Info

| Input Type                   | Accessed Type          | Description                                      | Notes |
| ---------------------------- | ---------------------- | ------------------------------------------------ | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, | Price list with set of prices for language pairs |

### Dictionary Keys

| Key                         | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------- |
| **name**                    | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **id**                      | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                        |
| **uid**                     | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                        |
| **dateCreated**             | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time               |
| **currencyCode**            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                        |
| **billingUnit**             | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] must be one of ["Character", "Word", "Page", "Hour", ] |
| **[priceSets](#priceSets)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                                        |
| **any_string_name**         | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                                        |

# priceSets

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                              | Input Type                                              | Accessed Type                                           | Description | Notes |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceSetDto**](TranslationPriceSetDto.md) | [**TranslationPriceSetDto**](TranslationPriceSetDto.md) | [**TranslationPriceSetDto**](TranslationPriceSetDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
