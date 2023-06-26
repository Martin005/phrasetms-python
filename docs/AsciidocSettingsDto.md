# AsciidocSettingsDto

## Properties

| Name                                               | Type     | Description                | Notes      |
| -------------------------------------------------- | -------- | -------------------------- | ---------- |
| **tag_regexp**                                     | **str**  |                            | [optional] |
| **html_in_passthrough**                            | **bool** | Default: &#x60;false&#x60; | [optional] |
| **nontranslatable_monospace_custom_styles_regexp** | **str**  |                            | [optional] |
| **extract_custom_document_attribute_name_regexp**  | **str**  | Default: &#x60;.\*&#x60;   | [optional] |
| **extract_btn_menu_labels**                        | **bool** | Default: &#x60;false&#x60; | [optional] |

## Example

```python
from phrasetms_client.models.asciidoc_settings_dto import AsciidocSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsciidocSettingsDto from a JSON string
asciidoc_settings_dto_instance = AsciidocSettingsDto.from_json(json)
# print the JSON string representation of the object
print AsciidocSettingsDto.to_json()

# convert the object into a dict
asciidoc_settings_dto_dict = asciidoc_settings_dto_instance.to_dict()
# create an instance of AsciidocSettingsDto from a dict
asciidoc_settings_dto_from_dict = AsciidocSettingsDto.from_dict(asciidoc_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
