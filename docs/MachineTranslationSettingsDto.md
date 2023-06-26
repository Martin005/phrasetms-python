# MachineTranslationSettingsDto

Machine translation related settings

## Properties

| Name                           | Type     | Description                                                                                            | Notes      |
| ------------------------------ | -------- | ------------------------------------------------------------------------------------------------------ | ---------- |
| **use_machine_translation**    | **bool** | Pre-translate from machine translation. Default: false                                                 | [optional] |
| **lock100_percent_matches**    | **bool** | Lock section: 100% machine translation matches. Default: false                                         | [optional] |
| **confirm100_percent_matches** | **bool** | Set segment status to confirmed for: 100% translation machine matches. Default: false                  | [optional] |
| **use_alt_trans_only**         | **bool** | Do not put machine translations to target and use alt-trans fields (alt-trans in mxlf). Default: false | [optional] |
| **mt_qe_matches_in_editors**   | **bool** | Display quality-estimated machine translation matches in Memsource Editor. Default: false              | [optional] |
| **mt_for_tm_above100**         | **bool** | Use machine translation for segments with a TM match of 100% or more. Default: false                   | [optional] |

## Example

```python
from phrasetms_client.models.machine_translation_settings_dto import MachineTranslationSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MachineTranslationSettingsDto from a JSON string
machine_translation_settings_dto_instance = MachineTranslationSettingsDto.from_json(json)
# print the JSON string representation of the object
print MachineTranslationSettingsDto.to_json()

# convert the object into a dict
machine_translation_settings_dto_dict = machine_translation_settings_dto_instance.to_dict()
# create an instance of MachineTranslationSettingsDto from a dict
machine_translation_settings_dto_from_dict = MachineTranslationSettingsDto.from_dict(machine_translation_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
