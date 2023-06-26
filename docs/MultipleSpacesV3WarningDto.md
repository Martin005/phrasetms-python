# MultipleSpacesV3WarningDto

## Properties

| Name          | Type                              | Description | Notes      |
| ------------- | --------------------------------- | ----------- | ---------- |
| **spaces**    | **str**                           |             | [optional] |
| **positions** | [**List[Position]**](Position.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.multiple_spaces_v3_warning_dto import MultipleSpacesV3WarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleSpacesV3WarningDto from a JSON string
multiple_spaces_v3_warning_dto_instance = MultipleSpacesV3WarningDto.from_json(json)
# print the JSON string representation of the object
print MultipleSpacesV3WarningDto.to_json()

# convert the object into a dict
multiple_spaces_v3_warning_dto_dict = multiple_spaces_v3_warning_dto_instance.to_dict()
# create an instance of MultipleSpacesV3WarningDto from a dict
multiple_spaces_v3_warning_dto_from_dict = MultipleSpacesV3WarningDto.from_dict(multiple_spaces_v3_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
