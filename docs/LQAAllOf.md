# LQAAllOf

## Properties

| Name                | Type                                  | Description | Notes      |
| ------------------- | ------------------------------------- | ----------- | ---------- |
| **references**      | [**LQAReferences**](LQAReferences.md) |             | [optional] |
| **lqa_description** | **str**                               |             | [optional] |

## Example

```python
from phrasetms_client.models.lqa_all_of import LQAAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of LQAAllOf from a JSON string
lqa_all_of_instance = LQAAllOf.from_json(json)
# print the JSON string representation of the object
print LQAAllOf.to_json()

# convert the object into a dict
lqa_all_of_dict = lqa_all_of_instance.to_dict()
# create an instance of LQAAllOf from a dict
lqa_all_of_from_dict = LQAAllOf.from_dict(lqa_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
