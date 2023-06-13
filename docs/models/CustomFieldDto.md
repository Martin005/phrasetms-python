# openapi_client.model.custom_field_dto.CustomFieldDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uid** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["MULTI_SELECT", "SINGLE_SELECT", "STRING", "NUMBER", "URL", "DATE", ] 
**[allowedEntities](#allowedEntities)** | list, tuple,  | tuple,  |  | [optional] 
**options** | [**CustomFieldOptionsTruncatedDto**](CustomFieldOptionsTruncatedDto.md) | [**CustomFieldOptionsTruncatedDto**](CustomFieldOptionsTruncatedDto.md) |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**createdBy** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | [optional] 
**lastModified** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**lastModifiedBy** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | [optional] 
**requiredFrom** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**required** | bool,  | BoolClass,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# allowedEntities

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["PROJECT", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

