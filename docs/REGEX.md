# REGEX

## Properties

| Name      | Type                                                      | Description | Notes      |
| --------- | --------------------------------------------------------- | ----------- | ---------- |
| **rules** | [**List[RegexpCheckRuleDtoV2]**](RegexpCheckRuleDtoV2.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.regex import REGEX

# TODO update the JSON string below
json = "{}"
# create an instance of REGEX from a JSON string
regex_instance = REGEX.from_json(json)
# print the JSON string representation of the object
print REGEX.to_json()

# convert the object into a dict
regex_dict = regex_instance.to_dict()
# create an instance of REGEX from a dict
regex_from_dict = REGEX.from_dict(regex_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
