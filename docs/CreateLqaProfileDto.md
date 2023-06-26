# CreateLqaProfileDto

## Properties

| Name                    | Type                                                | Description | Notes      |
| ----------------------- | --------------------------------------------------- | ----------- | ---------- |
| **name**                | **str**                                             |             |
| **error_categories**    | [**ErrorCategoriesDto**](ErrorCategoriesDto.md)     |             |
| **penalty_points**      | [**PenaltyPointsDto**](PenaltyPointsDto.md)         |             | [optional] |
| **pass_fail_threshold** | [**PassFailThresholdDto**](PassFailThresholdDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.create_lqa_profile_dto import CreateLqaProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLqaProfileDto from a JSON string
create_lqa_profile_dto_instance = CreateLqaProfileDto.from_json(json)
# print the JSON string representation of the object
print CreateLqaProfileDto.to_json()

# convert the object into a dict
create_lqa_profile_dto_dict = create_lqa_profile_dto_instance.to_dict()
# create an instance of CreateLqaProfileDto from a dict
create_lqa_profile_dto_from_dict = CreateLqaProfileDto.from_dict(create_lqa_profile_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
