# openapi_client.model.multilingual_xml_settings_dto.MultilingualXmlSettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**translatableElementsXPath** | str,  | str,  |  | [optional] 
**sourceElementsXPath** | str,  | str,  |  | [optional] 
**[targetElementsXPaths](#targetElementsXPaths)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | &#x27;Format: \&quot;language\&quot;:\&quot;xpath\&quot;;             example &#x3D; &#x27;{\&quot;en\&quot;: \&quot;tuv[@lang&#x3D;&#x27;en&#x27;]/seg\&quot;, \&quot;sk\&quot;: \&quot;tuv[@lang&#x3D;&#x27;sk&#x27;]/seg\&quot;} | [optional] 
**inlineElementsNonTranslatableXPath** | str,  | str,  |  | [optional] 
**tagRegexp** | str,  | str,  |  | [optional] 
**segmentation** | bool,  | BoolClass,  | Default: &#x60;true&#x60; | [optional] 
**htmlSubFilter** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**contextKeyXPath** | str,  | str,  |  | [optional] 
**contextNoteXPath** | str,  | str,  |  | [optional] 
**maxLenXPath** | str,  | str,  |  | [optional] 
**preserveWhitespace** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**preserveCharEntities** | str,  | str,  |  | [optional] 
**xslUrl** | str,  | str,  |  | [optional] 
**xslFile** | str,  | str,  | UID of uploaded XSL file, overrides xslUrl | [optional] 
**nonEmptySegmentAction** | str,  | str,  |  | [optional] must be one of ["NONE", "CONFIRM", "LOCK", "CONFIRM_LOCK", ] 
**saveConfirmedSegmentsToTm** | bool,  | BoolClass,  |  | [optional] 
**icuSubFilter** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# targetElementsXPaths

'Format: \"language\":\"xpath\";             example = '{\"en\": \"tuv[@lang='en']/seg\", \"sk\": \"tuv[@lang='sk']/seg\"}

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | &#x27;Format: \&quot;language\&quot;:\&quot;xpath\&quot;;             example &#x3D; &#x27;{\&quot;en\&quot;: \&quot;tuv[@lang&#x3D;&#x27;en&#x27;]/seg\&quot;, \&quot;sk\&quot;: \&quot;tuv[@lang&#x3D;&#x27;sk&#x27;]/seg\&quot;} | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
