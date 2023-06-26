# ImportSettingsDto

## Properties

| Name                     | Type                                                  | Description | Notes      |
| ------------------------ | ----------------------------------------------------- | ----------- | ---------- |
| **uid**                  | **str**                                               |             | [optional] |
| **name**                 | **str**                                               |             | [optional] |
| **created_by**           | [**UserReference**](UserReference.md)                 |             | [optional] |
| **date_created**         | **datetime**                                          |             | [optional] |
| **file_import_settings** | [**FileImportSettingsDto**](FileImportSettingsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.import_settings_dto import ImportSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImportSettingsDto from a JSON string
import_settings_dto_instance = ImportSettingsDto.from_json(json)
# print the JSON string representation of the object
print ImportSettingsDto.to_json()

# convert the object into a dict
import_settings_dto_dict = import_settings_dto_instance.to_dict()
# create an instance of ImportSettingsDto from a dict
import_settings_dto_from_dict = ImportSettingsDto.from_dict(import_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
