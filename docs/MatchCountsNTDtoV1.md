# MatchCountsNTDtoV1

## Properties

| Name         | Type                          | Description | Notes      |
| ------------ | ----------------------------- | ----------- | ---------- |
| **match100** | [**CountsDto**](CountsDto.md) |             | [optional] |
| **match99**  | [**CountsDto**](CountsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.match_counts_nt_dto_v1 import MatchCountsNTDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of MatchCountsNTDtoV1 from a JSON string
match_counts_nt_dto_v1_instance = MatchCountsNTDtoV1.from_json(json)
# print the JSON string representation of the object
print MatchCountsNTDtoV1.to_json()

# convert the object into a dict
match_counts_nt_dto_v1_dict = match_counts_nt_dto_v1_instance.to_dict()
# create an instance of MatchCountsNTDtoV1 from a dict
match_counts_nt_dto_v1_from_dict = MatchCountsNTDtoV1.from_dict(match_counts_nt_dto_v1_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
