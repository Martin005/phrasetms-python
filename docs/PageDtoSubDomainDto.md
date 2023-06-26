# PageDtoSubDomainDto

## Properties

| Name                   | Type                                      | Description | Notes      |
| ---------------------- | ----------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                   |             | [optional] |
| **total_pages**        | **int**                                   |             | [optional] |
| **page_size**          | **int**                                   |             | [optional] |
| **page_number**        | **int**                                   |             | [optional] |
| **number_of_elements** | **int**                                   |             | [optional] |
| **content**            | [**List[SubDomainDto]**](SubDomainDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_sub_domain_dto import PageDtoSubDomainDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoSubDomainDto from a JSON string
page_dto_sub_domain_dto_instance = PageDtoSubDomainDto.from_json(json)
# print the JSON string representation of the object
print PageDtoSubDomainDto.to_json()

# convert the object into a dict
page_dto_sub_domain_dto_dict = page_dto_sub_domain_dto_instance.to_dict()
# create an instance of PageDtoSubDomainDto from a dict
page_dto_sub_domain_dto_from_dict = PageDtoSubDomainDto.from_dict(page_dto_sub_domain_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
