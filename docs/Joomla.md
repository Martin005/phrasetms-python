# Joomla

## Properties

| Name      | Type    | Description | Notes |
| --------- | ------- | ----------- | ----- |
| **host**  | **str** |             |
| **token** | **str** |             |

## Example

```python
from phrasetms_client.models.joomla import Joomla

# TODO update the JSON string below
json = "{}"
# create an instance of Joomla from a JSON string
joomla_instance = Joomla.from_json(json)
# print the JSON string representation of the object
print Joomla.to_json()

# convert the object into a dict
joomla_dict = joomla_instance.to_dict()
# create an instance of Joomla from a dict
joomla_from_dict = Joomla.from_dict(joomla_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
