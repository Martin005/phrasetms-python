# openapi_client.model.error_categories_dto.ErrorCategoriesDto

Error categories and their importance weight. If not provided, defaults will be created.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Error categories and their importance weight. If not provided, defaults will be created. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accuracy** | [**AccuracyWeightsDto**](AccuracyWeightsDto.md) | [**AccuracyWeightsDto**](AccuracyWeightsDto.md) |  | [optional] 
**fluency** | [**FluencyWeightsDto**](FluencyWeightsDto.md) | [**FluencyWeightsDto**](FluencyWeightsDto.md) |  | [optional] 
**terminology** | [**TerminologyWeightsDto**](TerminologyWeightsDto.md) | [**TerminologyWeightsDto**](TerminologyWeightsDto.md) |  | [optional] 
**style** | [**StyleWeightsDto**](StyleWeightsDto.md) | [**StyleWeightsDto**](StyleWeightsDto.md) |  | [optional] 
**localeConvention** | [**LocaleConventionWeightsDto**](LocaleConventionWeightsDto.md) | [**LocaleConventionWeightsDto**](LocaleConventionWeightsDto.md) |  | [optional] 
**verity** | [**VerityWeightsDto**](VerityWeightsDto.md) | [**VerityWeightsDto**](VerityWeightsDto.md) |  | [optional] 
**design** | [**DesignWeightsDto**](DesignWeightsDto.md) | [**DesignWeightsDto**](DesignWeightsDto.md) |  | [optional] 
**other** | [**OtherWeightsDto**](OtherWeightsDto.md) | [**OtherWeightsDto**](OtherWeightsDto.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

