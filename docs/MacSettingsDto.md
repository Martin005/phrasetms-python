# MacSettingsDto

## Properties

| Name               | Type     | Description                | Notes      |
| ------------------ | -------- | -------------------------- | ---------- |
| **html_subfilter** | **bool** | Default: false             | [optional] |
| **tag_regexp**     | **str**  |                            | [optional] |
| **icu_sub_filter** | **bool** | Default: &#x60;false&#x60; | [optional] |

## Example

```python
from phrasetms_client.models.mac_settings_dto import MacSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MacSettingsDto from a JSON string
mac_settings_dto_instance = MacSettingsDto.from_json(json)
# print the JSON string representation of the object
print MacSettingsDto.to_json()

# convert the object into a dict
mac_settings_dto_dict = mac_settings_dto_instance.to_dict()
# create an instance of MacSettingsDto from a dict
mac_settings_dto_from_dict = MacSettingsDto.from_dict(mac_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
