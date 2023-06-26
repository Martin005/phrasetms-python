# IdmlSettingsDto

## Properties

| Name                                | Type     | Description    | Notes      |
| ----------------------------------- | -------- | -------------- | ---------- |
| **extract_notes**                   | **bool** | Default: false | [optional] |
| **simplify_codes**                  | **bool** | Default: true  | [optional] |
| **extract_master_spreads**          | **bool** | Default: true  | [optional] |
| **extract_locked_layers**           | **bool** | Default: true  | [optional] |
| **extract_invisible_layers**        | **bool** | Default: false | [optional] |
| **extract_hidden_conditional_text** | **bool** | Default: false | [optional] |
| **extract_hyperlinks**              | **bool** | Default: false | [optional] |
| **keep_kerning**                    | **bool** | Default: false | [optional] |
| **keep_tracking**                   | **bool** | Default: false | [optional] |
| **target_font**                     | **str**  |                | [optional] |
| **replace_font**                    | **bool** | Default: true  | [optional] |
| **remove_xml_elements**             | **bool** | Default: false | [optional] |
| **tag_regexp**                      | **str**  |                | [optional] |
| **extract_cross_reference_formats** | **bool** | Default: true  | [optional] |
| **extract_variables**               | **bool** | Default: true  | [optional] |

## Example

```python
from phrasetms_client.models.idml_settings_dto import IdmlSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of IdmlSettingsDto from a JSON string
idml_settings_dto_instance = IdmlSettingsDto.from_json(json)
# print the JSON string representation of the object
print IdmlSettingsDto.to_json()

# convert the object into a dict
idml_settings_dto_dict = idml_settings_dto_instance.to_dict()
# create an instance of IdmlSettingsDto from a dict
idml_settings_dto_from_dict = IdmlSettingsDto.from_dict(idml_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
