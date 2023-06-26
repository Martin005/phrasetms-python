# ImportSettingsReference

## Properties

| Name             | Type                                  | Description | Notes      |
| ---------------- | ------------------------------------- | ----------- | ---------- |
| **uid**          | **str**                               |             | [optional] |
| **name**         | **str**                               |             | [optional] |
| **created_by**   | [**UserReference**](UserReference.md) |             | [optional] |
| **date_created** | **datetime**                          |             | [optional] |

## Example

```python
from phrasetms_client.models.import_settings_reference import ImportSettingsReference

# TODO update the JSON string below
json = "{}"
# create an instance of ImportSettingsReference from a JSON string
import_settings_reference_instance = ImportSettingsReference.from_json(json)
# print the JSON string representation of the object
print ImportSettingsReference.to_json()

# convert the object into a dict
import_settings_reference_dict = import_settings_reference_instance.to_dict()
# create an instance of ImportSettingsReference from a dict
import_settings_reference_from_dict = ImportSettingsReference.from_dict(import_settings_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
