# openapi_client.model.search_tb_response_dto.SearchTbResponseDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**termBase** | [**TermBaseReference**](TermBaseReference.md) | [**TermBaseReference**](TermBaseReference.md) |  | [optional] 
**concept** | [**ConceptDtov2**](ConceptDtov2.md) | [**ConceptDtov2**](ConceptDtov2.md) |  | [optional] 
**sourceTerm** | [**TermV2Dto**](TermV2Dto.md) | [**TermV2Dto**](TermV2Dto.md) |  | [optional] 
**[translationTerms](#translationTerms)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# translationTerms

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TermV2Dto**](TermV2Dto.md) | [**TermV2Dto**](TermV2Dto.md) | [**TermV2Dto**](TermV2Dto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

