# openapi_client.model.abstract_analyse_settings_dto.AbstractAnalyseSettingsDto

Base analyseSettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Base analyseSettingsDto | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Response differs based on analyse type | [optional] must be one of ["PreAnalyse", "PostAnalyse", "PreAnalyseTarget", "Compare", ] 
**includeConfirmedSegments** | bool,  | BoolClass,  | Default: false | [optional] 
**includeNumbers** | bool,  | BoolClass,  | Default: false | [optional] 
**includeLockedSegments** | bool,  | BoolClass,  | Default: false | [optional] 
**countSourceUnits** | bool,  | BoolClass,  | Default: false | [optional] 
**includeTransMemory** | bool,  | BoolClass,  | Default: false | [optional] 
**namingPattern** | str,  | str,  |  | [optional] 
**analyzeByLanguage** | bool,  | BoolClass,  | Default: false | [optional] 
**analyzeByProvider** | bool,  | BoolClass,  | Default: false | [optional] 
**allowAutomaticPostAnalysis** | bool,  | BoolClass,  | If automatic post analysis should be created after update source. Default: false | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
