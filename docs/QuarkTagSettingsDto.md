# QuarkTagSettingsDto

## Properties

| Name                             | Type     | Description    | Notes      |
| -------------------------------- | -------- | -------------- | ---------- |
| **remove_kerning_tracking_tags** | **bool** | Default: false | [optional] |
| **tag_regexp**                   | **str**  |                | [optional] |

## Example

```python
from phrasetms_client.models.quark_tag_settings_dto import QuarkTagSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuarkTagSettingsDto from a JSON string
quark_tag_settings_dto_instance = QuarkTagSettingsDto.from_json(json)
# print the JSON string representation of the object
print QuarkTagSettingsDto.to_json()

# convert the object into a dict
quark_tag_settings_dto_dict = quark_tag_settings_dto_instance.to_dict()
# create an instance of QuarkTagSettingsDto from a dict
quark_tag_settings_dto_from_dict = QuarkTagSettingsDto.from_dict(quark_tag_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
