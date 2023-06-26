# PageDtoTermBaseDto

## Properties

| Name                   | Type                                    | Description | Notes      |
| ---------------------- | --------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                 |             | [optional] |
| **total_pages**        | **int**                                 |             | [optional] |
| **page_size**          | **int**                                 |             | [optional] |
| **page_number**        | **int**                                 |             | [optional] |
| **number_of_elements** | **int**                                 |             | [optional] |
| **content**            | [**List[TermBaseDto]**](TermBaseDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_term_base_dto import PageDtoTermBaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoTermBaseDto from a JSON string
page_dto_term_base_dto_instance = PageDtoTermBaseDto.from_json(json)
# print the JSON string representation of the object
print PageDtoTermBaseDto.to_json()

# convert the object into a dict
page_dto_term_base_dto_dict = page_dto_term_base_dto_instance.to_dict()
# create an instance of PageDtoTermBaseDto from a dict
page_dto_term_base_dto_from_dict = PageDtoTermBaseDto.from_dict(page_dto_term_base_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
