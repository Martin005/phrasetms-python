# TtxSettingsDto

## Properties

| Name                        | Type     | Description   | Notes      |
| --------------------------- | -------- | ------------- | ---------- |
| **save_confirmed_segments** | **bool** | Default: true | [optional] |

## Example

```python
from phrasetms_client.models.ttx_settings_dto import TtxSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TtxSettingsDto from a JSON string
ttx_settings_dto_instance = TtxSettingsDto.from_json(json)
# print the JSON string representation of the object
print TtxSettingsDto.to_json()

# convert the object into a dict
ttx_settings_dto_dict = ttx_settings_dto_instance.to_dict()
# create an instance of TtxSettingsDto from a dict
ttx_settings_dto_from_dict = TtxSettingsDto.from_dict(ttx_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
