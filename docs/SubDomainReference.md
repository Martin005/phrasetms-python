# SubDomainReference

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **name** | **str** |             | [optional] |
| **id**   | **str** |             | [optional] |
| **uid**  | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.sub_domain_reference import SubDomainReference

# TODO update the JSON string below
json = "{}"
# create an instance of SubDomainReference from a JSON string
sub_domain_reference_instance = SubDomainReference.from_json(json)
# print the JSON string representation of the object
print SubDomainReference.to_json()

# convert the object into a dict
sub_domain_reference_dict = sub_domain_reference_instance.to_dict()
# create an instance of SubDomainReference from a dict
sub_domain_reference_from_dict = SubDomainReference.from_dict(sub_domain_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
