# openapi_client.model.html_settings_dto.HtmlSettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**breakTagCreatesSegment** | bool,  | BoolClass,  | Default: true | [optional] 
**unknownTagCreatesTag** | bool,  | BoolClass,  | Default: true | [optional] 
**preserveWhitespace** | bool,  | BoolClass,  | Default: false | [optional] 
**importComments** | bool,  | BoolClass,  | Default: true | [optional] 
**excludeElements** | str,  | str,  | Example: \&quot;script,blockquote\&quot; | [optional] 
**tagRegexp** | str,  | str,  |  | [optional] 
**charEntitiesToTags** | str,  | str,  |  | [optional] 
**translateMetaTagRegexp** | str,  | str,  |  | [optional] 
**importDefaultMetaTags** | bool,  | BoolClass,  | Default: true | [optional] 
**translatableAttributes** | str,  | str,  |  | [optional] 
**importDefaultAttributes** | bool,  | BoolClass,  | Default: true | [optional] 
**nonTranslatableInlineElements** | str,  | str,  | Example: \&quot;code\&quot; | [optional] 
**translatableInlineElements** | str,  | str,  | Example: \&quot;span\&quot; | [optional] 
**updateLang** | bool,  | BoolClass,  | Default: false | [optional] 
**escapeDisabled** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
