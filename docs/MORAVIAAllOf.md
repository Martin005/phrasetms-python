# MORAVIAAllOf

## Properties

| Name          | Type     | Description | Notes      |
| ------------- | -------- | ----------- | ---------- |
| **enabled**   | **bool** |             | [optional] |
| **profile**   | **str**  |             | [optional] |
| **ignorable** | **bool** |             | [optional] |
| **instant**   | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.moravia_all_of import MORAVIAAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of MORAVIAAllOf from a JSON string
moravia_all_of_instance = MORAVIAAllOf.from_json(json)
# print the JSON string representation of the object
print MORAVIAAllOf.to_json()

# convert the object into a dict
moravia_all_of_dict = moravia_all_of_instance.to_dict()
# create an instance of MORAVIAAllOf from a dict
moravia_all_of_from_dict = MORAVIAAllOf.from_dict(moravia_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
