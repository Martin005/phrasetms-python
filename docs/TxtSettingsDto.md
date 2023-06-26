# TxtSettingsDto

## Properties

| Name                         | Type     | Description    | Notes      |
| ---------------------------- | -------- | -------------- | ---------- |
| **tag_regexp**               | **str**  |                | [optional] |
| **translatable_text_regexp** | **str**  |                | [optional] |
| **context_key**              | **str**  |                | [optional] |
| **regexp_capturing_groups**  | **bool** | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.txt_settings_dto import TxtSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TxtSettingsDto from a JSON string
txt_settings_dto_instance = TxtSettingsDto.from_json(json)
# print the JSON string representation of the object
print TxtSettingsDto.to_json()

# convert the object into a dict
txt_settings_dto_dict = txt_settings_dto_instance.to_dict()
# create an instance of TxtSettingsDto from a dict
txt_settings_dto_from_dict = TxtSettingsDto.from_dict(txt_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
