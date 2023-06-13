# phrasetms_client.model.user_dto.UserDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                             | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                                                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **id**                          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **uid**                         | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **userName**                    | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **firstName**                   | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **lastName**                    | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **email**                       | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **dateCreated**                 | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time                                                                       |
| **dateDeleted**                 | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time                                                                       |
| **createdBy**                   | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                                                                                                |
| **role**                        | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] must be one of ["SYS_ADMIN", "SYS_ADMIN_READ", "ADMIN", "PROJECT_MANAGER", "LINGUIST", "GUEST", "SUBMITTER", ] |
| **timezone**                    | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **note**                        | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **terminologist**               | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                                                                                                |
| **[sourceLangs](#sourceLangs)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                                                                                                |
| **[targetLangs](#targetLangs)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                                                                                                |
| **active**                      | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                                                                                                |
| **priceList**                   | [**PriceListReference**](PriceListReference.md)                                                                                             | [**PriceListReference**](PriceListReference.md)                                         |                                                                    | [optional]                                                                                                                |
| **netRateScheme**               | [**DiscountSchemeReference**](DiscountSchemeReference.md)                                                                                   | [**DiscountSchemeReference**](DiscountSchemeReference.md)                               |                                                                    | [optional]                                                                                                                |
| **any_string_name**             | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                                                                                                |

# sourceLangs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# targetLangs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
