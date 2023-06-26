# CsvSettingsDto

## Properties

| Name                     | Type     | Description    | Notes      |
| ------------------------ | -------- | -------------- | ---------- |
| **delimiter**            | **str**  | Default: ,     | [optional] |
| **delimiter_type**       | **str**  | Default: COMMA | [optional] |
| **html_sub_filter**      | **bool** | Default: false | [optional] |
| **tag_regexp**           | **str**  |                | [optional] |
| **import_columns**       | **str**  |                | [optional] |
| **context_note_columns** | **str**  |                | [optional] |
| **context_key_column**   | **str**  |                | [optional] |
| **max_len_column**       | **str**  |                | [optional] |
| **import_rows**          | **str**  |                | [optional] |

## Example

```python
from phrasetms_client.models.csv_settings_dto import CsvSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CsvSettingsDto from a JSON string
csv_settings_dto_instance = CsvSettingsDto.from_json(json)
# print the JSON string representation of the object
print CsvSettingsDto.to_json()

# convert the object into a dict
csv_settings_dto_dict = csv_settings_dto_instance.to_dict()
# create an instance of CsvSettingsDto from a dict
csv_settings_dto_from_dict = CsvSettingsDto.from_dict(csv_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
