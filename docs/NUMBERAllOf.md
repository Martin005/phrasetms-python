# NUMBERAllOf

## Properties

| Name          | Type       | Description | Notes      |
| ------------- | ---------- | ----------- | ---------- |
| **ignorable** | **bool**   |             | [optional] |
| **enabled**   | **bool**   |             | [optional] |
| **value**     | **object** |             | [optional] |
| **instant**   | **bool**   |             | [optional] |

## Example

```python
from phrasetms_client.models.number_all_of import NUMBERAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of NUMBERAllOf from a JSON string
number_all_of_instance = NUMBERAllOf.from_json(json)
# print the JSON string representation of the object
print NUMBERAllOf.to_json()

# convert the object into a dict
number_all_of_dict = number_all_of_instance.to_dict()
# create an instance of NUMBERAllOf from a dict
number_all_of_from_dict = NUMBERAllOf.from_dict(number_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
