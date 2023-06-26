# PageDtoString

## Properties

| Name                   | Type          | Description | Notes      |
| ---------------------- | ------------- | ----------- | ---------- |
| **total_elements**     | **int**       |             | [optional] |
| **total_pages**        | **int**       |             | [optional] |
| **page_size**          | **int**       |             | [optional] |
| **page_number**        | **int**       |             | [optional] |
| **number_of_elements** | **int**       |             | [optional] |
| **content**            | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_string import PageDtoString

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoString from a JSON string
page_dto_string_instance = PageDtoString.from_json(json)
# print the JSON string representation of the object
print PageDtoString.to_json()

# convert the object into a dict
page_dto_string_dict = page_dto_string_instance.to_dict()
# create an instance of PageDtoString from a dict
page_dto_string_from_dict = PageDtoString.from_dict(page_dto_string_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
