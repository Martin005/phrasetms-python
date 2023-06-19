# PreTranslateSettingsV3Dto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_translate_on_job_creation** | **bool** | Pre-translate &amp; set job to completed: Pre-translate on job creation. Default: false | [optional] 
**set_job_status_completed** | **bool** | Pre-translate &amp; set job to completed: Set job to completed once pre-translated. Default: false | [optional] 
**set_job_status_completed_when_confirmed** | **bool** | Pre-translate &amp; set job to completed when all segments confirmed: Set job to completed once pre-translated and all segments are confirmed. Default: false | [optional] 
**set_project_status_completed** | **bool** | Pre-translate &amp; set job to completed: Set project to completed once all jobs pre-translated.         Default: false | [optional] 
**overwrite_existing_translations** | **bool** | Overwrite existing translations in target segments. Default: false | [optional] 
**translation_memory_settings** | [**TranslationMemorySettingsDto**](TranslationMemorySettingsDto.md) |  | [optional] 
**machine_translation_settings** | [**MachineTranslationSettingsDto**](MachineTranslationSettingsDto.md) |  | [optional] 
**non_translatable_settings** | [**NonTranslatableSettingsDto**](NonTranslatableSettingsDto.md) |  | [optional] 
**repetitions_settings** | [**RepetitionsSettingsDto**](RepetitionsSettingsDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

