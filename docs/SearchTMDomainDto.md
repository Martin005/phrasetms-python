# SearchTMDomainDto

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **id**   | **int** |             | [optional] |
| **name** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tm_domain_dto import SearchTMDomainDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMDomainDto from a JSON string
search_tm_domain_dto_instance = SearchTMDomainDto.from_json(json)
# print the JSON string representation of the object
print SearchTMDomainDto.to_json()

# convert the object into a dict
search_tm_domain_dto_dict = search_tm_domain_dto_instance.to_dict()
# create an instance of SearchTMDomainDto from a dict
search_tm_domain_dto_from_dict = SearchTMDomainDto.from_dict(search_tm_domain_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
