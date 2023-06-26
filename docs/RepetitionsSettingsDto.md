# RepetitionsSettingsDto

Repetitions related settings

## Properties

| Name                                     | Type     | Description                                                                                              | Notes      |
| ---------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------- | ---------- |
| **auto_propagate_repetitions**           | **bool** | Propagate repetitions. Default: false                                                                    | [optional] |
| **confirm_repetitions**                  | **bool** | Set segment status to confirmed for: Repetitions. Default: false                                         | [optional] |
| **auto_propagate_to_locked_repetitions** | **bool** | Changes in 1st repetition propagate upon confirmation into subsequent locked repetitions. Default: false | [optional] |
| **lock_subsequent_repetitions**          | **bool** | If auto-propagated subsequent repetitions should be locked. Default: false                               | [optional] |

## Example

```python
from phrasetms_client.models.repetitions_settings_dto import RepetitionsSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RepetitionsSettingsDto from a JSON string
repetitions_settings_dto_instance = RepetitionsSettingsDto.from_json(json)
# print the JSON string representation of the object
print RepetitionsSettingsDto.to_json()

# convert the object into a dict
repetitions_settings_dto_dict = repetitions_settings_dto_instance.to_dict()
# create an instance of RepetitionsSettingsDto from a dict
repetitions_settings_dto_from_dict = RepetitionsSettingsDto.from_dict(repetitions_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
