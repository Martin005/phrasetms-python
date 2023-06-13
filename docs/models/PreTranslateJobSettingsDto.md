# openapi_client.model.pre_translate_job_settings_dto.PreTranslateJobSettingsDto

Pre-translate settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Pre-translate settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**autoPropagateRepetitions** | bool,  | BoolClass,  | Propagate repetitions. Default: false | [optional] 
**confirmRepetitions** | bool,  | BoolClass,  | Set segment status to confirmed for: Repetitions. Default: false | [optional] 
**setJobStatusCompleted** | bool,  | BoolClass,  | Pre-translate &amp; set job to completed: Set job to completed once pre-translated. Default: false | [optional] 
**setJobStatusCompletedWhenConfirmed** | bool,  | BoolClass,  | Pre-translate &amp; set job to completed when all segments confirmed: Set job to completed once pre-translated and all segments are confirmed. Default: false | [optional] 
**setProjectStatusCompleted** | bool,  | BoolClass,  | Pre-translate &amp; set job to completed: Set project to completed once all jobs pre-translated.         Default: false | [optional] 
**overwriteExistingTranslations** | bool,  | BoolClass,  | Overwrite existing translations in target segments. Default: false | [optional] 
**translationMemorySettings** | [**JobTranslationMemorySettingsDto**](JobTranslationMemorySettingsDto.md) | [**JobTranslationMemorySettingsDto**](JobTranslationMemorySettingsDto.md) |  | [optional] 
**machineTranslationSettings** | [**JobMachineTranslationSettingsDto**](JobMachineTranslationSettingsDto.md) | [**JobMachineTranslationSettingsDto**](JobMachineTranslationSettingsDto.md) |  | [optional] 
**nonTranslatableSettings** | [**JobNonTranslatableSettingsDto**](JobNonTranslatableSettingsDto.md) | [**JobNonTranslatableSettingsDto**](JobNonTranslatableSettingsDto.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

