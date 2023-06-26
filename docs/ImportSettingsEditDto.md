# ImportSettingsEditDto

## Properties

| Name                     | Type                                                              | Description | Notes |
| ------------------------ | ----------------------------------------------------------------- | ----------- | ----- |
| **uid**                  | **str**                                                           |             |
| **name**                 | **str**                                                           |             |
| **file_import_settings** | [**FileImportSettingsCreateDto**](FileImportSettingsCreateDto.md) |             |

## Example

```python
from phrasetms_client.models.import_settings_edit_dto import ImportSettingsEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImportSettingsEditDto from a JSON string
import_settings_edit_dto_instance = ImportSettingsEditDto.from_json(json)
# print the JSON string representation of the object
print ImportSettingsEditDto.to_json()

# convert the object into a dict
import_settings_edit_dto_dict = import_settings_edit_dto_instance.to_dict()
# create an instance of ImportSettingsEditDto from a dict
import_settings_edit_dto_from_dict = ImportSettingsEditDto.from_dict(import_settings_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
