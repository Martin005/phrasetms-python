# openapi_client.model.project_template_trans_memory_dto_v3.ProjectTemplateTransMemoryDtoV3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**targetLocale** | str,  | str,  |  | [optional] 
**workflowStep** | [**WorkflowStepReferenceV3**](WorkflowStepReferenceV3.md) | [**WorkflowStepReferenceV3**](WorkflowStepReferenceV3.md) |  | [optional] 
**readMode** | bool,  | BoolClass,  |  | [optional] 
**writeMode** | bool,  | BoolClass,  |  | [optional] 
**transMemory** | [**TransMemoryDtoV3**](TransMemoryDtoV3.md) | [**TransMemoryDtoV3**](TransMemoryDtoV3.md) |  | [optional] 
**penalty** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**applyPenaltyTo101Only** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

