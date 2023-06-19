# ProjectTemplateEditDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**template_name** | **str** |  | 
**source_lang** | **str** |  | [optional] 
**target_langs** | **list[str]** |  | [optional] 
**use_dynamic_title** | **bool** |  | [optional] 
**dynamic_title** | **str** |  | [optional] 
**notify_provider** | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md) |  | [optional] 
**work_flow_settings** | [**list[WorkflowStepSettingsEditDto]**](WorkflowStepSettingsEditDto.md) |  | [optional] 
**client** | [**IdReference**](IdReference.md) |  | [optional] 
**cost_center** | [**IdReference**](IdReference.md) |  | [optional] 
**business_unit** | [**IdReference**](IdReference.md) |  | [optional] 
**domain** | [**IdReference**](IdReference.md) |  | [optional] 
**sub_domain** | [**IdReference**](IdReference.md) |  | [optional] 
**vendor** | [**IdReference**](IdReference.md) |  | [optional] 
**import_settings** | [**UidReference**](UidReference.md) |  | [optional] 
**note** | **str** |  | [optional] 
**file_handover** | **bool** | Default: false | [optional] 
**assigned_to** | [**list[ProjectTemplateWorkflowSettingsAssignedToDto]**](ProjectTemplateWorkflowSettingsAssignedToDto.md) | only use for projects without workflows; otherwise specify in the workflowSettings object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

