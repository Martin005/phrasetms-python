# openapi_client.model.md_settings_dto.MdSettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hardLineBreaksSegments** | bool,  | BoolClass,  | Default: true | [optional] 
**preserveWhiteSpaces** | bool,  | BoolClass,  | Default: false | [optional] 
**tagRegexp** | str,  | str,  |  | [optional] 
**customElements** | str,  | str,  |  | [optional] 
**ignoredBlockPrefixes** | str,  | str,  |  | [optional] 
**flavor** | str,  | str,  | Default: PLAIN | [optional] must be one of ["PLAIN", "PHP", "GITHUB", ] 
**processJekyllFrontMatter** | bool,  | BoolClass,  | Default: false | [optional] 
**extractCodeBlocks** | bool,  | BoolClass,  | Default: true | [optional] 
**notEscapedCharacters** | str,  | str,  |  | [optional] 
**excludeCodeElements** | bool,  | BoolClass,  | Default: false | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
