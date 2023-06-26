# XlfSettingsDto

## Properties

| Name                                               | Type     | Description                                                                                          | Notes      |
| -------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------- | ---------- |
| **icu_sub_filter**                                 | **bool** | Default: false                                                                                       | [optional] |
| **import_notes**                                   | **bool** | Default: true                                                                                        | [optional] |
| **segmentation**                                   | **bool** | Default: true                                                                                        | [optional] |
| **skip_import_rules**                              | **str**  | Default: translate&#x3D;no; examples: translate&#x3D;no;approved&#x3D;no;state&#x3D;needs-adaptation | [optional] |
| **import_as_confirmed_rules**                      | **str**  | Multiple rules must be separated by semicolon                                                        | [optional] |
| **import_as_locked_rules**                         | **str**  |                                                                                                      | [optional] |
| **export_attrs_when_confirmed_and_locked**         | **str**  |                                                                                                      | [optional] |
| **export_attrs_when_confirmed_and_not_locked**     | **str**  |                                                                                                      | [optional] |
| **export_attrs_when_not_confirmed_and_locked**     | **str**  |                                                                                                      | [optional] |
| **export_attrs_when_not_confirmed_and_not_locked** | **str**  |                                                                                                      | [optional] |
| **save_confirmed_segments**                        | **bool** | Default: true                                                                                        | [optional] |
| **line_break_tags**                                | **bool** | Default: false                                                                                       | [optional] |
| **preserve_whitespace**                            | **bool** | Default: true                                                                                        | [optional] |
| **context_type**                                   | **str**  |                                                                                                      | [optional] |
| **preserve_char_entities**                         | **str**  |                                                                                                      | [optional] |
| **copy_source_to_target_if_not_imported**          | **bool** | Default: true                                                                                        | [optional] |
| **import_x_path**                                  | **str**  |                                                                                                      | [optional] |
| **import_as_confirmed_x_path**                     | **str**  |                                                                                                      | [optional] |
| **import_as_locked_x_path**                        | **str**  |                                                                                                      | [optional] |
| **xsl_url**                                        | **str**  |                                                                                                      | [optional] |
| **xsl_file**                                       | **str**  | UID of uploaded XSL file, overrides xslUrl                                                           | [optional] |
| **tag_regexp**                                     | **str**  |                                                                                                      | [optional] |

## Example

```python
from phrasetms_client.models.xlf_settings_dto import XlfSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of XlfSettingsDto from a JSON string
xlf_settings_dto_instance = XlfSettingsDto.from_json(json)
# print the JSON string representation of the object
print XlfSettingsDto.to_json()

# convert the object into a dict
xlf_settings_dto_dict = xlf_settings_dto_instance.to_dict()
# create an instance of XlfSettingsDto from a dict
xlf_settings_dto_from_dict = XlfSettingsDto.from_dict(xlf_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
