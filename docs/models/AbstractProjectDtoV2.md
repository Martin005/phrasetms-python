# openapi_client.model.abstract_project_dto_v2.AbstractProjectDtoV2

Base projectDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Base projectDto | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uid** | str,  | str,  |  | [optional] 
**internalId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**dateCreated** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**domain** | [**DomainReference**](DomainReference.md) | [**DomainReference**](DomainReference.md) |  | [optional] 
**subDomain** | [**SubDomainReference**](SubDomainReference.md) | [**SubDomainReference**](SubDomainReference.md) |  | [optional] 
**owner** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | [optional] 
**sourceLang** | str,  | str,  |  | [optional] 
**[targetLangs](#targetLangs)** | list, tuple,  | tuple,  |  | [optional] 
**[references](#references)** | list, tuple,  | tuple,  |  | [optional] 
**[mtSettingsPerLanguageList](#mtSettingsPerLanguageList)** | list, tuple,  | tuple,  |  | [optional] 
**userRole** | str,  | str,  | Response differs based on user&#x27;s role | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# targetLangs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# references

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReferenceFileReference**](ReferenceFileReference.md) | [**ReferenceFileReference**](ReferenceFileReference.md) | [**ReferenceFileReference**](ReferenceFileReference.md) |  | 

# mtSettingsPerLanguageList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MTSettingsPerLanguageReference**](MTSettingsPerLanguageReference.md) | [**MTSettingsPerLanguageReference**](MTSettingsPerLanguageReference.md) | [**MTSettingsPerLanguageReference**](MTSettingsPerLanguageReference.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

