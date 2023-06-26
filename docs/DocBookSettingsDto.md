# DocBookSettingsDto

## Properties

| Name                             | Type    | Description | Notes      |
| -------------------------------- | ------- | ----------- | ---------- |
| **include_tags**                 | **str** |             | [optional] |
| **exclude_tags**                 | **str** |             | [optional] |
| **inline_tags**                  | **str** |             | [optional] |
| **inline_tags_non_translatable** | **str** |             | [optional] |
| **tag_regexp**                   | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.doc_book_settings_dto import DocBookSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocBookSettingsDto from a JSON string
doc_book_settings_dto_instance = DocBookSettingsDto.from_json(json)
# print the JSON string representation of the object
print DocBookSettingsDto.to_json()

# convert the object into a dict
doc_book_settings_dto_dict = doc_book_settings_dto_instance.to_dict()
# create an instance of DocBookSettingsDto from a dict
doc_book_settings_dto_from_dict = DocBookSettingsDto.from_dict(doc_book_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
