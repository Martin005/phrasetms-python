# Xlf2SettingsDto

## Properties

| Name                                               | Type     | Description                                | Notes      |
| -------------------------------------------------- | -------- | ------------------------------------------ | ---------- |
| **icu_sub_filter**                                 | **bool** | Default: false                             | [optional] |
| **import_notes**                                   | **bool** | Default: true                              | [optional] |
| **save_confirmed_segments**                        | **bool** | Default: true                              | [optional] |
| **segmentation**                                   | **bool** | Default: true                              | [optional] |
| **line_break_tags**                                | **bool** | Default: false                             | [optional] |
| **preserve_whitespace**                            | **bool** | Default: true                              | [optional] |
| **copy_source_to_target_if_not_imported**          | **bool** | Default: true                              | [optional] |
| **respect_translate_attr**                         | **bool** | Default: true                              | [optional] |
| **skip_import_rules**                              | **str**  |                                            | [optional] |
| **import_as_confirmed_rules**                      | **str**  | Default: state&#x3D;final                  | [optional] |
| **import_as_locked_rules**                         | **str**  |                                            | [optional] |
| **export_attrs_when_confirmed_and_locked**         | **str**  | Default: state&#x3D;final                  | [optional] |
| **export_attrs_when_confirmed_and_not_locked**     | **str**  | Default: state&#x3D;final                  | [optional] |
| **export_attrs_when_not_confirmed_and_locked**     | **str**  |                                            | [optional] |
| **export_attrs_when_not_confirmed_and_not_locked** | **str**  |                                            | [optional] |
| **context_key_x_path**                             | **str**  |                                            | [optional] |
| **preserve_char_entities**                         | **str**  |                                            | [optional] |
| **xsl_url**                                        | **str**  |                                            | [optional] |
| **xsl_file**                                       | **str**  | UID of uploaded XSL file, overrides xslUrl | [optional] |
| **tag_regexp**                                     | **str**  |                                            | [optional] |

## Example

```python
from phrasetms_client.models.xlf2_settings_dto import Xlf2SettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of Xlf2SettingsDto from a JSON string
xlf2_settings_dto_instance = Xlf2SettingsDto.from_json(json)
# print the JSON string representation of the object
print Xlf2SettingsDto.to_json()

# convert the object into a dict
xlf2_settings_dto_dict = xlf2_settings_dto_instance.to_dict()
# create an instance of Xlf2SettingsDto from a dict
xlf2_settings_dto_from_dict = Xlf2SettingsDto.from_dict(xlf2_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
