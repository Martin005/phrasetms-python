# ProjectTemplateDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**source_lang** | **str** |  | [optional] 
**target_langs** | **list[str]** |  | [optional] 
**note** | **str** |  | [optional] 
**use_dynamic_title** | **bool** |  | [optional] 
**dynamic_title** | **str** |  | [optional] 
**owner** | [**UserReference**](UserReference.md) |  | [optional] 
**client** | [**ClientReference**](ClientReference.md) |  | [optional] 
**domain** | [**DomainReference**](DomainReference.md) |  | [optional] 
**sub_domain** | [**SubDomainReference**](SubDomainReference.md) |  | [optional] 
**vendor** | [**VendorReference**](VendorReference.md) |  | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**modified_by** | [**UserReference**](UserReference.md) |  | [optional] 
**date_modified** | **datetime** | Deprecated - use dateTimeModified field instead | [optional] 
**date_time_modified** | **datetime** |  | [optional] 
**workflow_steps** | [**list[WorkflowStepDto]**](WorkflowStepDto.md) |  | [optional] 
**workflow_settings** | [**list[WorkflowStepSettingsDto]**](WorkflowStepSettingsDto.md) |  | [optional] 
**business_unit** | [**BusinessUnitReference**](BusinessUnitReference.md) |  | [optional] 
**notify_providers** | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md) |  | [optional] 
**assigned_to** | [**list[AssignmentPerTargetLangDto]**](AssignmentPerTargetLangDto.md) |  | [optional] 
**import_settings** | [**UidReference**](UidReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

