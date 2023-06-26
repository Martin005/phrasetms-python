# MachineTranslateSettingsDto

## Properties

| Name                      | Type                                                                        | Description | Notes      |
| ------------------------- | --------------------------------------------------------------------------- | ----------- | ---------- |
| **id**                    | **str**                                                                     |             | [optional] |
| **uid**                   | **str**                                                                     |             | [optional] |
| **base_name**             | **str**                                                                     |             | [optional] |
| **name**                  | **str**                                                                     |             | [optional] |
| **type**                  | **str**                                                                     |             | [optional] |
| **category**              | **str**                                                                     |             | [optional] |
| **default\_**             | **bool**                                                                    |             | [optional] |
| **include_tags**          | **bool**                                                                    |             | [optional] |
| **mt_quality_estimation** | **bool**                                                                    |             | [optional] |
| **enabled**               | **bool**                                                                    |             | [optional] |
| **args**                  | **Dict[str, str]**                                                          |             | [optional] |
| **langs**                 | [**MachineTranslateSettingsLangsDto**](MachineTranslateSettingsLangsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.machine_translate_settings_dto import MachineTranslateSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MachineTranslateSettingsDto from a JSON string
machine_translate_settings_dto_instance = MachineTranslateSettingsDto.from_json(json)
# print the JSON string representation of the object
print MachineTranslateSettingsDto.to_json()

# convert the object into a dict
machine_translate_settings_dto_dict = machine_translate_settings_dto_instance.to_dict()
# create an instance of MachineTranslateSettingsDto from a dict
machine_translate_settings_dto_from_dict = MachineTranslateSettingsDto.from_dict(machine_translate_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
