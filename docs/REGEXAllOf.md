# REGEXAllOf

## Properties

| Name      | Type                                                      | Description | Notes      |
| --------- | --------------------------------------------------------- | ----------- | ---------- |
| **rules** | [**List[RegexpCheckRuleDtoV2]**](RegexpCheckRuleDtoV2.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.regex_all_of import REGEXAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of REGEXAllOf from a JSON string
regex_all_of_instance = REGEXAllOf.from_json(json)
# print the JSON string representation of the object
print REGEXAllOf.to_json()

# convert the object into a dict
regex_all_of_dict = regex_all_of_instance.to_dict()
# create an instance of REGEXAllOf from a dict
regex_all_of_from_dict = REGEXAllOf.from_dict(regex_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
