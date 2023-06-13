# openapi_client.model.job_part_patch_result_dto.JobPartPatchResultDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**updated** | decimal.Decimal, int,  | decimal.Decimal,  | Number of successfully updated job parts | [optional] value must be a 32 bit integer
**[errors](#errors)** | list, tuple,  | tuple,  | Errors and their counts encountered during the update | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

Errors and their counts encountered during the update

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Errors and their counts encountered during the update | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ErrorDetailDtoV3**](ErrorDetailDtoV3.md) | [**ErrorDetailDtoV3**](ErrorDetailDtoV3.md) | [**ErrorDetailDtoV3**](ErrorDetailDtoV3.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

