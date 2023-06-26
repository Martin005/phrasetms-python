# DomainDto

## Properties

| Name           | Type                                  | Description | Notes      |
| -------------- | ------------------------------------- | ----------- | ---------- |
| **id**         | **str**                               |             | [optional] |
| **uid**        | **str**                               |             | [optional] |
| **name**       | **str**                               |             | [optional] |
| **created_by** | [**UserReference**](UserReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.domain_dto import DomainDto

# TODO update the JSON string below
json = "{}"
# create an instance of DomainDto from a JSON string
domain_dto_instance = DomainDto.from_json(json)
# print the JSON string representation of the object
print DomainDto.to_json()

# convert the object into a dict
domain_dto_dict = domain_dto_instance.to_dict()
# create an instance of DomainDto from a dict
domain_dto_from_dict = DomainDto.from_dict(domain_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
