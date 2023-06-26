# LqaProfileDetailDto

## Properties

| Name                    | Type                                                | Description                                   | Notes |
| ----------------------- | --------------------------------------------------- | --------------------------------------------- | ----- |
| **uid**                 | **str**                                             | UID of the profile                            |
| **name**                | **str**                                             | Name of the profile                           |
| **error_categories**    | [**ErrorCategoriesDto**](ErrorCategoriesDto.md)     |                                               |
| **penalty_points**      | [**PenaltyPointsDto**](PenaltyPointsDto.md)         |                                               |
| **pass_fail_threshold** | [**PassFailThresholdDto**](PassFailThresholdDto.md) |                                               |
| **is_default**          | **bool**                                            | If profile is set as default for organization |
| **created_by**          | [**UserReference**](UserReference.md)               |                                               |
| **date_created**        | **datetime**                                        |                                               |
| **organization**        | [**UidReference**](UidReference.md)                 |                                               |

## Example

```python
from phrasetms_client.models.lqa_profile_detail_dto import LqaProfileDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of LqaProfileDetailDto from a JSON string
lqa_profile_detail_dto_instance = LqaProfileDetailDto.from_json(json)
# print the JSON string representation of the object
print LqaProfileDetailDto.to_json()

# convert the object into a dict
lqa_profile_detail_dto_dict = lqa_profile_detail_dto_instance.to_dict()
# create an instance of LqaProfileDetailDto from a dict
lqa_profile_detail_dto_from_dict = LqaProfileDetailDto.from_dict(lqa_profile_detail_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
