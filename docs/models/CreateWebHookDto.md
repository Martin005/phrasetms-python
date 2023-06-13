# openapi_client.model.create_web_hook_dto.CreateWebHookDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[events](#events)** | list, tuple,  | tuple,  |  | 
**url** | str,  | str,  |  | 
**name** | str,  | str,  |  | [optional] 
**secretToken** | str,  | str,  |  | [optional] 
**hidden** | bool,  | BoolClass,  | Default: false | [optional] 
**status** | str,  | str,  | Default: ENABLED | [optional] must be one of ["ENABLED", "DISABLED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# events

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["JOB_STATUS_CHANGED", "JOB_CREATED", "JOB_DELETED", "JOB_ASSIGNED", "JOB_DUE_DATE_CHANGED", "JOB_UPDATED", "JOB_TARGET_UPDATED", "JOB_EXPORTED", "JOB_UNEXPORTED", "PROJECT_CREATED", "PROJECT_DELETED", "PROJECT_STATUS_CHANGED", "PROJECT_DUE_DATE_CHANGED", "SHARED_PROJECT_ASSIGNED", "PROJECT_METADATA_UPDATED", "PRE_TRANSLATION_FINISHED", "ANALYSIS_CREATED", "CONTINUOUS_JOB_UPDATED", "PROJECT_TEMPLATE_CREATED", "PROJECT_TEMPLATE_UPDATED", "PROJECT_TEMPLATE_DELETED", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

