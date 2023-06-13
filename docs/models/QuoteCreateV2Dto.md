# openapi_client.model.quote_create_v2_dto.QuoteCreateV2Dto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**analyse** | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |  | 
**name** | str,  | str,  |  | 
**project** | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | 
**priceList** | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |  | 
**netRateScheme** | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |  | [optional] 
**provider** | [**ProviderReference**](ProviderReference.md) | [**ProviderReference**](ProviderReference.md) |  | [optional] 
**[workflowSettings](#workflowSettings)** | list, tuple,  | tuple,  |  | [optional] 
**[units](#units)** | list, tuple,  | tuple,  |  | [optional] 
**[additionalSteps](#additionalSteps)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# workflowSettings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**QuoteWorkflowSettingDto**](QuoteWorkflowSettingDto.md) | [**QuoteWorkflowSettingDto**](QuoteWorkflowSettingDto.md) | [**QuoteWorkflowSettingDto**](QuoteWorkflowSettingDto.md) |  | 

# units

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**QuoteUnitsDto**](QuoteUnitsDto.md) | [**QuoteUnitsDto**](QuoteUnitsDto.md) | [**QuoteUnitsDto**](QuoteUnitsDto.md) |  | 

# additionalSteps

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

