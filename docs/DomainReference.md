# DomainReference

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **name** | **str** |             | [optional] |
| **id**   | **str** |             | [optional] |
| **uid**  | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.domain_reference import DomainReference

# TODO update the JSON string below
json = "{}"
# create an instance of DomainReference from a JSON string
domain_reference_instance = DomainReference.from_json(json)
# print the JSON string representation of the object
print DomainReference.to_json()

# convert the object into a dict
domain_reference_dict = domain_reference_instance.to_dict()
# create an instance of DomainReference from a dict
domain_reference_from_dict = DomainReference.from_dict(domain_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
