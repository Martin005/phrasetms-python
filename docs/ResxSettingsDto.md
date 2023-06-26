# ResxSettingsDto

## Properties

| Name                | Type     | Description | Notes      |
| ------------------- | -------- | ----------- | ---------- |
| **tag_regexp**      | **str**  |             | [optional] |
| **html_sub_filter** | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.resx_settings_dto import ResxSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResxSettingsDto from a JSON string
resx_settings_dto_instance = ResxSettingsDto.from_json(json)
# print the JSON string representation of the object
print ResxSettingsDto.to_json()

# convert the object into a dict
resx_settings_dto_dict = resx_settings_dto_instance.to_dict()
# create an instance of ResxSettingsDto from a dict
resx_settings_dto_from_dict = ResxSettingsDto.from_dict(resx_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
