# FileImportSettingsDto

## Properties

| Name                              | Type                                                            | Description | Notes      |
| --------------------------------- | --------------------------------------------------------------- | ----------- | ---------- |
| **input_charset**                 | **str**                                                         |             | [optional] |
| **output_charset**                | **str**                                                         |             | [optional] |
| **zip_charset**                   | **str**                                                         |             | [optional] |
| **file_format**                   | **str**                                                         |             | [optional] |
| **autodetect_multilingual_files** | **bool**                                                        |             | [optional] |
| **target_length**                 | **bool**                                                        |             | [optional] |
| **target_length_max**             | **int**                                                         |             | [optional] |
| **target_length_percent**         | **bool**                                                        |             | [optional] |
| **target_length_percent_value**   | **float**                                                       |             | [optional] |
| **android**                       | [**AndroidSettingsDto**](AndroidSettingsDto.md)                 |             | [optional] |
| **idml**                          | [**IdmlSettingsDto**](IdmlSettingsDto.md)                       |             | [optional] |
| **xls**                           | [**XlsSettingsDto**](XlsSettingsDto.md)                         |             | [optional] |
| **multilingual_xml**              | [**MultilingualXmlSettingsDto**](MultilingualXmlSettingsDto.md) |             | [optional] |
| **php**                           | [**PhpSettingsDto**](PhpSettingsDto.md)                         |             | [optional] |
| **resx**                          | [**ResxSettingsDto**](ResxSettingsDto.md)                       |             | [optional] |
| **var_json**                      | [**JsonSettingsDto**](JsonSettingsDto.md)                       |             | [optional] |
| **html**                          | [**HtmlSettingsDto**](HtmlSettingsDto.md)                       |             | [optional] |
| **multilingual_xls**              | [**MultilingualXlsSettingsDto**](MultilingualXlsSettingsDto.md) |             | [optional] |
| **multilingual_csv**              | [**MultilingualCsvSettingsDto**](MultilingualCsvSettingsDto.md) |             | [optional] |
| **csv**                           | [**CsvSettingsDto**](CsvSettingsDto.md)                         |             | [optional] |
| **txt**                           | [**TxtSettingsDto**](TxtSettingsDto.md)                         |             | [optional] |
| **xlf2**                          | [**Xlf2SettingsDto**](Xlf2SettingsDto.md)                       |             | [optional] |
| **quark_tag**                     | [**QuarkTagSettingsDto**](QuarkTagSettingsDto.md)               |             | [optional] |
| **pdf**                           | [**PdfSettingsDto**](PdfSettingsDto.md)                         |             | [optional] |
| **tm_match**                      | [**TMMatchSettingsDto**](TMMatchSettingsDto.md)                 |             | [optional] |
| **xml**                           | [**XmlSettingsDto**](XmlSettingsDto.md)                         |             | [optional] |
| **mif**                           | [**MifSettingsDto**](MifSettingsDto.md)                         |             | [optional] |
| **properties**                    | [**PropertiesSettingsDto**](PropertiesSettingsDto.md)           |             | [optional] |
| **doc**                           | [**DocSettingsDto**](DocSettingsDto.md)                         |             | [optional] |
| **xlf**                           | [**XlfSettingsDto**](XlfSettingsDto.md)                         |             | [optional] |
| **sdl_xlf**                       | [**SdlXlfSettingsDto**](SdlXlfSettingsDto.md)                   |             | [optional] |
| **ttx**                           | [**TtxSettingsDto**](TtxSettingsDto.md)                         |             | [optional] |
| **ppt**                           | [**PptSettingsDto**](PptSettingsDto.md)                         |             | [optional] |
| **yaml**                          | [**YamlSettingsDto**](YamlSettingsDto.md)                       |             | [optional] |
| **dita**                          | [**DitaSettingsDto**](DitaSettingsDto.md)                       |             | [optional] |
| **doc_book**                      | [**DocBookSettingsDto**](DocBookSettingsDto.md)                 |             | [optional] |
| **po**                            | [**PoSettingsDto**](PoSettingsDto.md)                           |             | [optional] |
| **mac**                           | [**MacSettingsDto**](MacSettingsDto.md)                         |             | [optional] |
| **md**                            | [**MdSettingsDto**](MdSettingsDto.md)                           |             | [optional] |
| **psd**                           | [**PsdSettingsDto**](PsdSettingsDto.md)                         |             | [optional] |
| **asciidoc**                      | [**AsciidocSettingsDto**](AsciidocSettingsDto.md)               |             | [optional] |
| **seg_rule**                      | [**SegRuleReference**](SegRuleReference.md)                     |             | [optional] |
| **target_seg_rule**               | [**SegRuleReference**](SegRuleReference.md)                     |             | [optional] |

## Example

```python
from phrasetms_client.models.file_import_settings_dto import FileImportSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileImportSettingsDto from a JSON string
file_import_settings_dto_instance = FileImportSettingsDto.from_json(json)
# print the JSON string representation of the object
print FileImportSettingsDto.to_json()

# convert the object into a dict
file_import_settings_dto_dict = file_import_settings_dto_instance.to_dict()
# create an instance of FileImportSettingsDto from a dict
file_import_settings_dto_from_dict = FileImportSettingsDto.from_dict(file_import_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
