# PageDtoDomainDto

## Properties

| Name                   | Type                                | Description | Notes      |
| ---------------------- | ----------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                             |             | [optional] |
| **total_pages**        | **int**                             |             | [optional] |
| **page_size**          | **int**                             |             | [optional] |
| **page_number**        | **int**                             |             | [optional] |
| **number_of_elements** | **int**                             |             | [optional] |
| **content**            | [**List[DomainDto]**](DomainDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_domain_dto import PageDtoDomainDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoDomainDto from a JSON string
page_dto_domain_dto_instance = PageDtoDomainDto.from_json(json)
# print the JSON string representation of the object
print PageDtoDomainDto.to_json()

# convert the object into a dict
page_dto_domain_dto_dict = page_dto_domain_dto_instance.to_dict()
# create an instance of PageDtoDomainDto from a dict
page_dto_domain_dto_from_dict = PageDtoDomainDto.from_dict(page_dto_domain_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
