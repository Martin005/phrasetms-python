# openapi_client.model.job_non_translatable_settings_dto.JobNonTranslatableSettingsDto

Non-translatables related settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Non-translatables related settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**preTranslateNonTranslatables** | bool,  | BoolClass,  | Pre-translate non-translatables. Default: true | [optional] 
**confirm100PercentMatches** | bool,  | BoolClass,  | Set segment status to confirmed for: 100% non-translatable matches. Default: false | [optional] 
**lock100PercentMatches** | bool,  | BoolClass,  | Lock section: 100% non-translatable matches. Default: false | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

