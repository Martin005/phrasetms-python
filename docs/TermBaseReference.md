# TermBaseReference

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **name** | **str** |             | [optional] |
| **id**   | **str** |             | [optional] |
| **uid**  | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.term_base_reference import TermBaseReference

# TODO update the JSON string below
json = "{}"
# create an instance of TermBaseReference from a JSON string
term_base_reference_instance = TermBaseReference.from_json(json)
# print the JSON string representation of the object
print TermBaseReference.to_json()

# convert the object into a dict
term_base_reference_dict = term_base_reference_instance.to_dict()
# create an instance of TermBaseReference from a dict
term_base_reference_from_dict = TermBaseReference.from_dict(term_base_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
