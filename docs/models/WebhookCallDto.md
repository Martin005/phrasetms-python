# openapi_client.model.webhook_call_dto.WebhookCallDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uid** | str,  | str,  |  | [optional] 
**parentUid** | str,  | str,  |  | [optional] 
**eventUid** | str,  | str,  |  | [optional] 
**webhookSettings** | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**url** | str,  | str,  |  | [optional] 
**forced** | bool,  | BoolClass,  |  | [optional] 
**lastForcedAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**body** | str,  | str,  |  | [optional] 
**triggerEvent** | str,  | str,  |  | [optional] must be one of ["JOB_STATUS_CHANGED", "JOB_CREATED", "JOB_DELETED", "JOB_ASSIGNED", "JOB_DUE_DATE_CHANGED", "JOB_UPDATED", "JOB_TARGET_UPDATED", "JOB_EXPORTED", "JOB_UNEXPORTED", "PROJECT_CREATED", "PROJECT_DELETED", "PROJECT_STATUS_CHANGED", "PROJECT_DUE_DATE_CHANGED", "SHARED_PROJECT_ASSIGNED", "PROJECT_METADATA_UPDATED", "PRE_TRANSLATION_FINISHED", "ANALYSIS_CREATED", "CONTINUOUS_JOB_UPDATED", "PROJECT_TEMPLATE_CREATED", "PROJECT_TEMPLATE_UPDATED", "PROJECT_TEMPLATE_DELETED", ] 
**retryAttempt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**statusCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**errorMessage** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

