# HtmlSettingsDto

## Properties

| Name                                 | Type     | Description                              | Notes      |
| ------------------------------------ | -------- | ---------------------------------------- | ---------- |
| **break_tag_creates_segment**        | **bool** | Default: true                            | [optional] |
| **unknown_tag_creates_tag**          | **bool** | Default: true                            | [optional] |
| **preserve_whitespace**              | **bool** | Default: false                           | [optional] |
| **import_comments**                  | **bool** | Default: true                            | [optional] |
| **exclude_elements**                 | **str**  | Example: \&quot;script,blockquote\&quot; | [optional] |
| **tag_regexp**                       | **str**  |                                          | [optional] |
| **char_entities_to_tags**            | **str**  |                                          | [optional] |
| **translate_meta_tag_regexp**        | **str**  |                                          | [optional] |
| **import_default_meta_tags**         | **bool** | Default: true                            | [optional] |
| **translatable_attributes**          | **str**  |                                          | [optional] |
| **import_default_attributes**        | **bool** | Default: true                            | [optional] |
| **non_translatable_inline_elements** | **str**  | Example: \&quot;code\&quot;              | [optional] |
| **translatable_inline_elements**     | **str**  | Example: \&quot;span\&quot;              | [optional] |
| **update_lang**                      | **bool** | Default: false                           | [optional] |
| **escape_disabled**                  | **bool** | Default: &#x60;false&#x60;               | [optional] |

## Example

```python
from phrasetms_client.models.html_settings_dto import HtmlSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of HtmlSettingsDto from a JSON string
html_settings_dto_instance = HtmlSettingsDto.from_json(json)
# print the JSON string representation of the object
print HtmlSettingsDto.to_json()

# convert the object into a dict
html_settings_dto_dict = html_settings_dto_instance.to_dict()
# create an instance of HtmlSettingsDto from a dict
html_settings_dto_from_dict = HtmlSettingsDto.from_dict(html_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
