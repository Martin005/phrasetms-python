# MatchCounts101Dto

## Properties

| Name         | Type                          | Description | Notes      |
| ------------ | ----------------------------- | ----------- | ---------- |
| **match100** | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match95**  | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match85**  | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match75**  | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match50**  | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match0**   | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match101** | [**CountsDto**](CountsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.match_counts101_dto import MatchCounts101Dto

# TODO update the JSON string below
json = "{}"
# create an instance of MatchCounts101Dto from a JSON string
match_counts101_dto_instance = MatchCounts101Dto.from_json(json)
# print the JSON string representation of the object
print MatchCounts101Dto.to_json()

# convert the object into a dict
match_counts101_dto_dict = match_counts101_dto_instance.to_dict()
# create an instance of MatchCounts101Dto from a dict
match_counts101_dto_from_dict = MatchCounts101Dto.from_dict(match_counts101_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
