# phrasetms_client.model.async_response_dto.AsyncResponseDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                               | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- |
| **dateCreated**                   | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **errorCode**                     | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **errorDesc**                     | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **[errorDetails](#errorDetails)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **[warnings](#warnings)**         | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **acceptedSegmentsCount**         | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 64 bit integer           |
| **any_string_name**               | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                          |

# errorDetails

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                              | Input Type                              | Accessed Type                           | Description | Notes |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | ----------- | ----- |
| [**ErrorDetailDto**](ErrorDetailDto.md) | [**ErrorDetailDto**](ErrorDetailDto.md) | [**ErrorDetailDto**](ErrorDetailDto.md) |             |

# warnings

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                              | Input Type                              | Accessed Type                           | Description | Notes |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | ----------- | ----- |
| [**ErrorDetailDto**](ErrorDetailDto.md) | [**ErrorDetailDto**](ErrorDetailDto.md) | [**ErrorDetailDto**](ErrorDetailDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
