# openapi_client.model.pre_translate_jobs_v2_dto.PreTranslateJobsV2Dto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[jobs](#jobs)** | list, tuple,  | tuple,  | Jobs to be pre-translated | 
**[segmentFilters](#segmentFilters)** | list, tuple,  | tuple,  |  | [optional] 
**useProjectPreTranslateSettings** | bool,  | BoolClass,  | If pre-translate settings from project should be used. If true, preTranslateSettings values are ignored. Default: false | [optional] 
**callbackUrl** | str,  | str,  |  | [optional] 
**preTranslateSettings** | [**PreTranslateJobSettingsDto**](PreTranslateJobSettingsDto.md) | [**PreTranslateJobSettingsDto**](PreTranslateJobSettingsDto.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# jobs

Jobs to be pre-translated

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Jobs to be pre-translated | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | 

# segmentFilters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["LOCKED", "NOT_LOCKED", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

