# openapi_client.model.job_part_update_source_dto.JobPartUpdateSourceDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uid** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["NEW", "ACCEPTED", "DECLINED", "REJECTED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] 
**targetLang** | str,  | str,  |  | [optional] 
**filename** | str,  | str,  |  | [optional] 
**workflowLevel** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**workflowStep** | [**WorkflowStepReference**](WorkflowStepReference.md) | [**WorkflowStepReference**](WorkflowStepReference.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

