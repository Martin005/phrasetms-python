# DitaSettingsDto

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
from phrasetms_client.models.dita_settings_dto import DitaSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DitaSettingsDto from a JSON string
dita_settings_dto_instance = DitaSettingsDto.from_json(json)
# print the JSON string representation of the object
print DitaSettingsDto.to_json()

# convert the object into a dict
dita_settings_dto_dict = dita_settings_dto_instance.to_dict()
# create an instance of DitaSettingsDto from a dict
dita_settings_dto_from_dict = DitaSettingsDto.from_dict(dita_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
