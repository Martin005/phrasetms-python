# openapi_client.model.async_file_op_response_dto.AsyncFileOpResponseDto

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
**fileName** | str,  | str,  |  | [optional] 
**action** | str,  | str,  |  | [optional] must be one of ["GUI_UPLOAD", "GUI_DOWNLOAD", "GUI_REIMPORT", "GUI_REIMPORT_TARGET", "CJ_UPLOAD", "CJ_DOWNLOAD", "APC_UPLOAD", "APC_DOWNLOAD", "API_UPLOAD", "API_DOWNLOAD", "SUBMITTER_PORTAL_DOWNLOAD", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

