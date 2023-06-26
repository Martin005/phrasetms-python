# UpdateCustomFileTypeDto

## Properties

| Name                     | Type                                                              | Description | Notes      |
| ------------------------ | ----------------------------------------------------------------- | ----------- | ---------- |
| **name**                 | **str**                                                           |             | [optional] |
| **filename_pattern**     | **str**                                                           |             | [optional] |
| **type**                 | **str**                                                           |             | [optional] |
| **file_import_settings** | [**FileImportSettingsCreateDto**](FileImportSettingsCreateDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.update_custom_file_type_dto import UpdateCustomFileTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomFileTypeDto from a JSON string
update_custom_file_type_dto_instance = UpdateCustomFileTypeDto.from_json(json)
# print the JSON string representation of the object
print UpdateCustomFileTypeDto.to_json()

# convert the object into a dict
update_custom_file_type_dto_dict = update_custom_file_type_dto_instance.to_dict()
# create an instance of UpdateCustomFileTypeDto from a dict
update_custom_file_type_dto_from_dict = UpdateCustomFileTypeDto.from_dict(update_custom_file_type_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
