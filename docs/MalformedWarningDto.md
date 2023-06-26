# MalformedWarningDto

## Properties

| Name        | Type    | Description | Notes      |
| ----------- | ------- | ----------- | ---------- |
| **message** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.malformed_warning_dto import MalformedWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of MalformedWarningDto from a JSON string
malformed_warning_dto_instance = MalformedWarningDto.from_json(json)
# print the JSON string representation of the object
print MalformedWarningDto.to_json()

# convert the object into a dict
malformed_warning_dto_dict = malformed_warning_dto_instance.to_dict()
# create an instance of MalformedWarningDto from a dict
malformed_warning_dto_from_dict = MalformedWarningDto.from_dict(malformed_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
