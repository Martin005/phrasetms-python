# openapi_client.model.file_dto.FileDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**encodedName** | str,  | str,  |  | [optional] 
**contentType** | str,  | str,  |  | [optional] 
**note** | str,  | str,  |  | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**directory** | bool,  | BoolClass,  |  | [optional] 
**lastModified** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**selected** | bool,  | BoolClass,  |  | [optional] 
**error** | [**ErrorDto**](ErrorDto.md) | [**ErrorDto**](ErrorDto.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

