# AnalyseLanguagePartReference

## Properties

| Name            | Type                                                    | Description | Notes      |
| --------------- | ------------------------------------------------------- | ----------- | ---------- |
| **id**          | **str**                                                 |             | [optional] |
| **source_lang** | **str**                                                 |             | [optional] |
| **target_lang** | **str**                                                 |             | [optional] |
| **jobs**        | [**List[AnalyseJobReference]**](AnalyseJobReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.analyse_language_part_reference import AnalyseLanguagePartReference

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyseLanguagePartReference from a JSON string
analyse_language_part_reference_instance = AnalyseLanguagePartReference.from_json(json)
# print the JSON string representation of the object
print AnalyseLanguagePartReference.to_json()

# convert the object into a dict
analyse_language_part_reference_dict = analyse_language_part_reference_instance.to_dict()
# create an instance of AnalyseLanguagePartReference from a dict
analyse_language_part_reference_from_dict = AnalyseLanguagePartReference.from_dict(analyse_language_part_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
