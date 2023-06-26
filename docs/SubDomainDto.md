# SubDomainDto

## Properties

| Name           | Type                                  | Description | Notes      |
| -------------- | ------------------------------------- | ----------- | ---------- |
| **id**         | **str**                               |             | [optional] |
| **uid**        | **str**                               |             | [optional] |
| **name**       | **str**                               |             | [optional] |
| **created_by** | [**UserReference**](UserReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.sub_domain_dto import SubDomainDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubDomainDto from a JSON string
sub_domain_dto_instance = SubDomainDto.from_json(json)
# print the JSON string representation of the object
print SubDomainDto.to_json()

# convert the object into a dict
sub_domain_dto_dict = sub_domain_dto_instance.to_dict()
# create an instance of SubDomainDto from a dict
sub_domain_dto_from_dict = SubDomainDto.from_dict(sub_domain_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
