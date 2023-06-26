# PageDtoCustomFieldDto

## Properties

| Name                   | Type                                          | Description | Notes      |
| ---------------------- | --------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                       |             | [optional] |
| **total_pages**        | **int**                                       |             | [optional] |
| **page_size**          | **int**                                       |             | [optional] |
| **page_number**        | **int**                                       |             | [optional] |
| **number_of_elements** | **int**                                       |             | [optional] |
| **content**            | [**List[CustomFieldDto]**](CustomFieldDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_custom_field_dto import PageDtoCustomFieldDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoCustomFieldDto from a JSON string
page_dto_custom_field_dto_instance = PageDtoCustomFieldDto.from_json(json)
# print the JSON string representation of the object
print PageDtoCustomFieldDto.to_json()

# convert the object into a dict
page_dto_custom_field_dto_dict = page_dto_custom_field_dto_instance.to_dict()
# create an instance of PageDtoCustomFieldDto from a dict
page_dto_custom_field_dto_from_dict = PageDtoCustomFieldDto.from_dict(page_dto_custom_field_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
