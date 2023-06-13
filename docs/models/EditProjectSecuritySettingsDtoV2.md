# openapi_client.model.edit_project_security_settings_dto_v2.EditProjectSecuritySettingsDtoV2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**downloadEnabled** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**webEditorEnabledForLinguists** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**showUserDataToLinguists** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**emailNotifications** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**strictWorkflowFinish** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**useVendors** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**linguistsMayEditLockedSegments** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**usersMaySetAutoPropagation** | bool,  | BoolClass,  | Default: &#x60;true&#x60; | [optional] 
**allowLoadingExternalContentInEditors** | bool,  | BoolClass,  | Default: &#x60;true&#x60; | [optional] 
**allowLoadingIframes** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**linguistsMayEditSource** | bool,  | BoolClass,  | Default: &#x60;true&#x60; | [optional] 
**linguistsMayEditTagContent** | bool,  | BoolClass,  | Default: &#x60;true&#x60; | [optional] 
**linguistsMayDownloadLqaReport** | bool,  | BoolClass,  | Default: &#x60;true&#x60; | [optional] 
**usernamesDisplayedInLqaReport** | bool,  | BoolClass,  | Default: &#x60;true&#x60; | [optional] 
**userMaySetInstantQA** | bool,  | BoolClass,  | Default: &#x60;true&#x60; | [optional] 
**triggerWebhooks** | bool,  | BoolClass,  | Default: &#x60;true&#x60; | [optional] 
**notifyJobOwnerStatusChanged** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
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

