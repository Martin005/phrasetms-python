# AnalyseLanguagePartDto

## Properties

| Name                | Type                                                    | Description | Notes      |
| ------------------- | ------------------------------------------------------- | ----------- | ---------- |
| **id**              | **str**                                                 |             | [optional] |
| **source_lang**     | **str**                                                 |             | [optional] |
| **target_lang**     | **str**                                                 |             | [optional] |
| **data**            | [**DataDtoV1**](DataDtoV1.md)                           |             | [optional] |
| **discounted_data** | [**DataDtoV1**](DataDtoV1.md)                           |             | [optional] |
| **jobs**            | [**List[AnalyseJobReference]**](AnalyseJobReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.analyse_language_part_dto import AnalyseLanguagePartDto

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyseLanguagePartDto from a JSON string
analyse_language_part_dto_instance = AnalyseLanguagePartDto.from_json(json)
# print the JSON string representation of the object
print AnalyseLanguagePartDto.to_json()

# convert the object into a dict
analyse_language_part_dto_dict = analyse_language_part_dto_instance.to_dict()
# create an instance of AnalyseLanguagePartDto from a dict
analyse_language_part_dto_from_dict = AnalyseLanguagePartDto.from_dict(analyse_language_part_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
