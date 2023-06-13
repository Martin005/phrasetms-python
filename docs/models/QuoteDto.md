# openapi_client.model.quote_dto.QuoteDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**uid** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["APPROVED", "DECLINED", "DRAFT", "FOR_APPROVAL", "NEW", ] 
**currency** | str,  | str,  |  | [optional] 
**billingUnit** | str,  | str,  |  | [optional] must be one of ["Character", "Word", "Page", "Hour", ] 
**createdBy** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | [optional] 
**dateCreated** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**totalPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**netRateScheme** | [**NetRateSchemeReference**](NetRateSchemeReference.md) | [**NetRateSchemeReference**](NetRateSchemeReference.md) |  | [optional] 
**priceList** | [**PriceListReference**](PriceListReference.md) | [**PriceListReference**](PriceListReference.md) |  | [optional] 
**[workflowStepList](#workflowStepList)** | list, tuple,  | tuple,  |  | [optional] 
**provider** | [**ProviderReference**](ProviderReference.md) | [**ProviderReference**](ProviderReference.md) |  | [optional] 
**customerEmail** | str,  | str,  |  | [optional] 
**quoteType** | str,  | str,  |  | [optional] must be one of ["BUYER", "PROVIDER", ] 
**editable** | bool,  | BoolClass,  |  | [optional] 
**outdated** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# workflowStepList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WorkflowStepReference**](WorkflowStepReference.md) | [**WorkflowStepReference**](WorkflowStepReference.md) | [**WorkflowStepReference**](WorkflowStepReference.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

