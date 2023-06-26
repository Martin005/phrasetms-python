# PropertiesSettingsDto

## Properties

| Name           | Type    | Description | Notes      |
| -------------- | ------- | ----------- | ---------- |
| **tag_regexp** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.properties_settings_dto import PropertiesSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PropertiesSettingsDto from a JSON string
properties_settings_dto_instance = PropertiesSettingsDto.from_json(json)
# print the JSON string representation of the object
print PropertiesSettingsDto.to_json()

# convert the object into a dict
properties_settings_dto_dict = properties_settings_dto_instance.to_dict()
# create an instance of PropertiesSettingsDto from a dict
properties_settings_dto_from_dict = PropertiesSettingsDto.from_dict(properties_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
