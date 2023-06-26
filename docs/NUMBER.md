# NUMBER

## Properties

| Name          | Type       | Description | Notes      |
| ------------- | ---------- | ----------- | ---------- |
| **ignorable** | **bool**   |             | [optional] |
| **enabled**   | **bool**   |             | [optional] |
| **value**     | **object** |             | [optional] |
| **instant**   | **bool**   |             | [optional] |

## Example

```python
from phrasetms_client.models.number import NUMBER

# TODO update the JSON string below
json = "{}"
# create an instance of NUMBER from a JSON string
number_instance = NUMBER.from_json(json)
# print the JSON string representation of the object
print NUMBER.to_json()

# convert the object into a dict
number_dict = number_instance.to_dict()
# create an instance of NUMBER from a dict
number_from_dict = NUMBER.from_dict(number_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
