# openapi_client.model.job_part_ready_delete_translation_dto.JobPartReadyDeleteTranslationDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[jobs](#jobs)** | list, tuple,  | tuple,  |  | [optional] 
**deleteSettings** | [**TranslationSegmentsReferenceV2**](TranslationSegmentsReferenceV2.md) | [**TranslationSegmentsReferenceV2**](TranslationSegmentsReferenceV2.md) |  | [optional] 
**forAllJobs** | bool,  | BoolClass,  | Set true if you want to delete translations for all jobs from project from specific workflow step.                Default: false | [optional] 
**workflowLevel** | decimal.Decimal, int,  | decimal.Decimal,  | Specifies workflow level for all jobs | [optional] value must be a 32 bit integer
**filter** | [**JobPartReadyDeleteTranslationFilterDto**](JobPartReadyDeleteTranslationFilterDto.md) | [**JobPartReadyDeleteTranslationFilterDto**](JobPartReadyDeleteTranslationFilterDto.md) |  | [optional] 
**[getParts](#getParts)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
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

# getParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

