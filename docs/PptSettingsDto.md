# PptSettingsDto

## Properties

| Name              | Type     | Description    | Notes      |
| ----------------- | -------- | -------------- | ---------- |
| **hidden_slides** | **bool** | Default: false | [optional] |
| **other**         | **bool** | Default: false | [optional] |
| **notes**         | **bool** | Default: false | [optional] |
| **master_slides** | **bool** | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.ppt_settings_dto import PptSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PptSettingsDto from a JSON string
ppt_settings_dto_instance = PptSettingsDto.from_json(json)
# print the JSON string representation of the object
print PptSettingsDto.to_json()

# convert the object into a dict
ppt_settings_dto_dict = ppt_settings_dto_instance.to_dict()
# create an instance of PptSettingsDto from a dict
ppt_settings_dto_from_dict = PptSettingsDto.from_dict(ppt_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
