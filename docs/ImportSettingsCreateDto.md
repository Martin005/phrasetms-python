# ImportSettingsCreateDto

## Properties

| Name                     | Type                                                              | Description | Notes |
| ------------------------ | ----------------------------------------------------------------- | ----------- | ----- |
| **name**                 | **str**                                                           |             |
| **file_import_settings** | [**FileImportSettingsCreateDto**](FileImportSettingsCreateDto.md) |             |

## Example

```python
from phrasetms_client.models.import_settings_create_dto import ImportSettingsCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImportSettingsCreateDto from a JSON string
import_settings_create_dto_instance = ImportSettingsCreateDto.from_json(json)
# print the JSON string representation of the object
print ImportSettingsCreateDto.to_json()

# convert the object into a dict
import_settings_create_dto_dict = import_settings_create_dto_instance.to_dict()
# create an instance of ImportSettingsCreateDto from a dict
import_settings_create_dto_from_dict = ImportSettingsCreateDto.from_dict(import_settings_create_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
