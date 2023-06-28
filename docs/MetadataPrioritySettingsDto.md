# MetadataPrioritySettingsDto

## Properties

| Name                   | Type                                        | Description | Notes      |
| ---------------------- | ------------------------------------------- | ----------- | ---------- |
| **prioritized_fields** | [**List[MetadataField]**](MetadataField.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.metadata_priority_settings_dto import MetadataPrioritySettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataPrioritySettingsDto from a JSON string
metadata_priority_settings_dto_instance = MetadataPrioritySettingsDto.from_json(json)
# print the JSON string representation of the object
print MetadataPrioritySettingsDto.to_json()

# convert the object into a dict
metadata_priority_settings_dto_dict = metadata_priority_settings_dto_instance.to_dict()
# create an instance of MetadataPrioritySettingsDto from a dict
metadata_priority_settings_dto_from_dict = MetadataPrioritySettingsDto.from_dict(metadata_priority_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
