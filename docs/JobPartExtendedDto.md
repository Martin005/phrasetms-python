# JobPartExtendedDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] 
**inner_id** | **str** | InnerId is a sequential number of a job in a project. Jobs created from the same file share the same innerId across workflow steps. | [optional] 
**status** | **str** |  | [optional] 
**providers** | [**list[ProviderReference]**](ProviderReference.md) |  | [optional] 
**source_lang** | **str** |  | [optional] 
**target_lang** | **str** |  | [optional] 
**workflow_level** | **int** |  | [optional] 
**workflow_step** | [**ProjectWorkflowStepReference**](ProjectWorkflowStepReference.md) |  | [optional] 
**filename** | **str** |  | [optional] 
**date_due** | **datetime** |  | [optional] 
**words_count** | **int** |  | [optional] 
**begin_index** | **int** |  | [optional] 
**end_index** | **int** |  | [optional] 
**is_parent_job_split** | **bool** |  | [optional] 
**update_source_date** | **datetime** |  | [optional] 
**update_target_date** | **datetime** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**job_reference** | [**JobReference**](JobReference.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**last_workflow_level** | **int** |  | [optional] 
**work_unit** | [**ObjectReference**](ObjectReference.md) |  | [optional] 
**import_status** | [**ImportStatusDto**](ImportStatusDto.md) |  | [optional] 
**imported** | **bool** |  | [optional] 
**continuous** | **bool** |  | [optional] 
**continuous_job_info** | [**ContinuousJobInfoDto**](ContinuousJobInfoDto.md) |  | [optional] 
**original_file_directory** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

