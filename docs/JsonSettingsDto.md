# JsonSettingsDto

## Properties

| Name                   | Type     | Description    | Notes      |
| ---------------------- | -------- | -------------- | ---------- |
| **tag_regexp**         | **str**  |                | [optional] |
| **html_sub_filter**    | **bool** | Default: true  | [optional] |
| **icu_sub_filter**     | **bool** | Default: false | [optional] |
| **exclude_key_regexp** | **str**  |                | [optional] |
| **include_key_regexp** | **str**  |                | [optional] |
| **context_note_path**  | **str**  |                | [optional] |
| **max_len_path**       | **str**  |                | [optional] |
| **context_key_path**   | **str**  |                | [optional] |

## Example

```python
from phrasetms_client.models.json_settings_dto import JsonSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSettingsDto from a JSON string
json_settings_dto_instance = JsonSettingsDto.from_json(json)
# print the JSON string representation of the object
print JsonSettingsDto.to_json()

# convert the object into a dict
json_settings_dto_dict = json_settings_dto_instance.to_dict()
# create an instance of JsonSettingsDto from a dict
json_settings_dto_from_dict = JsonSettingsDto.from_dict(json_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
