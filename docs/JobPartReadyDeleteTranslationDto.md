# JobPartReadyDeleteTranslationDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**list[UidReference]**](UidReference.md) |  | [optional] 
**delete_settings** | [**TranslationSegmentsReferenceV2**](TranslationSegmentsReferenceV2.md) |  | [optional] 
**for_all_jobs** | **bool** | Set true if you want to delete translations for all jobs from project from specific workflow step.                Default: false | [optional] 
**workflow_level** | **int** | Specifies workflow level for all jobs | [optional] 
**filter** | [**JobPartReadyDeleteTranslationFilterDto**](JobPartReadyDeleteTranslationFilterDto.md) |  | [optional] 
**get_parts** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

