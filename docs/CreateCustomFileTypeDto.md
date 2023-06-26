# CreateCustomFileTypeDto

## Properties

| Name                     | Type                                                              | Description | Notes      |
| ------------------------ | ----------------------------------------------------------------- | ----------- | ---------- |
| **name**                 | **str**                                                           |             |
| **filename_pattern**     | **str**                                                           |             |
| **type**                 | **str**                                                           |             |
| **file_import_settings** | [**FileImportSettingsCreateDto**](FileImportSettingsCreateDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.create_custom_file_type_dto import CreateCustomFileTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomFileTypeDto from a JSON string
create_custom_file_type_dto_instance = CreateCustomFileTypeDto.from_json(json)
# print the JSON string representation of the object
print CreateCustomFileTypeDto.to_json()

# convert the object into a dict
create_custom_file_type_dto_dict = create_custom_file_type_dto_instance.to_dict()
# create an instance of CreateCustomFileTypeDto from a dict
create_custom_file_type_dto_from_dict = CreateCustomFileTypeDto.from_dict(create_custom_file_type_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
