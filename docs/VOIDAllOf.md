# VOIDAllOf

## Properties

| Name          | Type     | Description | Notes      |
| ------------- | -------- | ----------- | ---------- |
| **ignorable** | **bool** |             | [optional] |
| **enabled**   | **bool** |             | [optional] |
| **instant**   | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.void_all_of import VOIDAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of VOIDAllOf from a JSON string
void_all_of_instance = VOIDAllOf.from_json(json)
# print the JSON string representation of the object
print VOIDAllOf.to_json()

# convert the object into a dict
void_all_of_dict = void_all_of_instance.to_dict()
# create an instance of VOIDAllOf from a dict
void_all_of_from_dict = VOIDAllOf.from_dict(void_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
