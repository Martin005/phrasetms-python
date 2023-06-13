# openapi_client.model.workflow_step_settings_edit_dto.WorkflowStepSettingsEditDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**workflowStep** | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |  | [optional] 
**[assignedTo](#assignedTo)** | list, tuple,  | tuple,  |  | [optional] 
**notifyProvider** | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md) | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md) |  | [optional] 
**lqaProfile** | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# assignedTo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProjectTemplateWorkflowSettingsAssignedToDto**](ProjectTemplateWorkflowSettingsAssignedToDto.md) | [**ProjectTemplateWorkflowSettingsAssignedToDto**](ProjectTemplateWorkflowSettingsAssignedToDto.md) | [**ProjectTemplateWorkflowSettingsAssignedToDto**](ProjectTemplateWorkflowSettingsAssignedToDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

