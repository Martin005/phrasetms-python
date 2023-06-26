# MultilingualXlsSettingsDto

## Properties

| Name                              | Type               | Description                                                                                                                          | Notes      |
| --------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **source_column**                 | **str**            |                                                                                                                                      | [optional] |
| **target_columns**                | **Dict[str, str]** | Format: \&quot;language\&quot;:\&quot;column\&quot;; example: {\&quot;en\&quot;: \&quot;A\&quot;, \&quot;sk\&quot;: \&quot;B\&quot;} | [optional] |
| **context_note_column**           | **str**            |                                                                                                                                      | [optional] |
| **context_key_column**            | **str**            |                                                                                                                                      | [optional] |
| **tag_regexp**                    | **str**            |                                                                                                                                      | [optional] |
| **html_sub_filter**               | **bool**           | Default: false                                                                                                                       | [optional] |
| **segmentation**                  | **bool**           | Default: true                                                                                                                        | [optional] |
| **import_rows**                   | **str**            |                                                                                                                                      | [optional] |
| **max_len_column**                | **str**            |                                                                                                                                      | [optional] |
| **non_empty_segment_action**      | **str**            |                                                                                                                                      | [optional] |
| **save_confirmed_segments_to_tm** | **bool**           |                                                                                                                                      | [optional] |

## Example

```python
from phrasetms_client.models.multilingual_xls_settings_dto import MultilingualXlsSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualXlsSettingsDto from a JSON string
multilingual_xls_settings_dto_instance = MultilingualXlsSettingsDto.from_json(json)
# print the JSON string representation of the object
print MultilingualXlsSettingsDto.to_json()

# convert the object into a dict
multilingual_xls_settings_dto_dict = multilingual_xls_settings_dto_instance.to_dict()
# create an instance of MultilingualXlsSettingsDto from a dict
multilingual_xls_settings_dto_from_dict = MultilingualXlsSettingsDto.from_dict(multilingual_xls_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
