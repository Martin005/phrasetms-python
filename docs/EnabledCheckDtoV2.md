# EnabledCheckDtoV2

## Properties

| Name             | Type                                                        | Description | Notes      |
| ---------------- | ----------------------------------------------------------- | ----------- | ---------- |
| **checker_type** | **str**                                                     |             | [optional] |
| **context**      | [**EnabledCheckContextDtoV2**](EnabledCheckContextDtoV2.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.enabled_check_dto_v2 import EnabledCheckDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of EnabledCheckDtoV2 from a JSON string
enabled_check_dto_v2_instance = EnabledCheckDtoV2.from_json(json)
# print the JSON string representation of the object
print EnabledCheckDtoV2.to_json()

# convert the object into a dict
enabled_check_dto_v2_dict = enabled_check_dto_v2_instance.to_dict()
# create an instance of EnabledCheckDtoV2 from a dict
enabled_check_dto_v2_from_dict = EnabledCheckDtoV2.from_dict(enabled_check_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
