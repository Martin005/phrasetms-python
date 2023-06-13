# phrasetms_client.model.search_tm_segment_dto_v3.SearchTMSegmentDtoV3

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                             | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                     |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------- |
| **id**                          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **text**                        | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **lang**                        | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **rtl**                         | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                |
| **modifiedAt**                  | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 64 bit integer |
| **createdAt**                   | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 64 bit integer |
| **modifiedBy**                  | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                |
| **createdBy**                   | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                |
| **filename**                    | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **project**                     | [**SearchTMProjectDtoV3**](SearchTMProjectDtoV3.md)                                                                                         | [**SearchTMProjectDtoV3**](SearchTMProjectDtoV3.md)                                     |                                                                    | [optional]                                |
| **client**                      | [**SearchTMClientDtoV3**](SearchTMClientDtoV3.md)                                                                                           | [**SearchTMClientDtoV3**](SearchTMClientDtoV3.md)                                       |                                                                    | [optional]                                |
| **domain**                      | [**SearchTMDomainDtoV3**](SearchTMDomainDtoV3.md)                                                                                           | [**SearchTMDomainDtoV3**](SearchTMDomainDtoV3.md)                                       |                                                                    | [optional]                                |
| **subDomain**                   | [**SearchTMSubDomainDtoV3**](SearchTMSubDomainDtoV3.md)                                                                                     | [**SearchTMSubDomainDtoV3**](SearchTMSubDomainDtoV3.md)                                 |                                                                    | [optional]                                |
| **[tagMetadata](#tagMetadata)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                |
| **previousSegment**             | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **nextSegment**                 | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **key**                         | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **targetNote**                  | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **any_string_name**             | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                |

# tagMetadata

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                        | Input Type                        | Accessed Type                     | Description | Notes |
| --------------------------------- | --------------------------------- | --------------------------------- | ----------- | ----- |
| [**TagMetadata**](TagMetadata.md) | [**TagMetadata**](TagMetadata.md) | [**TagMetadata**](TagMetadata.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
