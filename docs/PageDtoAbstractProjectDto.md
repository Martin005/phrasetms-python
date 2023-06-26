# PageDtoAbstractProjectDto

## Properties

| Name                   | Type                                                  | Description | Notes      |
| ---------------------- | ----------------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                               |             | [optional] |
| **total_pages**        | **int**                                               |             | [optional] |
| **page_size**          | **int**                                               |             | [optional] |
| **page_number**        | **int**                                               |             | [optional] |
| **number_of_elements** | **int**                                               |             | [optional] |
| **content**            | [**List[AbstractProjectDto]**](AbstractProjectDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_abstract_project_dto import PageDtoAbstractProjectDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoAbstractProjectDto from a JSON string
page_dto_abstract_project_dto_instance = PageDtoAbstractProjectDto.from_json(json)
# print the JSON string representation of the object
print PageDtoAbstractProjectDto.to_json()

# convert the object into a dict
page_dto_abstract_project_dto_dict = page_dto_abstract_project_dto_instance.to_dict()
# create an instance of PageDtoAbstractProjectDto from a dict
page_dto_abstract_project_dto_from_dict = PageDtoAbstractProjectDto.from_dict(page_dto_abstract_project_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
