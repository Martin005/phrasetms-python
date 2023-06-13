# openapi_client.model.create_vendor_dto.CreateVendorDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vendorToken** | str,  | str,  |  | 
**netRateScheme** | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | [optional] 
**priceList** | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | [optional] 
**[sourceLocales](#sourceLocales)** | list, tuple,  | tuple,  |  | [optional] 
**[targetLocales](#targetLocales)** | list, tuple,  | tuple,  |  | [optional] 
**[clients](#clients)** | list, tuple,  | tuple,  |  | [optional] 
**[domains](#domains)** | list, tuple,  | tuple,  |  | [optional] 
**[subDomains](#subDomains)** | list, tuple,  | tuple,  |  | [optional] 
**[workflowSteps](#workflowSteps)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sourceLocales

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# targetLocales

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# clients

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | 

# domains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | 

# subDomains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | 

# workflowSteps

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

