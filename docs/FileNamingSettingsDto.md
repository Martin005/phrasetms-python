# FileNamingSettingsDto

## Properties

| Name                       | Type     | Description | Notes      |
| -------------------------- | -------- | ----------- | ---------- |
| **rename_completed**       | **bool** |             | [optional] |
| **completed_file_pattern** | **str**  |             | [optional] |
| **target_folder_path**     | **str**  |             | [optional] |

## Example

```python
from phrasetms_client.models.file_naming_settings_dto import FileNamingSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileNamingSettingsDto from a JSON string
file_naming_settings_dto_instance = FileNamingSettingsDto.from_json(json)
# print the JSON string representation of the object
print FileNamingSettingsDto.to_json()

# convert the object into a dict
file_naming_settings_dto_dict = file_naming_settings_dto_instance.to_dict()
# create an instance of FileNamingSettingsDto from a dict
file_naming_settings_dto_from_dict = FileNamingSettingsDto.from_dict(file_naming_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
