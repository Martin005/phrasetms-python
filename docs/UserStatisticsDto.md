# UserStatisticsDto

user login statistics

## Properties

| Name           | Type         | Description | Notes      |
| -------------- | ------------ | ----------- | ---------- |
| **var_date**   | **datetime** |             | [optional] |
| **ip_address** | **str**      |             | [optional] |
| **ip_country** | **str**      |             | [optional] |
| **user_agent** | **str**      |             | [optional] |

## Example

```python
from phrasetms_client.models.user_statistics_dto import UserStatisticsDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserStatisticsDto from a JSON string
user_statistics_dto_instance = UserStatisticsDto.from_json(json)
# print the JSON string representation of the object
print UserStatisticsDto.to_json()

# convert the object into a dict
user_statistics_dto_dict = user_statistics_dto_instance.to_dict()
# create an instance of UserStatisticsDto from a dict
user_statistics_dto_from_dict = UserStatisticsDto.from_dict(user_statistics_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
