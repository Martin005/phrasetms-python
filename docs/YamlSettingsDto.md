# YamlSettingsDto

## Properties

| Name                             | Type     | Description                | Notes      |
| -------------------------------- | -------- | -------------------------- | ---------- |
| **html_sub_filter**              | **bool** | Default: false             | [optional] |
| **tag_regexp**                   | **str**  |                            | [optional] |
| **include_key_regexp**           | **str**  |                            | [optional] |
| **exclude_value_regexp**         | **str**  |                            | [optional] |
| **context_path**                 | **str**  |                            | [optional] |
| **context_key_path**             | **str**  |                            | [optional] |
| **markdown_subfilter**           | **bool** | Default: false             | [optional] |
| **update_root_element_lang**     | **bool** | Default: false             | [optional] |
| **locale_format**                | **str**  |                            | [optional] |
| **indent_empty_lines_in_string** | **bool** | Default: true              | [optional] |
| **icu_sub_filter**               | **bool** | Default: &#x60;false&#x60; | [optional] |

## Example

```python
from phrasetms_client.models.yaml_settings_dto import YamlSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of YamlSettingsDto from a JSON string
yaml_settings_dto_instance = YamlSettingsDto.from_json(json)
# print the JSON string representation of the object
print YamlSettingsDto.to_json()

# convert the object into a dict
yaml_settings_dto_dict = yaml_settings_dto_instance.to_dict()
# create an instance of YamlSettingsDto from a dict
yaml_settings_dto_from_dict = YamlSettingsDto.from_dict(yaml_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
