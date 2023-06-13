# openapi_client.model.service_provider_config_dto.ServiceProviderConfigDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[authenticationSchemes](#authenticationSchemes)** | list, tuple,  | tuple,  |  | [optional] 
**[schemas](#schemas)** | list, tuple,  | tuple,  |  | [optional] 
**patch** | [**Supported**](Supported.md) | [**Supported**](Supported.md) |  | [optional] 
**bulk** | [**Supported**](Supported.md) | [**Supported**](Supported.md) |  | [optional] 
**filter** | [**Supported**](Supported.md) | [**Supported**](Supported.md) |  | [optional] 
**changePassword** | [**Supported**](Supported.md) | [**Supported**](Supported.md) |  | [optional] 
**sort** | [**Supported**](Supported.md) | [**Supported**](Supported.md) |  | [optional] 
**etag** | [**Supported**](Supported.md) | [**Supported**](Supported.md) |  | [optional] 
**xmlDataFormat** | [**Supported**](Supported.md) | [**Supported**](Supported.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# authenticationSchemes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AuthSchema**](AuthSchema.md) | [**AuthSchema**](AuthSchema.md) | [**AuthSchema**](AuthSchema.md) |  | 

# schemas

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

