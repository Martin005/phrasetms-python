# MachineTranslateResponse

## Properties

| Name             | Type          | Description | Notes      |
| ---------------- | ------------- | ----------- | ---------- |
| **translations** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.machine_translate_response import MachineTranslateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MachineTranslateResponse from a JSON string
machine_translate_response_instance = MachineTranslateResponse.from_json(json)
# print the JSON string representation of the object
print MachineTranslateResponse.to_json()

# convert the object into a dict
machine_translate_response_dict = machine_translate_response_instance.to_dict()
# create an instance of MachineTranslateResponse from a dict
machine_translate_response_from_dict = MachineTranslateResponse.from_dict(machine_translate_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
