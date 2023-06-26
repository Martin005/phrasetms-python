# PageDtoCustomFieldOptionDto

## Properties

| Name                   | Type                                                      | Description | Notes      |
| ---------------------- | --------------------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                                   |             | [optional] |
| **total_pages**        | **int**                                                   |             | [optional] |
| **page_size**          | **int**                                                   |             | [optional] |
| **page_number**        | **int**                                                   |             | [optional] |
| **number_of_elements** | **int**                                                   |             | [optional] |
| **content**            | [**List[CustomFieldOptionDto]**](CustomFieldOptionDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_custom_field_option_dto import PageDtoCustomFieldOptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoCustomFieldOptionDto from a JSON string
page_dto_custom_field_option_dto_instance = PageDtoCustomFieldOptionDto.from_json(json)
# print the JSON string representation of the object
print PageDtoCustomFieldOptionDto.to_json()

# convert the object into a dict
page_dto_custom_field_option_dto_dict = page_dto_custom_field_option_dto_instance.to_dict()
# create an instance of PageDtoCustomFieldOptionDto from a dict
page_dto_custom_field_option_dto_from_dict = PageDtoCustomFieldOptionDto.from_dict(page_dto_custom_field_option_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
