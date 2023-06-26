# MORAVIA

## Properties

| Name          | Type     | Description | Notes      |
| ------------- | -------- | ----------- | ---------- |
| **enabled**   | **bool** |             | [optional] |
| **profile**   | **str**  |             | [optional] |
| **ignorable** | **bool** |             | [optional] |
| **instant**   | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.moravia import MORAVIA

# TODO update the JSON string below
json = "{}"
# create an instance of MORAVIA from a JSON string
moravia_instance = MORAVIA.from_json(json)
# print the JSON string representation of the object
print MORAVIA.to_json()

# convert the object into a dict
moravia_dict = moravia_instance.to_dict()
# create an instance of MORAVIA from a dict
moravia_from_dict = MORAVIA.from_dict(moravia_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
