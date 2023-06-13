# phrasetms_client.model.marketo.Marketo

## Model Type Info

| Input Type                                                                                                                                              | Accessed Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------- | ----- |
| dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |             |

### Composed Schemas (allOf/anyOf/oneOf/not)

#### allOf

| Class Name                                      | Input Type                                          | Accessed Type                                       | Description | Notes |
| ----------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | ----------- | ----- |
| [AbstractConnectorDto](AbstractConnectorDto.md) | [**AbstractConnectorDto**](AbstractConnectorDto.md) | [**AbstractConnectorDto**](AbstractConnectorDto.md) |             |
| [all_of_1](#all_of_1)                           | dict, frozendict.frozendict,                        | frozendict.frozendict,                              |             |

# all_of_1

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                         | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **connectorType**           | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **apiKey**                  | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **identityURL**             | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **apiSecret**               | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **[variables](#variables)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **segmentationMapping**     | [**MarketoSegmentationMappingDto**](MarketoSegmentationMappingDto.md)                                                                       | [**MarketoSegmentationMappingDto**](MarketoSegmentationMappingDto.md)                   |                                                                    | [optional] |
| **translateTokens**         | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **debugMode**               | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **any_string_name**         | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# variables

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                        | Input Type                        | Accessed Type                     | Description | Notes |
| --------------------------------- | --------------------------------- | --------------------------------- | ----------- | ----- |
| [**VariableDto**](VariableDto.md) | [**VariableDto**](VariableDto.md) | [**VariableDto**](VariableDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
