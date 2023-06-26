# DocSettingsDto

## Properties

| Name                  | Type     | Description    | Notes      |
| --------------------- | -------- | -------------- | ---------- |
| **comments**          | **bool** | Default: false | [optional] |
| **index**             | **bool** | Default: true  | [optional] |
| **other**             | **bool** | Default: false | [optional] |
| **tag_regexp**        | **str**  |                | [optional] |
| **hyperlink_target**  | **bool** | Default: false | [optional] |
| **join_similar_runs** | **bool** | Default: false | [optional] |
| **target_font**       | **str**  |                | [optional] |
| **properties**        | **bool** | Default: false | [optional] |
| **hidden**            | **bool** | Default: false | [optional] |
| **header_footer**     | **bool** | Default: true  | [optional] |

## Example

```python
from phrasetms_client.models.doc_settings_dto import DocSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocSettingsDto from a JSON string
doc_settings_dto_instance = DocSettingsDto.from_json(json)
# print the JSON string representation of the object
print DocSettingsDto.to_json()

# convert the object into a dict
doc_settings_dto_dict = doc_settings_dto_instance.to_dict()
# create an instance of DocSettingsDto from a dict
doc_settings_dto_from_dict = DocSettingsDto.from_dict(doc_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
