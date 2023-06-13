# openapi_client.model.project_template_trans_memory_v2_dto.ProjectTemplateTransMemoryV2Dto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**targetLocale** | str,  | str,  |  | [optional] 
**workflowStep** | [**WorkflowStepReferenceV2**](WorkflowStepReferenceV2.md) | [**WorkflowStepReferenceV2**](WorkflowStepReferenceV2.md) |  | [optional] 
**readMode** | bool,  | BoolClass,  |  | [optional] 
**writeMode** | bool,  | BoolClass,  |  | [optional] 
**transMemory** | [**TransMemoryDtoV2**](TransMemoryDtoV2.md) | [**TransMemoryDtoV2**](TransMemoryDtoV2.md) |  | [optional] 
**penalty** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**applyPenaltyTo101Only** | bool,  | BoolClass,  |  | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

