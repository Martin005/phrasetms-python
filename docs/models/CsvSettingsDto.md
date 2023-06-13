# openapi_client.model.csv_settings_dto.CsvSettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**delimiter** | str,  | str,  | Default: , | [optional] 
**delimiterType** | str,  | str,  | Default: COMMA | [optional] must be one of ["TAB", "COMMA", "SEMICOLON", "OTHER", ] 
**htmlSubFilter** | bool,  | BoolClass,  | Default: false | [optional] 
**tagRegexp** | str,  | str,  |  | [optional] 
**importColumns** | str,  | str,  |  | [optional] 
**contextNoteColumns** | str,  | str,  |  | [optional] 
**contextKeyColumn** | str,  | str,  |  | [optional] 
**maxLenColumn** | str,  | str,  |  | [optional] 
**importRows** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

