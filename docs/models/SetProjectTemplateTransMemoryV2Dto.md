# openapi_client.model.set_project_template_trans_memory_v2_dto.SetProjectTemplateTransMemoryV2Dto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**transMemory** | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | 
**readMode** | bool,  | BoolClass,  | Default: false | [optional] 
**writeMode** | bool,  | BoolClass,  | Can be set only for Translation Memory with read &#x3D;&#x3D; true.&lt;br/&gt;         Max 2 write TMs allowed per project.&lt;br/&gt;         Default: false | [optional] 
**penalty** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**applyPenaltyTo101Only** | bool,  | BoolClass,  | Can be set only for penalty &#x3D;&#x3D; 1&lt;br/&gt;Default: false | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

