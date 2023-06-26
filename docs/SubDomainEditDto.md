# SubDomainEditDto

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **name** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.sub_domain_edit_dto import SubDomainEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubDomainEditDto from a JSON string
sub_domain_edit_dto_instance = SubDomainEditDto.from_json(json)
# print the JSON string representation of the object
print SubDomainEditDto.to_json()

# convert the object into a dict
sub_domain_edit_dto_dict = sub_domain_edit_dto_instance.to_dict()
# create an instance of SubDomainEditDto from a dict
sub_domain_edit_dto_from_dict = SubDomainEditDto.from_dict(sub_domain_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
