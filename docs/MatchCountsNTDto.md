# MatchCountsNTDto

## Properties

| Name         | Type                          | Description | Notes      |
| ------------ | ----------------------------- | ----------- | ---------- |
| **match100** | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match95**  | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match85**  | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match75**  | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match50**  | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match0**   | [**CountsDto**](CountsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.match_counts_nt_dto import MatchCountsNTDto

# TODO update the JSON string below
json = "{}"
# create an instance of MatchCountsNTDto from a JSON string
match_counts_nt_dto_instance = MatchCountsNTDto.from_json(json)
# print the JSON string representation of the object
print MatchCountsNTDto.to_json()

# convert the object into a dict
match_counts_nt_dto_dict = match_counts_nt_dto_instance.to_dict()
# create an instance of MatchCountsNTDto from a dict
match_counts_nt_dto_from_dict = MatchCountsNTDto.from_dict(match_counts_nt_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
