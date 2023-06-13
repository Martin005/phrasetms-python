# openapi_client.model.analyse_language_part_v2_dto.AnalyseLanguagePartV2Dto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**sourceLang** | str,  | str,  |  | [optional] 
**targetLang** | str,  | str,  |  | [optional] 
**data** | [**DataDto**](DataDto.md) | [**DataDto**](DataDto.md) |  | [optional] 
**discountedData** | [**DataDto**](DataDto.md) | [**DataDto**](DataDto.md) |  | [optional] 
**[jobs](#jobs)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# jobs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AnalyseJobReference**](AnalyseJobReference.md) | [**AnalyseJobReference**](AnalyseJobReference.md) | [**AnalyseJobReference**](AnalyseJobReference.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

