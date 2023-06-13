# openapi_client.model.job_part_reference_v2.JobPartReferenceV2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uid** | str,  | str,  |  | [optional] 
**innerId** | str,  | str,  | InnerId is a sequential number of a job in a project.             Jobs created from the same file share the same innerId across workflow steps | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["NEW", "ACCEPTED", "DECLINED", "REJECTED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] 
**[providers](#providers)** | list, tuple,  | tuple,  |  | [optional] 
**targetLang** | str,  | str,  |  | [optional] 
**workflowStep** | [**ProjectWorkflowStepReference**](ProjectWorkflowStepReference.md) | [**ProjectWorkflowStepReference**](ProjectWorkflowStepReference.md) |  | [optional] 
**filename** | str,  | str,  |  | [optional] 
**originalFileDirectory** | str,  | str,  |  | [optional] 
**dateDue** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**dateCreated** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**importStatus** | [**ImportStatusDtoV2**](ImportStatusDtoV2.md) | [**ImportStatusDtoV2**](ImportStatusDtoV2.md) |  | [optional] 
**continuous** | bool,  | BoolClass,  |  | [optional] 
**sourceFileUid** | str,  | str,  |  | [optional] 
**split** | bool,  | BoolClass,  |  | [optional] 
**serverTaskId** | str,  | str,  |  | [optional] 
**owner** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | [optional] 
**imported** | bool,  | BoolClass,  | Default: false | [optional] 
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

