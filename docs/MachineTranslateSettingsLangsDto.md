# MachineTranslateSettingsLangsDto

## Properties

| Name             | Type          | Description                                          | Notes      |
| ---------------- | ------------- | ---------------------------------------------------- | ---------- |
| **id**           | **str**       | Id                                                   | [optional] |
| **source_lang**  | **str**       | Source language for CUSTOMIZABLE engine              | [optional] |
| **target_langs** | **List[str]** | List of target languages for the CUSTOMIZABLE engine | [optional] |

## Example

```python
from phrasetms_client.models.machine_translate_settings_langs_dto import MachineTranslateSettingsLangsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MachineTranslateSettingsLangsDto from a JSON string
machine_translate_settings_langs_dto_instance = MachineTranslateSettingsLangsDto.from_json(json)
# print the JSON string representation of the object
print MachineTranslateSettingsLangsDto.to_json()

# convert the object into a dict
machine_translate_settings_langs_dto_dict = machine_translate_settings_langs_dto_instance.to_dict()
# create an instance of MachineTranslateSettingsLangsDto from a dict
machine_translate_settings_langs_dto_from_dict = MachineTranslateSettingsLangsDto.from_dict(machine_translate_settings_langs_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
