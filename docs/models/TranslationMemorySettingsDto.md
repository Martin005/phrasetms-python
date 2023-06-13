# openapi_client.model.translation_memory_settings_dto.TranslationMemorySettingsDto

Translation memory related settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Translation memory related settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**useTranslationMemory** | bool,  | BoolClass,  | Pre-translate from translation memory. Default: false | [optional] 
**translationMemoryThreshold** | decimal.Decimal, int, float,  | decimal.Decimal,  | Pre-translation threshold percent | [optional] value must be a 64 bit float
**confirm100PercentMatches** | bool,  | BoolClass,  | Set segment status to confirmed for: 100% translation memory matches. Default: false | [optional] 
**confirm101PercentMatches** | bool,  | BoolClass,  | Set segment status to confirmed for: 101% translation memory matches. Default: false | [optional] 
**lock100PercentMatches** | bool,  | BoolClass,  | Lock section: 100% translation memory matches. Default: false | [optional] 
**lock101PercentMatches** | bool,  | BoolClass,  | Lock section: 101% translation memory matches. Default: false | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

