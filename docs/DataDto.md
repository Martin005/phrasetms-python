# DataDto

## Properties

| Name                            | Type                                          | Description | Notes      |
| ------------------------------- | --------------------------------------------- | ----------- | ---------- |
| **available**                   | **bool**                                      |             | [optional] |
| **estimate**                    | **bool**                                      |             | [optional] |
| **all**                         | [**CountsDto**](CountsDto.md)                 |             | [optional] |
| **repetitions**                 | [**CountsDto**](CountsDto.md)                 |             | [optional] |
| **trans_memory_matches**        | [**MatchCounts101Dto**](MatchCounts101Dto.md) |             | [optional] |
| **machine_translation_matches** | [**MatchCountsDto**](MatchCountsDto.md)       |             | [optional] |
| **non_translatables_matches**   | [**MatchCountsNTDto**](MatchCountsNTDto.md)   |             | [optional] |
| **internal_fuzzy_matches**      | [**MatchCountsDto**](MatchCountsDto.md)       |             | [optional] |

## Example

```python
from phrasetms_client.models.data_dto import DataDto

# TODO update the JSON string below
json = "{}"
# create an instance of DataDto from a JSON string
data_dto_instance = DataDto.from_json(json)
# print the JSON string representation of the object
print DataDto.to_json()

# convert the object into a dict
data_dto_dict = data_dto_instance.to_dict()
# create an instance of DataDto from a dict
data_dto_from_dict = DataDto.from_dict(data_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
