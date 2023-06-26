# CustomFieldOptionsTruncatedDto

## Properties

| Name                  | Type                                                      | Description                                                                                                      | Notes      |
| --------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------- |
| **truncated_options** | [**List[CustomFieldOptionDto]**](CustomFieldOptionDto.md) | Truncated list of options with size 5. To get all options use endpoint for getting options of the specific field | [optional] |
| **remaining_count**   | **int**                                                   |                                                                                                                  | [optional] |

## Example

```python
from phrasetms_client.models.custom_field_options_truncated_dto import CustomFieldOptionsTruncatedDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldOptionsTruncatedDto from a JSON string
custom_field_options_truncated_dto_instance = CustomFieldOptionsTruncatedDto.from_json(json)
# print the JSON string representation of the object
print CustomFieldOptionsTruncatedDto.to_json()

# convert the object into a dict
custom_field_options_truncated_dto_dict = custom_field_options_truncated_dto_instance.to_dict()
# create an instance of CustomFieldOptionsTruncatedDto from a dict
custom_field_options_truncated_dto_from_dict = CustomFieldOptionsTruncatedDto.from_dict(custom_field_options_truncated_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
