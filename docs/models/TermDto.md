# openapi_client.model.term_dto.TermDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | 
**id** | str,  | str,  |  | [optional] 
**lang** | str,  | str,  |  | [optional] 
**rtl** | bool,  | BoolClass,  |  | [optional] 
**modifiedAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**modifiedBy** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | [optional] 
**createdBy** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | [optional] 
**caseSensitive** | bool,  | BoolClass,  |  | [optional] 
**exactMatch** | bool,  | BoolClass,  |  | [optional] 
**forbidden** | bool,  | BoolClass,  |  | [optional] 
**preferred** | bool,  | BoolClass,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["New", "Approved", ] 
**conceptId** | str,  | str,  |  | [optional] 
**usage** | str,  | str,  |  | [optional] 
**note** | str,  | str,  |  | [optional] 
**writable** | bool,  | BoolClass,  |  | [optional] 
**shortTranslation** | str,  | str,  |  | [optional] 
**termType** | str,  | str,  |  | [optional] 
**partOfSpeech** | str,  | str,  |  | [optional] 
**gender** | str,  | str,  |  | [optional] 
**number** | str,  | str,  |  | [optional] 
**definition** | str,  | str,  |  | [optional] 
**domain** | str,  | str,  |  | [optional] 
**[subDomains](#subDomains)** | list, tuple,  | tuple,  |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**conceptNote** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subDomains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
