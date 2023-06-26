# CustomFileTypeDto

## Properties

| Name                     | Type                                                  | Description | Notes      |
| ------------------------ | ----------------------------------------------------- | ----------- | ---------- |
| **uid**                  | **str**                                               |             | [optional] |
| **name**                 | **str**                                               |             | [optional] |
| **filename_pattern**     | **str**                                               |             | [optional] |
| **type**                 | **str**                                               |             | [optional] |
| **created_by**           | [**UserReference**](UserReference.md)                 |             | [optional] |
| **date_created**         | **datetime**                                          |             | [optional] |
| **file_import_settings** | [**FileImportSettingsDto**](FileImportSettingsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.custom_file_type_dto import CustomFileTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFileTypeDto from a JSON string
custom_file_type_dto_instance = CustomFileTypeDto.from_json(json)
# print the JSON string representation of the object
print CustomFileTypeDto.to_json()

# convert the object into a dict
custom_file_type_dto_dict = custom_file_type_dto_instance.to_dict()
# create an instance of CustomFileTypeDto from a dict
custom_file_type_dto_from_dict = CustomFileTypeDto.from_dict(custom_file_type_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
