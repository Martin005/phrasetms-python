# PreAnalyse

## Properties

| Name                                    | Type     | Description    | Notes      |
| --------------------------------------- | -------- | -------------- | ---------- |
| **include_fuzzy_repetitions**           | **bool** | Default: false | [optional] |
| **separate_fuzzy_repetitions**          | **bool** | Default: false | [optional] |
| **include_non_translatables**           | **bool** | Default: false | [optional] |
| **include_machine_translation_matches** | **bool** | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.pre_analyse import PreAnalyse

# TODO update the JSON string below
json = "{}"
# create an instance of PreAnalyse from a JSON string
pre_analyse_instance = PreAnalyse.from_json(json)
# print the JSON string representation of the object
print PreAnalyse.to_json()

# convert the object into a dict
pre_analyse_dict = pre_analyse_instance.to_dict()
# create an instance of PreAnalyse from a dict
pre_analyse_from_dict = PreAnalyse.from_dict(pre_analyse_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
