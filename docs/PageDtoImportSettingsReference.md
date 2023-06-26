# PageDtoImportSettingsReference

## Properties

| Name                   | Type                                                            | Description | Notes      |
| ---------------------- | --------------------------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                                         |             | [optional] |
| **total_pages**        | **int**                                                         |             | [optional] |
| **page_size**          | **int**                                                         |             | [optional] |
| **page_number**        | **int**                                                         |             | [optional] |
| **number_of_elements** | **int**                                                         |             | [optional] |
| **content**            | [**List[ImportSettingsReference]**](ImportSettingsReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_import_settings_reference import PageDtoImportSettingsReference

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoImportSettingsReference from a JSON string
page_dto_import_settings_reference_instance = PageDtoImportSettingsReference.from_json(json)
# print the JSON string representation of the object
print PageDtoImportSettingsReference.to_json()

# convert the object into a dict
page_dto_import_settings_reference_dict = page_dto_import_settings_reference_instance.to_dict()
# create an instance of PageDtoImportSettingsReference from a dict
page_dto_import_settings_reference_from_dict = PageDtoImportSettingsReference.from_dict(page_dto_import_settings_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
