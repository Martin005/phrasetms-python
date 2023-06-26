# XlsSettingsDto

## Properties

| Name                  | Type     | Description        | Notes      |
| --------------------- | -------- | ------------------ | ---------- |
| **sheet_names**       | **bool** | Default: false     | [optional] |
| **hidden**            | **bool** | Default: false     | [optional] |
| **comments**          | **bool** | Default: false     | [optional] |
| **other**             | **bool** | Default: false     | [optional] |
| **cell_flow**         | **str**  | Default: DownRight | [optional] |
| **html_subfilter**    | **bool** | Default: false     | [optional] |
| **tag_regexp**        | **str**  |                    | [optional] |
| **specified_columns** | **str**  |                    | [optional] |

## Example

```python
from phrasetms_client.models.xls_settings_dto import XlsSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of XlsSettingsDto from a JSON string
xls_settings_dto_instance = XlsSettingsDto.from_json(json)
# print the JSON string representation of the object
print XlsSettingsDto.to_json()

# convert the object into a dict
xls_settings_dto_dict = xls_settings_dto_instance.to_dict()
# create an instance of XlsSettingsDto from a dict
xls_settings_dto_from_dict = XlsSettingsDto.from_dict(xls_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
