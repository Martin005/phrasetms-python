# PoSettingsDto

## Properties

| Name                                   | Type     | Description                | Notes      |
| -------------------------------------- | -------- | -------------------------- | ---------- |
| **tag_regexp**                         | **str**  |                            | [optional] |
| **export_multiline**                   | **bool** | Default: true              | [optional] |
| **html_sub_filter**                    | **bool** | Default: false             | [optional] |
| **segment**                            | **bool** | Default: false             | [optional] |
| **markup_sub_filter_translatable**     | **str**  |                            | [optional] |
| **markup_sub_filter_non_translatable** | **str**  |                            | [optional] |
| **save_confirmed_segments**            | **bool** |                            | [optional] |
| **import_set_segment_confirmed_when**  | **str**  |                            | [optional] |
| **import_set_segment_locked_when**     | **str**  |                            | [optional] |
| **export_confirmed_locked**            | **str**  |                            | [optional] |
| **export_confirmed_not_locked**        | **str**  |                            | [optional] |
| **export_not_confirmed_locked**        | **str**  |                            | [optional] |
| **export_not_confirmed_not_locked**    | **str**  |                            | [optional] |
| **icu_sub_filter**                     | **bool** | Default: &#x60;false&#x60; | [optional] |

## Example

```python
from phrasetms_client.models.po_settings_dto import PoSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PoSettingsDto from a JSON string
po_settings_dto_instance = PoSettingsDto.from_json(json)
# print the JSON string representation of the object
print PoSettingsDto.to_json()

# convert the object into a dict
po_settings_dto_dict = po_settings_dto_instance.to_dict()
# create an instance of PoSettingsDto from a dict
po_settings_dto_from_dict = PoSettingsDto.from_dict(po_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
