# openapi_client.model.search_request_dto.SearchRequestDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sourceLang** | str,  | str,  |  | 
**query** | str,  | str,  |  | 
**[targetLangs](#targetLangs)** | list, tuple,  | tuple,  |  | [optional] 
**previousSegment** | str,  | str,  |  | [optional] 
**nextSegment** | str,  | str,  |  | [optional] 
**[tagMetadata](#tagMetadata)** | list, tuple,  | tuple,  |  | [optional] 
**trimQuery** | bool,  | BoolClass,  | Remove leading and trailing whitespace from query. Default: true | [optional] 
**phraseQuery** | bool,  | BoolClass,  | Return both wildcard and exact search results. Default: true | [optional] 
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

# tagMetadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TagMetadataDto**](TagMetadataDto.md) | [**TagMetadataDto**](TagMetadataDto.md) | [**TagMetadataDto**](TagMetadataDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

