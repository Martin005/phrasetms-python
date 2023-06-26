# MultilingualCsvSettingsDto

## Properties

| Name                              | Type               | Description                                                                                                                          | Notes      |
| --------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **source_columns**                | **str**            |                                                                                                                                      | [optional] |
| **target_columns**                | **str**            |                                                                                                                                      | [optional] |
| **context_note_columns**          | **str**            |                                                                                                                                      | [optional] |
| **context_key_columns**           | **str**            |                                                                                                                                      | [optional] |
| **tag_regexp**                    | **str**            |                                                                                                                                      | [optional] |
| **html_sub_filter**               | **bool**           | Default: false                                                                                                                       | [optional] |
| **segmentation**                  | **bool**           | Default: true                                                                                                                        | [optional] |
| **delimiter**                     | **str**            | Default: ,                                                                                                                           | [optional] |
| **delimiter_type**                | **str**            | Default: COMMA                                                                                                                       | [optional] |
| **import_rows**                   | **str**            |                                                                                                                                      | [optional] |
| **max_len_columns**               | **str**            |                                                                                                                                      | [optional] |
| **all_target_columns**            | **Dict[str, str]** | Format: \&quot;language\&quot;:\&quot;column\&quot;; example: {\&quot;en\&quot;: \&quot;A\&quot;, \&quot;sk\&quot;: \&quot;B\&quot;} | [optional] |
| **non_empty_segment_action**      | **str**            |                                                                                                                                      | [optional] |
| **save_confirmed_segments_to_tm** | **bool**           |                                                                                                                                      | [optional] |

## Example

```python
from phrasetms_client.models.multilingual_csv_settings_dto import MultilingualCsvSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualCsvSettingsDto from a JSON string
multilingual_csv_settings_dto_instance = MultilingualCsvSettingsDto.from_json(json)
# print the JSON string representation of the object
print MultilingualCsvSettingsDto.to_json()

# convert the object into a dict
multilingual_csv_settings_dto_dict = multilingual_csv_settings_dto_instance.to_dict()
# create an instance of MultilingualCsvSettingsDto from a dict
multilingual_csv_settings_dto_from_dict = MultilingualCsvSettingsDto.from_dict(multilingual_csv_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
