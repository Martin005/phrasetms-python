# openapi_client.model.xlf2_settings_dto.Xlf2SettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**icuSubFilter** | bool,  | BoolClass,  | Default: false | [optional] 
**importNotes** | bool,  | BoolClass,  | Default: true | [optional] 
**saveConfirmedSegments** | bool,  | BoolClass,  | Default: true | [optional] 
**segmentation** | bool,  | BoolClass,  | Default: true | [optional] 
**lineBreakTags** | bool,  | BoolClass,  | Default: false | [optional] 
**preserveWhitespace** | bool,  | BoolClass,  | Default: true | [optional] 
**copySourceToTargetIfNotImported** | bool,  | BoolClass,  | Default: true | [optional] 
**respectTranslateAttr** | bool,  | BoolClass,  | Default: true | [optional] 
**skipImportRules** | str,  | str,  |  | [optional] 
**importAsConfirmedRules** | str,  | str,  | Default: state&#x3D;final | [optional] 
**importAsLockedRules** | str,  | str,  |  | [optional] 
**exportAttrsWhenConfirmedAndLocked** | str,  | str,  | Default: state&#x3D;final | [optional] 
**exportAttrsWhenConfirmedAndNotLocked** | str,  | str,  | Default: state&#x3D;final | [optional] 
**exportAttrsWhenNotConfirmedAndLocked** | str,  | str,  |  | [optional] 
**exportAttrsWhenNotConfirmedAndNotLocked** | str,  | str,  |  | [optional] 
**contextKeyXPath** | str,  | str,  |  | [optional] 
**preserveCharEntities** | str,  | str,  |  | [optional] 
**xslUrl** | str,  | str,  |  | [optional] 
**xslFile** | str,  | str,  | UID of uploaded XSL file, overrides xslUrl | [optional] 
**tagRegexp** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

