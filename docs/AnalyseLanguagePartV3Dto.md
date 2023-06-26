# AnalyseLanguagePartV3Dto

## Properties

| Name                | Type                                                                | Description | Notes      |
| ------------------- | ------------------------------------------------------------------- | ----------- | ---------- |
| **id**              | **str**                                                             |             | [optional] |
| **source_lang**     | **str**                                                             |             | [optional] |
| **target_lang**     | **str**                                                             |             | [optional] |
| **data**            | [**DataDto**](DataDto.md)                                           |             | [optional] |
| **discounted_data** | [**DataDto**](DataDto.md)                                           |             | [optional] |
| **jobs**            | [**List[AnalyseJobReference]**](AnalyseJobReference.md)             |             | [optional] |
| **trans_memories**  | [**List[TransMemoryReferenceDtoV2]**](TransMemoryReferenceDtoV2.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.analyse_language_part_v3_dto import AnalyseLanguagePartV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyseLanguagePartV3Dto from a JSON string
analyse_language_part_v3_dto_instance = AnalyseLanguagePartV3Dto.from_json(json)
# print the JSON string representation of the object
print AnalyseLanguagePartV3Dto.to_json()

# convert the object into a dict
analyse_language_part_v3_dto_dict = analyse_language_part_v3_dto_instance.to_dict()
# create an instance of AnalyseLanguagePartV3Dto from a dict
analyse_language_part_v3_dto_from_dict = AnalyseLanguagePartV3Dto.from_dict(analyse_language_part_v3_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
