# openapi_client.model.patch_project_dto.PatchProjectDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["NEW", "ASSIGNED", "COMPLETED", "ACCEPTED_BY_VENDOR", "DECLINED_BY_VENDOR", "COMPLETED_BY_VENDOR", "CANCELLED", ] 
**client** | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |  | [optional] 
**businessUnit** | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |  | [optional] 
**domain** | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |  | [optional] 
**subDomain** | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |  | [optional] 
**owner** | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |  | [optional] 
**purchaseOrder** | str,  | str,  |  | [optional] 
**dateDue** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**note** | str,  | str,  |  | [optional] 
**machineTranslateSettings** | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | [optional] 
**[machineTranslateSettingsPerLangs](#machineTranslateSettingsPerLangs)** | list, tuple,  | tuple,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# machineTranslateSettingsPerLangs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProjectMTSettingsPerLangDto**](ProjectMTSettingsPerLangDto.md) | [**ProjectMTSettingsPerLangDto**](ProjectMTSettingsPerLangDto.md) | [**ProjectMTSettingsPerLangDto**](ProjectMTSettingsPerLangDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
