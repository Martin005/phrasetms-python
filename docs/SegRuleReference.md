# SegRuleReference

## Properties

| Name         | Type     | Description | Notes      |
| ------------ | -------- | ----------- | ---------- |
| **id**       | **str**  |             | [optional] |
| **uid**      | **str**  |             | [optional] |
| **language** | **str**  |             | [optional] |
| **name**     | **str**  |             | [optional] |
| **filename** | **str**  |             | [optional] |
| **primary**  | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.seg_rule_reference import SegRuleReference

# TODO update the JSON string below
json = "{}"
# create an instance of SegRuleReference from a JSON string
seg_rule_reference_instance = SegRuleReference.from_json(json)
# print the JSON string representation of the object
print SegRuleReference.to_json()

# convert the object into a dict
seg_rule_reference_dict = seg_rule_reference_instance.to_dict()
# create an instance of SegRuleReference from a dict
seg_rule_reference_from_dict = SegRuleReference.from_dict(seg_rule_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
