# STRING

## Properties

| Name          | Type     | Description | Notes      |
| ------------- | -------- | ----------- | ---------- |
| **ignorable** | **bool** |             | [optional] |
| **enabled**   | **bool** |             | [optional] |
| **value**     | **str**  |             | [optional] |
| **instant**   | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.string import STRING

# TODO update the JSON string below
json = "{}"
# create an instance of STRING from a JSON string
string_instance = STRING.from_json(json)
# print the JSON string representation of the object
print STRING.to_json()

# convert the object into a dict
string_dict = string_instance.to_dict()
# create an instance of STRING from a dict
string_from_dict = STRING.from_dict(string_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
