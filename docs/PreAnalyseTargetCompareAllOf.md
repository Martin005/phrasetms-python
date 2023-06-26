# PreAnalyseTargetCompareAllOf

## Properties

| Name                                    | Type     | Description    | Notes      |
| --------------------------------------- | -------- | -------------- | ---------- |
| **trans_memory_post_editing**           | **bool** | Default: false | [optional] |
| **non_translatable_post_editing**       | **bool** | Default: false | [optional] |
| **machine_translate_post_editing**      | **bool** | Default: false | [optional] |
| **include_fuzzy_repetitions**           | **bool** | Default: false | [optional] |
| **separate_fuzzy_repetitions**          | **bool** | Default: false | [optional] |
| **include_non_translatables**           | **bool** | Default: false | [optional] |
| **include_machine_translation_matches** | **bool** | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.pre_analyse_target_compare_all_of import PreAnalyseTargetCompareAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PreAnalyseTargetCompareAllOf from a JSON string
pre_analyse_target_compare_all_of_instance = PreAnalyseTargetCompareAllOf.from_json(json)
# print the JSON string representation of the object
print PreAnalyseTargetCompareAllOf.to_json()

# convert the object into a dict
pre_analyse_target_compare_all_of_dict = pre_analyse_target_compare_all_of_instance.to_dict()
# create an instance of PreAnalyseTargetCompareAllOf from a dict
pre_analyse_target_compare_all_of_from_dict = PreAnalyseTargetCompareAllOf.from_dict(pre_analyse_target_compare_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
