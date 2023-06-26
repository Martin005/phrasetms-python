# PageDtoUserDto

## Properties

| Name                   | Type                            | Description | Notes      |
| ---------------------- | ------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                         |             | [optional] |
| **total_pages**        | **int**                         |             | [optional] |
| **page_size**          | **int**                         |             | [optional] |
| **page_number**        | **int**                         |             | [optional] |
| **number_of_elements** | **int**                         |             | [optional] |
| **content**            | [**List[UserDto]**](UserDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_user_dto import PageDtoUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoUserDto from a JSON string
page_dto_user_dto_instance = PageDtoUserDto.from_json(json)
# print the JSON string representation of the object
print PageDtoUserDto.to_json()

# convert the object into a dict
page_dto_user_dto_dict = page_dto_user_dto_instance.to_dict()
# create an instance of PageDtoUserDto from a dict
page_dto_user_dto_from_dict = PageDtoUserDto.from_dict(page_dto_user_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
