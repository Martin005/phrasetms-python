# DataDtoV1

## Properties

| Name                            | Type                                            | Description | Notes      |
| ------------------------------- | ----------------------------------------------- | ----------- | ---------- |
| **available**                   | **bool**                                        |             | [optional] |
| **all**                         | [**CountsDto**](CountsDto.md)                   |             | [optional] |
| **repetitions**                 | [**CountsDto**](CountsDto.md)                   |             | [optional] |
| **trans_memory_matches**        | [**MatchCounts101Dto**](MatchCounts101Dto.md)   |             | [optional] |
| **machine_translation_matches** | [**MatchCountsDto**](MatchCountsDto.md)         |             | [optional] |
| **non_translatables_matches**   | [**MatchCountsNTDtoV1**](MatchCountsNTDtoV1.md) |             | [optional] |
| **internal_fuzzy_matches**      | [**MatchCountsDto**](MatchCountsDto.md)         |             | [optional] |

## Example

```python
from phrasetms_client.models.data_dto_v1 import DataDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of DataDtoV1 from a JSON string
data_dto_v1_instance = DataDtoV1.from_json(json)
# print the JSON string representation of the object
print DataDtoV1.to_json()

# convert the object into a dict
data_dto_v1_dict = data_dto_v1_instance.to_dict()
# create an instance of DataDtoV1 from a dict
data_dto_v1_from_dict = DataDtoV1.from_dict(data_dto_v1_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
