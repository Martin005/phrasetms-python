# openapi_client.model.job_part_patch_batch_dto.JobPartPatchBatchDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[jobs](#jobs)** | list, tuple,  | tuple,  |  | 
**status** | str,  | str,  |  | [optional] must be one of ["NEW", "ACCEPTED", "DECLINED", "REJECTED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] 
**dateDue** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**clearDateDue** | bool,  | BoolClass,  |  | [optional] 
**[providers](#providers)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# jobs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | 

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

