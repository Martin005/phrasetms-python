# MachineTranslateStatusDto

## Properties

| Name      | Type     | Description | Notes      |
| --------- | -------- | ----------- | ---------- |
| **uid**   | **str**  |             | [optional] |
| **ok**    | **bool** |             | [optional] |
| **error** | **str**  |             | [optional] |

## Example

```python
from phrasetms_client.models.machine_translate_status_dto import MachineTranslateStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of MachineTranslateStatusDto from a JSON string
machine_translate_status_dto_instance = MachineTranslateStatusDto.from_json(json)
# print the JSON string representation of the object
print MachineTranslateStatusDto.to_json()

# convert the object into a dict
machine_translate_status_dto_dict = machine_translate_status_dto_instance.to_dict()
# create an instance of MachineTranslateStatusDto from a dict
machine_translate_status_dto_from_dict = MachineTranslateStatusDto.from_dict(machine_translate_status_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
