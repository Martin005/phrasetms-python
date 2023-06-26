# XmlSettingsDto

## Properties

| Name                                        | Type     | Description                                                                            | Notes      |
| ------------------------------------------- | -------- | -------------------------------------------------------------------------------------- | ---------- |
| **rules_format**                            | **str**  | Default: &#x60;\&quot;PLAIN\&quot;&#x60;                                               | [optional] |
| **include_elements_plain**                  | **str**  | Default: &#x60;\&quot;\*\&quot;&#x60;, example: &#x60;\&quot;para,heading\&quot;&#x60; | [optional] |
| **exclude_elements_plain**                  | **str**  | Example: &#x60;\&quot;script,par\&quot;&#x60;                                          | [optional] |
| **include_attributes_plain**                | **str**  | Example: &#x60;\&quot;title\&quot;&#x60;                                               | [optional] |
| **exclude_attributes_plain**                | **str**  | Example: &#x60;\&quot;lang,href\&quot;&#x60;                                           | [optional] |
| **inline_elements_non_translatable_plain**  | **str**  | Example: &#x60;\&quot;tt,b\&quot;&#x60;                                                | [optional] |
| **inline_elements_plain**                   | **str**  |                                                                                        | [optional] |
| **inline_elements_auto_plain**              | **bool** | Default: &#x60;false&#x60;                                                             | [optional] |
| **html_subfilter_elements_plain**           | **str**  | Example: &#x60;\&quot;tt,b\&quot;&#x60;                                                | [optional] |
| **entities**                                | **bool** | Default: &#x60;false&#x60;                                                             | [optional] |
| **lock_elements_plain**                     | **str**  |                                                                                        | [optional] |
| **lock_attributes_plain**                   | **str**  |                                                                                        | [optional] |
| **include_x_path**                          | **str**  |                                                                                        | [optional] |
| **inline_elements_xpath**                   | **str**  |                                                                                        | [optional] |
| **inline_elements_non_translatable_x_path** | **str**  |                                                                                        | [optional] |
| **inline_elements_auto_x_path**             | **bool** | Default: &#x60;false&#x60;                                                             | [optional] |
| **html_subfilter_elements_xpath**           | **str**  |                                                                                        | [optional] |
| **lock_x_path**                             | **str**  |                                                                                        | [optional] |
| **segmentation**                            | **bool** | Default: &#x60;true&#x60;                                                              | [optional] |
| **tag_regexp**                              | **str**  |                                                                                        | [optional] |
| **context_note_xpath**                      | **str**  |                                                                                        | [optional] |
| **max_len_x_path**                          | **str**  |                                                                                        | [optional] |
| **preserve_whitespace_x_path**              | **str**  |                                                                                        | [optional] |
| **preserve_char_entities**                  | **str**  |                                                                                        | [optional] |
| **context_key_x_path**                      | **str**  |                                                                                        | [optional] |
| **xsl_url**                                 | **str**  |                                                                                        | [optional] |
| **xsl_file**                                | **str**  | UID of uploaded XSL file, overrides &#x60;xslUrl&#x60;                                 | [optional] |
| **import_comments**                         | **bool** | Default: &#x60;true&#x60;                                                              | [optional] |
| **icu_sub_filter**                          | **bool** | Default: &#x60;false&#x60;                                                             | [optional] |

## Example

```python
from phrasetms_client.models.xml_settings_dto import XmlSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of XmlSettingsDto from a JSON string
xml_settings_dto_instance = XmlSettingsDto.from_json(json)
# print the JSON string representation of the object
print XmlSettingsDto.to_json()

# convert the object into a dict
xml_settings_dto_dict = xml_settings_dto_instance.to_dict()
# create an instance of XmlSettingsDto from a dict
xml_settings_dto_from_dict = XmlSettingsDto.from_dict(xml_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
