# openapi_client.model.async_request_dto.AsyncRequestDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**createdBy** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | [optional] 
**dateCreated** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**action** | str,  | str,  |  | [optional] must be one of ["PRE_ANALYSE", "POST_ANALYSE", "COMPARE_ANALYSE", "PARENT_ANALYSE", "PRE_TRANSLATE", "ASYNC_TRANSLATE", "IMPORT_JOB", "IMPORT_FILE", "ALIGN", "EXPORT_TMX_BY_QUERY", "EXPORT_TMX", "IMPORT_TMX", "INSERT_INTO_TM", "DELETE_TM", "CLEAR_TM", "QA", "QA_V3", "UPDATE_CONTINUOUS_JOB", "UPDATE_SOURCE", "UPDATE_TARGET", "EXTRACT_CLEANED_TMS", "GLOSSARY_PUT", "GLOSSARY_DELETE", "CREATE_PROJECT", "EXPORT_COMPLETE_FILE", ] 
**asyncResponse** | [**AsyncResponseDto**](AsyncResponseDto.md) | [**AsyncResponseDto**](AsyncResponseDto.md) |  | [optional] 
**parent** | [**AsyncRequestDto**](AsyncRequestDto.md) | [**AsyncRequestDto**](AsyncRequestDto.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

