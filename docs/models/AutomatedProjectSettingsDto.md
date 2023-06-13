# openapi_client.model.automated_project_settings_dto.AutomatedProjectSettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**organization** | [**NameDto**](NameDto.md) | [**NameDto**](NameDto.md) |  | [optional] 
**active** | bool,  | BoolClass,  |  | [optional] 
**sourceLang** | str,  | str,  |  | [optional] 
**[targetLangs](#targetLangs)** | list, tuple,  | tuple,  |  | [optional] 
**connector** | [**NameDto**](NameDto.md) | [**NameDto**](NameDto.md) |  | [optional] 
**remoteFolder** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# targetLangs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

