# STRINGAllOf

## Properties

| Name          | Type     | Description | Notes      |
| ------------- | -------- | ----------- | ---------- |
| **ignorable** | **bool** |             | [optional] |
| **enabled**   | **bool** |             | [optional] |
| **value**     | **str**  |             | [optional] |
| **instant**   | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.string_all_of import STRINGAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of STRINGAllOf from a JSON string
string_all_of_instance = STRINGAllOf.from_json(json)
# print the JSON string representation of the object
print STRINGAllOf.to_json()

# convert the object into a dict
string_all_of_dict = string_all_of_instance.to_dict()
# create an instance of STRINGAllOf from a dict
string_all_of_from_dict = STRINGAllOf.from_dict(string_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
