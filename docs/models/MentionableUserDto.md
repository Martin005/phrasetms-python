# openapi_client.model.mentionable_user_dto.MentionableUserDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**firstName** | str,  | str,  |  | [optional] 
**lastName** | str,  | str,  |  | [optional] 
**userName** | str,  | str,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**role** | str,  | str,  |  | [optional] must be one of ["SYS_ADMIN", "SYS_ADMIN_READ", "ADMIN", "PROJECT_MANAGER", "LINGUIST", "GUEST", "SUBMITTER", ] 
**id** | str,  | str,  |  | [optional] 
**uid** | str,  | str,  |  | [optional] 
**unavailable** | bool,  | BoolClass,  |  | [optional] 
**[jobRoles](#jobRoles)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# jobRoles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**JobRoleDto**](JobRoleDto.md) | [**JobRoleDto**](JobRoleDto.md) | [**JobRoleDto**](JobRoleDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

