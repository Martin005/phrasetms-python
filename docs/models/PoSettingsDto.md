# openapi_client.model.po_settings_dto.PoSettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tagRegexp** | str,  | str,  |  | [optional] 
**exportMultiline** | bool,  | BoolClass,  | Default: true | [optional] 
**htmlSubFilter** | bool,  | BoolClass,  | Default: false | [optional] 
**segment** | bool,  | BoolClass,  | Default: false | [optional] 
**markupSubFilterTranslatable** | str,  | str,  |  | [optional] 
**markupSubFilterNonTranslatable** | str,  | str,  |  | [optional] 
**saveConfirmedSegments** | bool,  | BoolClass,  |  | [optional] 
**importSetSegmentConfirmedWhen** | str,  | str,  |  | [optional] must be one of ["FUZZY", "NONFUZZY", ] 
**importSetSegmentLockedWhen** | str,  | str,  |  | [optional] must be one of ["FUZZY", "NONFUZZY", ] 
**exportConfirmedLocked** | str,  | str,  |  | [optional] must be one of ["FUZZY", "NONFUZZY", ] 
**exportConfirmedNotLocked** | str,  | str,  |  | [optional] must be one of ["FUZZY", "NONFUZZY", ] 
**exportNotConfirmedLocked** | str,  | str,  |  | [optional] must be one of ["FUZZY", "NONFUZZY", ] 
**exportNotConfirmedNotLocked** | str,  | str,  |  | [optional] must be one of ["FUZZY", "NONFUZZY", ] 
**icuSubFilter** | bool,  | BoolClass,  | Default: &#x60;false&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
