# openapi_client.model.assigned_job_dto.AssignedJobDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uid** | str,  | str,  |  | [optional] 
**innerId** | str,  | str,  |  | [optional] 
**filename** | str,  | str,  |  | [optional] 
**dateDue** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**dateCreated** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**status** | str,  | str,  |  | [optional] must be one of ["NEW", "ACCEPTED", "DECLINED", "REJECTED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] 
**targetLang** | str,  | str,  |  | [optional] 
**sourceLang** | str,  | str,  |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**workflowStep** | [**ProjectWorkflowStepReference**](ProjectWorkflowStepReference.md) | [**ProjectWorkflowStepReference**](ProjectWorkflowStepReference.md) |  | [optional] 
**importStatus** | [**ImportStatusDto**](ImportStatusDto.md) | [**ImportStatusDto**](ImportStatusDto.md) |  | [optional] 
**imported** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
