# openapi_client.model.sdl_xlf_settings_dto.SdlXlfSettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**icuSubFilter** | bool,  | BoolClass,  | Default: false | [optional] 
**skipImportRules** | str,  | str,  | Default: translate&#x3D;no | [optional] 
**importAsConfirmedRules** | str,  | str,  |  | [optional] 
**importAsLockedRules** | str,  | str,  | Default: locked&#x3D;true | [optional] 
**exportAttrsWhenConfirmedAndLocked** | str,  | str,  | Default: locked&#x3D;true | [optional] 
**exportAttrsWhenConfirmedAndNotLocked** | str,  | str,  |  | [optional] 
**exportAttrsWhenNotConfirmedAndLocked** | str,  | str,  | Default: locked&#x3D;true | [optional] 
**exportAttrsWhenNotConfirmedAndNotLocked** | str,  | str,  |  | [optional] 
**saveConfirmedSegments** | bool,  | BoolClass,  | Default: true | [optional] 
**tagRegexp** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

