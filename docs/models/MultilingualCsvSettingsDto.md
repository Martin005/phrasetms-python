# openapi_client.model.multilingual_csv_settings_dto.MultilingualCsvSettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sourceColumns** | str,  | str,  |  | [optional] 
**targetColumns** | str,  | str,  |  | [optional] 
**contextNoteColumns** | str,  | str,  |  | [optional] 
**contextKeyColumns** | str,  | str,  |  | [optional] 
**tagRegexp** | str,  | str,  |  | [optional] 
**htmlSubFilter** | bool,  | BoolClass,  | Default: false | [optional] 
**segmentation** | bool,  | BoolClass,  | Default: true | [optional] 
**delimiter** | str,  | str,  | Default: , | [optional] 
**delimiterType** | str,  | str,  | Default: COMMA | [optional] must be one of ["TAB", "COMMA", "SEMICOLON", "OTHER", ] 
**importRows** | str,  | str,  |  | [optional] 
**maxLenColumns** | str,  | str,  |  | [optional] 
**[allTargetColumns](#allTargetColumns)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Format: \&quot;language\&quot;:\&quot;column\&quot;; example: {\&quot;en\&quot;: \&quot;A\&quot;, \&quot;sk\&quot;: \&quot;B\&quot;} | [optional] 
**nonEmptySegmentAction** | str,  | str,  |  | [optional] must be one of ["NONE", "CONFIRM", "LOCK", "CONFIRM_LOCK", ] 
**saveConfirmedSegmentsToTm** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# allTargetColumns

Format: \"language\":\"column\"; example: {\"en\": \"A\", \"sk\": \"B\"}

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Format: \&quot;language\&quot;:\&quot;column\&quot;; example: {\&quot;en\&quot;: \&quot;A\&quot;, \&quot;sk\&quot;: \&quot;B\&quot;} | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
