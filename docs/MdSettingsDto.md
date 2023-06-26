# MdSettingsDto

## Properties

| Name                            | Type     | Description    | Notes      |
| ------------------------------- | -------- | -------------- | ---------- |
| **hard_line_breaks_segments**   | **bool** | Default: true  | [optional] |
| **preserve_white_spaces**       | **bool** | Default: false | [optional] |
| **tag_regexp**                  | **str**  |                | [optional] |
| **custom_elements**             | **str**  |                | [optional] |
| **ignored_block_prefixes**      | **str**  |                | [optional] |
| **flavor**                      | **str**  | Default: PLAIN | [optional] |
| **process_jekyll_front_matter** | **bool** | Default: false | [optional] |
| **extract_code_blocks**         | **bool** | Default: true  | [optional] |
| **not_escaped_characters**      | **str**  |                | [optional] |
| **exclude_code_elements**       | **bool** | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.md_settings_dto import MdSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MdSettingsDto from a JSON string
md_settings_dto_instance = MdSettingsDto.from_json(json)
# print the JSON string representation of the object
print MdSettingsDto.to_json()

# convert the object into a dict
md_settings_dto_dict = md_settings_dto_instance.to_dict()
# create an instance of MdSettingsDto from a dict
md_settings_dto_from_dict = MdSettingsDto.from_dict(md_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
