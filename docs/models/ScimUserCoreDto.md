# openapi_client.model.scim_user_core_dto.ScimUserCoreDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[emails](#emails)** | list, tuple,  | tuple,  |  | 
**name** | [**Name**](Name.md) | [**Name**](Name.md) |  | 
**userName** | str,  | str,  |  | 
**id** | str,  | str,  |  | [optional] 
**active** | bool,  | BoolClass,  | Default: true | [optional] 
**meta** | [**ScimMeta**](ScimMeta.md) | [**ScimMeta**](ScimMeta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# emails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Email**](Email.md) | [**Email**](Email.md) | [**Email**](Email.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

