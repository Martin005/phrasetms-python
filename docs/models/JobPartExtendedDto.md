# openapi_client.model.job_part_extended_dto.JobPartExtendedDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uid** | str,  | str,  |  | [optional] 
**innerId** | str,  | str,  | InnerId is a sequential number of a job in a project. Jobs created from the same file share the same innerId across workflow steps. | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["NEW", "ACCEPTED", "DECLINED", "REJECTED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] 
**[providers](#providers)** | list, tuple,  | tuple,  |  | [optional] 
**sourceLang** | str,  | str,  |  | [optional] 
**targetLang** | str,  | str,  |  | [optional] 
**workflowLevel** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**workflowStep** | [**ProjectWorkflowStepReference**](ProjectWorkflowStepReference.md) | [**ProjectWorkflowStepReference**](ProjectWorkflowStepReference.md) |  | [optional] 
**filename** | str,  | str,  |  | [optional] 
**dateDue** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**wordsCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**beginIndex** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**endIndex** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**isParentJobSplit** | bool,  | BoolClass,  |  | [optional] 
**updateSourceDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**updateTargetDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**dateCreated** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**jobReference** | [**JobReference**](JobReference.md) | [**JobReference**](JobReference.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**lastWorkflowLevel** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[workUnit](#workUnit)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**importStatus** | [**ImportStatusDto**](ImportStatusDto.md) | [**ImportStatusDto**](ImportStatusDto.md) |  | [optional] 
**imported** | bool,  | BoolClass,  |  | [optional] 
**continuous** | bool,  | BoolClass,  |  | [optional] 
**continuousJobInfo** | [**ContinuousJobInfoDto**](ContinuousJobInfoDto.md) | [**ContinuousJobInfoDto**](ContinuousJobInfoDto.md) |  | [optional] 
**originalFileDirectory** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# providers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProviderReference**](ProviderReference.md) | [**ProviderReference**](ProviderReference.md) | [**ProviderReference**](ProviderReference.md) |  | 

# workUnit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
