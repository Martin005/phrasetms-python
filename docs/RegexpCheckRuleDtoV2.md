# RegexpCheckRuleDtoV2

## Properties

| Name              | Type     | Description | Notes      |
| ----------------- | -------- | ----------- | ---------- |
| **description**   | **str**  |             | [optional] |
| **source_regexp** | **str**  |             | [optional] |
| **target_regexp** | **str**  |             | [optional] |
| **id**            | **str**  |             | [optional] |
| **ignorable**     | **bool** |             | [optional] |
| **instant**       | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.regexp_check_rule_dto_v2 import RegexpCheckRuleDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of RegexpCheckRuleDtoV2 from a JSON string
regexp_check_rule_dto_v2_instance = RegexpCheckRuleDtoV2.from_json(json)
# print the JSON string representation of the object
print RegexpCheckRuleDtoV2.to_json()

# convert the object into a dict
regexp_check_rule_dto_v2_dict = regexp_check_rule_dto_v2_instance.to_dict()
# create an instance of RegexpCheckRuleDtoV2 from a dict
regexp_check_rule_dto_v2_from_dict = RegexpCheckRuleDtoV2.from_dict(regexp_check_rule_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
