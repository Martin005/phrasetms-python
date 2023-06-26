# EditProjectMTSettingsDto

## Properties

| Name                           | Type                              | Description | Notes      |
| ------------------------------ | --------------------------------- | ----------- | ---------- |
| **machine_translate_settings** | [**IdReference**](IdReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.edit_project_mt_settings_dto import EditProjectMTSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditProjectMTSettingsDto from a JSON string
edit_project_mt_settings_dto_instance = EditProjectMTSettingsDto.from_json(json)
# print the JSON string representation of the object
print EditProjectMTSettingsDto.to_json()

# convert the object into a dict
edit_project_mt_settings_dto_dict = edit_project_mt_settings_dto_instance.to_dict()
# create an instance of EditProjectMTSettingsDto from a dict
edit_project_mt_settings_dto_from_dict = EditProjectMTSettingsDto.from_dict(edit_project_mt_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
