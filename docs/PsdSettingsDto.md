# PsdSettingsDto

## Properties

| Name                      | Type     | Description   | Notes      |
| ------------------------- | -------- | ------------- | ---------- |
| **extract_hidden_layers** | **bool** | Default: true | [optional] |
| **extract_locked_layers** | **bool** | Default: true | [optional] |
| **tag_regexp**            | **str**  |               | [optional] |

## Example

```python
from phrasetms_client.models.psd_settings_dto import PsdSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PsdSettingsDto from a JSON string
psd_settings_dto_instance = PsdSettingsDto.from_json(json)
# print the JSON string representation of the object
print PsdSettingsDto.to_json()

# convert the object into a dict
psd_settings_dto_dict = psd_settings_dto_instance.to_dict()
# create an instance of PsdSettingsDto from a dict
psd_settings_dto_from_dict = PsdSettingsDto.from_dict(psd_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
