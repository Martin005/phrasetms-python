# openapi_client.model.xml_settings_dto.XmlSettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**rulesFormat** | str,  | str,  | Default: &#x60;\&quot;PLAIN\&quot;&#x60; | [optional] must be one of ["PLAIN", "XPATH", ] 
**includeElementsPlain** | str,  | str,  | Default: &#x60;\&quot;*\&quot;&#x60;, example: &#x60;\&quot;para,heading\&quot;&#x60; | [optional] 
**excludeElementsPlain** | str,  | str,  | Example: &#x60;\&quot;script,par\&quot;&#x60; | [optional] 
**includeAttributesPlain** | str,  | str,  | Example: &#x60;\&quot;title\&quot;&#x60; | [optional] 
**excludeAttributesPlain** | str,  | str,  | Example: &#x60;\&quot;lang,href\&quot;&#x60; | [optional] 
**inlineElementsNonTranslatablePlain** | str,  | str,  | Example: &#x60;\&quot;tt,b\&quot;&#x60; | [optional] 
**inlineElementsPlain** | str,  | str,  |  | [optional] 
**inlineElementsAutoPlain** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**htmlSubfilterElementsPlain** | str,  | str,  | Example: &#x60;\&quot;tt,b\&quot;&#x60; | [optional] 
**entities** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**lockElementsPlain** | str,  | str,  |  | [optional] 
**lockAttributesPlain** | str,  | str,  |  | [optional] 
**includeXPath** | str,  | str,  |  | [optional] 
**inlineElementsXpath** | str,  | str,  |  | [optional] 
**inlineElementsNonTranslatableXPath** | str,  | str,  |  | [optional] 
**inlineElementsAutoXPath** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**htmlSubfilterElementsXpath** | str,  | str,  |  | [optional] 
**lockXPath** | str,  | str,  |  | [optional] 
**segmentation** | bool,  | BoolClass,  | Default: &#x60;true&#x60; | [optional] 
**tagRegexp** | str,  | str,  |  | [optional] 
**contextNoteXpath** | str,  | str,  |  | [optional] 
**maxLenXPath** | str,  | str,  |  | [optional] 
**preserveWhitespaceXPath** | str,  | str,  |  | [optional] 
**preserveCharEntities** | str,  | str,  |  | [optional] 
**contextKeyXPath** | str,  | str,  |  | [optional] 
**xslUrl** | str,  | str,  |  | [optional] 
**xslFile** | str,  | str,  | UID of uploaded XSL file, overrides &#x60;xslUrl&#x60; | [optional] 
**importComments** | bool,  | BoolClass,  | Default: &#x60;true&#x60; | [optional] 
**icuSubFilter** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
