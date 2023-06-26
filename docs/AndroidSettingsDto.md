# AndroidSettingsDto

## Properties

| Name               | Type     | Description                | Notes      |
| ------------------ | -------- | -------------------------- | ---------- |
| **tag_regexp**     | **str**  |                            | [optional] |
| **icu_sub_filter** | **bool** | Default: &#x60;false&#x60; | [optional] |

## Example

```python
from phrasetms_client.models.android_settings_dto import AndroidSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AndroidSettingsDto from a JSON string
android_settings_dto_instance = AndroidSettingsDto.from_json(json)
# print the JSON string representation of the object
print AndroidSettingsDto.to_json()

# convert the object into a dict
android_settings_dto_dict = android_settings_dto_instance.to_dict()
# create an instance of AndroidSettingsDto from a dict
android_settings_dto_from_dict = AndroidSettingsDto.from_dict(android_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
