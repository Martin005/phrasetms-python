# MemTransMachineTranslateSettingsDto

## Properties

| Name                      | Type                                                                        | Description                               | Notes      |
| ------------------------- | --------------------------------------------------------------------------- | ----------------------------------------- | ---------- |
| **id**                    | **str**                                                                     |                                           | [optional] |
| **uid**                   | **str**                                                                     |                                           | [optional] |
| **base_name**             | **str**                                                                     |                                           | [optional] |
| **name**                  | **str**                                                                     |                                           | [optional] |
| **type**                  | **str**                                                                     |                                           | [optional] |
| **category**              | **str**                                                                     |                                           | [optional] |
| **default\_**             | **bool**                                                                    |                                           | [optional] |
| **include_tags**          | **bool**                                                                    |                                           | [optional] |
| **mt_quality_estimation** | **bool**                                                                    |                                           | [optional] |
| **enabled**               | **bool**                                                                    |                                           | [optional] |
| **glossary_supported**    | **bool**                                                                    |                                           | [optional] |
| **args**                  | **Dict[str, str]**                                                          |                                           | [optional] |
| **langs**                 | [**MachineTranslateSettingsLangsDto**](MachineTranslateSettingsLangsDto.md) |                                           | [optional] |
| **char_count**            | **int**                                                                     | Unknown value is represented by value: -1 | [optional] |

## Example

```python
from phrasetms_client.models.mem_trans_machine_translate_settings_dto import MemTransMachineTranslateSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MemTransMachineTranslateSettingsDto from a JSON string
mem_trans_machine_translate_settings_dto_instance = MemTransMachineTranslateSettingsDto.from_json(json)
# print the JSON string representation of the object
print MemTransMachineTranslateSettingsDto.to_json()

# convert the object into a dict
mem_trans_machine_translate_settings_dto_dict = mem_trans_machine_translate_settings_dto_instance.to_dict()
# create an instance of MemTransMachineTranslateSettingsDto from a dict
mem_trans_machine_translate_settings_dto_from_dict = MemTransMachineTranslateSettingsDto.from_dict(mem_trans_machine_translate_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
