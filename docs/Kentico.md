# Kentico

## Properties

| Name            | Type    | Description | Notes      |
| --------------- | ------- | ----------- | ---------- |
| **user_name**   | **str** |             |
| **password**    | **str** |             |
| **host**        | **str** |             |
| **source_lang** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.kentico import Kentico

# TODO update the JSON string below
json = "{}"
# create an instance of Kentico from a JSON string
kentico_instance = Kentico.from_json(json)
# print the JSON string representation of the object
print Kentico.to_json()

# convert the object into a dict
kentico_dict = kentico_instance.to_dict()
# create an instance of Kentico from a dict
kentico_from_dict = Kentico.from_dict(kentico_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
