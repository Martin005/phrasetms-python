# Tridion

## Properties

| Name                | Type    | Description | Notes      |
| ------------------- | ------- | ----------- | ---------- |
| **host**            | **str** |             |
| **port**            | **int** |             |
| **user_name**       | **str** |             |
| **password**        | **str** |             |
| **ssh_key_name**    | **str** |             | [optional] |
| **ssh_key**         | **str** |             | [optional] |
| **ssh_pass_phrase** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.tridion import Tridion

# TODO update the JSON string below
json = "{}"
# create an instance of Tridion from a JSON string
tridion_instance = Tridion.from_json(json)
# print the JSON string representation of the object
print Tridion.to_json()

# convert the object into a dict
tridion_dict = tridion_instance.to_dict()
# create an instance of Tridion from a dict
tridion_from_dict = Tridion.from_dict(tridion_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
