# CustomFieldOptionDto

## Properties

| Name      | Type    | Description | Notes      |
| --------- | ------- | ----------- | ---------- |
| **uid**   | **str** |             | [optional] |
| **value** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.custom_field_option_dto import CustomFieldOptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldOptionDto from a JSON string
custom_field_option_dto_instance = CustomFieldOptionDto.from_json(json)
# print the JSON string representation of the object
print CustomFieldOptionDto.to_json()

# convert the object into a dict
custom_field_option_dto_dict = custom_field_option_dto_instance.to_dict()
# create an instance of CustomFieldOptionDto from a dict
custom_field_option_dto_from_dict = CustomFieldOptionDto.from_dict(custom_field_option_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
