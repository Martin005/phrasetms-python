# openapi_client.model.project_security_settings_dto_v2.ProjectSecuritySettingsDtoV2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**downloadEnabled** | bool,  | BoolClass,  |  | [optional] 
**webEditorEnabledForLinguists** | bool,  | BoolClass,  |  | [optional] 
**showUserDataToLinguists** | bool,  | BoolClass,  |  | [optional] 
**emailNotifications** | bool,  | BoolClass,  |  | [optional] 
**strictWorkflowFinish** | bool,  | BoolClass,  |  | [optional] 
**useVendors** | bool,  | BoolClass,  |  | [optional] 
**linguistsMayEditLockedSegments** | bool,  | BoolClass,  |  | [optional] 
**usersMaySetAutoPropagation** | bool,  | BoolClass,  |  | [optional] 
**allowLoadingExternalContentInEditors** | bool,  | BoolClass,  |  | [optional] 
**allowLoadingIframes** | bool,  | BoolClass,  |  | [optional] 
**linguistsMayEditSource** | bool,  | BoolClass,  |  | [optional] 
**linguistsMayEditTagContent** | bool,  | BoolClass,  |  | [optional] 
**linguistsMayDownloadLqaReport** | bool,  | BoolClass,  |  | [optional] 
**usernamesDisplayedInLqaReport** | bool,  | BoolClass,  |  | [optional] 
**userMaySetInstantQA** | bool,  | BoolClass,  |  | [optional] 
**triggerWebhooks** | bool,  | BoolClass,  |  | [optional] 
**vendors** | [**VendorSecuritySettingsDto**](VendorSecuritySettingsDto.md) | [**VendorSecuritySettingsDto**](VendorSecuritySettingsDto.md) |  | [optional] 
**[allowedDomains](#allowedDomains)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# allowedDomains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

