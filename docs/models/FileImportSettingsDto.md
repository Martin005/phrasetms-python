# openapi_client.model.file_import_settings_dto.FileImportSettingsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**inputCharset** | str,  | str,  |  | [optional] 
**outputCharset** | str,  | str,  |  | [optional] 
**zipCharset** | str,  | str,  |  | [optional] 
**fileFormat** | str,  | str,  |  | [optional] 
**autodetectMultilingualFiles** | bool,  | BoolClass,  |  | [optional] 
**targetLength** | bool,  | BoolClass,  |  | [optional] 
**targetLengthMax** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**targetLengthPercent** | bool,  | BoolClass,  |  | [optional] 
**targetLengthPercentValue** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**android** | [**AndroidSettingsDto**](AndroidSettingsDto.md) | [**AndroidSettingsDto**](AndroidSettingsDto.md) |  | [optional] 
**idml** | [**IdmlSettingsDto**](IdmlSettingsDto.md) | [**IdmlSettingsDto**](IdmlSettingsDto.md) |  | [optional] 
**xls** | [**XlsSettingsDto**](XlsSettingsDto.md) | [**XlsSettingsDto**](XlsSettingsDto.md) |  | [optional] 
**multilingualXml** | [**MultilingualXmlSettingsDto**](MultilingualXmlSettingsDto.md) | [**MultilingualXmlSettingsDto**](MultilingualXmlSettingsDto.md) |  | [optional] 
**php** | [**PhpSettingsDto**](PhpSettingsDto.md) | [**PhpSettingsDto**](PhpSettingsDto.md) |  | [optional] 
**resx** | [**ResxSettingsDto**](ResxSettingsDto.md) | [**ResxSettingsDto**](ResxSettingsDto.md) |  | [optional] 
**json** | [**JsonSettingsDto**](JsonSettingsDto.md) | [**JsonSettingsDto**](JsonSettingsDto.md) |  | [optional] 
**html** | [**HtmlSettingsDto**](HtmlSettingsDto.md) | [**HtmlSettingsDto**](HtmlSettingsDto.md) |  | [optional] 
**multilingualXls** | [**MultilingualXlsSettingsDto**](MultilingualXlsSettingsDto.md) | [**MultilingualXlsSettingsDto**](MultilingualXlsSettingsDto.md) |  | [optional] 
**multilingualCsv** | [**MultilingualCsvSettingsDto**](MultilingualCsvSettingsDto.md) | [**MultilingualCsvSettingsDto**](MultilingualCsvSettingsDto.md) |  | [optional] 
**csv** | [**CsvSettingsDto**](CsvSettingsDto.md) | [**CsvSettingsDto**](CsvSettingsDto.md) |  | [optional] 
**txt** | [**TxtSettingsDto**](TxtSettingsDto.md) | [**TxtSettingsDto**](TxtSettingsDto.md) |  | [optional] 
**xlf2** | [**Xlf2SettingsDto**](Xlf2SettingsDto.md) | [**Xlf2SettingsDto**](Xlf2SettingsDto.md) |  | [optional] 
**quarkTag** | [**QuarkTagSettingsDto**](QuarkTagSettingsDto.md) | [**QuarkTagSettingsDto**](QuarkTagSettingsDto.md) |  | [optional] 
**pdf** | [**PdfSettingsDto**](PdfSettingsDto.md) | [**PdfSettingsDto**](PdfSettingsDto.md) |  | [optional] 
**tmMatch** | [**TMMatchSettingsDto**](TMMatchSettingsDto.md) | [**TMMatchSettingsDto**](TMMatchSettingsDto.md) |  | [optional] 
**xml** | [**XmlSettingsDto**](XmlSettingsDto.md) | [**XmlSettingsDto**](XmlSettingsDto.md) |  | [optional] 
**mif** | [**MifSettingsDto**](MifSettingsDto.md) | [**MifSettingsDto**](MifSettingsDto.md) |  | [optional] 
**properties** | [**PropertiesSettingsDto**](PropertiesSettingsDto.md) | [**PropertiesSettingsDto**](PropertiesSettingsDto.md) |  | [optional] 
**doc** | [**DocSettingsDto**](DocSettingsDto.md) | [**DocSettingsDto**](DocSettingsDto.md) |  | [optional] 
**xlf** | [**XlfSettingsDto**](XlfSettingsDto.md) | [**XlfSettingsDto**](XlfSettingsDto.md) |  | [optional] 
**sdlXlf** | [**SdlXlfSettingsDto**](SdlXlfSettingsDto.md) | [**SdlXlfSettingsDto**](SdlXlfSettingsDto.md) |  | [optional] 
**ttx** | [**TtxSettingsDto**](TtxSettingsDto.md) | [**TtxSettingsDto**](TtxSettingsDto.md) |  | [optional] 
**ppt** | [**PptSettingsDto**](PptSettingsDto.md) | [**PptSettingsDto**](PptSettingsDto.md) |  | [optional] 
**yaml** | [**YamlSettingsDto**](YamlSettingsDto.md) | [**YamlSettingsDto**](YamlSettingsDto.md) |  | [optional] 
**dita** | [**DitaSettingsDto**](DitaSettingsDto.md) | [**DitaSettingsDto**](DitaSettingsDto.md) |  | [optional] 
**docBook** | [**DocBookSettingsDto**](DocBookSettingsDto.md) | [**DocBookSettingsDto**](DocBookSettingsDto.md) |  | [optional] 
**po** | [**PoSettingsDto**](PoSettingsDto.md) | [**PoSettingsDto**](PoSettingsDto.md) |  | [optional] 
**mac** | [**MacSettingsDto**](MacSettingsDto.md) | [**MacSettingsDto**](MacSettingsDto.md) |  | [optional] 
**md** | [**MdSettingsDto**](MdSettingsDto.md) | [**MdSettingsDto**](MdSettingsDto.md) |  | [optional] 
**psd** | [**PsdSettingsDto**](PsdSettingsDto.md) | [**PsdSettingsDto**](PsdSettingsDto.md) |  | [optional] 
**asciidoc** | [**AsciidocSettingsDto**](AsciidocSettingsDto.md) | [**AsciidocSettingsDto**](AsciidocSettingsDto.md) |  | [optional] 
**segRule** | [**SegRuleReference**](SegRuleReference.md) | [**SegRuleReference**](SegRuleReference.md) |  | [optional] 
**targetSegRule** | [**SegRuleReference**](SegRuleReference.md) | [**SegRuleReference**](SegRuleReference.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
