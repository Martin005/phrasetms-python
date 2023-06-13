# openapi_client.model.create_analyse_list_async_dto.CreateAnalyseListAsyncDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[jobs](#jobs)** | list, tuple,  | tuple,  |  | 
**type** | str,  | str,  | default: PreAnalyse | [optional] must be one of ["PreAnalyse", "PostAnalyse", "Compare", ] 
**includeFuzzyRepetitions** | bool,  | BoolClass,  | Default: true | [optional] 
**separateFuzzyRepetitions** | bool,  | BoolClass,  | Default: false | [optional] 
**includeConfirmedSegments** | bool,  | BoolClass,  | Default: true | [optional] 
**includeNumbers** | bool,  | BoolClass,  | Default: true | [optional] 
**includeLockedSegments** | bool,  | BoolClass,  | Default: true | [optional] 
**countSourceUnits** | bool,  | BoolClass,  | Default: true | [optional] 
**includeTransMemory** | bool,  | BoolClass,  | Default: true. Works only for type&#x3D;PreAnalyse. | [optional] 
**includeNonTranslatables** | bool,  | BoolClass,  | Default: false. Works only for type&#x3D;PreAnalyse. | [optional] 
**includeMachineTranslationMatches** | bool,  | BoolClass,  | Default: false. Works only for type&#x3D;PreAnalyse. | [optional] 
**transMemoryPostEditing** | bool,  | BoolClass,  | Default: false. Works only for type&#x3D;PostAnalyse. | [optional] 
**nonTranslatablePostEditing** | bool,  | BoolClass,  | Default: false. Works only for type&#x3D;PostAnalyse. | [optional] 
**machineTranslatePostEditing** | bool,  | BoolClass,  | Default: false. Works only for type&#x3D;PostAnalyse. | [optional] 
**name** | str,  | str,  |  | [optional] 
**netRateScheme** | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |  | [optional] 
**compareWorkflowLevel** | decimal.Decimal, int,  | decimal.Decimal,  | Required for type&#x3D;Compare | [optional] value must be a 32 bit integer
**useProjectAnalysisSettings** | bool,  | BoolClass,  | Default: false. Use default project settings. Will be overwritten with setting sent         in the API call. | [optional] 
**callbackUrl** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# jobs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

