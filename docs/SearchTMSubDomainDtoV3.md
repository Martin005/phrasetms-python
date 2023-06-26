# SearchTMSubDomainDtoV3

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **id**   | **int** |             | [optional] |
| **name** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tm_sub_domain_dto_v3 import SearchTMSubDomainDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMSubDomainDtoV3 from a JSON string
search_tm_sub_domain_dto_v3_instance = SearchTMSubDomainDtoV3.from_json(json)
# print the JSON string representation of the object
print SearchTMSubDomainDtoV3.to_json()

# convert the object into a dict
search_tm_sub_domain_dto_v3_dict = search_tm_sub_domain_dto_v3_instance.to_dict()
# create an instance of SearchTMSubDomainDtoV3 from a dict
search_tm_sub_domain_dto_v3_from_dict = SearchTMSubDomainDtoV3.from_dict(search_tm_sub_domain_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
