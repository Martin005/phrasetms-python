# VOID

## Properties

| Name          | Type     | Description | Notes      |
| ------------- | -------- | ----------- | ---------- |
| **ignorable** | **bool** |             | [optional] |
| **enabled**   | **bool** |             | [optional] |
| **instant**   | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.void import VOID

# TODO update the JSON string below
json = "{}"
# create an instance of VOID from a JSON string
void_instance = VOID.from_json(json)
# print the JSON string representation of the object
print VOID.to_json()

# convert the object into a dict
void_dict = void_instance.to_dict()
# create an instance of VOID from a dict
void_from_dict = VOID.from_dict(void_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
