# openapi_client.model.file_import_settings_create_dto.FileImportSettingsCreateDto

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
**fileFormat** | str,  | str,  | default: auto-detect | [optional] must be one of ["doc", "ppt", "xls", "xlf", "xlf2", "sdlxlif", "ttx", "html", "xml", "mif", "tmx", "idml", "dita", "json", "po", "ts", "icml", "yaml", "properties", "csv", "android_string", "desktop_entry", "mac_strings", "pdf", "windows_rc", "xml_properties", "joomla_ini", "magento_csv", "dtd", "mozilla_properties", "plist", "plain_text", "srt", "sub", "sbv", "wiki", "resx", "resjson", "chrome_json", "epub", "svg", "docbook", "wpxliff", "multiling_xml", "multiling_xls", "mqxliff", "php", "psd", "tag", "md", "vtt", ] 
**autodetectMultilingualFiles** | bool,  | BoolClass,  | Try to use multilingual variants for auto-detected CSV and Excel files. Default: true | [optional] 
**targetLength** | bool,  | BoolClass,  | Default: false | [optional] 
**targetLengthMax** | decimal.Decimal, int,  | decimal.Decimal,  | default: 1000 | [optional] value must be a 32 bit integer
**targetLengthPercent** | bool,  | BoolClass,  | Default: false | [optional] 
**targetLengthPercentValue** | decimal.Decimal, int, float,  | decimal.Decimal,  | default: 130 | [optional] value must be a 64 bit float
**segmentationRuleId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**targetSegmentationRuleId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**android** | [**AndroidSettingsDto**](AndroidSettingsDto.md) | [**AndroidSettingsDto**](AndroidSettingsDto.md) |  | [optional] 
**csv** | [**CsvSettingsDto**](CsvSettingsDto.md) | [**CsvSettingsDto**](CsvSettingsDto.md) |  | [optional] 
**dita** | [**DitaSettingsDto**](DitaSettingsDto.md) | [**DitaSettingsDto**](DitaSettingsDto.md) |  | [optional] 
**docBook** | [**DocBookSettingsDto**](DocBookSettingsDto.md) | [**DocBookSettingsDto**](DocBookSettingsDto.md) |  | [optional] 
**doc** | [**DocSettingsDto**](DocSettingsDto.md) | [**DocSettingsDto**](DocSettingsDto.md) |  | [optional] 
**html** | [**HtmlSettingsDto**](HtmlSettingsDto.md) | [**HtmlSettingsDto**](HtmlSettingsDto.md) |  | [optional] 
**idml** | [**IdmlSettingsDto**](IdmlSettingsDto.md) | [**IdmlSettingsDto**](IdmlSettingsDto.md) |  | [optional] 
**json** | [**JsonSettingsDto**](JsonSettingsDto.md) | [**JsonSettingsDto**](JsonSettingsDto.md) |  | [optional] 
**mac** | [**MacSettingsDto**](MacSettingsDto.md) | [**MacSettingsDto**](MacSettingsDto.md) |  | [optional] 
**md** | [**MdSettingsDto**](MdSettingsDto.md) | [**MdSettingsDto**](MdSettingsDto.md) |  | [optional] 
**mif** | [**MifSettingsDto**](MifSettingsDto.md) | [**MifSettingsDto**](MifSettingsDto.md) |  | [optional] 
**multilingualXls** | [**MultilingualXlsSettingsDto**](MultilingualXlsSettingsDto.md) | [**MultilingualXlsSettingsDto**](MultilingualXlsSettingsDto.md) |  | [optional] 
**multilingualCsv** | [**MultilingualCsvSettingsDto**](MultilingualCsvSettingsDto.md) | [**MultilingualCsvSettingsDto**](MultilingualCsvSettingsDto.md) |  | [optional] 
**multilingualXml** | [**MultilingualXmlSettingsDto**](MultilingualXmlSettingsDto.md) | [**MultilingualXmlSettingsDto**](MultilingualXmlSettingsDto.md) |  | [optional] 
**pdf** | [**PdfSettingsDto**](PdfSettingsDto.md) | [**PdfSettingsDto**](PdfSettingsDto.md) |  | [optional] 
**php** | [**PhpSettingsDto**](PhpSettingsDto.md) | [**PhpSettingsDto**](PhpSettingsDto.md) |  | [optional] 
**po** | [**PoSettingsDto**](PoSettingsDto.md) | [**PoSettingsDto**](PoSettingsDto.md) |  | [optional] 
**ppt** | [**PptSettingsDto**](PptSettingsDto.md) | [**PptSettingsDto**](PptSettingsDto.md) |  | [optional] 
**properties** | [**PropertiesSettingsDto**](PropertiesSettingsDto.md) | [**PropertiesSettingsDto**](PropertiesSettingsDto.md) |  | [optional] 
**psd** | [**PsdSettingsDto**](PsdSettingsDto.md) | [**PsdSettingsDto**](PsdSettingsDto.md) |  | [optional] 
**quarkTag** | [**QuarkTagSettingsDto**](QuarkTagSettingsDto.md) | [**QuarkTagSettingsDto**](QuarkTagSettingsDto.md) |  | [optional] 
**resx** | [**ResxSettingsDto**](ResxSettingsDto.md) | [**ResxSettingsDto**](ResxSettingsDto.md) |  | [optional] 
**sdlXlf** | [**SdlXlfSettingsDto**](SdlXlfSettingsDto.md) | [**SdlXlfSettingsDto**](SdlXlfSettingsDto.md) |  | [optional] 
**tmMatch** | [**TMMatchSettingsDto**](TMMatchSettingsDto.md) | [**TMMatchSettingsDto**](TMMatchSettingsDto.md) |  | [optional] 
**ttx** | [**TtxSettingsDto**](TtxSettingsDto.md) | [**TtxSettingsDto**](TtxSettingsDto.md) |  | [optional] 
**txt** | [**TxtSettingsDto**](TxtSettingsDto.md) | [**TxtSettingsDto**](TxtSettingsDto.md) |  | [optional] 
**xlf2** | [**Xlf2SettingsDto**](Xlf2SettingsDto.md) | [**Xlf2SettingsDto**](Xlf2SettingsDto.md) |  | [optional] 
**xlf** | [**XlfSettingsDto**](XlfSettingsDto.md) | [**XlfSettingsDto**](XlfSettingsDto.md) |  | [optional] 
**xls** | [**XlsSettingsDto**](XlsSettingsDto.md) | [**XlsSettingsDto**](XlsSettingsDto.md) |  | [optional] 
**xml** | [**XmlSettingsDto**](XmlSettingsDto.md) | [**XmlSettingsDto**](XmlSettingsDto.md) |  | [optional] 
**yaml** | [**YamlSettingsDto**](YamlSettingsDto.md) | [**YamlSettingsDto**](YamlSettingsDto.md) |  | [optional] 
**asciidoc** | [**AsciidocSettingsDto**](AsciidocSettingsDto.md) | [**AsciidocSettingsDto**](AsciidocSettingsDto.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

