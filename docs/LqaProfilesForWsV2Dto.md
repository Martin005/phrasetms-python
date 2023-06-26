# LqaProfilesForWsV2Dto

## Properties

| Name              | Type                                | Description | Notes      |
| ----------------- | ----------------------------------- | ----------- | ---------- |
| **workflow_step** | [**IdReference**](IdReference.md)   |             | [optional] |
| **lqa_profile**   | [**UidReference**](UidReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.lqa_profiles_for_ws_v2_dto import LqaProfilesForWsV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of LqaProfilesForWsV2Dto from a JSON string
lqa_profiles_for_ws_v2_dto_instance = LqaProfilesForWsV2Dto.from_json(json)
# print the JSON string representation of the object
print LqaProfilesForWsV2Dto.to_json()

# convert the object into a dict
lqa_profiles_for_ws_v2_dto_dict = lqa_profiles_for_ws_v2_dto_instance.to_dict()
# create an instance of LqaProfilesForWsV2Dto from a dict
lqa_profiles_for_ws_v2_dto_from_dict = LqaProfilesForWsV2Dto.from_dict(lqa_profiles_for_ws_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
