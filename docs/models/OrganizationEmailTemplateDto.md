# openapi_client.model.organization_email_template_dto.OrganizationEmailTemplateDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**uid** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["JobAssigned", "JobStatusChanged", "NextWorkflowStep", "JobRejected", "LoginInfo", "ProjectTransferredToBuyer", "SharedProjectAssigned", "SharedProjectStatusChanged", "AutomatedProjectCreated", "AutomatedProjectSourceUpdated", "AutomatedProjectStatusChanged", "JobWidgetProjectQuotePrepared", "JobWidgetProjectQuotePreparationFailure", "JobWidgetProjectCreated", "JobWidgetProjectCompleted", "CmsQuoteReady", "CmsWorkCompleted", "CmsJobRejected", "QUOTE_UPDATED", "QUOTE_STATUS_CHANGED", "LQA_SHARE_REPORT", ] 
**name** | str,  | str,  |  | [optional] 
**subject** | str,  | str,  |  | [optional] 
**body** | str,  | str,  |  | [optional] 
**ccAddress** | str,  | str,  |  | [optional] 
**bccAddress** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

