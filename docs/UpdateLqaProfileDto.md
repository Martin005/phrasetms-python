# UpdateLqaProfileDto

## Properties

| Name                    | Type                                                | Description | Notes      |
| ----------------------- | --------------------------------------------------- | ----------- | ---------- |
| **name**                | **str**                                             |             |
| **error_categories**    | [**ErrorCategoriesDto**](ErrorCategoriesDto.md)     |             |
| **penalty_points**      | [**PenaltyPointsDto**](PenaltyPointsDto.md)         |             | [optional] |
| **pass_fail_threshold** | [**PassFailThresholdDto**](PassFailThresholdDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.update_lqa_profile_dto import UpdateLqaProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLqaProfileDto from a JSON string
update_lqa_profile_dto_instance = UpdateLqaProfileDto.from_json(json)
# print the JSON string representation of the object
print UpdateLqaProfileDto.to_json()

# convert the object into a dict
update_lqa_profile_dto_dict = update_lqa_profile_dto_instance.to_dict()
# create an instance of UpdateLqaProfileDto from a dict
update_lqa_profile_dto_from_dict = UpdateLqaProfileDto.from_dict(update_lqa_profile_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
