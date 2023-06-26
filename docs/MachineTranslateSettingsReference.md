# MachineTranslateSettingsReference

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **id**   | **str** |             | [optional] |
| **uid**  | **str** |             | [optional] |
| **name** | **str** |             | [optional] |
| **type** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.machine_translate_settings_reference import MachineTranslateSettingsReference

# TODO update the JSON string below
json = "{}"
# create an instance of MachineTranslateSettingsReference from a JSON string
machine_translate_settings_reference_instance = MachineTranslateSettingsReference.from_json(json)
# print the JSON string representation of the object
print MachineTranslateSettingsReference.to_json()

# convert the object into a dict
machine_translate_settings_reference_dict = machine_translate_settings_reference_instance.to_dict()
# create an instance of MachineTranslateSettingsReference from a dict
machine_translate_settings_reference_from_dict = MachineTranslateSettingsReference.from_dict(machine_translate_settings_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
