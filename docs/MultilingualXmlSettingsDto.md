# MultilingualXmlSettingsDto

## Properties

| Name                                        | Type               | Description                                                                                                                                                                                                       | Notes      |
| ------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **translatable_elements_x_path**            | **str**            |                                                                                                                                                                                                                   | [optional] |
| **source_elements_x_path**                  | **str**            |                                                                                                                                                                                                                   | [optional] |
| **target_elements_x_paths**                 | **Dict[str, str]** | &#39;Format: \&quot;language\&quot;:\&quot;xpath\&quot;; example &#x3D; &#39;{\&quot;en\&quot;: \&quot;tuv[@lang&#x3D;&#39;en&#39;]/seg\&quot;, \&quot;sk\&quot;: \&quot;tuv[@lang&#x3D;&#39;sk&#39;]/seg\&quot;} | [optional] |
| **inline_elements_non_translatable_x_path** | **str**            |                                                                                                                                                                                                                   | [optional] |
| **tag_regexp**                              | **str**            |                                                                                                                                                                                                                   | [optional] |
| **segmentation**                            | **bool**           | Default: &#x60;true&#x60;                                                                                                                                                                                         | [optional] |
| **html_sub_filter**                         | **bool**           | Default: &#x60;false&#x60;                                                                                                                                                                                        | [optional] |
| **context_key_x_path**                      | **str**            |                                                                                                                                                                                                                   | [optional] |
| **context_note_x_path**                     | **str**            |                                                                                                                                                                                                                   | [optional] |
| **max_len_x_path**                          | **str**            |                                                                                                                                                                                                                   | [optional] |
| **preserve_whitespace**                     | **bool**           | Default: &#x60;false&#x60;                                                                                                                                                                                        | [optional] |
| **preserve_char_entities**                  | **str**            |                                                                                                                                                                                                                   | [optional] |
| **xsl_url**                                 | **str**            |                                                                                                                                                                                                                   | [optional] |
| **xsl_file**                                | **str**            | UID of uploaded XSL file, overrides xslUrl                                                                                                                                                                        | [optional] |
| **non_empty_segment_action**                | **str**            |                                                                                                                                                                                                                   | [optional] |
| **save_confirmed_segments_to_tm**           | **bool**           |                                                                                                                                                                                                                   | [optional] |
| **icu_sub_filter**                          | **bool**           | Default: &#x60;false&#x60;                                                                                                                                                                                        | [optional] |

## Example

```python
from phrasetms_client.models.multilingual_xml_settings_dto import MultilingualXmlSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualXmlSettingsDto from a JSON string
multilingual_xml_settings_dto_instance = MultilingualXmlSettingsDto.from_json(json)
# print the JSON string representation of the object
print MultilingualXmlSettingsDto.to_json()

# convert the object into a dict
multilingual_xml_settings_dto_dict = multilingual_xml_settings_dto_instance.to_dict()
# create an instance of MultilingualXmlSettingsDto from a dict
multilingual_xml_settings_dto_from_dict = MultilingualXmlSettingsDto.from_dict(multilingual_xml_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
