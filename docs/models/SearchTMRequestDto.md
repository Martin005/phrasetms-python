# phrasetms_client.model.search_tm_request_dto.SearchTMRequestDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                             | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                     |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------- |
| **segment**                     | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **[targetLangs](#targetLangs)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    |
| **workflowLevel**               | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 32 bit integer |
| **scoreThreshold**              | decimal.Decimal, int, float,                                                                                                                | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 64 bit float   |
| **previousSegment**             | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **nextSegment**                 | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **contextKey**                  | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **maxSegments**                 | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        | Default: 5                                                         | [optional] value must be a 32 bit integer |
| **maxSubSegments**              | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        | Default: 5                                                         | [optional] value must be a 32 bit integer |
| **[tagMetadata](#tagMetadata)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                |
| **any_string_name**             | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                |

# targetLangs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# tagMetadata

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                              | Input Type                              | Accessed Type                           | Description | Notes |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | ----------- | ----- |
| [**TagMetadataDto**](TagMetadataDto.md) | [**TagMetadataDto**](TagMetadataDto.md) | [**TagMetadataDto**](TagMetadataDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
