# openapi_client.model.abstract_user_edit_dto.AbstractUserEditDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**firstName** | str,  | str,  |  | 
**lastName** | str,  | str,  |  | 
**role** | str,  | str,  | Enum: \&quot;ADMIN\&quot;, \&quot;PROJECT_MANAGER\&quot;, \&quot;LINGUIST\&quot;, \&quot;GUEST\&quot;, \&quot;SUBMITTER\&quot; | must be one of ["SYS_ADMIN", "SYS_ADMIN_READ", "ADMIN", "PROJECT_MANAGER", "LINGUIST", "GUEST", "SUBMITTER", ] 
**timezone** | str,  | str,  |  | 
**userName** | str,  | str,  |  | 
**email** | str,  | str,  |  | 
**receiveNewsletter** | bool,  | BoolClass,  | Default: true | [optional] 
**note** | str,  | str,  |  | [optional] 
**active** | bool,  | BoolClass,  | Default: true | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
