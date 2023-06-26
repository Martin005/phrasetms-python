# UserStatisticsListDto

envelope for user statistics

## Properties

| Name                | Type                                                | Description | Notes |
| ------------------- | --------------------------------------------------- | ----------- | ----- |
| **user_statistics** | [**List[UserStatisticsDto]**](UserStatisticsDto.md) |             |

## Example

```python
from phrasetms_client.models.user_statistics_list_dto import UserStatisticsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserStatisticsListDto from a JSON string
user_statistics_list_dto_instance = UserStatisticsListDto.from_json(json)
# print the JSON string representation of the object
print UserStatisticsListDto.to_json()

# convert the object into a dict
user_statistics_list_dto_dict = user_statistics_list_dto_instance.to_dict()
# create an instance of UserStatisticsListDto from a dict
user_statistics_list_dto_from_dict = UserStatisticsListDto.from_dict(user_statistics_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
