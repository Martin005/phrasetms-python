# JobPartReferenceV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] 
**inner_id** | **str** | InnerId is a sequential number of a job in a project.             Jobs created from the same file share the same innerId across workflow steps | [optional] 
**status** | **str** |  | [optional] 
**providers** | [**list[ProviderReference]**](ProviderReference.md) |  | [optional] 
**target_lang** | **str** |  | [optional] 
**workflow_step** | [**ProjectWorkflowStepReference**](ProjectWorkflowStepReference.md) |  | [optional] 
**filename** | **str** |  | [optional] 
**original_file_directory** | **str** |  | [optional] 
**date_due** | **datetime** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**import_status** | [**ImportStatusDtoV2**](ImportStatusDtoV2.md) |  | [optional] 
**continuous** | **bool** |  | [optional] 
**source_file_uid** | **str** |  | [optional] 
**split** | **bool** |  | [optional] 
**server_task_id** | **str** |  | [optional] 
**owner** | [**UserReference**](UserReference.md) |  | [optional] 
**imported** | **bool** | Default: false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

