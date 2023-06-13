# openapi_client.model.login_user_dto.LoginUserDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | [optional] 
**csrfToken** | str,  | str,  |  | [optional] 
**organization** | [**OrganizationReference**](OrganizationReference.md) | [**OrganizationReference**](OrganizationReference.md) |  | [optional] 
**edition** | [**EditionDto**](EditionDto.md) | [**EditionDto**](EditionDto.md) |  | [optional] 
**features** | [**FeaturesDto**](FeaturesDto.md) | [**FeaturesDto**](FeaturesDto.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

