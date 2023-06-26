# EnabledCheckContextDtoV2

## Properties

| Name                       | Type    | Description | Notes      |
| -------------------------- | ------- | ----------- | ---------- |
| **moravia_profile_id**     | **str** |             | [optional] |
| **custom_qa_display_name** | **str** |             | [optional] |
| **provider**               | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.enabled_check_context_dto_v2 import EnabledCheckContextDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of EnabledCheckContextDtoV2 from a JSON string
enabled_check_context_dto_v2_instance = EnabledCheckContextDtoV2.from_json(json)
# print the JSON string representation of the object
print EnabledCheckContextDtoV2.to_json()

# convert the object into a dict
enabled_check_context_dto_v2_dict = enabled_check_context_dto_v2_instance.to_dict()
# create an instance of EnabledCheckContextDtoV2 from a dict
enabled_check_context_dto_v2_from_dict = EnabledCheckContextDtoV2.from_dict(enabled_check_context_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
