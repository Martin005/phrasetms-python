# SdlXlfSettingsDto

## Properties

| Name                                               | Type     | Description                | Notes      |
| -------------------------------------------------- | -------- | -------------------------- | ---------- |
| **icu_sub_filter**                                 | **bool** | Default: false             | [optional] |
| **skip_import_rules**                              | **str**  | Default: translate&#x3D;no | [optional] |
| **import_as_confirmed_rules**                      | **str**  |                            | [optional] |
| **import_as_locked_rules**                         | **str**  | Default: locked&#x3D;true  | [optional] |
| **export_attrs_when_confirmed_and_locked**         | **str**  | Default: locked&#x3D;true  | [optional] |
| **export_attrs_when_confirmed_and_not_locked**     | **str**  |                            | [optional] |
| **export_attrs_when_not_confirmed_and_locked**     | **str**  | Default: locked&#x3D;true  | [optional] |
| **export_attrs_when_not_confirmed_and_not_locked** | **str**  |                            | [optional] |
| **save_confirmed_segments**                        | **bool** | Default: true              | [optional] |
| **tag_regexp**                                     | **str**  |                            | [optional] |

## Example

```python
from phrasetms_client.models.sdl_xlf_settings_dto import SdlXlfSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SdlXlfSettingsDto from a JSON string
sdl_xlf_settings_dto_instance = SdlXlfSettingsDto.from_json(json)
# print the JSON string representation of the object
print SdlXlfSettingsDto.to_json()

# convert the object into a dict
sdl_xlf_settings_dto_dict = sdl_xlf_settings_dto_instance.to_dict()
# create an instance of SdlXlfSettingsDto from a dict
sdl_xlf_settings_dto_from_dict = SdlXlfSettingsDto.from_dict(sdl_xlf_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
