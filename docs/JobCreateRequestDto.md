# JobCreateRequestDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_langs** | **list[str]** |  | 
**due** | **datetime** | only use for projects without workflows; otherwise specify in the workflowSettings object. Use ISO 8601 date format. | [optional] 
**workflow_settings** | [**list[WorkflowStepConfiguration]**](WorkflowStepConfiguration.md) |  | [optional] 
**assignments** | [**list[ProvidersPerLanguage]**](ProvidersPerLanguage.md) | only use for projects without workflows; otherwise specify in the workflowSettings object | [optional] 
**import_settings** | [**UidReference**](UidReference.md) |  | [optional] 
**use_project_file_import_settings** | **bool** | Default: false | [optional] 
**pre_translate** | **bool** |  | [optional] 
**notify_provider** | [**NotifyProviderDto**](NotifyProviderDto.md) |  | [optional] 
**callback_url** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**remote_file** | [**JobCreateRemoteFileDto**](JobCreateRemoteFileDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

