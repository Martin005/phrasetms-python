# PenaltyPointsDto

Penalty points for each severity level. By default neutral is 0, minor is 1, major is 5, critical is 10.

## Properties

| Name         | Type                              | Description | Notes      |
| ------------ | --------------------------------- | ----------- | ---------- |
| **neutral**  | [**SeverityDto**](SeverityDto.md) |             | [optional] |
| **minor**    | [**SeverityDto**](SeverityDto.md) |             | [optional] |
| **major**    | [**SeverityDto**](SeverityDto.md) |             | [optional] |
| **critical** | [**SeverityDto**](SeverityDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.penalty_points_dto import PenaltyPointsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PenaltyPointsDto from a JSON string
penalty_points_dto_instance = PenaltyPointsDto.from_json(json)
# print the JSON string representation of the object
print PenaltyPointsDto.to_json()

# convert the object into a dict
penalty_points_dto_dict = penalty_points_dto_instance.to_dict()
# create an instance of PenaltyPointsDto from a dict
penalty_points_dto_from_dict = PenaltyPointsDto.from_dict(penalty_points_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
