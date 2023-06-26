# LQA

## Properties

| Name                | Type                                  | Description | Notes      |
| ------------------- | ------------------------------------- | ----------- | ---------- |
| **references**      | [**LQAReferences**](LQAReferences.md) |             | [optional] |
| **lqa_description** | **str**                               |             | [optional] |

## Example

```python
from phrasetms_client.models.lqa import LQA

# TODO update the JSON string below
json = "{}"
# create an instance of LQA from a JSON string
lqa_instance = LQA.from_json(json)
# print the JSON string representation of the object
print LQA.to_json()

# convert the object into a dict
lqa_dict = lqa_instance.to_dict()
# create an instance of LQA from a dict
lqa_from_dict = LQA.from_dict(lqa_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
