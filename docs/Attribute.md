# Attribute

## Properties

| Name               | Type                                | Description | Notes      |
| ------------------ | ----------------------------------- | ----------- | ---------- |
| **name**           | **str**                             |             | [optional] |
| **type**           | **str**                             |             | [optional] |
| **sub_attributes** | [**List[Attribute]**](Attribute.md) |             | [optional] |
| **multi_valued**   | **bool**                            |             | [optional] |
| **description**    | **str**                             |             | [optional] |
| **required**       | **bool**                            |             | [optional] |
| **case_exact**     | **bool**                            |             | [optional] |
| **mutability**     | **str**                             |             | [optional] |
| **returned**       | **str**                             |             | [optional] |
| **uniqueness**     | **str**                             |             | [optional] |

## Example

```python
from phrasetms_client.models.attribute import Attribute

# TODO update the JSON string below
json = "{}"
# create an instance of Attribute from a JSON string
attribute_instance = Attribute.from_json(json)
# print the JSON string representation of the object
print Attribute.to_json()

# convert the object into a dict
attribute_dict = attribute_instance.to_dict()
# create an instance of Attribute from a dict
attribute_from_dict = Attribute.from_dict(attribute_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
