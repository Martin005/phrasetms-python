# DomainEditDto

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **name** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.domain_edit_dto import DomainEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of DomainEditDto from a JSON string
domain_edit_dto_instance = DomainEditDto.from_json(json)
# print the JSON string representation of the object
print DomainEditDto.to_json()

# convert the object into a dict
domain_edit_dto_dict = domain_edit_dto_instance.to_dict()
# create an instance of DomainEditDto from a dict
domain_edit_dto_from_dict = DomainEditDto.from_dict(domain_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
