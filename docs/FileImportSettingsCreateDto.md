# FileImportSettingsCreateDto

## Properties

| Name                              | Type                                                            | Description                                                                           | Notes      |
| --------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------- |
| **input_charset**                 | **str**                                                         |                                                                                       | [optional] |
| **output_charset**                | **str**                                                         |                                                                                       | [optional] |
| **zip_charset**                   | **str**                                                         |                                                                                       | [optional] |
| **file_format**                   | **str**                                                         | default: auto-detect                                                                  | [optional] |
| **autodetect_multilingual_files** | **bool**                                                        | Try to use multilingual variants for auto-detected CSV and Excel files. Default: true | [optional] |
| **target_length**                 | **bool**                                                        | Default: false                                                                        | [optional] |
| **target_length_max**             | **int**                                                         | default: 1000                                                                         | [optional] |
| **target_length_percent**         | **bool**                                                        | Default: false                                                                        | [optional] |
| **target_length_percent_value**   | **float**                                                       | default: 130                                                                          | [optional] |
| **segmentation_rule_id**          | **int**                                                         |                                                                                       | [optional] |
| **target_segmentation_rule_id**   | **int**                                                         |                                                                                       | [optional] |
| **android**                       | [**AndroidSettingsDto**](AndroidSettingsDto.md)                 |                                                                                       | [optional] |
| **csv**                           | [**CsvSettingsDto**](CsvSettingsDto.md)                         |                                                                                       | [optional] |
| **dita**                          | [**DitaSettingsDto**](DitaSettingsDto.md)                       |                                                                                       | [optional] |
| **doc_book**                      | [**DocBookSettingsDto**](DocBookSettingsDto.md)                 |                                                                                       | [optional] |
| **doc**                           | [**DocSettingsDto**](DocSettingsDto.md)                         |                                                                                       | [optional] |
| **html**                          | [**HtmlSettingsDto**](HtmlSettingsDto.md)                       |                                                                                       | [optional] |
| **idml**                          | [**IdmlSettingsDto**](IdmlSettingsDto.md)                       |                                                                                       | [optional] |
| **var_json**                      | [**JsonSettingsDto**](JsonSettingsDto.md)                       |                                                                                       | [optional] |
| **mac**                           | [**MacSettingsDto**](MacSettingsDto.md)                         |                                                                                       | [optional] |
| **md**                            | [**MdSettingsDto**](MdSettingsDto.md)                           |                                                                                       | [optional] |
| **mif**                           | [**MifSettingsDto**](MifSettingsDto.md)                         |                                                                                       | [optional] |
| **multilingual_xls**              | [**MultilingualXlsSettingsDto**](MultilingualXlsSettingsDto.md) |                                                                                       | [optional] |
| **multilingual_csv**              | [**MultilingualCsvSettingsDto**](MultilingualCsvSettingsDto.md) |                                                                                       | [optional] |
| **multilingual_xml**              | [**MultilingualXmlSettingsDto**](MultilingualXmlSettingsDto.md) |                                                                                       | [optional] |
| **pdf**                           | [**PdfSettingsDto**](PdfSettingsDto.md)                         |                                                                                       | [optional] |
| **php**                           | [**PhpSettingsDto**](PhpSettingsDto.md)                         |                                                                                       | [optional] |
| **po**                            | [**PoSettingsDto**](PoSettingsDto.md)                           |                                                                                       | [optional] |
| **ppt**                           | [**PptSettingsDto**](PptSettingsDto.md)                         |                                                                                       | [optional] |
| **properties**                    | [**PropertiesSettingsDto**](PropertiesSettingsDto.md)           |                                                                                       | [optional] |
| **psd**                           | [**PsdSettingsDto**](PsdSettingsDto.md)                         |                                                                                       | [optional] |
| **quark_tag**                     | [**QuarkTagSettingsDto**](QuarkTagSettingsDto.md)               |                                                                                       | [optional] |
| **resx**                          | [**ResxSettingsDto**](ResxSettingsDto.md)                       |                                                                                       | [optional] |
| **sdl_xlf**                       | [**SdlXlfSettingsDto**](SdlXlfSettingsDto.md)                   |                                                                                       | [optional] |
| **tm_match**                      | [**TMMatchSettingsDto**](TMMatchSettingsDto.md)                 |                                                                                       | [optional] |
| **ttx**                           | [**TtxSettingsDto**](TtxSettingsDto.md)                         |                                                                                       | [optional] |
| **txt**                           | [**TxtSettingsDto**](TxtSettingsDto.md)                         |                                                                                       | [optional] |
| **xlf2**                          | [**Xlf2SettingsDto**](Xlf2SettingsDto.md)                       |                                                                                       | [optional] |
| **xlf**                           | [**XlfSettingsDto**](XlfSettingsDto.md)                         |                                                                                       | [optional] |
| **xls**                           | [**XlsSettingsDto**](XlsSettingsDto.md)                         |                                                                                       | [optional] |
| **xml**                           | [**XmlSettingsDto**](XmlSettingsDto.md)                         |                                                                                       | [optional] |
| **yaml**                          | [**YamlSettingsDto**](YamlSettingsDto.md)                       |                                                                                       | [optional] |
| **asciidoc**                      | [**AsciidocSettingsDto**](AsciidocSettingsDto.md)               |                                                                                       | [optional] |

## Example

```python
from phrasetms_client.models.file_import_settings_create_dto import FileImportSettingsCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileImportSettingsCreateDto from a JSON string
file_import_settings_create_dto_instance = FileImportSettingsCreateDto.from_json(json)
# print the JSON string representation of the object
print FileImportSettingsCreateDto.to_json()

# convert the object into a dict
file_import_settings_create_dto_dict = file_import_settings_create_dto_instance.to_dict()
# create an instance of FileImportSettingsCreateDto from a dict
file_import_settings_create_dto_from_dict = FileImportSettingsCreateDto.from_dict(file_import_settings_create_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
