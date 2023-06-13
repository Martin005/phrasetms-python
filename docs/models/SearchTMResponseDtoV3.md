# openapi_client.model.search_tm_response_dto_v3.SearchTMResponseDtoV3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**segmentId** | str,  | str,  |  | [optional] 
**source** | [**SearchTMSegmentDtoV3**](SearchTMSegmentDtoV3.md) | [**SearchTMSegmentDtoV3**](SearchTMSegmentDtoV3.md) |  | [optional] 
**[translations](#translations)** | list, tuple,  | tuple,  |  | [optional] 
**transMemory** | [**SearchTMTransMemoryDtoV3**](SearchTMTransMemoryDtoV3.md) | [**SearchTMTransMemoryDtoV3**](SearchTMTransMemoryDtoV3.md) |  | [optional] 
**grossScore** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**subSegment** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# translations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SearchTMSegmentDtoV3**](SearchTMSegmentDtoV3.md) | [**SearchTMSegmentDtoV3**](SearchTMSegmentDtoV3.md) | [**SearchTMSegmentDtoV3**](SearchTMSegmentDtoV3.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

