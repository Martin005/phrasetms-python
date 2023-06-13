# openapi_client.model.quality_assurance_checks_dto_v2.QualityAssuranceChecksDtoV2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[forbiddenStrings](#forbiddenStrings)** | list, tuple,  | tuple,  |  | [optional] 
**[enabledChecks](#enabledChecks)** | list, tuple,  | tuple,  | enabledChecks | [optional] 
**excludeLockedSegments** | bool,  | BoolClass,  |  | [optional] 
**userCanSetInstantQA** | bool,  | BoolClass,  |  | [optional] 
**strictJobStatus** | bool,  | BoolClass,  |  | [optional] 
**[regexpRules](#regexpRules)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# forbiddenStrings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# enabledChecks

enabledChecks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | enabledChecks | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EnabledCheckDtoV2**](EnabledCheckDtoV2.md) | [**EnabledCheckDtoV2**](EnabledCheckDtoV2.md) | [**EnabledCheckDtoV2**](EnabledCheckDtoV2.md) |  | 

# regexpRules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RegexpCheckRuleDtoV2**](RegexpCheckRuleDtoV2.md) | [**RegexpCheckRuleDtoV2**](RegexpCheckRuleDtoV2.md) | [**RegexpCheckRuleDtoV2**](RegexpCheckRuleDtoV2.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

